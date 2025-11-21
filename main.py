from openai import OpenAI
import json


client = OpenAI()

def gptGPTRespond(prompt: dict):
    response = client.responses.create(
        model= "gpt-5",
        input=[
            {
                "role": "system",
                "content": (
                    "You are a helpful and knowledgeable assistant. "
                    "Always provide clear, accurate, and concise answers. "
                    "Always return VALID JSON. Thank you."
                )
            },
            {
                "role": "user",
                "content": json.dumps(prompt, indent=2)
            }
        ],
        text={
            "format": {
                "type": "json_object"
            }
        }
    )
    return response.output_text

# template = {
#   "task": "summarize",
#   "input": "JSON prompts are better for consistency, reliability, and control, especially in production environments, while normal text prompts are better for flexible, creative, and conversational tasks. JSON's structured format precisely defines instructions, reducing misinterpretation and ensuring the AI provides consistent, predictable results. Normal prompts are more akin to natural language and excel when the goal is a free-form, human-like interaction",
#   "output_format": {
#     "summary": "string"
#   }
# }

# template = {
#   "context": "You are a productivity assistant.",
#   "task": "Generate 3 tasks from the topic.",
#   "input": "Improve mobile app performance",
#   "output_format": {
#     "tasks": [
#       {
#         "title": "string",
#         "description": "string",
#         "priority": "low | medium | high"
#       }
#     ]
#   }
# }

template = {
    "role": "Strict Service Generator",
    "objective": "Generate exactly 40 unique and highly relevant residential and commercial service names for a given business type and city/cities.",
    "inputs": {
        "business_type": "GYM Instruction",
        "cities": "Delhi, Mumbai, Kolkata"
    },
    "rules": [
        "If there is only ONE city, return a JSON object with the city name as the key and an array of 40 service names as values.",
        "If there are MULTIPLE cities, return a JSON object with each city as a separate key, each containing an array of exactly 40 service names customized for that city.",
        "Include the city name in each service name (e.g., 'Personal Training').",
        "All service names must be unique and highly relevant to the business type.",
        "Return the response ONLY as valid JSON with no explanations, introductions, or extra text.",
        "Do not send partial responses — the output must be fully complete."
    ],
    "output_format": {
        "type": "json",
        "single_city_example": {
            "Kolkata": [
                "<string>",
            ]
        },
        "multiple_cities_example": {
            "Kolkata": [
                "<string>",
            ],
            "Delhi": [
                "<string>",
            ],
            "Mumbai": [
                "<string>",
            ]
        }
    },
};
output =  gptGPTRespond(template)
print(output);