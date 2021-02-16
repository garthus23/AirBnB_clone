#!/usr/bin/python3
""" module cmd """
import cmd

"""
    class HBNBCommand
"""

class HBNBCommand(cmd.Cmd):
    """ HBNBCommand """

    def emptyline(self):
        """ empty line """
        pass

    def do_EOF(self, line):
        """Quit shortcut to exit the program\n"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program\n"""
        return True

if __name__ == '__main__':
    prompt = HBNBCommand()
    prompt.prompt = '(hbnb) '
    prompt.cmdloop()
