import time
#Welcoming 
print("Welcome to the game, Are You A Gamer ?")
#Chances 
chances = 1 
print("You will have", chances, "chance to answer correctly. \nChoose Your Answer Wisely! \n")

time.sleep(2)

#Score
score = -1 

#question 0

question_0 = print ("Lets start the game with a simple question, Are You A Gamer?) \n Yes(a) or No(b) \n\n")
answer_0 = "a"
for i in range(chances) :
    answer = input("Answer :")
    if (answer.lower() == answer_0):
        print("We will see, Let's Begin!\n")
        score = score + 1 
        break
    else: 
        print("Why Are You Here, Leave!\n ")
        quit()

time.sleep(2)

#question 1 

question_1 = print ("1. Do You Love Games ?) \n Obviously Not!(a) \n yes(b) \n Nah(c) \n I devote myself to games(d) \n\n")
answer_1 = "d"
for i in range(chances) :
    answer = input("Answer :")
    if (answer.lower() == answer_1):
        print("Correct! Good Job\n")
        score = score + 1 
        break
    else: 
        print("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is" , answer_1, "\n\n ")

time.sleep(2)

#question 2

question_2 = print ("2. Greatest Classical Game) \n GTA V(a) \n Mario Kart 64 Released: 1996(b) \n 2k22(c) \n Outlast(d) \n\n")
answer_2 = "b"
for i in range(chances) :
    answer = input("Answer :")
    if (answer.lower() == answer_2):
        print("Correct! Good Job\n")
        score = score + 1 
        break
    else: 
        print("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is" , answer_2, "\n\n ")

time.sleep(2)

#question 3 

question_3 = print ("3. Worst to Best) \n PC, PlayStation, Xbox, wii(a) \n PC, wii, Xbox, PlayStation(b) \n wii, PlayStation, Xbox, PC(c) \n PlayStation, PC, Xbox, wii(d) \n\n")
answer_3 = "a"
for i in range(chances) :
    answer = input("Answer :")
    if (answer.lower() == answer_3):
        print("Correct! Good Job\n")
        score = score + 1 
        break
    else: 
        print("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is" , answer_3, "\n\n ")

time.sleep(2)

#question 4 

question_4 = print ("4. how many hours do you sleep?) \n 8 Hours(a) \n 10 Hours(b) \n You Sleep?(c) \n 24 Hours(d) \n\n")
answer_4 = "c"
for i in range(chances) :
    answer = input("Answer :")
    if (answer.lower() == answer_4):
        print("Correct! Good Job\n")
        score = score + 1 
        break
    else: 
        print("Incorrect!\n ")
        time.sleep(0.5)
        print("The correct answer is" , answer_4, "\n\n ")

time.sleep(2)

#print the score
while score >= 4: 
    print("Well done! Your score was", score)
    break 

while score <= 3: 
    print ("Better luck next time! Your score was", score)

#Closing 
print("Thank you for playing the Simple Quiz Game!")
quit()