from langgraph.graph import StateGraph, START, END
from agent_state import AgentState
from nodes import extract_pdf, identify_fields,highlight_fields

builder = StateGraph(AgentState)

builder.add_node("extract_pdf", extract_pdf)
builder.add_node("identify_fields", identify_fields)
builder.add_node("highlight_fields", highlight_fields)

builder.add_edge(START, "extract_pdf")
builder.add_edge("extract_pdf", "identify_fields")
builder.add_edge("identify_fields", "highlight_fields")
builder.add_edge("highlight_fields", END)

graph = builder.compile()


