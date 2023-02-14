import random


def play():
    player = input('Insert Rock(r), Paper(p) or Scissors(s) : ')
    computer = random.choice(['r', 'p', 's'])

    # r>s,p>r,s>p

    if player == computer:
        return 'Its a Tie'
    elif isWin(player, computer):
        return 'You win'
    return 'You Lose'


def isWin(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (
            player == 's' and opponent == 'p'):
        return True
    return False


print(play())
