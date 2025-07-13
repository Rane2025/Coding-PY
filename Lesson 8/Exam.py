medical_cause = input("did you have a medical cause? Y or N:")
atten = int(input("enter your attendance: "))

if  medical_cause.lower() == "y" :
    print ("Allowed")
else:
    if atten>=78:
        print ("Allowed")
    else:
        print("Not Allowed")