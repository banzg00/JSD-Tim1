class SimpleType:
    def __init__(self, parent, name):  # remember to include parent param.
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name


class BodyParam:
    def __init__(self, parent, type):  # remember to include parent param.
        self.parent = parent
        if type.sType:
            self.type = type.sType.name
            self.typeOfType = type.sType.__class__.__name__
        elif type.eType:
            self.type = type.eType.name
            self.typeOfType = type.eType.__class__.__name__
        elif type.cType:
            self.type = type.cType.name
            self.typeOfType = type.cType.__class__.__name__

    def __str__(self):
        return self.type


class ReturnValue:
    def __init__(self, parent, type):  # remember to include parent param.
        self.parent = parent
        if type.sType:
            self.type = type.sType.name
            self.typeOfType = type.sType.__class__.__name__
        elif type.eType:
            self.type = type.eType.name
            self.typeOfType = type.eType.__class__.__name__
        elif type.cType:
            self.type = type.cType.name
            self.typeOfType = type.cType.__class__.__name__

    def __str__(self):
        return self.type
