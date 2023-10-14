#!/usr/bin/python3
# console.py

# imports the cmd module
import cmd
from models.base_model import BaseModel
from models import storage
import re

"""
This module conatains the entry point of the command line interpreter
Implementations:
    quit and EOF -> Exit the program.
    help -> help documentation for the module.
    custom prompt -> (hbnb)
    Empty + ENTER -> Executes anything.
"""


class HBNBCommand(cmd.Cmd):
    """A customized cmd interpreter."""
    prompt = "(hbnb) "
    classes_lists = ['BaseModel']

    def do_EOF(self):
        """Quit command to exit the program
        """
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Does nothing when <Enter> key is pressed without argument
        """
        pass

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel,
        and Saves it to the json file. Afterwards print it
        """
        if arg is None or arg == '':
            print("** class name is missing **")
        elif arg not in HBNBCommand.classes_lists:
            print("** class doesn't exit **")
        else:
            classes = HBNBCommand.classes_lists()[arg]()
            obj.save()
            print(obj.id)

    def do_show(self, arg):
        """
        Prints the string representation of an instance based
        on the class name and id.
        """
        if arg is None or arg == '':
            print("** class name missing **")
        else:
            obj = arg.split(' ')
            if obj[0] not in storage.classes_lists():
                print("** class doesn't exist **")
            elif len(obj) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(obj[0], obj[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, arg):
        """
        Destroys an instance based
        on the class name and id.
        """
        if arg is None or arg == '':
            print("** class name missing **")
        else:
            obj = arg.split(' ')
            if obj[0] not in storage.classes_lists():
                print("** class doesn't exist **")
            elif len(obj) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(obj[0], obj[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, arg):
        """Prints all string representation all instances
        based or not in the class name"""
        if arg is not "":
            obj = arg.split(' ')
            if obj[0] not in storage.classes_lists():
                print("** class doesn't exist **")
            else:
                lists = [
                    str(objs) for key, objs in storage.all().items() if
                    type(objs).__name__ == obj[0]
                    ]
                print(lists)
        else:
            lists = [
                str(objs) for key, objs in storage.all().items()
            ]
            print(lists)

    def do_update(slef, arg):
        """Updates an instance based on the class name and id by adding or
        updating attributes.
        """
        if arg is None or arg == "":
            print("** class name missing")
            return

        exp = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        to_match = re.search(exp, arg)
        classes_lists = match.group(1)
        usrid = to_match.group(2)
        attr = to_match.group(3)
        val = to_match.group(4)
        if not to_match:
            print("** class name missing **")
        elif classes_lists not in storage.classes_lists():
            print("** class doesn't exist **")
        elif usrid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classes_lists, usrid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attr:
                print("** attribute name missing **")
            elif not val:
                print("** value missing **")
            else:
                val_type = None
                if not re.search('^".*"$', val):
                    if '.' in val:
                        val_type = float
                    else:
                        val_type = int
                else:
                    val = val.replace('"', '')
                    all_atr = storage.all_attr()[classes_lists]
                    if attr in all_attr:
                        val = all_attr[attr](val)
                    elif val_type:
                        try:
                            val = val_type(val)
                        except ValueError:
                            pass    # meanning we are on string, and that's ok
                    setattr(storage.all()[key], attr, val)
                    storage.all()[key].save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
