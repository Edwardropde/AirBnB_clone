#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Serialize instances to JSON file, deserialize JSON file to instance."""

    __file_path = "file.json"
    __objects = {}
    classes = {
        'BaseModel': BaseModel,
        'User': User,
        'Place': Place,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Review': Review,
    }

    def all(self, cls=None):
        """Returns the dictionary __objects."""
        if cls:
            instances = {k: v for k, v in self.__objects.items() if v.__class__ == cls}
        else:
            instances = self.__objects
        return instances

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)."""
        obj_dict = {}
        for key, value in self.__objects.items():
            obj_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    class_type = self.classes.get(class_name, None)
                    if class_type:
                        obj = class_type(**value)
                        self.__objects[key] = obj

    def add_class(self, class_obj):
        """Add a class to the classes dictionary."""
        class_name = class_obj.__name__
        self.classes[class_name] = class_obj

    def serializable(self):
        """
        Serializes objects for JSON storage.
        """
        data = {}
        for key, value in self.__objects.items():
            class_name = value.__class__.__name__
            if class_name not in data:
                data[class_name] = {}
            data[class_name][value.id] = value.to_dict()
        return data

    def deserializable(self):
        """
        Deserializes JSON data to recreate objects.
        """
        data = self.reload()
        objects = {}
        for class_name, objects_dict in data.items():
            class_type = self.classes.get(class_name, None)
            if class_type:
                for obj_id, obj_data in objects_dict.items():
                    obj = class_type(**obj_data)
                    objects[obj.id] = obj
        self.__objects = objects


storage = FileStorage()
storage.reload()
