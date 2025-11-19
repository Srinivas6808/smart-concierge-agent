# Smart Personal Task & Mail Assistant (Concierge Track)

**Capstone:** Demonstrates Tool Calling, Memory, and Multi-step Reasoning using ADK patterns  
**Author:** Rasala Srinivas  
**Track:** Concierge Agents  
**Submission:** Kaggle Notebook + GitHub repo

---

## Project Overview (one-line)
An ADK-style personal assistant agent that ingests emails, extracts actions and tasks, prioritizes them using memory-aware rules, drafts replies, and (optionally) schedules events — demonstrating tool-calling, session & long-term memory, and multi-step planning.

---

## Motivation & Problem
Reading, summarizing, prioritizing, and replying to email consumes time and mental effort. The Smart Personal Task & Mail Assistant automates the routine parts of email triage: extract action items, create prioritized tasks, suggest or create calendar events, and draft professional replies — reducing friction and saving time.

---

## Key Features (what this submission demonstrates)
- **Tool calling** — email parsing tool, calendar tool, task storage tool.  
- **Memory & Sessions** — long-term memory (task history, user preferences), session state for multi-step flows.  
- **Multi-step reasoning / Planning** — classification → extraction → decide (task or meeting) → action → draft reply.  
- **Multi-agent / worker pattern** (conceptual) — coordinator agent + worker tools.  
- **Observability** (basic) — simple logs printed in notebook for traceability.  
- **No secret keys in repo** — ready to swap in LLM/Calendar APIs with credentials locally.

This satisfies the Capstone requirement to apply ≥3 ADK concepts.

---

## What’s included in this repo
smart-concierge-agent/
├─ README.md ← (this file)
├─ notebook/
│ └─ smart_concierge_agent.ipynb ← Kaggle notebook (main demo)
├─ agent/
│ ├─ init.py
│ ├─ core_agent.py ← main coordinator agent
│ ├─ tools.py ← email/calendar/task tool implementations
│ ├─ memory.py ← JSON-backed long-term memory store
│ ├─ workflows.py ← orchestration & planning helpers
│ └─ config.py ← config/constants (no API keys)
├─ demo_data/
│ ├─ sample_emails.json ← sample input emails used in demo
│ └─ example_tasks.json
├─ assets/
│ └─ demo_reply.gif ← GIF produced by the notebook demo
└─ requirements.txt

markdown
Copy code

---

## Quick architecture (text + mermaid)
High-level components and flow:

- **Notebook (client)** → uploads/feeds emails → **Coordinator agent**  
- Coordinator performs parsing via **EmailTool** → planner (LLM or rule engine) → decides actions  
- If meeting requested → **CalendarTool** (worker) creates event (simulated)  
- If actionable → **TaskTool** writes to **Memory** (MemoryStore)  
- Coordinator composes reply draft (LLM) and returns results

```mermaid
flowchart LR
  subgraph Client
    NB[Notebook / UI]
  end
  NB --> Agent[Coordinator Agent]
  Agent --> EmailTool[EmailTool (parse)]
  Agent --> Planner[Planner (LLM/rules)]
  Planner -->|schedule_meeting| CalendarTool[Calendar Tool]
  Planner -->|create_task| TaskTool[Task Tool]
  TaskTool --> Memory[MemoryStore (JSON)]
  CalendarTool --> Storage[demo_calendar.json]
  Agent --> Reply[Draft Reply (LLM)]


How to run (Kaggle Notebook — recommended)
1. Open the notebook: notebook/smart_concierge_agent.ipynb on Kaggle.
2. Upload project files to the Kaggle notebook Files panel (or run the notebook cell that writes files). Ensure the agent/, demo_data/, and assets/ folders exist in /kaggle/working/smart-concierge-agent/
3. Run cells in order. Cells will:
write project files if not present,
load demo emails (demo_data/sample_emails.json),
run the agent on each email,
create memory.json (tasks) and demo_calendar.json (events),
generate assets/demo_reply.gif (visual demo).
4. Inspect outputs printed in notebook and generated files in the Files panel.

How to run locally (development)
Clone repo to local machine.
Create and activate a Python 3.10+ venv.
pip install -r requirements.txt
Run the notebook locally (Jupyter) or run a demo script that calls agent/core_agent.py on demo_data/sample_emails.json.
Note: The repo uses simulated calendar & rule-based parsing by default. To integrate with real LLMs or Google Calendar, replace the placeholder functions in agent/tools.py and add your credentials locally (do NOT commit them).

Files to inspect (important)
agent/core_agent.py — orchestrates parsing, planning and actions (Tool calling + Memory usage).
agent/tools.py — parse_email(), suggest_event(), create_event(), create_task() (worker tools).
agent/memory.py — MemoryStore (JSON persistence API: get, set, append_task).
notebook/smart_concierge_agent.ipynb — demonstration, explanations, and GIF generation.

ADK concepts mapping (explicit, for judges)
Tool calling: agent → calls tools.parse_email, tools.suggest_event, tools.create_event, tools.create_task.
Long-term memory: MemoryStore (writes memory.json) for storing tasks & preference keys.
Session/state management: Notebook-level agent instance maintains short-term state; MemoryStore provides long-term state.
Multi-step reasoning: handle_email() shows parse → classify → plan → act → reply.
Multi-agent pattern: conceptually Coordinator Agent + Worker Tools (Calendar Worker, Task Worker).
Observability: Notebook prints decision logs for each email and shows generated artifacts.

Evaluation checklist (for Kaggle judges)
 Submission includes runnable Kaggle Notebook.
 Demo uses sample inputs and shows outputs (tasks, calendar events, reply drafts).
 README.md with architecture, run instructions, and file list.
 Shows ≥3 ADK concepts (explicit mapping above).
 No API keys or secrets committed.

Limitations
Email parsing uses simple regex heuristics by default (replace with LLM-based extractor for higher accuracy).
Calendar creation is simulated; integration with Google Calendar requires OAuth and local credentials.
Memory is JSON-backed for demo simplicity (not production-grade DB).

Future improvements (recommended for Top-12)
Replace rule-based extraction with LLM (Gemini or OpenAI) to extract dates, times, action items, entities.
Add calendar integration and conflict resolution with Google Calendar API.
Add a small interactive UI (Streamlit / Flask) to accept user approval for actions.
Add unit tests and a small evaluation suite (precision/recall on extraction).
Add robust logging/tracing (OpenTelemetry) for observability.

Submission details (what to include in Kaggle writeup)
Notebook link (primary) and/or GitHub repo link (public).
Title: Smart Personal Task & Mail Assistant (Concierge Track)
Subtitle: Automates email triage, task extraction, and reply drafting using ADK patterns.
Track: Concierge Agents
Attach thumbnail/GIF: assets/demo_reply.gif
Project Description: Use the Project Description portion of your Kaggle submission to paste the content from the "Architecture", "ADK concepts mapping", and "What to run" sections above (keep <1500 words).
Optional: YouTube demo (<3 minutes) to earn bonus points.


Contact
Author: Rasala Srinivas
Kaggle profile: 
GitHub: 


License
MIT (or choose suitable license). Do not include any proprietary keys or credentials in the repository.


I can now:
- generate the **exact `agent/` Python files** (all code ready-to-paste), or  
- produce the **1500-word Kaggle submission write-up** (ready to paste into the Kaggle project description), or  
- create the **architecture diagram image** (`assets/architecture.png`) and embed it into the notebook.

Which one next? (Reply with: `code`, `writeup`, `diagram`, or `all`)
::contentReference[oaicite:0]{index=0}