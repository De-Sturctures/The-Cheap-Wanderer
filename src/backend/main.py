from fastapi import FastAPI
from backend.routes import travel, chat, search

app = FastAPI()

# Include routes
app.include_router(travel.router)
app.include_router(chat.router)
app.include_router(search.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to The Cheap Wanderer API"}
