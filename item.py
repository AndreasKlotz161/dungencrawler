class item:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

    def getName(self):
        return self.name
    
    def getValue(self):
        return self.value
    
    def getType(self):
        return self.type