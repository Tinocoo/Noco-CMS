from datetime import datetime
from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import String, SmallInteger, Integer, DateTime
from app.models import db



class MenuLists(db.Model):

    __tablename__ = 'menu_lists'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    description = Column(String(60), nullable=False, unique=False)
    menu_id = Column(Integer, ForeignKey('menu_settings.id'), nullable=True, unique=False)
    url = Column(String(255), nullable=False, unique=False)
    
    @property
    def serialize(self):
        return {c: getattr(self, c) for c in inspect(self).attrs.keys()}
    
    def __repr__(self):
        return self.description
