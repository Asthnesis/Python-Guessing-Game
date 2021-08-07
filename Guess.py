import time
import random
items = ["Duck", "Chicken", "Dog", "Rabbit"]  # Gifts/Rewards for the player upon completion
random_number = random.randint(1, 10)  # The import random  function is implemented to generate a random number
guess = int(input("input a number between 1 and 10: "))  # To get a user input and store it as an Integer
tries = 1

while guess != random_number:  # Loop generation

    if guess < random_number:
        print("Checking-----")
        time.sleep(2)  # To delay next action by an amount of seconds (The import Time function/library)
        print("Number too small!! Try again ")
        print("-----------------------------")
        tries += 1
        time.sleep(1)
    elif guess > random_number:
        print("Checking-----")
        time.sleep(2)
        print("Number too Big!! Try again ")
        print("-----------------------------")
        time.sleep(1)
    guess = int(input("Enter Your Guess here: "))  # This loops the statements


print("Checking----")
time.sleep(2)
print("You got the right Guess!! in " + str(tries), "Tries You get a pet. Choose a pet between 1 to 4 ")
time.sleep(5)


print("1")
print("2")
print("3")
print("4")

option = int(input("Select your option:"))  # Prompts the user to input an integer for the gifts option

if option == 1:
    print("You get a Duck lol")
elif option == 2:
    print("You get a Chicken lol")
elif option == 3:
    print("You get a Dog lol")
elif option == 4:
    print("You get a Rabbit lol")
time.sleep(3)
print("                       ")
time.sleep(3)
print("Thank you for playing :)")