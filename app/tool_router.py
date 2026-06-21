def route_tools(user_question):
    """
    Decides which diagnostic tools should run based on the user's question.

    This is the first routing layer of the DBA Agent.
    It does not run the tools directly.
    It only returns the names of the tools that should be executed.
    """

    question_lower = user_question.lower()
    selected_tools = []

    cpu_keywords = [
        "cpu",
        "high cpu",
        "processor",
        "performance",
        "slow server",
        "server is slow",
    ]

    blocking_keywords = [
        "blocking",
        "blocked",
        "lock",
        "locks",
        "stuck",
        "waiting",
        "users are stuck",
    ]

    wait_stats_keywords = [
        "wait",
        "waits",
        "wait stats",
        "slow",
        "latency",
    ]

    long_query_keywords = [
        "long query",
        "long running",
        "running long",
        "slow query",
        "expensive query",
    ]

    if any(keyword in question_lower for keyword in cpu_keywords):
        selected_tools.append("top_cpu_procedures")

    if any(keyword in question_lower for keyword in blocking_keywords):
        selected_tools.append("blocking_sessions")

    if any(keyword in question_lower for keyword in wait_stats_keywords):
        selected_tools.append("wait_stats")

    if any(keyword in question_lower for keyword in long_query_keywords):
        selected_tools.append("long_running_queries")

    return selected_tools