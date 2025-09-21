class Employees:
    def __init__(self):
        print("Employees crafted")
    def __del__(self):
        print("Employees deleted")

def create_object():
    print("Making object")
    obj = Employees()
    print("Function end")
    return obj
print("Calling create_object()")
obj = create_object()
print("Program Ended")