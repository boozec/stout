import redis
import sys
import socket

r = redis.Redis()

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
host = s.getsockname()[0]

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


class Command(object):

    info = {
        "info" : "this is stout",
        "set" : "set a value",
    }

    commands = {
        'quit' : None,
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


class Stout(object):

    def __init__(self):
        self.name = 'stout'
        self.user = Stout.username()

    def getName(self):
        word = " (" + self.name + ") "
        if self.user == '':
            return word
        else:
            return word + Colors.grey + "(" + self.user + ":" + host + ") "

    @staticmethod
    def username():
        if r.hget('user:'+host, 'name') is not None:
            return r.hget('user:'+host, 'name').decode("utf-8")
        else:
            return ''

    @staticmethod
    def userexist(name):
        lista = r.zrange('usersname', 0, -1)
        for i in lista:
            if name == i.decode("utf-8"):
                return True
        else:
            return False

    def command(self, what, cmd):
        if what == 'set':
            try:
                if cmd[1] == 'user' and cmd[2] is not None:
                    if len(cmd[2]) > 10: raise PersonalError("lunghezza maggiore del consetito. Max 10")

                    if Stout.userexist(cmd[2]) == True: raise PersonalError("questo nome utente esiste già")

                    if self.user != '': r.zrem('usersname', self.user)

                    self.user = cmd[2]
                    r.hset('user:'+host, 'name', self.user)
                    r.zadd('usersname', self.user, 0)

                    print("Ok")
                elif cmd[1] is not Command.commands['set']:
                    raise IndexError
            except IndexError:
                Command.err('wrong')
            except PersonalError as e:
                Command.err('personal', e.value)

    def action(self, cmd):
        if cmd is None:
            return None
        else:
            cmd = cmd.split()
            count = len(cmd)

            if (count == 1 or count == 2) and cmd[0] not in Command.commands:
                try:
                    if cmd[0] == 'info' and count == 1:
                        print(Command.info['info'])
                    else:
                        print(Command.info[cmd[1]])
                except (KeyError, IndexError):
                    Command.err('keyword')
            else:
                what = cmd[0]
                if what in Command.commands:
                    self.command(what, cmd)
                else:
                    Command.err('keyword')


if __name__ == '__main__':
    app = Stout()
    cmd = ''
    while cmd != 'quit':
        cmd = input(">" + Colors.yellow + app.getName() + Colors.black)
        app.action(cmd)
        r.save()

    s.close()
