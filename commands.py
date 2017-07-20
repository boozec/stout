from classes import userexist, PersonalError, r, host
from listcommands import ListCommands

class Commands(object):

    def command(self, what, cmd):
        if what == 'clear':
            clear()
        elif what == 'set':
            try:
                if cmd[1] == 'user' and cmd[2] is not None:
                    if len(cmd[2]) > 10: raise PersonalError("lunghezza maggiore del consetito. Max 10")

                    if userexist(cmd[2]) == True: raise PersonalError("questo nome utente esiste già")

                    if self.user != '': r.zrem('usersname', self.user)

                    self.user = cmd[2]
                    r.hset('user:'+host, 'name', self.user)
                    r.zadd('usersname', self.user, 0)

                    print("Ok")
                elif cmd[1] is not ListCommands.commands['set']:
                    raise IndexError
            except IndexError:
                ListCommands.err('wrong')
            except PersonalError as e:
                ListCommands.err('personal', e.value)
