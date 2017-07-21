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
                else:
                    raise KeyError
            except IndexError:
                ListCommands.err('wrong')
            except KeyError:
                ListCommands.err('keyword')
            except PersonalError as e:
                ListCommands.err('personal', e.value)
