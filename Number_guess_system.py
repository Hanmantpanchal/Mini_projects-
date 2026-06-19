import random
number = random.randint(1,10)
#give 3 attempts only to guees the number 
print("guess the number between 1 to 100")
attempts =3 
for i in range(1,attempts+1):
    guess=int(input(f"attempts{attempts}"))
    if guess < number:
        print("too low")
    elif guess > number :
        print("you guessed it right")
        break
else:
    print(f"you have exhausted all your attempts . the number was{number}")