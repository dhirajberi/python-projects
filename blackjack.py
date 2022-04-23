# blackjack or 21
# 21 se jyda then loose
# 2 to 10 face value
# J,Q,K = 10
# A = 1 or 11
import random
cards = [2,3,4,5,6,7,8,9,10,'j','q','k','a']

your_cards = []
computer_cards = []

# total of your cards
def calcTotalYourCard():
    total_your_cards = 0
    for card in your_cards:
        if card=='j' or card=='q' or card=='k':
            total_your_cards = total_your_cards + 10
        elif card=='a':
            total_your_cards = total_your_cards + 11
        else:
            total_your_cards = total_your_cards + card
    return total_your_cards
        

# total of computer cards
def calcTotalComputerCard():
    total_computer_cards = 0
    for card in computer_cards:
        if card=='j' or card=='q' or card=='k':
            total_computer_cards = total_computer_cards + 10
        elif card=='a':
            total_computer_cards = total_computer_cards + 11
        else:
            total_computer_cards = total_computer_cards + card
    return total_computer_cards

def pickNewCard():
    call = input("Pick new card?: ")
    if call == 'y':
        your_cards.append(random.choice(cards))
        print(f"Your cards: {your_cards}, total: {calcTotalYourCard()}")
        print(f"Computer first card: {computer_cards[0]}")
        if calcTotalYourCard() > 21:
            print("You Bust!")
            print(f"Your cards: {your_cards}, total: {calcTotalYourCard()}")
            print(f"Computer final cards: {computer_cards}, total: {calcTotalComputerCard()}")
            return
        elif calcTotalYourCard() == 21:
            print("You blackjack!")
            print(f"Your cards: {your_cards}, total: {calcTotalYourCard()}")
            print(f"Computer final cards: {computer_cards}, total: {calcTotalComputerCard()}")
            return
        pickNewCard()
    else:
        calculate()
        
def calculate():
    print(f"Your cards: {your_cards}, total: {calcTotalYourCard()}")
    print(f"Computer final cards: {computer_cards}, total: {calcTotalComputerCard()}")
    if calcTotalComputerCard() > 21:
        print("Computer Bust!")
        return
    elif calcTotalComputerCard() == 21:
        print("Computer blackjack!")
        return
    elif calcTotalComputerCard() == calcTotalYourCard():
        print("Draw")
        return
    elif calcTotalComputerCard() > calcTotalYourCard():
        print("Computer wins!")
        return
    elif calcTotalComputerCard() < calcTotalYourCard():
        computer_cards.append(random.choice(cards))
        calculate()
        
# at start pick two cards
your_cards.append(random.choice(cards))
your_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))
computer_cards.append(random.choice(cards))


print(f"Your cards: {your_cards}, total: {calcTotalYourCard()}")
print(f"Computer first card: {computer_cards[0]}")
pickNewCard()
