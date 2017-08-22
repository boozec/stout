from classes import PersonalError, r, clear, RED, GREY
from listcommands import ListCommands
from config import config as co

class Commands(object):

    def command(self, what, cmd):
        """
        this function is used for execute a command
        """
        if what == 'set':
            try:
                if cmd[1] == 'user' and cmd[2] is not None: #set name for user
                    if len(cmd[2]) > 10:
                        raise PersonalError('lunghezza maggiore del consetito. Max 10')

                    if len(cmd) > ListCommands.info['set'][1]:
                        raise PersonalError(GREY + 'set user' + RED + ' accetta 1 parametro')


                    self.user = cmd[2]
                    with open(co['path'], 'wb') as fout:
                        fout.write(cmd[2].encode('utf-8'))

                    print('Ok')
                elif cmd[1] is not ListCommands.commands['set']:
                    raise KeyError
            except (IndexError, KeyError) as e:
                ListCommands.err(type(e).__name__)
            except PersonalError as e:
                ListCommands.err('personal', e.value)
        elif what == 'get':
            try:
                if len(cmd) > ListCommands.info['get'][1]:
                    raise PersonalError(GREY + 'get ' + RED + 'accetta 2 parametri')

                if cmd[1] == 'i': #if first word after get is 'i', there is an info
                    if cmd[2] == 'user':
                        #if self.user is empty, print 'nil'
                        if self.user != '':
                            with open(co['path'], 'rb') as fin:
                                print(fin.readline().decode('utf-8'))
                        else:
                            print('nil')
                    elif cmd[2] not in ListCommands.commands['get'][1]: #check if the word after 'i' exists
                        raise KeyError     
                    else:
                        print(co[cmd[2]])
                elif cmd[1] == 'todo':
                    with open(co['path'], 'rb') as fout:
                        try:
                            lines = fout.readlines()
                        except:
                            lines = ''

                    if lines is not None:
                        todolist = [x.strip() for i, x in enumerate(lines) if i > 0]
                    else:
                        todolist = []

                    if len(todolist) == 0: #if todo is empty
                        print('nessun todo in lista: goditi una Stout')
                    else:
                        for num, i in enumerate(todolist): #num = index, i = value
                            print('| {} |\t {}'.format(num, i.decode('utf-8')))
                elif cmd[1] == 'ctodo':
                    with open(co['path'], 'rb') as fout:
                        for i, val in enumerate(fout.readlines()):
                            count = i
                    
                    if count is 0: #if idTODO is None or 0
                        print('0')
                    else:
                        print(count)
                else:
                    raise KeyError
            except (IndexError, KeyError) as e:
                ListCommands.err(type(e).__name__)
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
            except (IndexError, KeyError):
                ListCommands.err(type(e).__name__)
        elif what == 'del':
            try:
                if len(cmd) > ListCommands.info['del'][1]:
                    raise PersonalError(GREY + 'del ' + RED + 'accetta 1 parametro')

                if r.get('idTODO') is None or r.get('idTODO') == 0: #idTODO is null or 0
                    print('nessun todo in lista: goditi una Stout')
                elif cmd[1] >= r.get('idTODO').decode('utf-8'):
                    print('nessun todo con questo id')
                else:
                    try:
                        msg = msgFromId(cmd[1]) #return value of sorted set's rank
                        r.zrem('todo', msg)
                        r.decr('idTODO')
                        print('Ok')
                    except Exception as e:
                        print(e)
            except (IndexError, KeyError) as e:
                ListCommands.err(type(e).__name__)


def msgFromId(value):
    for i, val in enumerate(r.zrange('todo', 0, -1)):
        if i == int(value):
            return val.decode('utf-8')
