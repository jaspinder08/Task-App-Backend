import uvicorn 
from fastapi import FastAPI
from database import Base,engine
from routers.users import user_router




app = FastAPI()

app.include_router(user_router, prefix='/auth')

Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run('app:app' ,host='0.0.0.0',port=8080,reload=True,)