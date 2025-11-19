# agent/core_agent.py

"""
Core Agent Module
This is the brain of the Smart Concierge AI agent.
It orchestrates model responses, tool usage, memory, and workflows.
"""

import json
from typing import Optional, Dict, Any

from agent.config import get_default_config, AgentConfig
from agent.memory_manager import MemoryManager
from agent.tools import TOOLS_REGISTRY
from agent.workflows import WORKFLOW_REGISTRY


class CoreAgent:

    def __init__(self, config: Optional[AgentConfig] = None):
        self.config = config or get_default_config()
        self.memory = MemoryManager(self.config.memory)

    # ----------------------------------------------------
    # Model Simulation (Since Kaggle has no API access)
    # ----------------------------------------------------
    def _simulate_llm(self, prompt: str) -> str:
        """
        Simulated LLM for Kaggle (no OpenAI API allowed).
        You can later replace it with actual API calls.
        """
        return f"[Simulated LLM Reply]: {prompt[:200]}..."

    # ----------------------------------------------------
    # TOOL CALLING
    # ----------------------------------------------------
    def call_tool(self, tool_name: str, **kwargs) -> Any:
        if tool_name not in TOOLS_REGISTRY:
            return {"error": f"Unknown tool: {tool_name}"}

        tool_fn = TOOLS_REGISTRY[tool_name]
        return tool_fn(**kwargs)

    # ----------------------------------------------------
    # WORKFLOW EXECUTION
    # ----------------------------------------------------
    def run_workflow(self, workflow_name: str, **kwargs) -> Any:
        if workflow_name not in WORKFLOW_REGISTRY:
            return {"error": f"Unknown workflow: {workflow_name}"}

        workflow_fn = WORKFLOW_REGISTRY[workflow_name]
        return workflow_fn(self, **kwargs)

    # ----------------------------------------------------
    # MEMORY SYSTEM
    # ----------------------------------------------------
    def store_memory(self, user_input: str, agent_reply: str):
        if self.config.memory.enable_memory:
            self.memory.add_interaction(user_input, agent_reply)

    def recall_history(self) -> str:
        return self.memory.get_recent_history()

    # ----------------------------------------------------
    # MAIN PROCESSOR
    # ----------------------------------------------------
    def process(self, user_input: str) -> Dict[str, Any]:

        # 1) Use workflows (if input matches workflow names)
        if user_input.lower().startswith("workflow:"):
            workflow_name = user_input.split(":", 1)[1].strip()
            result = self.run_workflow(workflow_name)
            return {
                "type": "workflow",
                "workflow": workflow_name,
                "result": result
            }

        # 2) Tool request
        if user_input.lower().startswith("tool:"):
            parts = user_input.split(":", 2)
            tool_name = parts[1].strip()
            arg = parts[2].strip() if len(parts) > 2 else ""
            result = self.call_tool(tool_name, query=arg)
            return {
                "type": "tool",
                "tool": tool_name,
                "result": result
            }

        # 3) Standard LLM Response
        reply = self._simulate_llm(user_input)

        # 4) Store memory
        self.store_memory(user_input, reply)

        # 5) Respond
        return {
            "type": "chat",
            "reply": reply
        }
