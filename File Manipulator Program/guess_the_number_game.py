import random

def guess_number_game():

    first_number = input('Give me the first number.\n')
    end_number = input('Give me the end number \n')

    correct_number = random.randint(int(first_number), int(end_number))

    for i in range(0,5):

        guess_number = input('Please tell me what numbers you guessed.\n')

        if correct_number == int(guess_number):
            return 'congratulations!'
    
    return 'Too Bad...'


def __main__():
    print(guess_number_game())

if __name__ == "__main__":
    __main__()