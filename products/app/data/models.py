from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, func
from sqlalchemy.orm import relationship
from app.data.base import Base

class Category(Base):
    __tablename__ = 'Categories'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    products = relationship('Product', back_populates='category')

class Product(Base):
    __tablename__ = 'Products'
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    slug = Column('slug', String, nullable=False)
    slug = Column('price', Float, nullable=False)
    stock = Column('stock', Integer, nullable=False)
    created_at = Column('created_at', DateTime, server_default=func.now())
    updated_at = Column('updated_at', DateTime, server_default=func.now(), onupdate=func.now())
    category_id = Column('category_id', ForeignKey('Categories.id'), nullable=False)
    category = relationship('Category', back_populates='products')