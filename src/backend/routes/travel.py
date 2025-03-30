from fastapi import APIRouter, Depends
from backend.schemas import TravelRequest
from backend.scraping import scrape_travel_data

router = APIRouter(prefix="/travel", tags=["Travel"])

@router.post("/recommend")
def get_travel_recommendations(request: TravelRequest):
    return scrape_travel_data(f"https://example.com/flights?dest={request.destination}")