import sys

class Entry:
    """
    Entry class for To Do project.
    """

    def __init__(self):
        self.title = None
        self.define = None
        self.notify = False

    def titleassigner(self, name):
        self.title = name

    def titlechanger(self, name):
        self.titleassigner(name)

    def definitionassigner(self, define):
        self.define = define


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Simple ToDo application used from terminal. Run help command to see more help.')

    if len(sys.argv) >= 2:
        if sys.argv[1].lower() == 'add':
            entry = Entry()
            entry.titleassigner(sys.argv[2])
            entry.definitionassigner(sys.argv[3])
        if sys.argv[1]:
            pass
