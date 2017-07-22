from classes import PersonalError, r, clear, Colors
from listcommands import ListCommands
from config import config as co

class Commands(object):

    def command(self, what, cmd):
        """
        this function is used for execute a command
        """
        if what == 'clear':
            clear()
        elif what == 'set':
            try:
                if cmd[1] == 'user' and cmd[2] is not None: #set name for user
                    if len(cmd[2]) > 10:
                        raise PersonalError('lunghezza maggiore del consetito. Max 10')

                    if len(cmd) > ListCommands.info['set'][1]:
                        raise PersonalError(Colors.grey + 'set user' + Colors.red + ' accetta 1 parametro')


                    self.user = cmd[2]
                    r.set('user', self.user) #change name of user

                    print('Ok')
                elif cmd[1] is not ListCommands.commands['set']:
                    raise KeyError
            except IndexError:
                ListCommands.err('wrong')
            except KeyError:
                ListCommands.err('keyword')
            except PersonalError as e:
                ListCommands.err('personal', e.value)
        elif what == 'get':
            try:
                if len(cmd) > ListCommands.info['get'][1]:
                    raise PersonalError(Colors.grey + 'get ' + Colors.red + 'accetta 2 parametri')

                if cmd[1] == 'i': #if first word after get is 'i', there is an info
                    if cmd[2] == 'user':
                        #if self.user is empty, print 'nil'
                        if self.user != '':
                            print(r.get('user').decode('utf-8'))
                        else:
                            print('nil')
                    elif cmd[2] not in ListCommands.commands['get'][1]: #check if the word after 'i' exists
                        ListCommands.err('keyword')
                    else:
                        print(co[cmd[2]])
                elif cmd[1] == 'todo':
                    todolist = r.zrange('todo', 0, -1)

                    if len(todolist) == 0: #if todo is empty
                        print('nessun todo in lista: goditi una Stout')
                    else:
                        for num, i in enumerate(todolist): #num = index, i = value
                            print('| {} |\t {}'.format(num, i.decode('utf-8')))
                elif cmd[1] == 'ctodo':
                    count = r.get('idTODO')

                    if count is None: #if idTODO is None or 0
                        print('0')
                    else:
                        print(count.decode('utf-8'))
                else:
                    raise KeyError
            except IndexError:
                ListCommands.err('wrong')
            except KeyError:
                ListCommands.err('keyword')
            except PersonalError as e:
                ListCommands.err('personal', e.value)
        elif what == 'add':
            try:
                if r.get('idTODO') is None: #create idTODO if it's null
                    r.set('idTODO', '0')

                idTODO = r.get('idTODO').decode('utf-8')

                msg = ' '.join(cmd[1:]) #join first word after 'add' to last word

                try:
                    r.zadd('todo', msg, idTODO)
                    r.incr('idTODO')
                    print('Ok')
                except:
                    raise KeyError
            except IndexError:
                ListCommands.err('wrong')
            except KeyError:
                ListCommands.err('keyword')
        elif what == 'del':
            try:
                if len(cmd) > ListCommands.info['del'][1]:
                    raise PersonalError(Colors.grey + 'del ' + Colors.red + 'accetta 1 parametro')

                if r.get('idTODO') is None or r.get('idTODO') == 0: #idTODO is null or 0
                    print('nessun todo in lista: goditi una Stout')
                elif cmd[1] >= r.get('idTODO').decode('utf-8'):
                    print('nessun todo con questo id')
                else:
                    try:
                        msg = self.msgFromId(cmd[1]) #return value of sorted set's rank
                        r.zrem('todo', msg)
                        r.decr('idTODO')
                        print('Ok')
                    except:
                        print('0')
            except IndexError:
                ListCommands.err('wrong')
            except KeyError:
                ListCommands.err('keyword')

    def msgFromId(self, value):
        for i, val in enumerate(r.zrange('todo', 0, -1)):
            if i == int(value):
                return val.decode('utf-8')
