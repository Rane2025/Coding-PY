cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

if (cost_price > selling_price):
    print("No profit")
    pt = cost_price - selling_price
    print("Loss is -", pt)

else :
    print("Profit")
    pt = selling_price - cost_price
    print("Profit is", pt)