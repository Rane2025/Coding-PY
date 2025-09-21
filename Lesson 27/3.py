class pairElements:
    def twosum(self, nums, target):
        LookUP = {}

        for i,num in enumerate(nums):
            if target == num in LookUP:
                return (LookUP[target-num], i)
            LookUP[num] = i
val = int(input("Enter a sum:(1-5) "))
print("index1=%d, index2=%d" % pairElements().twosum([1, 2, 3, 4, 5], val))