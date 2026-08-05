from database import Base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import column,Integer, String, Boolean, text, TIMESTAMP, ForeignKey
from datetime import datetime
class Post(Base):
    __tablename__="posts"
    id: Mapped[int]= mapped_column(Integer,primary_key =True, nullable= False)
    title: Mapped[str]= mapped_column(String, nullable = False)
    content : Mapped[str]= mapped_column(String, nullable= False)
    published: Mapped[bool]= mapped_column(Boolean, nullable=False, server_default= 'True')
    createdat: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), nullable=False, server_default= text('now()'))
    ownerid:Mapped[int] = mapped_column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User")
class User (Base):
    __tablename__ = "users"
    id:Mapped[int]=mapped_column(Integer, primary_key=True, nullable=False)
    email:Mapped[str]=mapped_column(String, nullable=False, unique=True)
    password:Mapped[str]=mapped_column (String, nullable=False)
    created_at:Mapped[datetime]=mapped_column (TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))

class Vote (Base):
    __tablename__ = "votes"
    user_id:Mapped[int]=mapped_column(Integer, ForeignKey ("users.id", ondelete="CASCADE"), primary_key=True)
    post_id : Mapped[int]=mapped_column(Integer, ForeignKey("posts.id", ondelete="CASCADE"), primary_key=True)