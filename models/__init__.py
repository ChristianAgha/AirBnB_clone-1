from models.engine import file_storage, db_storage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv

if getenv("HBNB_TYPE_STORAGE") == "db":
    storage = db_storage.DBStorage()
    CNC = db_storage.DBStorage.CNC
else:
    storage = file_storage.FileStorage()
    CNC = file_storage.FileStorage.CNC

storage.reload()
