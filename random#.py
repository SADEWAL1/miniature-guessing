
import random
import sys

x = 0
while x == 0:
  #generate a random number to be used
  randomnum = random.randint	(1, 100)
  print("Random Number Has been Generated")
  
  guesses = 0
  while guesses <= 11:
    guesses += 1
    if guesses == 11:
      print("you have guessed 10 times")
      break
    
    try:
      guess = int(input("You can begin guessing: You get only 10 attempts. Enter Your guesses. \n"))
    except ValueError:
      print("Please enter a number")

    if guess == randomnum:
      print("you Guessed the number correctly")
      break
      
    elif guess < randomnum:
      print("Too low try again")
      continue
    
    elif guess > randomnum:
      print("too High try again")
      
       
  QorC = input("Press any key to continue or type quit to exit\n")
  if QorC == 'quit':
      break
  else:
      continue

print("Thanks for playing")
x += 1

  
