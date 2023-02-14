import random


def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f"Input number between 1 and {x} : "))

        if guess > random_number:
            print("Number is smaller")
        elif guess < random_number:
            print("Number is bigger")
    print("Correct !")


def guess_computer(x):
    high = x
    low = 1
    feedback = ''

    while feedback != 'c':
        guess = random.randint(low, high)
        feedback = input(f"Is {guess} correct(c)?? or too high (h) , or too low(l)?? ").lower()
        print(feedback)
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
            print(low)
    print(f"Yay computer guessed {guess} correctly")


guess_computer(100)