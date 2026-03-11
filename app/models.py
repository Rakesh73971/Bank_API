from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Bank(Base):
    __tablename__ = "banks"

    id = Column(Integer,primary_key=True,nullable=False)
    name = Column(String,nullable=False)
    branches = relationship("Branch",back_populates="bank")

class Branch(Base):
    __tablename__ = "branches"

    id = Column(Integer,primary_key=True,nullable=False)
    bank_id = Column(Integer,ForeignKey("banks.id"))
    branch_name = Column(String,nullable=False)
    city = Column(String,nullable=False)
    ifsc = Column(String,nullable=False)
    bank = relationship("Bank",back_populates='branches')


