#Guess the Number  : The Actual Number is 87

actual_number = 545
attempts = 0


while True:
    attempts += 1
    guess = int(input("Guess the Number: \nHint : Number is three digits  : "))
    if guess<actual_number:
        print("Your guess was too low")
    elif guess == actual_number:
        print("Congo! You Won the game! ")
    elif guess > actual_number:
        print(" Your guess was too high")

    else:
        print(f"You gussed the number in {attempts} attempts")
        break
print("Thanks for playing")