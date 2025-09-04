
class MenuItem:
    def __init__(self, name: str, action):
        self.name = name
        self.action = action

    def select(self):
        self.action()