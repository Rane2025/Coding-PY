import array as arr

array_num = arr.array('i', [1,2,3,4,5])
print("orignal array:"+str(array_num))
print('number of occurenes of the nuber 3 in the said array: ', str(array_num.count(3)))
array_num.reverse()
print('reversed array: ', str(array_num))