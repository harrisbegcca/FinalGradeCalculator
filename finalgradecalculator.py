i = 0
found = False
num = input("What I have in the class: ")
w = input("Weight of the final (%): ")
n = input("What I need in the class: ")

num = float(num)
w = float(w)
n = float(n)

while (i <= 100 and found == False):
    if float(n) <= ((i * (w / 100)) + (num * ((100 - w) / 100))):
        found = True
        print ("You need %s percent on the final!" % (i))
        if (i <= 85):
            print("Relax!")
        if (i <= 90 and not (i <= 85)):
            print("You might want to study a bit!")
        if i <= 100 and not (i <= 90):
            print("Study!")
    i += 0.01

if not (found):
    print("You can't logically get that grade without extra credit :(")
