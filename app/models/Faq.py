from flask import Markup
from datetime import datetime
from sqlalchemy.inspection import inspect
from sqlalchemy.schema import Column
from sqlalchemy.types import String, SmallInteger, Integer, DateTime, Text
from app.models import db



class Faq(db.Model):

    __tablename__ = 'faqs'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    title = Column(String(255), nullable=False, unique=False)
    url_img = Column(String(255), nullable=True, unique=False)
    body = Column(Text, nullable=False, unique=False, )
    button_text = Column(String(255), nullable=True, unique=False)
    button_link = Column(String(255), nullable=True, unique=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    status = Column(SmallInteger, nullable=False, unique=False, default=1)
    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'url_img': self.url_img,
            'body': Markup(self.body),
            'button_text': self.button_text,
            'button_link': self.button_link,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'status': self.status
        }
