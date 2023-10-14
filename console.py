#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    """custom console"""
    intro = "Our custom console, the HBNB"
    prompt = "(hbnb)"

    def do_quit(self, line):
        """exit the console on quit command"""
        return True

    def do_EOF(self, line):
        """exit the console on CTRL+D"""
        return True

    def emptyline(self):
        """do nothing upon getting a newline"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
