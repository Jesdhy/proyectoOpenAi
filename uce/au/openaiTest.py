import openai
from pydantic import BaseModel


class Document(BaseModel):
    prompt: str = ' '


def inference(prompt: str) -> list:
    print("PROCESSABLE")
    openai.organization = 'org-CchAKJZNmsw58UYwmpUBTXZS'
    openai.api_key = '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'

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": """You are a programming teacher for children, 
            E.G: programming 
            -It's like putting together a puzzle where each piece forms a complete system"""},
            {"role": "user", "content": prompt}
        ]
    )
    print("TERMINATE")
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    return [content, total_tokens]
