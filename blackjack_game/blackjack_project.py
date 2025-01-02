import random # 1

def deal_card(): # 1:
    """ Returns a random card from the deck """

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards) # gives a random choice from the list, which is assigned to a variable called cards
    return card

def calculate_score(cards): # 3: cards is added to the parameter as an input
    """ Take a list of cards and return the score after the cards has been calculated using the sum() function """
    if sum(cards) == 21 and len(cards) == 2: # 4: checks if a hand has dealt 2 cards: ace + 10 then it will
        return 0 # 4: returns zero, which represents blackjack in the game

    if 11 in cards and sum(cards) > 21: # 5: checks if 11(ace) is in cards and the total score is already over 21,
                                        # so then the 11 will be removed and be replaces it with 1(ace)
        cards.remove(11)
        cards.append(1)

    return sum(cards) # 3: returns tha value of the cards and using the sum function to calculate
                        # what has been added to the list of the variable called cards
                        # e.g: cards = [1, 3, 5, 6] which is 1 + 3 + 5 + 6 and the output will be 15

def compare(u_score, c_score): # 10 - compare the result of each outcome
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Lose, opponent has Blackjack!"
    elif u_score == 0:
        return "You WIN with a BLACKJACK!"
    elif u_score > 21:
        return "You went over, you Lose"
    elif c_score > 21:
        return "Opponent went over, you WIN"
    elif u_score > c_score:
        return "You WIN"
    else:
        return "You Lose"

def play_game():
    user_cards = [] # 2: empty list
    computer_cards = [] # 2: empty list
    user_score = -1 # 9
    computer_score = -1 # 9
    is_game_over = False # 6: stays False until user or computer meet 0 or has > 21 score, which will end the game

    for _ in range(2): # 2: '_' - underscore is there as the variable is not needed, a loop is required to run twice (2)
        new_card = deal_card() # dealer deal new cards
        user_cards.append(new_card) # deal a new cards to user and gets added to the empty user_cards list
        computer_cards.append(new_card) # deal a new cards to computer and gets added to the empty computer_cards list

    while not is_game_over: # 8: creating a while loop
        user_score = calculate_score(user_cards) # 6: calls the function
        computer_score = calculate_score(computer_cards) # 6: calls the function
        print(f"Your cards: {user_cards}, current score: {user_score}") # 6: print's the user's cards and score
        print(f"Computer's first card: {computer_cards[0]}") # 6: print's the computer's first card

        if user_score == 0 or computer_score == 0 or user_score > 21: # 6: Ends the game if user or computer score 0 or > 21
            is_game_over = True # True is active if the user or computer meet the above statement
        else:
            user_should_deal = input("Type 'y' to get another card or type 'n' to pass: ") # 7: asking user if they want to continue or pass
            if user_should_deal == "y":
                user_cards.append(deal_card()) # deal draws another card
            else:
                is_game_over = True # 'n' to end the game

    while computer_score != 0 and computer_score < 17: # 9: allows the computer to play and keep drawing cards as long as the score is under 17
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # 10: prints out the result of the final hand
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y": # 11: asking the user if they want to a play a Blackjack game
    # print("\n" * 20)
    play_game()
