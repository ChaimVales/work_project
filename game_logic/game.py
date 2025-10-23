from utils.deck import shuffle, create_deck

def create_player(name:str='AI') -> dict:
    player = {"name":name,"hand":[],"won_pile":[]}
    return player


def init_game()->dict:
    p1 = create_player("haim")
    p2 = create_player()
    deck_of_card = create_deck()
    shuffle(deck_of_card)
    for i in range(26):
         p1["hand"].append([i])
         p2["hand"].append([i+26])
    return {"deck":deck_of_card,"player_1":p1,"player_2":p2}


    
def play_round(p1:dict,p2:dict):
        card1 = p1["hand"].pop(0)
        card2 = p2["hand"].pop(0)
        if card1["value"] > card2["value"]:
            p1["won_pile"].append(card1)
            p1["won_pile"].append(card2)
        elif card2["value"] > card1["value"]:
            p2["won_pile"].append(card1)
            p2["won_pile"].append(card2)
        else:
            p1["won_pile"].append(card1)
            p2["won_pile"].append(card2)

