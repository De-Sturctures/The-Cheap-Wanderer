from fastapi import APIRouter
from backend.search import search_duckduckgo

router = APIRouter(prefix="/search", tags=["Search"])

@router.get("/")
def search(query: str):
    return search_duckduckgo(query)