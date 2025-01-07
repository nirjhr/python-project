name = input("typ your name")
print("welcome",name, "to this adventure")
answer = input("You are on a dirt road , it has come to a dead end and you can go left or right,  tyupe left to go left or right to go right  ").lower()

if answer == "left":
    answer = input("you come across a river: you can walk around it or swim around it.type walk to walk or swium to swim").lower()
    if answer =="swim ":
        print("you swam accross and encountered an alligator and  were eaten")
    elif answer =="walk":
        print("you walked for miles, rn out of water and died")
    else:
        print("not a valid option")
elif answer =="rigt":
    answer = ("you come across a bridge, it looks woobly, do you want to go back  or cross, enter cross to cross it or enter back to back off").lower()
    if answer == "back":
        print ("you backed off you lose")
    elif answer == "cross":
        print ("you came across a stranger, you survive")
else:
    print("wrong input ,try again!!!")
