# Hey there. I am Mewtue
print("Hello, to Mewtue's Car Finder and I will help you buy a brand new car from the current Cherry, Chevlote, Ford, Honda, Hyundai, Kia, BMW models.")
print("Enter vote for the car brand")
print("Only could be used in Kenya.")

Cherry = int( input(f"Cherry is a really futuristic affordable car brand,and it is better when you compare it with BMW.Please enter from 1 to 100000: "))
Cherry_vote_left = 100000 - Cherry
Chevlote = int(input(f"Chevlote is not that good and comfortable as Cherry, but faster than Cherry. You have {Cherry_vote_left} votes left. Please enter from that many votes left: "))
Chevlote_vote_left = Cherry_vote_left - Chevlote
Ford = int(input(f"Ford is a really nice HUV brand and is good for traveling. You have {Chevlote_vote_left} votes left. Please enter from that many votes left: "))
Ford_vote_left = Chevlote_vote_left - Ford
Honda = int(input(f"Honda is not a really nice brand but nice for riding around cities and towns it is very cheap. You have {Ford_vote_left} votes left. Please enter from that many votes left: "))
Honda_votes_left = Ford_vote_left - Honda
Hyundai = int(input(f"Hyundai is a really nice car brand and is recommended for the most cheapest luxury car. You have {Honda_votes_left} votes left. Please enter from that many votes left:  "))
Hyundai_votes_left = Honda_votes_left - Hyundai
Kia = int(input(f"Kia is a really nice car brand and is recommended for the most chepest luxury car. You have {Hyundai_votes_left} votes left. please enter from that many votes left: "))
Kia_votes_left = Hyundai_votes_left - Kia
BMW = int(input(f"BMW is a really nice car brand and is recommend for the most expensive luxury car. You have {Kia_votes_left} votes left. Please enter fronm that many votes left: "))

if Cherry > Chevlote and Cherry > Ford and Cherry > Honda and Cherry > Hyundai and Cherry > Kia and Cherry > BMW:
    print("You have voted Cherry the most.")
    print("Kenya, Nairobi, Contact number: +25420652398")
elif Chevlote > Cherry and Chevlote > Ford and Chevlote > Honda and Chevlote > Hyundai and Chevlote > Kia and Chevlote > BMW:
    print("You have voted Chevlote the most.")
    print("Kenya, Nairobi, Contact number: +254707055600")
elif Ford > Cherry and Ford > Chevlote and Ford > Honda and Ford > Hyundai and Ford > Kia and Ford > BMW:
    print("You have voted Ford the most.")
    print("No Phone number available, website: https://www.ford.co.ke/")
elif Honda > Cherry and Honda > Chevlote and Honda > Ford and Honda > Hyundai and Honda > Kia and Honda > BMW:
    print("You have voted Honda the most.")
    print("Kenya, Nairobi, Contact number: +254718111111")
elif Hyundai > Cherry and Hyundai > Chevlote and Hyundai > Ford and Hyundai > Honda and Hyundai > Kia and Hyundai > BMW:
    print("You Have voted Hyundai the most.")
    print("Kenya, Nairobi, Contact number: +254110094309")
elif Kia > Cherry and Kia > Chevlote and Kia > Ford and Kia > Honda and Kia > Hyundai and Kia > BMW:
    print("You have voted Kia the most.")
    print("No Phone number available, website: https://www.kia.co.ke/")
elif BMW > Cherry and BMW > Chevlote and BMW > Ford and BMW > Honda and BMW > Hyundai and BMW > Kia:
    print("You have voted BMW the most.")
    print("No Phone number avalable, website: https://www.bmw.co.ke/en/index.html")
else:
    print("You have voted none of the car brands, please try again.")

print("Thank you for using Mewtue's car dealer, have a nice day!")

# Extra Variables that are used in the project

google_maps = input("Did you ever use google maps?[Yes/No]")

if google_maps == 'Y' or google_maps == 'Yes' or google_maps == 'ya' or google_maps == 'Ya':
    google_maps2 = input("Do you like it?")
    if google_maps2 == 'Y' or google_maps2 == 'Yes' or google_maps2 == 'ya' or google_maps2 == 'Ya':
        print("Give feedback to google [Click the website!!] : https://www.google.com/tools/feedback/intl/en/learnmore.html. These are the steps give by google [a guide] to help you fill up your feedback form.")
    else:
        print("Not usefull to you")
else:
    print("Never mind")

# Now the end of most of the main part but I did not forget about the rules!

print("\nMewtue's Car Finder is a project by Rane2025, and it is not affiliated with any car brand. All right reserved")
print("The creater is not from Kenaya and and all credits are given to the car brands mentioned above and https://www.google.com/maps. ")
print("This project for usefull information only and not a game, so please do not 'prank call' or do illegal activities with the contact numbers provided.")
print("Please do not remix this project without the permission of the creater, Rane2025")
print("If you are caught breaking the rules, you will be in trouble. ")
print("Thank's for using Mewtue's Car Finder, have a nice day/night!")

print("Please give a star if liked the hard work. ")

print("Mewtue's car finder Kenya[The first one!]")
print("Mewtue's Car finder V.1")
print("Have fun in Kenya")