from sqlalchemy import Column, Integer, String
from database import Base

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_email = Column(String)
    amount = Column(Integer)
    status = Column(String)
