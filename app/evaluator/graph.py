from typing import TypedDict
from langgraph.graph import StateGraph, END


class EvalState(TypedDict):
    prompt: str
    response: str
    safety: dict
    ragas: dict


def generate_node(state):
    from evaluator.llm_runner import generate_response

    response = generate_response(state["prompt"])

    return {
        **state,
        "response": response
    }


def safety_node(state):
    return {
        **state,
        "safety": {
            "status": "checked"
        }
    }


def ragas_node(state):
    return {
        **state,
        "ragas": {
            "faithfulness": 0.91
        }
    }


graph = StateGraph(EvalState)

graph.add_node("generate", generate_node)
graph.add_node("safety", safety_node)
graph.add_node("ragas", ragas_node)

graph.set_entry_point("generate")

graph.add_edge("generate", "safety")
graph.add_edge("safety", "ragas")
graph.add_edge("ragas", END)

workflow = graph.compile()