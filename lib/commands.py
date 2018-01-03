from classes import PersonalError, RED, GREY
from listcommands import ListCommands
from config import config as co

class Commands(object):

    def command(self, what, cmd):
        """
        this function is used for execute a command
        """
        if what == 'get':
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
                    elif cmd[2] not in ListCommands.commands['get'][1]:
                        raise KeyError     
                    else:
                        print(co[cmd[2]])
                elif cmd[1] == 'todo':
                    with open(co['path'], 'rb') as fout:
                        try:
                            lines = fout.readlines()
                        except Exception as e:
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
                    count = countID()

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
                msg = ' '.join(cmd[1:]) #join first word after 'add' to last word

                try:
                    with open(co['path'], 'ab+') as fout:
                        fout.write((msg + '\n').encode('utf-8'))

                    print('Ok')
                except:
                    raise KeyError
            except (IndexError, KeyError):
                ListCommands.err(type(e).__name__)
        elif what == 'del':
            try:
                if len(cmd) > ListCommands.info['del'][1]:
                    raise PersonalError(GREY + 'del ' + RED + 'accetta 1 parametro')
                count = countID()

                if count == 0: #todo list is empty
                    print('nessun todo in lista: goditi una Stout')
                elif int(cmd[1]) >= count:
                    print('nessun todo con questo id')
                else:
                    try:
                        with open(co['path'], 'rb') as fin:
                             lines = [x.strip() for x in fin.readlines()]
                             
                             del lines[int(cmd[1])+1]
                        
                        with open(co['path'], 'wb') as fout:
                             for line in lines:
                                 fout.write(line + ('\n'.encode('utf-8')))

                        print('Ok')
                    except Exception as e:
                        print(e)
            except (IndexError, KeyError) as e:
                ListCommands.err(type(e).__name__)


def countID():
     with open(co['path'], 'rb') as fout:
         for i, _ in enumerate(fout.readlines()):
             count = i
     
     return count
