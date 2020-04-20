from datetime import datetime
from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, SmallInteger, Integer, DateTime
from app.models import db



class Category(db.Model):

    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    description = Column(String(60), nullable=False, unique=False)
    post_id = Column(Integer, ForeignKey('posts.id'), nullable=True, unique=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    status = Column(SmallInteger, nullable=False, unique=False, default=1)
    

    @property
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    
    def __repr__(self):
        return self.description
