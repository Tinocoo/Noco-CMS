from datetime import datetime
from sqlalchemy.inspection import inspect
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
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    