class iostring():
    def __init__(self):
        self.str1 = ""
    def get_string(self):
        self.str1 = input("Enter a string: ")
    def printing_string(self):
        print("Result is: ", self.str1.upper())
    
str1 = iostring()
str1.get_string()
str1.printing_string()