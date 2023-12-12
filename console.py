#!/usr/bin/python3
import cmd
import json
from models.engine.file_storage import storage


class HBNBCommand(cmd.Cmd):
    '''Entry point of the command interpreter'''
    prompt = "(hbnb) "

    def do_quit(self, args):
        """
        Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when EOF (Ctrl+D) is encountered
        """
        print()
        return True

    def emptyline(self):
        """
        Do nothing on empty line + ENTER
        """
        pass

    def do_create(self, arg):
        '''Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id.'''
        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        class_name = args[0]
        new_instance = storage.classes()[class_name]()
        storage.new(new_instance)
        storage.save()
        print(new_instance.id)

    def do_show(self, arg):
        '''Prints the string representation of an instance based on the class name and id.'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        instances_dict = storage.all().get(class_name, {})
        key = "{}.{}".format(class_name, instance_id)

        if key not in instances_dict:
            print("** no instance found **")
            return

        instance = instances_dict[key]
        print(instance)

    def do_destroy(self, arg):
        '''Deletes an instance based on the class name and id (save the change into the JSON file).'''
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        instance_id = args[1]
        instances_dict = storage.all().get(class_name, {})
        key = "{}.{}".format(class_name, instance_id)

        if key not in instances_dict:
            print("** no instance found **")
            return

        del instances_dict[key]
        storage.save()

    def do_all(self, arg):
        '''Prints all string representation of all instances based or not on the class name. '''
        args = arg.split()
        if args and args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        class_name = args[0]
        if class_name not in storage.all():
            print("[]")
            return

        instances = storage.all()[class_name].values()
        print(instances)

    def do_update(self, arg):
        '''
        Updates an instance based on the class name and id by adding or 
        updating attribute (save the change into the JSON file).
        '''
        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        attribute_name = args[2]
        attribute_value = args[3]

        instances_dict = storage.all().get(class_name, {})
        key = "{}.{}".format(class_name, instance_id)

        if key not in instances_dict:
            print("** no instance found **")
            return

        instance = instances_dict[key]
        setattr(instance, attribute_name, attribute_value)
        storage.save()

    def do_count(self, arg):
        '''To retrieve the number of instances of a class'''
        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class doesn't exist **")
            return

        class_name = args[0]
        count = len(storage.all().get(class_name, {}))
        print(count)

    def do_update_dict(self, arg):
        '''update an instance based on his ID with a dictionary'''
        args = arg.split()
        if not args or args[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        instance_id = args[1]
        instances_dict = storage.all().get(class_name, {})
        key = "{}.{}".format(class_name, instance_id)

        if key not in instances_dict:
            print("** no instance found **")
            return

        instance = instances_dict[key]

        if len(args) < 4:
            print("** dictionary missing **")
            return

        try:
            # Convert the dictionary string to a dictionary
            update_dict = eval(args[3])
            if not isinstance(update_dict, dict):
                raise ValueError("Invalid dictionary representation")
        except (SyntaxError, ValueError):
            print("** invalid dictionary representation **")
            return

        for key, value in update_dict.items():
            setattr(instance, key, value)
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
