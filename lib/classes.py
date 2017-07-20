import redis, socket, os
from config import config as co

r = redis.Redis(host=co['host'], port=co['port'], unix_socket_path=co['unix_socket_path'], db=co['db'])
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(('8.8.8.8', 80))
host = s.getsockname()[0]

def clear():
    try:
        os.system('clear')
    except:
        os.system('cls')

def userexist(name):
    lista = r.zrange('usersname', 0, -1)
    for i in lista:
        if name == i.decode('utf-8'):
            return True
        else:
            return False

class PersonalError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Colors(object):

    red = '\033[91m'
    yellow = '\033[93m'
    grey = '\033[90m'
    black = '\033[0m'
    bold = '\033[1m'
