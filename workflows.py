"""
Orchestration helpers and simple planner.
This module implements a Planner class that takes parsed_email and returns a plan:
- actions: list like ["create_task", "schedule_meeting"]
- metadata for each action
Planner is intentionally simple (rules + priority mapping) but designed to be replaced by an LLM planner.
"""

from typing import Dict, Any, List

# Example priority rules
SENDER_PRIORITY = {
    # if sender matches a key, boost priority
    # "boss@company.com": "high",
}

def determine_priority(parsed_email: Dict[str, Any]) -> str:
    # Example: keywords -> priority
    raw = parsed_email.get("raw", "").lower()
    if "urgent" in raw or "asap" in raw or "today" in raw:
        return "high"
    if "please" in raw and "thanks" in raw:
        return "medium"
    return "low"

class Planner:
    def __init__(self, use_llm: bool = False):
        self.use_llm = use_llm

    def plan(self, parsed_email: Dict[str, Any]) -> Dict[str, Any]:
        """
        Return a plan dict with:
        - actions: List[str]
        - priorities: mapping for actions
        - notes: optional explanation
        """
        actions: List[str] = []
        if "schedule_meeting" in parsed_email.get("actions", []):
            actions.append("schedule_meeting")
        if "create_task" in parsed_email.get("actions", []):
            actions.append("create_task")
        # If no explicit action but body contains "please" and "share", create task
        if not actions and ("please" in parsed_email.get("raw", "").lower() or "could you" in parsed_email.get("raw","").lower()):
            actions.append("create_task")

        priorities = {a: determine_priority(parsed_email) for a in actions}
        notes = "Rule-based planner produced actions: " + ", ".join(actions) if actions else "No actions detected."

        return {
            "actions": actions,
            "priorities": priorities,
            "notes": notes
        }
