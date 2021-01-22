import random


def play():
    user = input("select - r/s/p: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'its a tie'

    if is_win(user, computer):  # helping function
        return 'you win'

    elif is_win(computer, user):
        return 'you lose'


def is_win(player, opponent):  # game rule how it works
    if player == 'r' and opponent == 's' or player == 's' and opponent == 'p'\
            or player == 'p' and opponent == 'r':
        return True


print(play())  # calling play function to start playing
