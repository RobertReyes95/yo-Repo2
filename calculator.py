import random 
import math 
import numpy as np 


class subtract(): 
    number = int(input("Please enter a number:"))
    randomNumber = random.randint(2, 30)
    print("The second number will be " + str(randomNumber))
    print("Let's subtract " + str(number) + " with " + str(randomNumber))
    total = number - randomNumber
    print("Your total is " + str(total))

subtract()