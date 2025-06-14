number =9
count =3
while count!=0:
    guess_number = int(input("enter the number "))
    count-=1
    if guess_number<number:
        print("Number Too low!.")
    elif guess_number>number:
        print("Number Too high!")
    elif guess_number == number:
        print("Congratulations! You guessed it!")
        break
    if count!=0:
        print("Try again")
if guess_number!=number:
    print(f"Sorry, you're out of attempts. The number was {number}") 
   
    

    