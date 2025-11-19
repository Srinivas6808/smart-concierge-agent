# agent/tools.py

"""
All tools used by the Smart Concierge Agent.
Includes:
• Task creation
• Email searching
• Email drafting
• Task summarization

Tools follow ADK ToolSpec patterns.
"""

from adk.types import ToolSpec
import datetime


# --------------------------------------------------
# 1. CREATE TASK TOOL
# --------------------------------------------------
def create_task_tool():
    def create_task(title: str, due_date: str = None):
        task = {
            "title": title,
            "due_date": due_date,
            "created_at": datetime.datetime.now().isoformat()
        }
        return {
            "status": "success",
            "message": f"Task added: {title}",
            "task": task
        }

    return ToolSpec(
        name="create_task",
        description="Creates a personal task with optional due date.",
        input_spec={
            "title": "string",
            "due_date": "string?"
        },
        func=create_task
    )


# --------------------------------------------------
# 2. EMAIL SEARCH TOOL
# --------------------------------------------------
def search_mail_tool():
    def search_mail(keyword: str):
        # In the Capstone version this is a mock — real systems query email API
        fake_emails = [
            {"id": 1, "subject": "Meeting Tomorrow", "body": "Don't forget our call."},
            {"id": 2, "subject": "Invoice Reminder", "body": "Payment pending."}
        ]
        matches = [e for e in fake_emails if keyword.lower() in e["subject"].lower()]
        return {
            "matches": matches,
            "count": len(matches)
        }

    return ToolSpec(
        name="search_mail",
        description="Search emails by subject keyword.",
        input_spec={
            "keyword": "string"
        },
        func=search_mail
    )


# --------------------------------------------------
# 3. EMAIL DRAFTING TOOL
# --------------------------------------------------
def draft_email_tool():
    def draft_email(to: str, subject: str, message: str):
        draft = {
            "to": to,
            "subject": subject,
            "body": message,
            "status": "draft_created"
        }
        return draft

    return ToolSpec(
        name="draft_email",
        description="Drafts an email for the user.",
        input_spec={
            "to": "string",
            "subject": "string",
            "message": "string"
        },
        func=draft_email
    )


# --------------------------------------------------
# 4. TASK SUMMARY TOOL
# --------------------------------------------------
def summarize_tasks_tool():
    def summarize(tasks: list):
        if not tasks:
            return {"summary": "No tasks available."}

        titles = [t["title"] for t in tasks]
        summary = f"You have {len(titles)} tasks: " + ", ".join(titles)
        return {"summary": summary}

    return ToolSpec(
        name="summarize_tasks",
        description="Summarizes a list of tasks.",
        input_spec={
            "tasks": "list"
        },
        func=summarize
    )
