#save the file as assignment02yourlastname.py

Vakantiepaklijst = ["tandenborstel", "paspoort", "handdoek", "zonnebril"]
print(Vakantiepaklijst)

Vakantiepaklijst.append("teenslippers")
Vakantiepaklijst.append("wandelschoenen")
Vakantiepaklijst.append("fotocamera")
Vakantiepaklijst.pop(0)
Vakantiepaklijst.remove("paspoort")
print(Vakantiepaklijst)

task_1= input("Which task would you like to add?")
Vakantiepaklijst.append(task_1)
print(Vakantiepaklijst)

hoeveelheid_tasks_vakantiepaklijst = len(Vakantiepaklijst)
print(hoeveelheid_tasks_vakantiepaklijst)

if(hoeveelheid_tasks_vakantiepaklijst == 6):
    print("You can't add more tasks")

if(hoeveelheid_tasks_vakantiepaklijst <= 4):
    print("You can add more tasks")

if(hoeveelheid_tasks_vakantiepaklijst == 6):
    task_2= input("Which task would you like remove?")
    Vakantiepaklijst.remove(task_2)
print(Vakantiepaklijst)
print("Good luck with packing!")

#zo zou je voor eeuwig kunnen doorloopen