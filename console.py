#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):

    def emptyline(self):
        pass

    def do_create(self, line):


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
