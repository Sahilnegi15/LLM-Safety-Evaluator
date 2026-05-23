from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy
from datasets import Dataset


def evaluate_rag(question, answer, context):
    data = {
        "question": [question],
        "answer": [answer],
        "contexts": [[context]]
    }

    dataset = Dataset.from_dict(data)

    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy]
    )

    return result