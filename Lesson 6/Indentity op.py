a = input("Write someting like a word not a number: ")
b = input("Write someting like a word not a number: ")

if a is b:
    print(a, "and", b, "are equal")
if a is not b:
    print(a, "and", b, "are not equal")

print ("next project")

print("Enter Marks obtained in 5 subjects out of 100")
mark1 = int(input())
mark2 = int(input())
mark3 = int(input())
mark4 = int(input())
mark5 = int(input())

tot = mark1  + mark2 + mark3 + mark4 + mark5
avg = tot/5

if avg >=91 and avg <= 100:
    print("A1")
elif avg >=81 and avg <= 91:
    print("A2")
elif avg >=71 and avg <= 81:
    print("B1")
elif avg >=61 and avg <= 71:
    print("B2")
elif avg >=51 and avg <= 61:
    print("C1")
elif avg >=41 and avg <= 51:
    print("C2")
elif avg >=31 and avg <= 41:
    print("D1")
elif avg >=21 and avg <= 31:
    print("D2")
elif avg >=11 and avg <= 21:
    print("E2")
elif avg >=0 and avg <= 11:
    print("F")
else:
    print("Invalid Marks")