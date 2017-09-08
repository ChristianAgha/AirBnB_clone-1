#!/usr/bin/python3
"""
Place Class from Models Module
"""
from sqlalchemy import *
from sqlalchemy.orm import *
from models.base_model import BaseModel, Base
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == 'db':
    metadata = Base.metadata
    place_amenity = Table("place_amenity", metadata,
                          Column("place_id", String(60),
                                 ForeignKey("places.id"), nullable=False),
                          Column("amenity_id", String(60),
                                 ForeignKey("amenities.id"), nullable=False))


class Place(BaseModel, Base):
    """
    Place class handles all application places
    """

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'places'
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, default=0, nullable=False)
        number_bathrooms = Column(Integer, default=0, nullable=False)
        max_guest = Column(Integer, default=0, nullable=False)
        price_by_night = Column(Integer, default=0, nullable=False)
        latitude = Column(Float)
        longitude = Column(Float)
        amenities = relationship('Amenity', secondary="place_amenity",
                                 viewonly=False)
        reviews = relationship('Review', backref='place',
                               cascade="all, delete-orphan")

    else:
        city_id = ''
        user_id = ''
        name = ''
        description = ''
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = ['', '']

    def __init__(self, *args, **kwargs):
        """instantiates a new place"""
        super().__init__(self, *args, **kwargs)
