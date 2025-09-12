s1 = {1, 2, 3}
s2 = {'a', 'b', 'c'}
s3 = list(zip(s1, s2))
print(s3, "\n")

list1 = [10, 20, 30]
list2 = [100, 200, 300]

for x, y in zip(list1, list2[:: -1]):
    print(x, y)

stock = ['reliance', 'infosys', 'tcs']
price = [1000, 2000, 3000]

new_dict = {stock: price for stock,
            price in zip(stock, price)}
print(new_dict)