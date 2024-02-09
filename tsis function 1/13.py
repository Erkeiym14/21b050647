import random
number = random.randint(1, 20)

print("Hello! What is your name?")
name = str(input())

txt1 = "Well, {}, I am thinking of a number between 1 and 20."
print(txt1.format(name))

print("Take a guess.")
guess = int(input())
n = 1

while guess != number:
    if guess < number:
        n += 1
        print("Your guess is too low.")
        print("Take a guess.")
        guess = int(input())
    if guess > number:
        n += 1
        print("Your guess is too high.")
        print("Take a guess.")
        guess = int(input())

txt2 = "Good job, {}! You guessed my number in {} guesses!"
print(txt2.format(name, n)) 