# SQL Server AI DBA Assistant

Learning project for building an AI-powered DBA assistant with Python, SQL Server, Git, and AI.
# SQL Server AI DBA Assistant

An AI-powered SQL Server DBA Assistant built with Python, SQL Server, vector search, diagnostic tools, and Gemini AI.

The goal of this project is to demonstrate how an AI assistant can help a DBA investigate SQL Server issues by combining internal knowledge, real SQL Server diagnostic data, and an LLM-generated professional response.

---

## Project Overview

This project is not a simple chatbot.

It is a DBA diagnostic assistant that uses:

* SQL Server as the operational database
* A Knowledge Base table for internal DBA troubleshooting articles
* Vector search to retrieve relevant knowledge
* A Tool Router to decide which diagnostic tools should run
* SQL Server DMV queries to collect real diagnostic evidence
* Gemini AI to generate a structured DBA answer

The assistant receives a user question, finds relevant DBA knowledge, runs the correct diagnostic tools, and builds a final answer based on evidence.

---

## High-Level Architecture

```text
User Question
     ↓
Vector Search
     ↓
Relevant Knowledge Base Articles
     ↓
Tool Router
     ↓
SQL Server Diagnostic Tools
     ↓
Prompt Builder
     ↓
Gemini AI Model
     ↓
Final DBA Answer
```

---

## Main Features

### RAG-Based Knowledge Retrieval

The assistant uses a Knowledge Base stored in SQL Server.

When the user asks a question, the system converts the question into a vector and searches for the most relevant DBA article.

Example:

```text
User question:
high cpu

Relevant article:
High CPU Troubleshooting
```

This helps the AI answer based on project-specific DBA knowledge instead of only giving a generic answer.

---

### Tool Router

The Tool Router decides which diagnostic tools should run based on the user's question.

Examples:

```text
high cpu
→ top_cpu_procedures

users are blocked
→ blocking_sessions
```

This makes the system more agent-like because it can decide which tool is relevant for each problem.

---

### SQL Server Diagnostic Tools

The assistant includes real SQL Server diagnostic tools based on DMVs.

Current tools:

* Top CPU Stored Procedures
* Blocking Sessions

These tools collect real evidence from SQL Server and pass it into the final AI prompt.

---

### Gemini AI Integration

Gemini is used to generate the final DBA response.

The model receives:

* The original user question
* Relevant Knowledge Base articles
* Real SQL Server diagnostic results
* A structured DBA answer format
* Safety rules to avoid inventing server-specific facts

Gemini does not connect directly to SQL Server.
The Python application prepares the context and sends it to the model.

---

## Example Questions

The assistant can answer questions such as:

```text
high cpu
```

```text
users are blocked
```

```text
why is my sql server slow?
```

```text
which stored procedures are using the most cpu?
```

---

## Example Output Structure

The final answer is generated in a structured DBA format:

```text
1. Short summary of the problem
2. Most relevant knowledge base article used
3. Possible root causes
4. What to check first
5. Recommended T-SQL queries
6. Risk level
7. Next recommended action
```

---

## Tech Stack

* Python
* SQL Server
* SQL Server DMVs
* SQL Server Vector Search
* pyodbc
* Gemini AI
* Git and GitHub
* VS Code
* PowerShell

---

## Project Structure

```text
sqlserver-ai-dba-assistant/
│
├── app/
│   ├── ai_client.py
│   ├── config.py
│   ├── db.py
│   ├── dba_diagnostic_tools.py
│   ├── local_embedding.py
│   ├── run_dba_assistant.py
│   ├── tool_router.py
│   └── tests/
│
├── agents/
│   └── dba_agent.py
│
├── sql/
│   ├── database setup scripts
│   └── demo diagnostic scripts
│
├── docs/
│   └── agent_architecture.md
│
├── README.md
└── requirements.txt
```

---

## How It Works

### 1. User Asks a DBA Question

Example:

```text
high cpu
```

### 2. Vector Search Finds Relevant Knowledge

The system searches the SQL Server Knowledge Base for the most relevant troubleshooting article.

### 3. Tool Router Selects Diagnostic Tools

The Tool Router identifies that this is a CPU-related question and selects:

```text
top_cpu_procedures
```

### 4. Diagnostic Tool Runs Against SQL Server

The CPU diagnostic tool queries SQL Server DMVs and collects evidence about stored procedures with high CPU usage.

### 5. Prompt Builder Creates the Final Prompt

The system combines:

* User question
* Relevant Knowledge Base article
* Diagnostic results
* Answer format rules

### 6. Gemini Generates the Final Answer

Gemini receives the prepared context and returns a practical DBA-style answer.

---

## Why This Project Is Valuable

This project demonstrates several important skills:

* Building an AI assistant with real backend logic
* Using RAG architecture
* Working with SQL Server vector search
* Writing SQL Server DMV diagnostic queries
* Designing an agent-style Tool Router
* Integrating Python with SQL Server
* Integrating an LLM into a practical workflow
* Building a GitHub-ready portfolio project

---

## Resume Summary

Example resume description:

```text
Built an AI-powered SQL Server DBA Assistant using Python, SQL Server vector search, RAG, Gemini AI, and real-time DMV diagnostic tools. The assistant routes user questions to relevant DBA tools, retrieves internal troubleshooting knowledge, collects SQL Server evidence, and generates structured DBA recommendations.
```

---

## Current Status

Implemented:

* SQL Server connection layer
* Knowledge Base retrieval
* Local embedding generation
* SQL Server vector search
* Gemini AI client
* DBA Agent prompt builder
* Tool Router
* Top CPU Stored Procedures diagnostic tool
* Blocking Sessions diagnostic tool
* Basic tests
* Architecture documentation

Planned future improvements:

* Wait Stats diagnostic tool
* Long Running Queries diagnostic tool
* SQL Agent Failed Jobs tool
* Backup Health tool
* Run history table
* FastAPI backend
* Professional UI or dashboard
