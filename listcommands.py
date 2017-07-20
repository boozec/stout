import sys
from classes import Colors

class ListCommands(object):

    info = {
        "info" : "this is stout",
        "set" : "set a value",
    }

    commands = {
        'quit' : None,
        'clear' : None,
        'set' : ['user', 'host'],
        'get' : None
    }

    @staticmethod
    def err(err, info = ''):
        if err == 'keyword':
            sys.stderr.write(Colors.red + "keyword inesistente\n" + Colors.black)
        elif err == 'wrong':
            sys.stderr.write(Colors.red + "sintassi comando errata\n" + Colors.black)
        elif err == 'personal':
            sys.stderr.write(Colors.red + str(info) + "\n" + Colors.black)
        else:
            pass
