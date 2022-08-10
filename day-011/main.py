import art
import random


BLACKJACK = 21
DECK = {
    **{str(value): value for value in range(2, 11)},
    **dict.fromkeys(("K", "J", "Q"), 10),
    "A": 11
}


def deal_card() -> str:
    """
        Return random card from the deck.
    """
    return random.choice(list(DECK.keys()))


def calculate_score(cards:'list[str]') -> int:
    """
        Take a list of cards and return score calculated from the cards.
    """
    values = [DECK.get(card) for card in cards]
    score = sum(values)

    while DECK["A"] in values and score > BLACKJACK:
        values.remove(11)
        values.append(1)
        score = sum(values)

    return score


def compare_scores(user:int, dealer:int) -> str:
    """
        Compares user and dealer scores and returns game result.
    """
    if user == dealer:
        return "Draw! 🙃"
    elif user == BLACKJACK:
        return "Blackjack! You won 🤑"
    elif dealer == BLACKJACK:
        return "You lost, the Dealer has a Blackjack 😤💸"
    elif user > BLACKJACK:
        return "BUST! You lose 😤💸"
    elif dealer > BLACKJACK:
        return "You won, the Dealer Bust. 🤑"
    elif user > dealer:
        return "You won. 🤑"
    else:
        return "You lose. 😤💸"


def show_hands(user_hands, dealer_hands, scores, user_turn=True):
    user_hands = ", ".join(user_hands)
    dealer_hands = ", ".join(dealer_hands)
    
    print((      
    f"""
        {f"Your final hand: {user_hands}":50} Final score: {scores["user"]}
        {f"Dealer's final hand: {dealer_hands}":50} Final score: {scores["dealer"]}
    """,
    f"""
        {f"Your hand: {user_hands}":50} Current score: {scores['user']}
        Dealer's first card: {dealer_hands.split(',')[0]}
    """
    )[user_turn])
     

def clear_console() -> None:
    print("\033[H\033[J", end="")


def play_game():

    user_cards, dealer_cards = [deal_card(), deal_card()], [deal_card(), deal_card()]
    user_turn_is_over, game_scores = False, {}
    
    while not user_turn_is_over:
        print(art.LOGO, "Welcome to Blackjack game!", sep="\n", end="\n\n")
        
        game_scores["user"] = calculate_score(user_cards)
        game_scores["dealer"] = calculate_score(dealer_cards)

        show_hands(user_cards, dealer_cards, game_scores)        
     
        if game_scores["user"] >= BLACKJACK:
            user_turn_is_over = True
        else:
            user_decision = None
            while user_decision not in ("h", "s"):   
                user_decision = input("Type 'h' to HINT or type 's' to STAND: ").lower()
            
            if user_decision == "s":
                user_turn_is_over = True
            else: 
                clear_console()
                user_cards.append(deal_card())

            
    while game_scores["user"] <= BLACKJACK and game_scores["dealer"] < 17:
        dealer_cards.append(deal_card())
        game_scores["dealer"] = calculate_score(dealer_cards)
    
    show_hands(user_cards, dealer_cards, game_scores, user_turn=False)
    print(compare_scores(**game_scores))



if __name__ == "__main__":
    clear_console()                 
    while True:
        want_to_play = input("\nDo you want to play a game of Blackjack (y/n)? ").lower()
        
        if want_to_play == "n":
            break
        
        clear_console()                 
        play_game()
        

    print("\nUntil next time!")