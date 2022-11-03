import sys
class VaData():
    def __init__(self):
        self.va_data = {}

    def defineVariable(self, key, value):
        temp = []
        temp = key.split('...')
        if temp[1] in self.va_data:
            sys.exit('Error:Attempt to define existing variable [' + key + ']')
        if temp[1] not in self.va_data:
            self.va_data[temp[1]] = {}
            self.va_data[temp[1]][0] = value
            self.va_data[temp[1]][1] = temp[0]
            self.va_data[temp[1]][2] = temp[0]

    def set(self, key, value):
        temp = []
        temp = key.split('...')
        if temp[1] in self.va_data:
            self.va_data[temp[1]][0] = value
            self.va_data[temp[1]][1] = temp[0]
        if temp[1] not in self.va_data:
            sys.exit('Error: Attempt to set undefined variable')

    def get(self, key):
        temp = []
        temp = key.split('...')
        if temp[1] not in self.va_data:
            sys.exit('Error: Attempt to get undefined variable [' + key + ']')

        return self.va_data[temp[1]][0]


    def getNameValue(self, key):
        temp = []
        temp = key.split('...')
        if temp[1] not in self.va_data:
            sys.exit('Error: Attempt to get undefined variable [' + key + ']')
        
        return self.va_data[temp[1]][1] + ':[' + str(self.va_data[temp[1]][0]) +']'

    def printNameValue(self, key):
        temp = []
        temp = key.split('...')
        if temp[1] not in self.va_data:
            sys.exit('Error: Attempt to get undefined variable [' + key + ']')
        
        temp_10 = self.va_data[temp[1]][2] + ':[' + str(self.va_data[temp[1]][0]) +']'
        print(temp_10)

        return temp_10
       

    def getAll(self):

        return self.va_data


        

    