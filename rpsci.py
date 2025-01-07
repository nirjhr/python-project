import random

u_w=0
c_w=0
options = ["rock","paper","scissor"]
score=0
c_s=0
while True:
    u_i = input("Type Rock/Paper/Scissor or Q to quit  ").lower()
    if u_i== "q":
        break
    if u_i not in ["rock","paper","scissor"]:
        continue
    r_n = random.randint(0,2)
    c_p = options[r_n]
    print("Computer picked "+c_p)
    if u_i =="rock" and c_p =="scissor":
        print("you won")
        score+=1
       
    elif u_i =="scissor" and c_p =="paper":
        print("you won")
        score+=1
        
    elif u_i =="paper" and c_p =="rock":
        print("you won")
        score+=1
    elif u_i =="rock" and c_p =="rock":
        print("tied")
        
        
    elif u_i =="paper" and c_p =="paper":
        print("tied")

    elif u_i =="scissor" and c_p =="scissor":
        print("tied")  
    else:
        print("Computer won")
        c_s+=1
print("You won "+str(score)+" times")   
print("Computer won "+str(c_s)+" times") 
print("Goodbye.....")




