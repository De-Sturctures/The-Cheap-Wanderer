from fastapi import APIRouter, Depends
from auth import get_current_user
from database import get_db
from models import SearchHistory
from caching import cache_data, get_cached_data
from schemas import UserCreate
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/")
def search(query: str, current_user: UserCreate = Depends(get_current_user), db: Session = Depends(get_db)):
    cache_key = f"search:{query}"
    cached_result = get_cached_data(cache_key)

    if cached_result:
        return {"cached": True, "data": cached_result}

    # Perform search operation (e.g., web scraping)
    result = {"query": query, "cheapest_flight": "$200", "cheapest_train": "$50"}  # Example

    # Store in Redis Cache
    cache_data(cache_key, result)

    # Save in MySQL Search History
    search_entry = SearchHistory(user_id=current_user.id, query=query)
    db.add(search_entry)
    db.commit()

    return {"cached": False, "data": result}
