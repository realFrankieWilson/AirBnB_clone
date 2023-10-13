#!/usr/bin/python3
# console.py

# imports the cmd module
import cmd

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
