from app.db import save_diagnostic_run_history


def test_save_diagnostic_run_history():
    run_id = save_diagnostic_run_history(
        user_question="test high cpu question",
        selected_tools="top_cpu_procedures",
        knowledge_articles_used="High CPU Troubleshooting",
        diagnostic_context="Test diagnostic context",
        ai_answer="Test AI answer",
    )

    assert run_id is not None

    print(f"Diagnostic run history test passed. RunID: {run_id}")


if __name__ == "__main__":
    test_save_diagnostic_run_history()