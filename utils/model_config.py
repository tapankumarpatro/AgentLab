from typing import Optional
from dataclasses import dataclass
import os

from phi.model.ollama import Ollama
from phi.model.google import Gemini
from phi.model.openai import OpenAIChat

from dotenv import load_dotenv
import os

load_dotenv()

@dataclass
class ModelConfig:
    model_type: str = "ollama"  # "openai", "gemini", or "ollama"
    model_name: str = "llama3.1:latest"  # default model name
    temperature: float = 0.0
    max_tokens: Optional[int] = None
    api_key: Optional[str] = None

class ModelLoader:
    def __init__(self, config: ModelConfig):
        self.config = config
        self._model = None
    
    def load_model(self):
        if self._model is not None:
            return self._model
            
        if self.config.model_type == "ollama":
            self._model = Ollama(model=self.config.model_name, options={"temperature": 0.0})
        elif self.config.model_type == "gemini":
            if not self.config.api_key:
                raise ValueError("API key is required for Gemini model")
            self._model = Gemini(
                model=self.config.model_name,
                api_key=self.config.api_key
            )
        elif self.config.model_type == "openai":
            if not self.config.api_key:
                raise ValueError("API key is required for OpenAI model")
            self._model = OpenAIChat(id=self.config.model_name, api_key=self.config.api_key)
        else:
            raise ValueError(f"Unsupported model type: {self.config.model_type}")
            
        return self._model

# Example configurations
ollama_config = ModelConfig(
    model_type="ollama",
    model_name="llama3.1:latest"
)

ollama_qwen_coder_tool_config = ModelConfig(
    model_type="ollama",
    model_name="hhao/qwen2.5-coder-tools:latest"
)

openai_config = ModelConfig(
    model_type="openai",
    model_name="gpt-4o-mini",
    api_key=os.getenv("OPENAI_API_KEY")
)

gemini_config = ModelConfig(
    model_type="gemini",
    model_name="gemini-2.0-flash-exp",
    api_key=os.getenv("GOOGLE_API_KEY")
)
