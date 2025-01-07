import random

top = input("Type a number ")

if top.isdigit():
    top=int(top)
    if top<=0:
        print("please type a number more than 0")
        quit()
else:
    print("Please type a number next time")

r= random.randint(0,top)
while True:
    u_g= input("Make a guess")
    if u_g.isdigit():
        u_g= int(u_g)
    else:
        print("Please enter a number \n")
        continue
    if u_g =="r":
        print("HURRAY! you got it")
        break
    else:
        print("OOPS!Please try again ")


