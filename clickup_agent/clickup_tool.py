import os
import json
import re
from typing import Optional, List, Dict, Any, Union, Tuple

from phi.tools import Toolkit
from phi.utils.log import logger

try:
    import requests
except ImportError:
    raise ImportError("`requests` not installed. Please install using `pip install requests`")


class ClickUpTools(Toolkit):
    def __init__(
        self,
        api_key: Optional[str] = None,
        master_space_id: Optional[str] = None,
        list_tasks: bool = True,
        create_task: bool = True,
        get_task: bool = True,
        update_task: bool = True,
        delete_task: bool = True,
        list_spaces: bool = True,
        list_lists: bool = True
    ):
        super().__init__(name="clickup")

        self.api_key = api_key or os.getenv("CLICKUP_API_KEY")
        self.master_space_id = master_space_id or os.getenv("MASTER_SPACE_ID")
        self.base_url = "https://api.clickup.com/api/v2"
        self.headers = {"Authorization": self.api_key}

        if not self.api_key:
            raise ValueError("ClickUp API key is required")
        if not self.master_space_id:
            raise ValueError("ClickUp Master Space ID is required")

        if list_tasks:
            self.register(self.list_tasks)
        if create_task:
            self.register(self.create_task)
        if get_task:
            self.register(self.get_task)
        if update_task:
            self.register(self.update_task)
        if delete_task:
            self.register(self.delete_task)
        if list_spaces:
            self.register(self.list_spaces)
        if list_lists:
            self.register(self.list_lists)

    def _make_request(self, method: str, endpoint: str, params: Dict = None, data: Dict = None) -> Dict[str, Any]:
        """Make a request to the ClickUp API."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(
                method=method,
                url=url,
                headers=self.headers,
                params=params,
                json=data
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error(f"Error making request to {url}: {e}")
            return {"error": str(e)}

    def _find_by_name(self, items: List[Dict[str, Any]], name: str, item_type: str) -> Union[Dict[str, Any], None]:
        """Find an item in a list by name using exact match or regex pattern.
        
        Args:
            items: List of items to search through
            name: Name to search for
            item_type: Type of item (for error message)
            
        Returns:
            Matching item or None if not found
        """
        if not name:
            return items[0] if items else None

        pattern = re.compile(name, re.IGNORECASE)
        for item in items:
            # Try exact match first (case-insensitive)
            if item["name"].lower() == name.lower():
                return item
            # Then try regex pattern match
            if pattern.search(item["name"]):
                return item
        return None

    def _get_space(self, space_name: str = None) -> Dict[str, Any]:
        """Get space information by name."""
        spaces = self._make_request("GET", f"team/{self.master_space_id}/space")
        if "error" in spaces:
            return spaces

        spaces_list = spaces.get("spaces", [])
        if not spaces_list:
            return {"error": "No spaces found"}

        space = self._find_by_name(spaces_list, space_name, "space")
        if not space:
            return {"error": f"Space '{space_name}' not found"}
        return space

    def _get_list(self, space_id: str, list_name: str = None) -> Dict[str, Any]:
        """Get list information by name."""
        lists = self._make_request("GET", f"space/{space_id}/list")
        if "error" in lists:
            return lists

        lists_data = lists.get("lists", [])
        if not lists_data:
            return {"error": "No lists found in space"}

        list_item = self._find_by_name(lists_data, list_name, "list")
        if not list_item:
            return {"error": f"List '{list_name}' not found"}
        return list_item

    def _get_tasks(self, list_id: str, task_name: str = None) -> List[Dict[str, Any]]:
        """Get tasks in a list, optionally filtered by name."""
        tasks = self._make_request("GET", f"list/{list_id}/task")
        if "error" in tasks:
            return []

        tasks_data = tasks.get("tasks", [])
        if task_name:
            task = self._find_by_name(tasks_data, task_name, "task")
            return [task] if task else []
        return tasks_data

    def list_tasks(self, space_name: str, list_name: str = None, task_name: str = None) -> str:
        """List tasks in a space, optionally filtered by list name and task name.

        Args:
            space_name (str): Name of the space to list tasks from
            list_name (str, optional): Filter tasks by list name
            task_name (str, optional): Filter tasks by task name

        Returns:
            str: JSON string containing matching tasks
        """
        # Get space
        space = self._get_space(space_name)
        if "error" in space:
            return json.dumps(space, indent=2)

        # Get lists
        lists = self._make_request("GET", f"space/{space['id']}/list")
        lists_data = lists.get("lists", [])
        if not lists_data:
            return json.dumps({"error": f"No lists found in space '{space_name}'"}, indent=2)

        # Filter lists if list_name provided
        if list_name:
            list_item = self._find_by_name(lists_data, list_name, "list")
            if list_item:
                lists_data = [list_item]
            else:
                return json.dumps({"error": f"List '{list_name}' not found"}, indent=2)

        # Get tasks from all matching lists
        all_tasks = []
        for list_info in lists_data:
            tasks = self._get_tasks(list_info["id"], task_name)
            for task in tasks:
                task["list_name"] = list_info["name"]  # Add list name for context
            all_tasks.extend(tasks)

        return json.dumps({"tasks": all_tasks}, indent=2)

    def create_task(self, space_name: str, task_name: str, list_name: str = None, task_description: str = "", priority: int = None) -> str:
        """Create a new task in a space.

        Args:
            space_name (str): Name of the space to create task in
            task_name (str): Name of the task
            list_name (str, optional): Name of the list to create task in (uses first list if not specified)
            task_description (str, optional): Description of the task
            priority (int, optional): Priority of the task (1-4)

        Returns:
            str: JSON string containing created task details
        """
        # Get space
        space = self._get_space(space_name)
        if "error" in space:
            return json.dumps(space, indent=2)

        # Get list
        list_info = self._get_list(space["id"], list_name)
        if "error" in list_info:
            return json.dumps(list_info, indent=2)

        # Create task
        data = {
            "name": task_name,
            "description": task_description
        }
        if priority:
            data["priority"] = priority

        task = self._make_request("POST", f"list/{list_info['id']}/task", data=data)
        return json.dumps(task, indent=2)

    def get_task(self, task_id: str) -> str:
        """Get details of a specific task.

        Args:
            task_id (str): The ID of the task

        Returns:
            str: JSON string containing task details
        """
        task = self._make_request("GET", f"task/{task_id}")
        return json.dumps(task, indent=2)

    def update_task(self, task_id: str, **kwargs) -> str:
        """Update a specific task.

        Args:
            task_id (str): The ID of the task
            **kwargs: Task fields to update (name, description, status, priority, etc.)

        Returns:
            str: JSON string containing updated task details
        """
        task = self._make_request("PUT", f"task/{task_id}", data=kwargs)
        return json.dumps(task, indent=2)

    def delete_task(self, task_id: str) -> str:
        """Delete a specific task.

        Args:
            task_id (str): The ID of the task

        Returns:
            str: JSON string containing deletion status
        """
        result = self._make_request("DELETE", f"task/{task_id}")
        if "error" not in result:
            result = {"success": True, "message": f"Task {task_id} deleted successfully"}
        return json.dumps(result, indent=2)

    def list_spaces(self, space_name: str = None) -> str:
        """List all spaces in the workspace, optionally filtered by name.

        Args:
            space_name (str, optional): Filter spaces by name

        Returns:
            str: JSON string containing list of spaces
        """
        spaces = self._make_request("GET", f"team/{self.master_space_id}/space")
        if space_name and "spaces" in spaces:
            space = self._find_by_name(spaces["spaces"], space_name, "space")
            if space:
                spaces["spaces"] = [space]
            else:
                return json.dumps({"error": f"Space '{space_name}' not found"}, indent=2)
        return json.dumps(spaces, indent=2)

    def list_lists(self, space_name: str, list_name: str = None) -> str:
        """List lists in a space, optionally filtered by name.

        Args:
            space_name (str): Name of the space to list lists from
            list_name (str, optional): Filter lists by name

        Returns:
            str: JSON string containing list of lists
        """
        # Get space
        space = self._get_space(space_name)
        if "error" in space:
            return json.dumps(space, indent=2)

        # Get lists
        lists = self._make_request("GET", f"space/{space['id']}/list")
        if list_name and "lists" in lists:
            list_item = self._find_by_name(lists["lists"], list_name, "list")
            if list_item:
                lists["lists"] = [list_item]
            else:
                return json.dumps({"error": f"List '{list_name}' not found"}, indent=2)
        return json.dumps(lists, indent=2)


# # Working example
# if __name__ == "__main__":
#     clickup_tools = ClickUpTools()

#     # List all spaces or filter by name
#     print("Listing spaces:")
#     spaces = clickup_tools.list_spaces("My.*")  # Regex pattern match
#     print(spaces)

#     # List all lists in a space or filter by name
#     print("\nListing lists in 'My Space':")
#     lists = clickup_tools.list_lists("My Space", "Dev.*")  # Regex pattern match
#     print(lists)

#     # List all tasks in a space, optionally filtered by list and task name
#     print("\nListing tasks in 'My Space':")
#     tasks = clickup_tools.list_tasks("My Space", "Dev List", "Bug.*")  # Regex pattern matches
#     print(tasks)
