# Hey there. I am Mewtue
print("Hello, to Mewtue's Car Dealer and I will help you buy a brand new car from the current Cherry, Chevlote, Ford, Honda, Hyundai, Kia, BMW models.")
print("Enter vote for the car brand")

Cherry = int( input("Cherry is a really futuristic affordable car brand,and it is better when you compare it with BMW.Please enter from 100000 to 1: "))
Cherry_vote_left = 100000 - Cherry
Chevlote = int(input(f"Chevlote is not that good and comfortable as Cherry, but faster than Cherry. You have {Cherry_vote_left} votes left. Please enter from that many votes left: "))
Chevlote_vote_left = Cherry_vote_left - Chevlote
Ford = int(input(f"Ford is a really nice HUV brand and is good for traveling. You have {Chevlote_vote_left} votes left. Please enter from that many votes left: "))
Ford_vote_left = Chevlote_vote_left - Ford
Honda = int(input(f"Honda is not a really nice brand but nice for riding around cities and towns it is very cheap. You have {Ford_vote_left} votes left. Please enter from that many votes left: "))
Honda_votes_left = Ford_vote_left - Honda
Hyundai = int(input(f"Hyundai is a really nice car brand and is recommended for the most cheapest luxury car. You have {Honda_votes_left} votes left. Please enter from that many votes left: "))
Hyundai_votes_left = Honda_votes_left - Hyundai
Kia = int(input(f"Kia is a really nice car brand and is recommended for the most chepest luxury car. You have {Hyundai_votes_left} votes left. please enter from that many votes left: "))
Kia_votes_left = Hyundai_votes_left - Kia
BMW = int(input(f"BMW is a really nice car brand and is recommend for the most expensive luxury car. You have {Kia_votes_left} votes left. Please enter fronm that many votes left: "))

if Cherry > Chevlote and Cherry > Ford and Cherry > Honda and Cherry > Hyundai and Cherry > Kia and Cherry > BMW:
    print("You have voted Cherry the most.")
    print("Kenya, Nairobi, Contact number: +25420652398")
elif Chevlote > Cherry and Chevlote > Ford and Chevlote > Honda and Chevlote > Hyundai and Chevlote > Kia and Chevlote > BMW:
    print("You have voted Chevlote the most,")
    print("Kenya, Nairobi, Contact number: +254707055600")
elif Ford > Cherry and Ford > Chevlote and Ford > Honda and Ford > Hyundai and Ford 