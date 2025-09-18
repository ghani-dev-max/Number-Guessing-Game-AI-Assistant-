import math
import random

def aiGuesses(aiScore, userScore):
    fnum = int(input("Enter the starting number: "))
    lnum = int(input("Enter the last number: "))

    if fnum >= lnum:
        print("Invalid range. Starting number must be less than the last number.\n")
        return aiScore, userScore

    print("\nAI will try to guess the number between", fnum, "and", lnum)

    print("User instructions:")
    print("Type 'low' if the guess is less than your number.")
    print("Type 'high' if the guess is greater than your number.")
    print("Type 'correct' if the guess is right.")

    low = fnum
    high = lnum
    attempt = 0

    rangeSize = lnum - fnum + 1
    maxAttempts = math.ceil(math.log2(rangeSize))
    print("\nAI will try to guess in at most", maxAttempts, "attempts.\n")

    aiWon = False

    while low <= high and attempt < maxAttempts:
        attempt += 1
        guess = (low + high) // 2
        print("Attempt", attempt, "of", maxAttempts, "- AI guess is:", guess)

        feedback = input("Your feedback (low/high/correct): ").strip().lower()

        if feedback == "low":
            low = guess + 1
        elif feedback == "high":
            high = guess - 1
        elif feedback == "correct":
            print("\nAI guessed your number", guess, "in", attempt,
                  "tries out of", maxAttempts)
            aiScore += 1
            aiWon = True
            break
        else:
            print("Invalid input. Please type low, high, or correct.")

    if not aiWon:
        if attempt >= maxAttempts:
            print("\nAI could not guess your number within", maxAttempts, "attempts. You win this round.")
        else:
            print("\nInconsistent answers were given. AI could not guess correctly.")
        userScore += 1

    return aiScore, userScore


def userGuesses(aiScore, userScore):
    fnum = int(input("Enter the starting number: "))
    lnum = int(input("Enter the last number: "))

    if fnum >= lnum:
        print("Invalid range. Starting number must be less than the last number.\n")
        return aiScore, userScore

    secret = random.randint(fnum, lnum)
    attempt = 0
    maxAttempts = math.ceil(math.log2(lnum - fnum + 1))

    print("\nYou must guess the number between", fnum, "and", lnum)
    print("You have at most", maxAttempts, "attempts.\n")

    while attempt < maxAttempts:
        attempt += 1
        try:
            guess = int(input("Attempt " + str(attempt) + " of " + str(maxAttempts) + ". Your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if guess < secret:
            print("Too low.")
        elif guess > secret:
            print("Too high.")
        else:
            print("Correct! You guessed the number in", attempt, "tries.")
            userScore += 1
            return aiScore, userScore

    print("\nYou did not guess the number in time. The correct number was", secret)
    aiScore += 1
    return aiScore, userScore


def showScoreboard(aiScore, userScore):
    print("\n--- Scoreboard ---")
    print("AI:", aiScore, " | User:", userScore)
    print("------------------")


def main():
    print("\tNumber Guessing Game (AI Assistant)\t\n")
    aiScore = 0
    userScore = 0

    while True:
        print("Choose game mode:")
        print("1. AI guesses your number")
        print("2. You guess AI's number")

        mode = input("Enter 1 or 2: ").strip()

        if mode == "1":
            aiScore, userScore = aiGuesses(aiScore, userScore)
        elif mode == "2":
            aiScore, userScore = userGuesses(aiScore, userScore)
        else:
            print("Invalid choice. Try again.")
            continue

        showScoreboard(aiScore, userScore)

        playagain = input("\nDo you want to play again (yes/no): ").strip().lower()
        if playagain not in ("yes", "y"):
            print("\nFinal Score - AI:", aiScore, " User:", userScore)
            if aiScore > userScore:
                print("AI wins the game overall.")
            elif userScore > aiScore:
                print("You win the game overall.")
            else:
                print("The game is a tie.")
            print("Thanks for playing. Goodbye.")
            break


if __name__ == "__main__":
    main()
