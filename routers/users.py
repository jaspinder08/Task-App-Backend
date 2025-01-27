from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from db.user import User
from dependencies import get_db
from schemas.user import UserCreate ,UserLogin


user_router = APIRouter()

@user_router.post("/signup", tags='auth',)
def signup(
    user_data : UserCreate,
    db: Session = Depends(get_db),
):
    user = User(username= user_data.username,
                email = user_data.email,
                password = user_data.password,
                )
    return
