
import random
import sys

 #generate a random number to be used
randomnum = random.randint	(1, 100)
print("Random Number Has been Generated")
  
x = 0
while x < 10:
  x += 1
 
  print(randomnum)
  guess = int(input("You can begin guessing: You get only 10 attempts. Enter Your guesses. \n"))
  
  if guess < randomnum:
      print("Too low try again")
      continue
  if guess > randomnum:
      print("too High try again")
      continue

  if guess == randomnum:
      print("you Guessed the number correctly")
      
      QorC = input("Type Q to quick or C to continue\n")
      if QorC == 'Q' or 'q':
        break
      if QorC == 'C' or 'c':
        continue



  
