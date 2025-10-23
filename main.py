from game_logic import game

if __name__ == "__main__":
    start = game.init_game()
    while len(start["player_1"]["hand"]) > 0 & len(start["player_2"]["hand"]):
        game.play_round(start["player_1"],start["player_2"])
    if len(start["player_1"]["won_pile"]) > len(start["player_2"]["won_pile"]):
        print("p1")
    elif len(start["player_1"]["won_pile"]) > len(start["player_2"]["won_pile"]):
        print("p1")
    else:
        print("war")



