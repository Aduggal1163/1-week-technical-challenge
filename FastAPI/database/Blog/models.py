from sqlalchemy import Column, Integer, String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__='users'
    id = Column(Integer, primary_key=True, index=True) #index means it will increase performance a lil bit whenever we search using id
    username = Column(String(50), unique=True)
    # Relationship: One user can have many posts
    posts = relationship("Post", back_populates="owner")
    #back_populates means “This relationship on this model is connected to that relationship on the other model.”

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title=Column(String(50))
    content = Column(String(100))
    user_id = Column(Integer,ForeignKey('users.id'))
    # Relationship
    owner = relationship("User", back_populates="posts")