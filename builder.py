"""
Builder for the Smart Concierge Agent.

This agent supports:
• Multi-step task planning
• Calendar/task scheduling
• Email drafting
• Long-term memory (summaries + preferences)
• Tool calling with ADK patterns
"""

from adk import Agent, SequentialAgent, ToolNode
from adk.session import InMemorySessionService
from .tools import (
    create_task_tool,
    search_mail_tool,
    draft_email_tool,
    summarize_tasks_tool,
)


def create_concierge_agent(config, memory_manager):
    """
    Constructs the Smart Concierge Agent.
    
    Args:
        config: AgentConfig instance
        memory_manager: MemoryManager instance
    
    Returns:
        Agent object
    """

    # -----------------------------
    # 1. MEMORY SYSTEM
    # -----------------------------
    session_service = memory_manager.session_service
    memory_bank = memory_manager.memory_bank

    # -----------------------------
    # 2. TOOL NODES
    # -----------------------------
    tool_nodes = [
        ToolNode(create_task_tool()),
        ToolNode(search_mail_tool()),
        ToolNode(draft_email_tool()),
        ToolNode(summarize_tasks_tool()),
    ]

    # -----------------------------
    # 3. SEQUENTIAL AGENT
    # -----------------------------
    concierge_agent = SequentialAgent(
        name=config.name,
        description="A smart assistant for tasks, reminders, summaries, and email drafting.",
        steps=tool_nodes,
        session_service=session_service,
        memory_bank=memory_bank,
    )

    return concierge_agent
