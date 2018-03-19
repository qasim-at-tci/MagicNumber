#!/user/bin/python 


def play_again():
    while True:
        again = input('Play again? Y/N:  ').lower()
        if again == 'y' or again == 'n':
            return again

play_again()
