from fastapi import FastAPI
from evaluator.graph import workflow

app = FastAPI()


@app.post("/evaluate")
def evaluate(prompt: str):
    result = workflow.invoke({
        "prompt": prompt
    })

    return result