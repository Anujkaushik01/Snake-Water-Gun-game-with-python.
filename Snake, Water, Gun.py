# Snake, Water, Gun is a game similar to Rock, Paper, Scissors.
# The logic of the game is as follows:
# Snake beats Water.
# Water beats Gun.
# Gun beats Snake.

from random import randint

def computer_choice() -> int:
    random_choice: int = randint(0,2)
    return random_choice


def battle(user_guess: int, computer_guess: int) -> str:
    if user_guess == computer_guess:
        return 'Match Draw.'
    elif ((user_guess == 0 and computer_guess == 1) or
        (user_guess == 1 and computer_guess == 2) or
        (user_guess == 2 and computer_guess == 0)):
        return 'You win!'
    else:
        return 'You lose!'


def main() -> None:
    # Greeting message with choices to choose from.
    print('Welcome!')
    print('Make a choice from 0, 1, or 2')
    print('0: Snake, 1: Water, 2: Gun\n')
    choices: dict[int, str] = {0: 'snake', 1: 'water', 2: 'gun'}

    # Ensures user input correct choice.
    while True:
        try:
            user_guess: int = int(input('Enter your choice: '))
            if user_guess in [0,1,2]:
                break
            else:
                raise ValueError
        except ValueError:
            print('Enter valid choice between 0, 1, or 2.\n')

    computer_guess: int = computer_choice()
    
    # Prints user and computer choice.
    print(f'\nYour choice is: {choices.get(user_guess)}')
    print(f'Computer choice is: {choices.get(computer_guess)}')
    
    # Initializes game.
    print(battle(user_guess, computer_guess))


if __name__ == '__main__':
    main()
