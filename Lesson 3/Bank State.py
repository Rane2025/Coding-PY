Amount = int(input("Enter how much money you want to withdraw:"))

note_1 = Amount // 1000
note_2 = (Amount%1000)//50
note_3 = ((Amount%1000)%50)//20

print("Note of 1000 Rands: ", note_1)
print("Note of 50 Rands: ", note_2)
print("Note of 20 Rands: ", note_3 )