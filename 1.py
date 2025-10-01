class Myclass:
    def getString(self):
        return input()
    def printString(self, s):
        print(s.upper())

obj = Myclass()
a = obj.getString()  
obj.printString(a)
