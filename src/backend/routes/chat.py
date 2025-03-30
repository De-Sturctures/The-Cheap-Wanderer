from fastapi import APIRouter
from backend.schemas import ChatRequest
from backend.llm import generate_response
from backend.memory import chat_memory

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat(request: ChatRequest):
    response = generate_response(request.message)
    chat_memory.add_message({"user": request.message, "bot": response})
    return {"response": response, "history": chat_memory.get_history()}