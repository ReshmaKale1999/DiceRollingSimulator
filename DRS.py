import random

x = 'y'

while x == 'y':
    number = random.randint(1 , 6)

    if number == 1:
        print(' _____')
        print('|     |')
        print('|  0  |')
        print(' -----')
        print('You Got One')

    if number == 2:
        print(' _____')
        print('|  0  |')
        print('|  0  |')
        print(' -----')
        print('You Got Two')

    if number == 3:
        print(' _____')
        print('| 0 0 |')
        print('|  0  |')
        print(' -----')
        print('You Got Three')

    if number == 4:
        print(' _____')
        print('| 0 0 |')
        print('| 0 0 |')
        print(' -----')
        print('You Got Four')

    if number == 5:
        print(' _____')
        print('| 0 0 |')
        print('| 0 0 |')
        print('|  0  |')
        print(' -----')
        print('You Got Five')

    if number == 6:
        print(' ______')
        print('| 0 0  |')
        print('| 0 0  |')
        print('| 0 0  |')
        print(' ------')
        print('You Got Six')
        print('\n')

    x = input('Press Y to play again and N to exit ')
    print('\n')










