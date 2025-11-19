"""
Config module for Smart Concierge Agent
Handles all environment, model, and system-level settings.
"""

from dataclasses import dataclass, field

@dataclass
class ModelConfig:
    model_name: str = "gpt-4o-mini"
    temperature: float = 0.2
    max_tokens: int = 300
    top_p: float = 0.9
    frequency_penalty: float = 0
    presence_penalty: float = 0

@dataclass
class MemoryConfig:
    enable_memory: bool = True
    store_email_history: bool = True
    max_history_items: int = 50
    long_term_memory_path: str = "assistant_memory.json"

@dataclass
class AgentConfig:
    name: str = "Smart Concierge AI Agent"
    version: str = "1.0.0"
    model: ModelConfig = field(default_factory=ModelConfig)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    default_language: str = "English"
    allow_tools: bool = True
    use_workflows: bool = True
    max_output_chars: int = 1500
    safety_mode: bool = True

def get_default_config() -> AgentConfig:
    return AgentConfig()
