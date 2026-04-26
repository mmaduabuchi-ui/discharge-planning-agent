from agent.discharge_summarizer import build_discharge_summary


def run_discharge_tool(patient_id: str):
    """
    MCP TOOL:
    Generates a structured discharge summary for any agent that calls it.
    """

    result = build_discharge_summary(patient_id)

    return {
        "tool_name": "discharge_summary_tool",
        "status": "success",
        "data": result
    }