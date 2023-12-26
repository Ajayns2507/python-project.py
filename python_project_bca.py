# -*- coding: utf-8 -*-
"""python project BCA

Original file is located at
    https://colab.research.google.com/drive/1FkgBFFt6lqq8f8Fp4NcU5ks0KremWkae
"""

import random
def guess_the_number():
  number=random.randint(1,100)

  print("Welcome To The Number Guessing Game! ")
  print("I have selected a random number between 1 to 100. Try to guess it!")

  attempts = 0
  while True:
    guess = int(input("Enter your guessing number :"))
    attempts += 1

    if guess == number:
      print(f"congratulations! you guessed the number in {attempts} attempts.")
      break
    elif guess < number:
      print("Too low! Try again.")
    else:
      print("Too high! Try again.")

guess_the_number()
