from classes import PersonalError, Colors, r, s, host, clear
from commands import Commands
from listcommands import ListCommands

class Stout(Commands):

    def __init__(self):
        self.name = 'stout'
        self.user = Stout.username()

    def getName(self):
        word = ' (' + self.name + ') '
        if self.user == '':
            return word
        else:
            return word + Colors.grey + '(' + self.user + ':' + host + ') '

    @staticmethod
    def username():
        if r.hget('user:'+host, 'name') is not None:
            return r.hget('user:'+host, 'name').decode('utf-8')
        else:
            return ''

    def action(self, cmd):
        if cmd is None:
            return None
        else:
            cmd = cmd.split()
            count = len(cmd)

            if (count == 1 or count == 2) and cmd[0] not in ListCommands.commands:
                try:
                    if cmd[0] == 'info' and count == 1:
                        print(ListCommands.info['info'])
                    elif cmd[0] == 'info' and count == 2:
                        print(ListCommands.info[cmd[1]][0])
                    else:
                        raise KeyError
                except (KeyError, IndexError):
                    ListCommands.err('keyword')
            else:
                what = cmd[0]
                if what in ListCommands.commands:
                    self.command(what, cmd)
                else:
                    ListCommands.err('keyword')


if __name__ == '__main__':
    clear()
    app = Stout()
    cmd = ''
    while cmd != 'quit':
        cmd = input('>' + Colors.yellow + app.getName() + Colors.black)
        app.action(cmd)
        r.save()

    s.close()
    clear()
