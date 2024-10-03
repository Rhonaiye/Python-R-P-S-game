import random

try:
    user_range = int(input('Input a number higher than 50: '))

    # Validate the input range
    if user_range <= 50:
        print('Please input a number higher than 50.')
    else:
        print(f'Guess a number between 1 and {user_range}')
        ranNum = random.randint(1, user_range)  # Generate a random number between 1 and user_range
        
        user_guess = int(input('Input your guess: '))

        # Main guessing loop
        while user_guess != ranNum:
            if user_guess < ranNum:
                print('Your guess was less than the number.')
            elif user_guess > ranNum:
                print('Your guess was higher than the number.')

            print('Try again, you were close!')
            user_guess = int(input('Input your guess: '))

        # When the guess is correct
        print('You guessed correctly!')

except ValueError:
    print('Please enter a valid number.')

