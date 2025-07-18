string = input("Please enter a string: ")
string2 = ""

# Loop for printing in reverse
for i in string:
    string2 = i + string2

print("\nThe orignal string = ", string)
print("The reverse string = ", string2)