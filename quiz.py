print("welcome to my computr quiz!")

playing =  input("Do you want to play ? ")

if playing.lower()!= "yes":
           quit()
print("Okay lets playy ;)")
score = 0
answer = input("what does cpu stand for? ")

if answer.lower() == "central processing unit":
     print("correct")
     score+=1
else :
     print("Incorrect")
answer = input("Currency of Iran ")

if answer.lower() == "rial":
     print("correct")
     score+=1
else :
     print("Incorrect")
answer = input("most obese country in The world? ")

if answer.lower() == "cook island":
     print("correct")
     score+=1
else :
     print("Incorrect")
answer = input("which continent  got the most football WORLD CUP? ")

if answer.lower() == "europe":
     print("correct")
     score+=1
else :
     print("Incorrect")
 
print("You got "+str(score)+" question correct")