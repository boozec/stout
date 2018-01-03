from classes import BLACK, GREY
from commands import Commands
from listcommands import ListCommands
import os.path
from config import config

class Stout(Commands):

    def __init__(self):
        self.name = u'\U0001F37A' #beer icon

    def action(self, cmd):
        """
        if cmd is empty, do nothing.
        if length of cmd is less than 3 and the first word isnt in list of commands, the command is INFO
        else execute command into ListCommands.commands (<- list)
        """
        if cmd is None:
            return None
        else:
            cmd = cmd.split()
            count = len(cmd)

            if (count == 1 or count == 2) and cmd[0] not in ListCommands.commands:
                try:
                    if cmd[0] == 'info' and count == 1: #general info
                        print(ListCommands.info['info'])
                    elif cmd[0] == 'info' and count == 2: #info of a command
                        print(ListCommands.info[cmd[1]][0])
                    else:
                        raise KeyError
                except (KeyError, IndexError):
                    ListCommands.err('KeyError')
            else:
                try:
                    what = cmd[0]
                    if what in ListCommands.commands:
                        self.command(what, cmd)
                    else:
                        ListCommands.err('KeyError')
                except IndexError:
                   pass

if __name__ == '__main__':

    app = Stout()
    cmd = ''

    if not os.path.isfile(config['path']):
        open(config['path'], 'wb').close()

    while cmd != 'quit':
        try:
            cmd = input('>' + GREY  + ' (' + app.name  + ' ) '  + BLACK)
        except (EOFError, KeyboardInterrupt):
            break

        app.action(cmd)
