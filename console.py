#!/usr/bin/python3
""" module cmd """
import cmd
from models.base_model import BaseModel
from models import storage

"""
    class HBNBCommand
"""


class HBNBCommand(cmd.Cmd):
    """ HBNBCommand """

    def emptyline(self):
        """ empty line """
        pass

    def do_create(self, line):
        """ create something, an object i think """
        if line:
            l = line.split()
            my_model = BaseModel()
            my_model.name = l[0]
            my_model.save()
            print(my_model.id)
        else:
            print("** class name missing **")

    def do_show(self, line):
        """ show something """
        if not line:
            print("** class name missing **")
        else:
            l = line.split()
            if len(l) < 2:
                print("** instance id missing **")
            else:
                all_objs = storage.all()
                ok_found = 0
                for obj_id in all_objs.keys():
                    if obj_id == "{}.{}".format(l[0], l[1]):
                        obj = all_objs[obj_id]
                        print(obj)
                        ok_found = 1
                if ok_found == 0:
                    print("** no instance found **")

    def do_all(self,line):
        """ show must go on """
        all_objs = storage.all()
        for obj_id in all_objs.keys():
            if not line:
                obj = all_objs[obj_id]
                print(obj)
            else:
                l = line.split()
                if len(l) == 1:
                    obj1 = obj_id.split(".")
                    if obj1[0] == l[0]:
                        obj = all_objs[obj_id]
                        print(obj)
                        
            

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
