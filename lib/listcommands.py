import sys
from classes import Colors

class ListCommands(object):

    info = {
        'info' : 'this is stout',
        'set' : ['set a value', 3],
    }

    commands = {
        'quit' : None,
        'clear' : None,
        'set' : ['user'],
        'get' : ['user', 'user?', 'host', 'port']
    }

    @staticmethod
    def err(err, info = ''):
        if err == 'keyword':
            sys.stderr.write(Colors.red + 'keyword inesistente\n' + Colors.black)
        elif err == 'wrong':
            sys.stderr.write(Colors.red + 'sintassi comando errata\n' + Colors.black)
        elif err == 'personal':
            sys.stderr.write(Colors.red + str(info) + '\n' + Colors.black)
        else:
            pass
