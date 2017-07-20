from classes import userexist, PersonalError, r, host, clear, Colors
from listcommands import ListCommands

class Commands(object):

    def command(self, what, cmd):
        if what == 'clear':
            clear()
        elif what == 'set':
            try:
                if cmd[1] == 'user' and cmd[2] is not None:
                    if len(cmd[2]) > 10: raise PersonalError('lunghezza maggiore del consetito. Max 10')

                    if userexist(cmd[2]) == True: raise PersonalError('questo nome utente esiste già')

                    if len(cmd) > ListCommands.info['set'][1]: raise PersonalError(Colors.grey + 'set user' + Colors.red + ' accetta 1 parametri')

                    if self.user != '': r.zrem('usersname', self.user)

                    self.user = cmd[2]
                    r.hset('user:'+host, 'name', self.user)
                    r.zadd('usersname', self.user, 0)

                    print('Ok')
                elif cmd[1] is not ListCommands.commands['set']:
                    raise IndexError
            except IndexError:
                ListCommands.err('wrong')
            except PersonalError as e:
                ListCommands.err('personal', e.value)
        elif what == 'get':
            try:
                if len(cmd) > 2 and cmd[1] != 'user?': raise PersonalError(Colors.grey + 'get ' + Colors.red + 'accetta 1 parametro')

                if cmd[1] == 'user':
                    if self.user != '':
                        print(r.hget('user:'+host, 'name').decode('utf-8'))
                    else:
                        print('nil')
                elif cmd[1] == 'host':
                    print('localhost')
                elif cmd[1] == 'port':
                    print('6379')
                elif cmd[1] == 'user?':
                    if len(cmd) > 3: raise PersonalError(Colors.grey + 'get user?' + Colors.red + ' accetta 1 parametro')
                    print(userexist(cmd[2]))
                elif cmd[1] not in ListCommands.commands:
                    raise KeyError
                else:
                    raise IndexError
            except IndexError:
                ListCommands.err('wrong')
            except KeyError:
                ListCommands.err('keyword')
            except PersonalError as e:
                ListCommands.err('personal', e.value)
