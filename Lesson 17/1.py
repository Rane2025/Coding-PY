try:
    num = int(input("Enter a number : "))
    print(num)
except ValueError as exe_num:
    print(exe_num)

print("I am outside the try and except world")