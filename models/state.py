#!/usr/bin/python3
"""
State Class from Models Module
"""
from sqlalchemy import Column, String
from sqlalchemy import *
from sqlalchemy.orm import *
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class handles all application states"""
    """if storage is db"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state')
    """if storage is file"""
    name = ''

    def __init__(self, *args, **kwargs):
        """instantiates a new state"""
        super().__init__(self, *args, **kwargs)
