"""
Main entrypoint for Smart Concierge Agent
Demonstrates: Tool Calling, Memory, Multi-step Reasoning.
"""

from agent.builder import create_concierge_agent
from agent.memory_manager import MemoryManager
from agent.config import get_default_config
import json
import os


def load_tasks():
    """Load demo tasks from data/tasks.json"""
    try:
        with open("data/tasks.json", "r") as f:
            return json.load(f)["tasks"]
    except Exception as e:
        return [{"error": f"Failed to load tasks: {e}"}]


def main():
    print("\n🚀 Starting Smart Concierge Agent...\n")

    # Load config & initialize memory
    config = get_default_config()
    memory = MemoryManager(config)

    # Build the agent
    agent = create_concierge_agent(config, memory)

    # Load example tasks
    tasks = load_tasks()

    print("📌 Loaded Tasks:")
    for t in tasks:
        print(f" - [{t['type']}] {t['content']} (priority: {t['priority']})")

    print("\n🤖 Agent is ready! Type a message below.\n")
    print("Example: 'Write a reply for an interview HR email'\n")

    # Start interaction loop
    while True:
        user_input = input("\nYou: ").strip()

        if user_input.lower() in ["exit", "quit", "q", "stop"]:
            print("\n👋 Exiting Smart Concierge Agent. Goodbye!")
            break

        # Run agent
        print("\nAI Assistant:")
        response = agent.run(user_input)
        print(response)


if __name__ == "__main__":
    main()
