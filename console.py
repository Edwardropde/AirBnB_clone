#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage, storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User


storage = FileStorage()
storage.reload()
storage.add_class(BaseModel)
storage.add_class(User)
storage.add_class(State)
storage.add_class(City)
storage.add_class(Amenity)
storage.add_class(Review)


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class is a command interpreter for the AirBnB project.

    It uses the 'cmd' module to create a command line interface with a custom
    prompt, and provides commands to interact with the program.

    Attributes:
        prompt (str): The custom command prompt (default is '(hbnb)').

    Methods:
        do_quit(arg): Quit command to exit the program.
        do_EOF(arg): EOF command to exit the program.
    """

    prompt = "(hbnb) "

    def emptyline(self):
        pass

    def do_quit(self, arg):
        """
        Quit command to exit the program.

        Usage: quit
        """
        return True

    def do_EOF(self, arg):
        """
        EOF to exit the program.

        Usage: EOF
        """
        return True

    def help_quit(self):
        print("Quit command to exit the program")

    def help_EOF(self):
        print("Exit the program using EOF (Ctrl+D)")

    def do_create(self, arg):
        """Create a new instance of BaseModel"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return

        new_instance = storage.classes[class_name]()
        for attribute in args[1:]:
            key, value = attribute.split("=")
            value = value.strip("\"'")
            setattr(new_instance, key, value)
        new_instance.save(storage)
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints instance based on class name/all instances if class not given
        """
        args = arg.split()
        all_instances = storage.all()
        if not args:
            instance_list = [str(value) for value in all_instances.values()]
            return instance_list
        else:
            class_name = args[0]
            if class_name not in storage.classes:
                print("** class doesn't exist **")
                return
            class_instances = storage.all(class_name)
            instance_list = [str(value) for value in class_instances.values()]
            print(instance_list)

    def do_count(self, arg):
        """
        Counts the number of instances of a class.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        class_instances = storage.all(class_name)
        count = len(class_instances)
        print(count)

    def do_update(self, arg):
        """
        Updates instance based on class name &  id with new attribute value
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** dictionary missing **")
            return
        try:
            dictionary_str = args[2]
            dictionary = eval(dictionary_str)
            if not isinstance(dictionary, dict):
                raise ValueError("** invalid dictionary format **")
        except (ValueError, TypeError, NameError, SyntaxError):
            print("** value conversion error **")
            return
        obj = storage.all()[key]
        for attr_name, attr_value in dictionary.items():
            attr_type = type(getattr(obj, attr_name))
            try:
                if attr_type is int:
                    attr_value = int(attr_value)
                elif attr_type is float:
                    attr_value = float(attr_value)
            except (ValueError, TypeError):
                print("** value conversion error **")
                return
            setattr(obj, attr_name, attr_value)
        obj.save(storage)
        if len(args) > 4:
            print("Cannot use these arguments")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
