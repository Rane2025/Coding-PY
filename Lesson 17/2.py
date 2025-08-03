try:
    num1 = int(input("Enter a number : "))
    num2 = int(input("Enter a second number : "))
    result = num1/num2
    print("Result is:", result)
    print("Result is:", result1)

except ZeroDivisionError:
    print("You cannot divide by zero: ")
    print("Please enter a valid second number.")
except ValueError:
    print("Please enter a numeric number.")
except NameError as ex:
    print("The exception is ",ex)

except:
    print("some error occurred")
finally:
    print("I will Execute no matter what happens")