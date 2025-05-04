from sqlalchemy import Column, String, Float, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = "products"

    id = Column(String, primary_key=True, index=True)
    name = Column(String, nullable=False)
    rate = Column(Float, nullable=False)
    min_amount = Column(Float, nullable=False)
    max_amount = Column(Float, nullable=False)
    min_term = Column(Integer, nullable=False)
    max_term = Column(Integer, nullable=False)
    color = Column(String, nullable=False)
