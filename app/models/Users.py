from datetime import datetime
from sqlalchemy.schema import Column
from sqlalchemy.types import String, SmallInteger, Integer, DateTime
from app.models import db



class Users(db.Model):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(60), nullable=False, unique=False)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False, unique=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now(), onupdate=datetime.now())
    status = Column(SmallInteger, nullable=False, unique=False, default=1)
    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'status': self.status
        }
        