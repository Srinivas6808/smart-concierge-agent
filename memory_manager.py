# agent/memory_manager.py

"""
Memory Manager for Smart Concierge Agent.
Handles: short-term history, long-term memory, and
persistent interaction storage.
"""

import json
from typing import List, Dict, Any


class MemoryManager:

    def __init__(self, config):
        self.enable_memory = config.enable_memory
        self.max_entries = config.max_entries
        self.history: List[Dict[str, str]] = []

    # --------------------------------------------
    # ADD MEMORY
    # --------------------------------------------
    def add_interaction(self, user_input: str, agent_reply: str):
        if not self.enable_memory:
            return

        self.history.append({
            "user": user_input,
            "agent": agent_reply
        })

        # Limit memory to max entries
        if len(self.history) > self.max_entries:
            self.history.pop(0)

    # --------------------------------------------
    # RETRIEVE MEMORY
    # --------------------------------------------
    def get_recent_history(self, limit: int = 5) -> str:
        """
        Returns last 'limit' dialog turns as text block.
        """
        if not self.history:
            return ""

        last = self.history[-limit:]
        formatted = [
            f"User: {h['user']}\nAgent: {h['agent']}"
            for h in last
        ]
        return "\n\n".join(formatted)

    # --------------------------------------------
    # EXPORT MEMORY (Debugging)
    # --------------------------------------------
    def export_memory(self) -> List[Dict[str, Any]]:
        return self.history

    # --------------------------------------------
    # RESET MEMORY
    # --------------------------------------------
    def clear(self):
        self.history = []
