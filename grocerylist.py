
zuivel = ["Kaas", "Melk", "Zuivelspread"]
groenten = ["Prei", "Broccoli", "Tomaat", "Ui", "Bloed"]

zuivel.append ("Volle Melk")
groenten.append ("Aardbeien")
zuivel.append ("Pasta")
zuivel.append ("Kaas")

zuivel.sort()
groenten.sort()

# nieuwe list aangemaakt zodat het aan elkaar toegevoegd wordt.
boodschappen = []
boodschappen.append(groenten)
boodschappen.append(zuivel)

print(boodschappen)