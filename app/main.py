from fastapi import FastAPI
from app.routes import auth, users

app = FastAPI()

@app.get("/")
def home():
  return {'message': 'Application is Running..'}

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth.router)
app.include_router(users.router)

