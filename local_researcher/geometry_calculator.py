import json
import math
from phi.tools import Toolkit


class GeometryCalculator(Toolkit):
    def __init__(
        self,
        area: bool = True,
        perimeter: bool = True,
        volume: bool = True,
        distance: bool = False,
        angles: bool = False,
        enable_all: bool = False,
    ):
        super().__init__(name="geometry_calculator")

        # Register functions in the toolkit
        if area or enable_all:
            self.register(self.rectangle_area)
            self.register(self.circle_area)
            self.register(self.triangle_area)
        
        if perimeter or enable_all:
            self.register(self.rectangle_perimeter)
            self.register(self.circle_circumference)
            self.register(self.triangle_perimeter)
        
        if volume or enable_all:
            self.register(self.cube_volume)
            self.register(self.sphere_volume)
            self.register(self.cylinder_volume)
        
        if distance or enable_all:
            self.register(self.point_distance)
            self.register(self.midpoint)
        
        if angles or enable_all:
            self.register(self.degrees_to_radians)
            self.register(self.radians_to_degrees)

    # Area calculations
    def rectangle_area(self, length: float, width: float) -> str:
        """Calculate the area of a rectangle.
        
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
            
        Returns:
            str: JSON string with the area result
        """
        area = length * width
        return json.dumps({"area": area})

    def circle_area(self, radius: float) -> str:
        """Calculate the area of a circle.
        
        Args:
            radius (float): Radius of the circle
            
        Returns:
            str: JSON string with the area result
        """
        area = math.pi * radius * radius
        return json.dumps({"area": area})

    def triangle_area(self, base: float, height: float) -> str:
        """Calculate the area of a triangle.
        
        Args:
            base (float): Base of the triangle
            height (float): Height of the triangle
            
        Returns:
            str: JSON string with the area result
        """
        area = 0.5 * base * height
        return json.dumps({"area": area})

    # Perimeter calculations
    def rectangle_perimeter(self, length: float, width: float) -> str:
        """Calculate the perimeter of a rectangle.
        
        Args:
            length (float): Length of the rectangle
            width (float): Width of the rectangle
            
        Returns:
            str: JSON string with the perimeter result
        """
        perimeter = 2 * (length + width)
        return json.dumps({"perimeter": perimeter})

    def circle_circumference(self, radius: float) -> str:
        """Calculate the circumference of a circle.
        
        Args:
            radius (float): Radius of the circle
            
        Returns:
            str: JSON string with the circumference result
        """
        circumference = 2 * math.pi * radius
        return json.dumps({"circumference": circumference})

    def triangle_perimeter(self, side1: float, side2: float, side3: float) -> str:
        """Calculate the perimeter of a triangle.
        
        Args:
            side1 (float): First side length
            side2 (float): Second side length
            side3 (float): Third side length
            
        Returns:
            str: JSON string with the perimeter result
        """
        perimeter = side1 + side2 + side3
        return json.dumps({"perimeter": perimeter})

    # Volume calculations
    def cube_volume(self, side: float) -> str:
        """Calculate the volume of a cube.
        
        Args:
            side (float): Length of cube side
            
        Returns:
            str: JSON string with the volume result
        """
        volume = side ** 3
        return json.dumps({"volume": volume})

    def sphere_volume(self, radius: float) -> str:
        """Calculate the volume of a sphere.
        
        Args:
            radius (float): Radius of the sphere
            
        Returns:
            str: JSON string with the volume result
        """
        volume = (4/3) * math.pi * radius ** 3
        return json.dumps({"volume": volume})

    def cylinder_volume(self, radius: float, height: float) -> str:
        """Calculate the volume of a cylinder.
        
        Args:
            radius (float): Radius of the base
            height (float): Height of the cylinder
            
        Returns:
            str: JSON string with the volume result
        """
        volume = math.pi * radius * radius * height
        return json.dumps({"volume": volume})

    # Distance calculations
    def point_distance(self, x1: float, y1: float, x2: float, y2: float) -> str:
        """Calculate the distance between two points.
        
        Args:
            x1 (float): X coordinate of first point
            y1 (float): Y coordinate of first point
            x2 (float): X coordinate of second point
            y2 (float): Y coordinate of second point
            
        Returns:
            str: JSON string with the distance result
        """
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return json.dumps({"distance": distance})

    def midpoint(self, x1: float, y1: float, x2: float, y2: float) -> str:
        """Calculate the midpoint between two points.
        
        Args:
            x1 (float): X coordinate of first point
            y1 (float): Y coordinate of first point
            x2 (float): X coordinate of second point
            y2 (float): Y coordinate of second point
            
        Returns:
            str: JSON string with the midpoint coordinates
        """
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        return json.dumps({"x": mid_x, "y": mid_y})

    # Angle conversions
    def degrees_to_radians(self, degrees: float) -> str:
        """Convert degrees to radians.
        
        Args:
            degrees (float): Angle in degrees
            
        Returns:
            str: JSON string with the angle in radians
        """
        radians = math.radians(degrees)
        return json.dumps({"radians": radians})

    def radians_to_degrees(self, radians: float) -> str:
        """Convert radians to degrees.
        
        Args:
            radians (float): Angle in radians
            
        Returns:
            str: JSON string with the angle in degrees
        """
        degrees = math.degrees(radians)
        return json.dumps({"degrees": degrees})
