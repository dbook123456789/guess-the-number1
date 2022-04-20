import random
a=random.randint (0,10)
x=input ("Hello, whats your name=")
print ("ok",x ,"guess a number between 0 and 10 ")
guesses = 0
while guesses < 3:
    v=int(input ())
    guesses+=1 
    if v<a :
        print (" your guess is too low")
    elif v>a :
        print ("your guess is too high")
    elif v==a :
        break 
if v==a:
    print("you have guessed the number in ",guesses,"turn")
else :
    print ( "you have not guessed the number is", a ) 
    
            

     