from nemoguardrails import LLMRails
from nemoguardrails.rails import RailsConfig

config = RailsConfig.from_path("app/guardrails")
rails = LLMRails(config)


async def evaluate_safety(prompt: str):
    response = await rails.generate_async(prompt=prompt)

    return {
        "safe_response": response
    }