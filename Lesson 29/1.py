class myClass:
    #private variable
    __privateVar = 25

    #private method
    def __privmeth(self):
        print("I'm inside a private method")
    def hello(self):
        print("Private variable value: ",myClass.__privateVar)

f = myClass()
f.hello()   
f.__privmeth()  # This will raise an AttributeError