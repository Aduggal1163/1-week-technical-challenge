from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship
from database import Base

class Notes(Base):
    __tablename__='notes'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), unique=True)
    content=Column(String(100))