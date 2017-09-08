#!/usr/bin/python3
"""
Database Storage Engine DBStorage
"""
from sqlalchemy import create_engine, func, MetaData
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from models.state import State
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.user import User


class DBStorage:
    """
    class DBStorage
    """
    __engine = None
    __session = None
    CNC = {
        'Amenity': Amenity,
        'City': City,
        'Place': Place,
        'Review': Review,
        'State': State,
        'User': User
    }

    def __init__(self):
        """
        initialize engine
        """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                                getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')))

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """
        queries all or selected database objects
        """
        objs = {}
        if cls is not None:
            for item in self.__session.query(self.CNC[cls]).all():
                key = str(cls) + "." + item.id
                objs[key] = item
        else:
            for clas in self.CNC.values():
                for item in self.__session.query(clas).all():
                    key = type(item).__name__ + "." + str(item.id)
                    objs[key] = item
        return (objs)

    def new(self, obj):
        """
        add new object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        """
        if obj is not None:
            self.__session.delete(obj)
            self.__session.commit()

    def reload(self):
        """
        create all tables in the database
        """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = scoped_session(Session)

    def close(self):
        """calls remove() method"""
        self.__session.remove()
