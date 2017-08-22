import sys
from classes import RED, BLACK

class ListCommands(object):
    """
    ListCommands is used for return errors and check what commands exists
    """

    info = {
        'info' : '''Stout è distribuito sotto licenza MIT e pertanto è possibile farne il fork, modificarlo e distribuirlo nuovamente.
La lista dei comandi è disponibile su https://github.com/dcariotti/Stout.
Scrivere info [cmd] per avere più informazioni su un comando.''',
        'set' : ['''Inserire un valore; accetta solo 1 parametro (user) e viene utilizzato nel modo seguente: set user NAME''', 3],
        'get' : ['''Ritorna un valore e accetta i parametri todo (ritorna la lista dei todo) e ctodo (ritorna il numero dei todo).
Se utilizzato con il "flag" i, si possono visualizzare le info: get i host, get i port, get i unix_socket_path, get i db, get i user''', 3],
        'add' : ['Inserisce un nuovo todo: ogni carattere dopo add sarà considerato tale',],
        'del' : ['Elimina un todo in base alla sua chiave di valore; per vederle tutte, digitare get todo', 2]
    }

    commands = {
        'quit' : None,
        'set' : ['user'],
        'get' : ['i', ['user', 'host', 'port', 'unix_socket_path', 'db'], 'todo', 'ctodo'],
        'add' : None,
        'del' : None,
    }

    @staticmethod
    def err(err, info = ''):
        if err == 'KeyError':
            sys.stderr.write(RED + 'keyword inesistente\n' + BLACK)
        elif err == 'IndexError':
            sys.stderr.write(RED + 'sintassi comando errata\n' + BLACK)
        elif err == 'personal':
            sys.stderr.write(RED + str(info) + '\n' + BLACK)
        else:
            pass
