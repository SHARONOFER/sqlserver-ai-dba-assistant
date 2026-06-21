from app.tool_router import route_tools


def test_cpu_question_routes_to_cpu_tool():
    tools = route_tools("high cpu on sql server")

    assert "top_cpu_procedures" in tools


def test_blocking_question_routes_to_blocking_tool():
    tools = route_tools("users are blocked and stuck")

    assert "blocking_sessions" in tools


def test_slow_server_routes_to_multiple_tools():
    tools = route_tools("the sql server is slow")

    assert "top_cpu_procedures" in tools
    assert "wait_stats" in tools


def test_unrelated_question_returns_no_tools():
    tools = route_tools("how many databases do I have")

    assert tools == []


if __name__ == "__main__":
    test_cpu_question_routes_to_cpu_tool()
    test_blocking_question_routes_to_blocking_tool()
    test_slow_server_routes_to_multiple_tools()
    test_unrelated_question_returns_no_tools()

    print("All tool router tests passed successfully.")