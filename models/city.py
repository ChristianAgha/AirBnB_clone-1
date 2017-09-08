#!/usr/bin/python3
"""
City Class from Models Module
"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy import *
from sqlalchemy.orm import *
from models.base_model import BaseModel, Base
from os import getenv


class City(BaseModel, Base):
    """City class handles all application cities"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship('Place', backref='cities',
                              cascade='all, delete-orphan')
    else:
        state_id = ''
        name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new city"""
        super().__init__(self, *args, **kwargs)
