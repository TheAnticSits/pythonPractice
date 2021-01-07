
secret_word = input("What is the secret word: ")
guess = ""
guess_count = 0
guess_limit = int(input("How many guesses to you get: "))
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("You Win!")