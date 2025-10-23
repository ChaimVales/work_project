
import random
def create_card(rank:str,suite:str) -> dict:
    card_dict = {"rank":rank,"suite":suite}
    if card_dict["rank"] == "J":
        card_dict["value"] = 11
    elif card_dict["rank"] == "Q":
        card_dict["value"] = 12
    elif card_dict["rank"] == "K":
        card_dict["value"] = 13
    elif card_dict["rank"] == "A":
        card_dict["value"] = 14
    else:
        card_dict["value"] = card_dict["rank"]
    return card_dict
    

def compare_cards(p1_card:dict, p2_card:dict) -> str:
    if p1_card["value"] > p2_card["value"]:
        return "p1"
    elif p2_card["value"] > p1_card["value"]:
        return "p2"
    else:
        "WAR"


def create_deck() -> list[dict]:
    deck_dict = []
    ranc_dict = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
    suite_dict =['h','c','d','s']
    for i in suite_dict:
        for j in ranc_dict:
            deck_dict.append(create_card(j,i))
    return deck_dict
    

def shuffle(deck:list[dict]) -> list[dict]:
    card1 = 0
    card2 = 0
    for i in range(1000):
        while card1 == card2:
            card1 = random.randint(0,51)
            card2 = random.randint(0,51)
        deck[card1],deck[card2] = deck[card2],deck[card1]
    return deck






