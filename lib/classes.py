RED = '\033[91m'
YELLOW = '\033[93m'
GREY = '\033[90m'
BLACK = '\033[0m'
BOLD = '\033[1m'

class PersonalError(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)
