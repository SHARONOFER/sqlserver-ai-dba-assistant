# SQL Server AI DBA Assistant - Agent Architecture

## Project Goal

This project is an AI-powered SQL Server DBA Assistant.

The goal is not only to ask an AI model a general SQL Server question, but to build a smarter DBA Agent that combines:

* Internal DBA knowledge
* SQL Server vector search
* Real SQL Server diagnostic tools
* An AI model that summarizes the findings into a practical DBA answer

This makes the assistant more accurate, more operational, and more relevant to the actual SQL Server environment.

---

## High-Level Flow

The flow of the system is:

```text
User Question
     ↓
Vector Search --> find relevant data.
     ↓
Relevant Knowledge Base Articles -->  we will provide its gemeni to provide us infromation we need about the issue.
     ↓
Tool Router 
     ↓
SQL Server Diagnostic Tools --> we build it in our system --> wew build function retrun top cpu consmption.
     ↓
Prompt Builder
     ↓
Gemini AI Model
     ↓
Final DBA Answer
```

---

## Knowledge Base

The Knowledge Base is the internal DBA knowledge of the system.

It contains articles such as:

* High CPU troubleshooting
* Blocking troubleshooting
* Index issues
* Backup checks
* SQL Server performance investigation steps

The Knowledge Base helps the AI model answer according to project-specific DBA knowledge instead of giving only a generic answer.

In simple words:

```text
Knowledge Base = what the assistant should know
```

---

## Vector Search

Vector Search is used to find the most relevant Knowledge Base articles for the user's question.

For example, if the user asks:

```text
high cpu on sql server
```

The system converts the question into a vector and compares it against stored article vectors in SQL Server.

The most relevant article might be:

```text
High CPU Troubleshooting
```

In simple words:

```text
Vector Search = finds the most relevant knowledge
```

---

## Tool Router

The Tool Router decides which diagnostic tools should run based on the user's question.

For example:

```text
high cpu
```

Routes to:

```text
top_cpu_procedures
```

Another example:

```text
users are blocked
```

Routes to:

```text
blocking_sessions
```

The Tool Router does not run the tools directly.
It only decides which tools are relevant.

In simple words:

```text
Tool Router = decides what should be checked
```

---

## Diagnostic Tools

Diagnostic Tools run real read-only checks against SQL Server.

For example, the CPU diagnostic tool runs a DMV query against:

```sql
sys.dm_exec_procedure_stats
```

This helps identify stored procedures that consumed the most CPU.

In simple words:

```text
Diagnostic Tools = collect real SQL Server evidence
```

---

## Gemini AI Model

Gemini is the AI model used to generate the final DBA answer.

Gemini receives a complete prompt that includes:

* The original user question
* Relevant Knowledge Base articles
* Real SQL Server diagnostic results
* Required answer format
* Rules for safe and practical DBA answers

Gemini does not directly connect to SQL Server.
It only receives the context prepared by the application.

In simple words:

```text
Gemini = writes the final professional answer
```

---

## Why Not Ask Gemini Directly?

Gemini can answer SQL Server questions directly, but the answer would usually be generic.

This project improves the answer by giving Gemini:

* Internal DBA knowledge
* Real SQL Server diagnostic data
* Project-specific instructions
* A structured DBA response format

So instead of asking Gemini to guess, the system gives Gemini accurate context.

In simple words:

```text
We are not training Gemini.
We are grounding Gemini with relevant knowledge and real diagnostic data.
```

---

## Difference Between Vector Search and Tool Router

Both use the same user question, but they do different jobs.

### Vector Search

Answers this question:

```text
What knowledge should we bring?
```

Example result:

```text
High CPU Troubleshooting article
```

### Tool Router

Answers this question:

```text
What diagnostic tool should we run?
```

Example result:

```text
top_cpu_procedures
```

Together:

```text
Vector Search = brings knowledge
Tool Router = chooses checks
Diagnostic Tools = collect evidence
Gemini = creates the final DBA answer
```

---

## Example

User question:

```text
high cpu
```

System behavior:

```text
1. Vector Search finds the High CPU troubleshooting article.
2. Tool Router selects top_cpu_procedures.
3. The CPU diagnostic tool runs against SQL Server.
4. The system builds a prompt with knowledge and evidence.
5. Gemini generates a structured DBA answer.
```

Example diagnostic context:

```text
Selected diagnostic tools: top_cpu_procedures
```

Meaning:

```text
The system identified this as a CPU-related question
and selected the Top CPU Procedures diagnostic tool.
```

---

## Why This Architecture Is Valuable

This architecture is stronger than a simple chatbot because it combines AI with real database diagnostics.

It demonstrates:

* Python development
* SQL Server DBA knowledge
* SQL Server DMV usage
* Vector search
* RAG architecture
* Agentic tool routing
* Prompt engineering
* AI integration with Gemini
* Clean project documentation

This makes the project suitable for a professional portfolio or resume.
