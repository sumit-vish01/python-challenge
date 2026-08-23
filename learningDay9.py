

import random

number = random.randint(1, 100)

print("Number guessing game")
print("Maine 1 se 100 ka beecha me ek number socho")

guess = int(input("Apna guess number enter karo:"))
if number <= 10 and number<20:
    print("ur winner")
elif number <=30 and number<40:
    print("ur are looser")
elif number <= 50 and number<100:
    print("ur are powerful winner")

