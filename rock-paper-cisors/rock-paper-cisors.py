import typing, random

available = [ 'rock', 'paper', 'cisors' ]

def bot_play() -> str:
    return available[random.randint(0, 2)]

def player_play() -> str:
    player = input()
    while not player in available:
        print(f"tip: should be one of {available}")
        player = input()

    return player

def play() -> (int, int):
    relationship = {
        'rock': 'paper',
        'paper': 'cisors',
        'cisors': 'rock'
    }
    player = player_play()
    bot = bot_play()

    print(f"bot played {bot}")

    if relationship[player] == bot:
        print("bot scores")
        return (0, 1)
    elif relationship[bot] == player:
        print("player scores")
        return (1, 0)
    else:
        print("nothing happend")
        return (0, 0)

score = (0, 0)
while score[0] != 3 and score[1] != 3:
    turn_score = play()
    score = (turn_score[0] + score[0], turn_score[1] + score[1])
    print(f"player: {score[0]}, bot: {score[1]}")

if score[0] == 3:
    print("player win!!!")
else:
    print("bot win!")




