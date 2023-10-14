#!/usr/bin/python3
"""This is the entry point of our program """
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """custom console"""
    intro = "Our custom console, the HBNB"
    prompt = "(hbnb)"
    classes = { "BaseModel"}

    def do_quit(self, line):
        """exit the console on quit command"""
        return True

    def do_EOF(self, line):
        """exit the console on CTRL+D"""
        return True

    def emptyline(self):
        """do nothing upon getting a newline"""
        pass
    def do_create(self, line):
        """ saves intances of the basemodel in the JSON file and prints it"""
        if len(line) == 0: # check if a user provide any argument
            print("** class name missing **")
        elif line not in HBNBCommand.classes: # if classname is provided but does not exist in list of classes
            print("** class doesn't  exist **")
        else:
            # if the classname exist and is provided
            bsmodel= eval(line)()
            bsmodel.save() # save to the jsonfile
            print(bsmodel.id)



if __name__ == '__main__':
    HBNBCommand().cmdloop()
