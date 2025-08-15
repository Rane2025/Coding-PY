L = [4, 5, 1, 9, 7, 10, 8]
print("Original List :", L)

count = 0

for i in L:
    count += i

avg = count/len(L)

print("sum =", count)
print("Average =", avg)

L.sort()

print("Smallest element is:", L[0])
print("The largest element is:", L[-1])