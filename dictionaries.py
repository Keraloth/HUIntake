#{} curly brackets is to denote a dictionary
power_rangers = {
    1: {"ranger":"Blue", "name": "Billy Cranston", "roll_call": "Triceratops"},
    2: {"ranger":"Red", "name": "Jason Lee Scott", "roll_call": "Tyrannosaurus"},
    3: {"ranger":"Mighty Morphin Yellow Ranger", "name": "Trini Kwan", "roll_call": "Sabertoothed Tiger"},
}

pink_ranger = {
    "ranger" : "Mighty Morphin Pink Ranger",
    "name" : "Kimberley Ann Hart",
    "roll_call" : "Pterodactyl",
}
glitter_ranger = {
    "ranger" : "Glitter Ranger",
    "name" : "Denise van Doorn",
    "roll_call" : "Arahaaa"
}

power_rangers[4] = pink_ranger
power_rangers[5] = glitter_ranger
#print("There are currently", len(power_rangers),"powerrangers.")

#print alle inhoud van de dictionary power_rangers
print(power_rangers)
#print de hoeveelheid rangers
print(len(power_rangers))

#print items in een mooie lijst. value kun je veranderen voor bijv 'ranger' print(value["ranger"] Value maakt van alles een lijst. (print(value))
for key, value in power_rangers.items():
    print(value["ranger"])

#printing values and printing out on the screen
for id, info in power_rangers.items():
    name = info ["name"]
    ranger = info ["ranger"]
    call = info ["roll_call"]
    print("There is the", ranger, "who yells", call, "when Morphin and is secrelty", name)