class SimpleType:
    def __init__(self, parent, name):  # remember to include parent param.
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name
