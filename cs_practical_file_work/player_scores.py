player_dict = {"Aman": 45, "Riya" : 82, "Sarthak": 80}
def players(player_dict):
    highest = 0
    for i in player_dict:
        if player_dict[i] > highest:
            highest = player_dict[i]
            winner = i
    return winner, highest

print(players(player_dict))