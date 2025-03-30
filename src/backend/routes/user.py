from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.auth import get_password_hash, verify_password, create_access_token, get_current_user
from backend.models import User, SearchHistory
from backend.schemas import UserCreate, UserLogin, Token

router = APIRouter()

# Define route for sign-up for new users
@router.post("/signup", response_model=Token)
def signup(user: UserCreate, db: Session = Depends(get_db)):

    existing_user = db.query(User).filter(User.username == user.username).first()
    #Check if the user exists
    if existing_user:
        #raise error
        raise HTTPException(status_code=400, detail="Username already taken")
    # get the password
    hashed_password = get_password_hash(user.password)
    #encryt password
    new_user = User(username=user.username, password_hash=hashed_password)

    #add new user data to database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    #assign a new access token
    access_token = create_access_token(data={"sub": str(new_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

# Define route for login for existing users
@router.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):

    #fetch data using user-name
    db_user = db.query(User).filter(User.username == user.username).first()

    #Check user details
    if not db_user or not verify_password(user.password, db_user.password_hash):

        #raise error if data doesn't match
        raise HTTPException(status_code=401, detail="Invalid credentials")

    #create session access token
    access_token = create_access_token(data={"sub": str(db_user.id)})
    return {"access_token": access_token, "token_type": "bearer"}

# define search history for search history for the current user
@router.get("/history")
def get_search_history(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    history = db.query(SearchHistory).filter(SearchHistory.user_id == current_user.id).all()
    return history
