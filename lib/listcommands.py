import sys
from classes import Colors

class ListCommands(object):
    """
    ListCommands is used for return errors and check what commands exists
    """

    info = {
        'info' : 'this is stout',
        'set' : ['set a value', 3],
        'get' : ['return a value', 3]
    }

    commands = {
        'quit' : None,
        'clear' : None,
        'set' : ['user'],
        'get' : ['i', ['user', 'host', 'port', 'unix_socket_path', 'db'], 'user?']
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
