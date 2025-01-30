from fastapi import APIRouter,HTTPException, Depends
from sqlalchemy.orm import Session
from models.user import User
from dependencies import get_db
from schemas.user import UserCreate ,UserLogin, Token


user_router = APIRouter()

@user_router.post("/signup", tags=["auth"],)
def signup(
    user_data : UserCreate,
    db: Session = Depends(get_db),
):
    user = User(username= user_data.username,
                email = user_data.email,
                hashed_password = user_data.password,
                )
    user.hash_password(user_data.password)
    db.add(user)
    db.commit()
    
    return{
        'message' : "User has been created"
    }


@user_router.post('/login',tags=["auth"])
def login(
    user_data: UserLogin , db : Session = Depends(get_db)
):
    
    user = db.query(User).filter(User.username == user_data.username).first()
    
    if user is None or not user.verify_password(user.user_data.password):
        raise HTTPException (status_code=401, default ='Invalid Credentals')
    token = user.generate_token() 
    return Token(access_token= token, token_type='bearer')
