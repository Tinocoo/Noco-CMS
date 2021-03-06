from datetime import datetime
from flask import Markup
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column
from sqlalchemy.types import String, SmallInteger, Integer, DateTime, Text
from app.models import db



class Posts(db.Model):

    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    title = Column(String(255), nullable=False, unique=False)
    thumbnail = Column(String(255), nullable=True, unique=False)
    description = Column(Text, nullable=False, unique=False)
    categories = relationship("Category", backref="post")
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    status = Column(SmallInteger, nullable=False, unique=False, default=1)
    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'thumbnail': self.thumbnail,
            'description': Markup(self.description),
            'categories': self.categories,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'status': self.status
        }
    