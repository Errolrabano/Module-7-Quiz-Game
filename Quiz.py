import time 
#Welcoming

def main():
    testFile = open("testFile.txt", "r")

    line = testFile.readline()

    while line != "":
        print( line )
        line = testFile.readline()




time.sleep(2)
#Chances 
chances = 1 
print("You will have", chances, "chance to answer correctly. \nChoose Your Answer Wisely! \n")

time.sleep(2)

#Score
score = -1 

#question list 
q1 = ["(a)Obviously Not!", "(b)yes", "(c)Nah", "(d)I devote myself to games"] 
q2 = ["(a)GTA V(a)", "(b)Mario Kart 64 Released: 1996", "(c)2k22", "(d)Outlast"] 
q3 = ["(a)PC, PlayStation, Xbox, wii","(b)PC, wii, Xbox, PlayStation", "(c)wii, PlayStation, Xbox, PC", "(d)PlayStation, PC, Xbox, wii"] 
q4 = ["(a)8 Hours","(b)10 Hours", "(c)You Sleep?","(d)24 Hours"] 

#question 0

question_0 = print ("Lets start the game with a simple question, Are You A Gamer?) \n Yes(a) or No(b) \n\n")
answer_0 = "a"
for i in range(chances) :
    answer = input("Answer :")
    if (answer.lower() == answer_0):
        print("Are you sure about that, We will see!\n")
        score = score + 1 
        break
    else: 
        print("Why Are You Here, Leave!\n ")
        quit()

time.sleep(2)

#question 1 
question_1 = print ("1. Do You Love Games ?\n")
for question1 in range (len(q1)): 
    print(q1 [question1], end=" \n\n") 
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

question_2 = print ("2. Greatest Classical Game\n")
for question2 in range (len(q2)): 
    print(q2 [question2], end=" \n\n") 
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

question_3 = print ("3. Worst to Best")
for question3 in range (len(q3)): 
    print(q3 [question3], end=" \n\n") 
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

question_4 = print ("4. how many hours do you sleep?")
for question4 in range (len(q4)): 
    print(q4 [question4], end=" \n\n") 
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
    break
#Closing 
print("Thank you for playing the Game!")
exit()
