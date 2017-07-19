import redis
import sys

r = redis.Redis()

if r.get('iduser') is None:
    r.set('iduser', '0')

def iduser():
    try:
        with open('myid.txt', 'r') as f:
            iduser = f.read()

    except FileNotFoundError:
        iduser = ''

    return iduser

def user():
    if r.hget('user:'+iduser(), 'name') is not None:
        return r.hget('user:'+iduser(), 'name').decode("utf-8")
    else:
        return ''

class Colors(object):
    red = '\033[91m'
    yellow = '\033[93m'
    grey = '\033[90m'
    black = '\033[0m'
    bold = '\033[1m'


class Command(object):
    info = {
        "info" : "this is stout",
    }

    c_info = {
        "set" : "set a value",
    }

    c_commands = ('quit','set', 'get')

    whatdo = {
        'set' : ['user', 'host'],
    }

    @staticmethod
    def err(err):
        if err == 'keyword':
            sys.stderr.write(Colors.red + "keyword inesistente\n" + Colors.black)
        elif err == 'wrong':
            sys.stderr.write(Colors.red + "sintassi comando errata\n" + Colors.black)
        else:
            pass

class Stout(object):

    def __init__(self):
        self.name = 'stout'
        self.user = user()

    def getName(self):
        word = " (" + self.name + ") "
        if self.user == '':
            return word
        else:
            return word + Colors.grey + "(" + self.user + ") "

    def command(self, what, cmd):
        if what == 'set':
            try:
                if cmd[1] == 'user' and cmd[2] is not None:
                    if self.user == '':
                        new_id = str(int(r.get('iduser').decode("utf-8"))+1)
                        r.incr('iduser')
                    else:
                        new_id = iduser()

                    self.user = cmd[2]
                    r.hset('user:'+new_id,'name', self.user)

                    with open('myid.txt', 'w') as f:
                        f.write(new_id)

                    print("Ok")
                elif cmd[1] is not Command.whatdo['set']:
                    raise IndexError
            except IndexError:
                Command.err('wrong')

    def action(self, cmd):
        if cmd is None:
            return None
        else:
            cmd = cmd.split()
            count = len(cmd)

            if count == 1 and cmd[0] not in Command.c_commands:
                try:
                    print(Command.info[cmd[0]])
                except KeyError:
                    Command.err('keyword')
            elif count == 2 and cmd[0] == 'info' and cmd[0] not in Command.c_commands:
                try:
                    print(Command.c_info[cmd[1]])
                except KeyError:
                    Command.err('keyword')
            else:
                what = cmd[0]
                if what in Command.c_commands:
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
