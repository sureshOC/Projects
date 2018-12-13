from sqlalchemy import Column, Integer, String, func, DateTime
from app.database import Base

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    password = Column(String)
    role = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())