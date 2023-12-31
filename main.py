from os import environ
from typing import Optional
from fastapi import FastAPI, Form
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT

anthropic = Anthropic(
   # defaults to os.environ.get("ANTHROPIC_API_KEY")
)

app = FastAPI()

@app.post("/chat/complete")
def read_item(text: str=Form(...)):
    response = anthropic.completions.create(
        model="claude-2.1",
        max_tokens_to_sample=300,
        prompt=f"{HUMAN_PROMPT} {text}{AI_PROMPT}",
    )
    return {"messages":response.completions}