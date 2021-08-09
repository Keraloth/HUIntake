#calculate how much one Oreo cookie is concerning: calories, sodium, carbohydrate, fat 
#create a user input that asks how much cookies you ate 
#calculate how much calories, etc. you consumed 
#warn the user that if he/she surpasses 2000kcal he/she should stop eating these darn delicious cookies 
#use variables! 
#save the file as assignment01yourlastname.py

calories= 160
calories_cookie = 53.33
total_fat = 7
fat_cookie = 2.333
sodium_total = 0.19
sodium_cookie = 0.063
potassium = 0
potassium_cookie = 0
total_carbohydrate = 25
carbohydrate_cookie = 8.33
protein = 2
protein_cookie = 0.666

# print(protein/3) / print(total_carbohydrate/3) and so on.

how_many_oreos = int(input("How many oreos did you eat? "))  
total_calories = how_many_oreos * calories_cookie
print("You ate " + str(total_calories)+ " calories")

total_sodium_cookies = how_many_oreos * sodium_cookie
print("You ate " + str(total_sodium_cookies)+ " grams of sodium") 

total_fat_cookies = how_many_oreos * fat_cookie
print("You ate " + str(total_fat_cookies)+ " grams of fat") 

total_potassium_cookies = how_many_oreos * potassium_cookie
print("You ate " + str(total_potassium_cookies)+ " grams of potassium") 

total_carbohydrate_cookies = how_many_oreos * carbohydrate_cookie
print("You ate " + str(total_carbohydrate_cookies)+ " grams of carbohydrate") 

total_protein_cookies = how_many_oreos * protein_cookie
print("You ate " + str(total_protein_cookies)+ " grams of protein") 

if (total_calories >= 2000):
    print("You should stop eating these darn delicious cookies!")
