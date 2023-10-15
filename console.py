#!/usr/bin/python3
"""Defines HBnB console"""


import cmd
import re
import json
import sys
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage, storage
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.user import User
from shlex import split


def parse(arg):
    thebrace = re.search(r"\{(.*?)\}", arg)
    bracks = re.search(r"\[(.*?)\]", arg)
    if thebrace is None:
        if bracks is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lex = split(arg[:bracks.span()[0]])
            rel = [i.strip(",") for i in lex]
            rel.append(bracks.group())
            return rel


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
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

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
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(args[0], args[1])]
            storage.save()        
        
    def do_all(self, arg):
        """
        Prints instance based on class name/all instances if class not given
        """
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            obj_dict = storage.all()
            for obj in obj_dict.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_count(self, arg):
        """
        Counts the number of instances of a class.
        """
        args = parse(arg)
        count = 0
        for obj in storage.all().values():
            if args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Updates instance based on class name &  id with new attribute value
        """
        args = parse(arg)
        obj_dict = storage.all()
        if len(args) == 0:
            sys.stderr.write("** class name missing **")
            return
        if args[0] not in HBNBCommand.__classes:
            sys.stderr.write("** class doesn't exist **")
            return
        if len(args) < 2:
            sys.stderr.write("** instance id missing **")
            return
        obj_id = args[1]
        key = "{}.{}".format(args[0], obj_id)
        if key not in obj_dict:
            sys.stderr.write("** no instance found **")
            return
        if len(args) < 3:
            sys.stderr.write("** attribute name missing **")
            return
        if len(args) < 4:
            sys.stderr.write("** value missing **")
            return
        obj = obj_dict[key]
        attribute_name = args[2]
        attribute_value = args[3]
        if attribute_value.startswith("{") and attribute_value.endswith("}"):
            try:
                attribute_value = json.loads(attribute_value)
            except ValueError:
                sys.stderr.write("** invalid dictionary format **")
                return
        if attribute_name in obj.__class__.__dict__.keys():
            attr_type = type(obj.__class__.__dict__[attribute_name])
            try:
                if attr_type is int:
                    attribute_value = int(attribute_value)
                elif attr_type is float:
                    attribute_value = float(attribute_value)
            except (ValueError, TypeError):
                sys.stderr.write("** value conversion error **")
                return
        setattr(obj, attribute_name, attribute_value)
        obj.save(storage)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
