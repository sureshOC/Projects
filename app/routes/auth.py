from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database import get_db
from app.models import Base, UserDB
from app.schemas import User
from app.auth import hash_password, verify_password, create_access_token


router = APIRouter()

@router.post('/register')
def register(user: User, db: Session = Depends(get_db)):
  # db = get_db()
  existing_user = db.query(UserDB).filter(UserDB.username == user.username).first()
  if existing_user:
    raise HTTPException(status_code=400, detail="User already exists")

  user_dict = UserDB(
    username=user.username,
    password=hash_password(user.password),
    role=user.role
  )
  db.add(user_dict)
  db.commit()

  return f'{user.username}: registered into database with role: {user.role}'


@router.post('/login')
def login(user: User, db: Session = Depends(get_db)):
  db_user = db.query(UserDB).filter(UserDB.username == user.username).first()

  if db_user and verify_password(user.password, db_user.password) and db_user.role == user.role:
    token = create_access_token({
      'sub': db_user.username,
      'role': db_user.role
    })
    return f"{db_user.username} login success. Access Token: {token}"

  raise HTTPException(status_code=401, detail="Invalid credentials")
