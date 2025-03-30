from pydantic import BaseModel

class TravelRequest(BaseModel):
    start_date: str
    end_date: str
    destination: str

class ChatRequest(BaseModel):
    message: str