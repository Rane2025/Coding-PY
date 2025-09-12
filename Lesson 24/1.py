number1 = [1, 2, 3]
number2 = [4, 5, 6]
reasult = map(lambda x, y: x + y, number1, number2)
print("The sum of two lists")
print(list(reasult))

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
def sq(n):
    return n * n
square= list(map(sq, nums))
print(square)