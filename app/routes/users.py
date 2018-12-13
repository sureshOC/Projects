from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends

from app.database import get_db
from app.models import Base, UserDB
from app.dependencies import  get_current_user, get_current_admin_user

router = APIRouter()

@router.get('/users/list')
def users_list(db: Session = Depends(get_db)):
  db_user = db.query(UserDB).all()
  users = [{'username': user.username,
            'role': user.role
            } for user in db_user]

  return f'{users}'


@router.get("/users/me")
def get_me(current_user: dict = Depends(get_current_user)):
    return {"user": current_user}


@router.get("/admin")
def admin_dashboard(admin: dict = Depends(get_current_admin_user)):
    return {"msg": f"Welcome admin {admin['sub']}"}
