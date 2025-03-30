from fastapi import FastAPI
from routes import travel, chat, search, user
from rate_limiter import limiter
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust based on security needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add Rate Limiting Middleware
app.state.limiter = limiter

# Include API routes
app.include_router(user.router, prefix="/user", tags=["User"])
app.include_router(travel.router, prefix="/travel", tags=["Travel"])
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(search.router, prefix="/search", tags=["Search"])

@app.get("/")
def root():
    return {"message": "Welcome to The Cheap Wanderer API"}
