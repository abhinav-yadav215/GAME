import random 
print("Winning Rules : \n"+"Rock vs paper->paper wins \n"+ "Rock vs scissor->Rock wins \n"+"paper vs scissor->scissor wins \n")
choice1 = random.randint(1, 3)
if choice1 == 1: 
	choice1_name = 'Rock'
elif choice1 == 2: 
	choice1_name = 'paper'
else: 
	choice1_name = 'scissor'
		
print("player1 choice is: " + choice1_name) 

choice2 = random.randint(1, 3)
if choice2 == 1: 
        choice2_name = 'Rock'
elif choice2 == 2: 
	choice2_name = 'paper'
else: 
	choice2_name = 'scissor'
		
print("player2 choice is: " + choice2_name) 

choice3 = random.randint(1, 3)
if choice3 == 1: 
	choice3_name = 'Rock'
elif choice3 == 2: 
	choice3_name = 'paper'
else: 
	choice3_name = 'scissor'
		
print("player3 choice is: " + choice3_name) 

choice4 = random.randint(1, 3)
if choice4 == 1: 
	choice4_name = 'Rock'
elif choice4 == 2: 
	choice4_name = 'paper'
else: 
	choice4_name = 'scissor'

print("player4 choice is: " + choice4_name)
count=1
while (count<=5):
        print('the count is:',count)
        if((choice1 == 1 and choice2 == 2) or(choice2 == 1 and choice1 ==2 )): 
                print("paper wins => ", end = "") 
                result = "paper"
		
        elif((choice1 == 1 and choice2 == 3) or
            (choice2 == 1 and choice1 == 3)): 
                print("Rock wins =>", end = "") 
                result = "Rock"
        else: 
                print("scissor wins =>", end = "") 
                result = "scissor"
        print('the result between 1 and 2')
        if result == choice1_name: 
                print("<== player1 wins ==>") 
        else: 
                print("<== player2 wins ==>") 
		
        if((choice1 == 1 and choice3 == 2) or(choice3 == 1 and choice1 ==2 )): 
                print("paper wins => ", end = "") 
                result = "paper"

        elif((choice1 == 1 and choice3 == 3) or
                (choice3 == 1 and choice1 == 3)): 
                print("Rock wins =>", end = "") 
                result = "Rock"
        else: 
                print("scissor wins =>", end = "") 
                result = "scissor"
        print('the result between 1 and 3')
        if result == choice1_name: 
                print("<== player1 wins ==>") 
        else: 
                print("<== player3 wins ==>") 
        if((choice1 == 1 and choice4 == 2) or
                (choice4 == 1 and choice1 ==2 )): 
                print("paper wins => ", end = "") 
                result = "paper"
		
        elif((choice1 == 1 and choice4 == 3) or
                (choice4 == 1 and choice1 == 3)): 
                print("Rock wins =>", end = "") 
                result = "Rock"
        else: 
                print("scissor wins =>", end = "") 
                result = "scissor"
        print('the result between 1 and 4')
        if result == choice1_name: 
                print("<== player1 wins ==>") 
        else: 
                print("<== player4 wins ==>") 
        if((choice3 == 1 and choice2 == 2) or
                (choice2 == 1 and choice3 ==2 )): 
                print("paper wins => ", end = "") 
                result = "paper"
		
        elif((choice3 == 1 and choice2 == 3) or
                (choice2 == 1 and choice3 == 3)): 
                print("Rock wins =>", end = "") 
                result = "Rock"
        else: 
                print("scissor wins =>", end = "") 
                result = "scissor"
        print('the result between 3 and 2')
        if result == choice3_name: 
                print("<== player3 wins ==>") 
        else: 
                print("<== player2 wins ==>") 
        if((choice4 == 1 and choice2 == 2) or
            (choice2 == 1 and choice4 ==2 )): 
                print("paper wins => ", end = "") 
                result = "paper"
		
        elif((choice4 == 1 and choice2 == 3) or
                (choice2 == 1 and choice4 == 3)): 
                print("Rock wins =>", end = "") 
                result = "Rock"
        else: 
                print("scissor wins =>", end = "") 
                result = "scissor"
        print('the result between 4 and 2')
        if result == choice4_name: 
                print("<== player4 wins ==>") 
        else: 
                print("<== player2 wins ==>") 
        if((choice3 == 1 and choice4 == 2) or
            (choice4 == 1 and choice3 ==2 )): 
                print("paper wins => ", end = "") 
                result = "paper"
		
        elif((choice3 == 1 and choice4 == 3) or
                (choice4 == 1 and choice3 == 3)): 
                print("Rock wins =>", end = "") 
                result = "Rock"
        else: 
                print("scissor wins =>", end = "") 
                result = "scissor"
        print('the result between 3 and 4')
        if result == choice3_name: 
                print("<== player3 wins ==>") 
        else: 
                print("<== player4 wins ==>") 
        count=count+1
print('overall result')
if result == choice1_name: 
    print("<== player1 wins ==>")
elif result==choice2_name:
    print("<== player2 win ==>")
elif result==choice3_name:
    print("<== player3 win ==>")
else: 
    print("<== player4 win ==>") 
		

