from langchain.llms import OpenAI
from backend.config import LLM_API_KEY

llm = OpenAI(api_key=LLM_API_KEY)

def generate_response(prompt: str):
    return llm.generate(prompt)