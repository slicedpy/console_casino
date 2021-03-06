# Import the random module to implement 'chance' element
import random


# There's only one deck and it must be shuffled.
global shuffled
shuffled = []

# Before it's shuffled, the deck must be created.
def newDeck():
    # Couldn't figure out unicode stuff for the symbols, using letters instead to
    # respective shape
    suits = ["S","H","C","D"]
    values = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
    stack = []

    # Make the cards (One value per suit)
    for face in values:
        for card in suits:
            stack.append(str(face)+str(card))

    # Create the shuffled deck
    for cards in stack:
        while len(stack)<>1:
                pickedcard = stack[int(random.randrange(0,len(stack)))]
                shuffled.append(pickedcard)
                stack.remove(pickedcard)
                
        if len(stack) == 1:
            pickedcard = stack[0]
            shuffled.append(pickedcard)
            stack.remove(pickedcard)

        # Let the use know that the desk has been shuffle
        print "**Cards are shuffled**\n"
        return shuffled


# Supply the shuffled deck for first round
newDeck()

# Set up game cues including credits and wager
flag = True
playerpts = 100
wager = 0

# Set game in loop
while flag == True:
    
    # Broke players can't play
    if playerpts == 0:
        break

    # Stay in the loop if the play stays on their hand  
    stay = False

    # Set game wager--no changing in the middle. GH||GH
    if wager == 0:
        wager = int(raw_input("How much do you want to wager per hand?: ") or 5)

    # To make sure there's another cards in the deck, reshuffle.
    # Also makes harder to count
    if len(shuffled) < 15:
        newDeck()

    # Enable dictionary for card value reference not numeric
    cardkey = {
    'A': 11,'K': 10,'Q': 10,
    'J': 10,'1': 10,'9': 9,
    '8': 8,'7': 7,'6': 6,
    '5': 5,'4': 4,'3': 3,
    '2': 2};

    # Create card holders for both players
    dealer=[]
    player=[]

    # Establish blank slate
    dealerhand = 0
    playerhand = 0

    # Deal the first two cards for the dealer
    for each in range (0,2):
        drawcard = shuffled[int(random.randrange(0,len(shuffled)))]
        dealer.append(drawcard)
        shuffled.remove(drawcard)

    # Deal the first two cards for the player
    for each in range(0,2):
        drawcard = shuffled[int(random.randrange(0,len(shuffled)))]
        player.append(drawcard)
        shuffled.remove(drawcard)

    # Add up the initial value of the player
    # '10' a little tricky because of 1 being the first digit
    # TODO: Maybe just change the dictionary to accept '1' as 10?
    # Won't cause a big problem, it's the only one.
##    
##    for card in dealer:
##        try:
##            dealerhand += cardkey[card[0]]
##        except Exception:
##            dealerhand += cardkey["10"]
##
##    for card in player:
##        try:
##            playerhand += cardkey[card[0]]
##        except Exception:
##            playerhand += cardkey["10"]

    # Implemented from above--mod the dictionary for reverting back
    for card in dealer:
        dealerhand += cardkey[card[0]]


    for card in player:
        playerhand += cardkey[card[0]]
            
    # Show player their hand but not the dealer's
    print "\nDealer: " + dealer[0] + "- ?"
    print "Player: " + player[0] + "-" + player[1]


    # Automatically give player win for BlackJack
    if playerhand == 21:
        print "Player BlackJack\n-----------------------------------\n"
        playerpts +=wager
        print "Player has: " + str(playerpts) +" credits."
        print "Dealer's hand: " + str(dealer[0:]) + "(" + str(dealerhand) +")"
        print "Player's hand: " + str(player[0:]) + "(" + str(playerhand) +")\n"
        stay = True
        raw_input("Next Hand")

    # Let player decide to hit or not 
    if playerhand < 21:
        while stay == False:
            hit = raw_input("Hit?\n-----------------------------------\n") or 'Y'

            if hit == 'N' or hit =='n':
                stay = True

                # Once the player stay, allow the dealer to draw
                # Cards can't be split and dealer will hit on anything
                while dealerhand <= 21:
                    if dealerhand == 21:
                        print "Dealer BlackJack\n-----------------------------------\n"
                        playerpts -=wager
                        print "Player has: " + str(playerpts) +" credits."
                        print "Dealer's hand: " + str(dealer[0:]) + "(" + str(dealerhand) +")"
                        print "Player's hand: " + str(player[0:]) + "(" + str(playerhand) +")\n"
                        raw_input("Next Hand")
                        break

                    if dealerhand < 21:
                        
                        if dealerhand >= playerhand:
                            print "Dealer wins!"
                            print "Dealer's hand: " + str(dealer[0:]) + "(" + str(dealerhand) +")"
                            print "Player's hand: " + str(player[0:]) + "(" + str(playerhand) +")\n"
                            playerpts -=wager
                            print "Player has: " + str(playerpts) +" credits."
                            break

                        if dealerhand <= playerhand:
                            drawcard = shuffled[int(random.randrange(0,len(shuffled)))]
                            dealer.append(drawcard)
                            shuffled.remove(drawcard)
                            dealerhand = 0

                            for card in dealer:
                                try:
                                    dealerhand += cardkey[card[0]]
                                except Exception:
                                    dealerhand += cardkey["10"]
                        

                    if dealerhand > 21:
                        print "Dealer Bust"
                        print "Dealer's hand: " + str(dealer[0:]) + "(" + str(dealerhand) +")"
                        print "Player Wins!" + str(player[0:]) + "(" + str(playerhand) +")\n"
                        playerpts += wager
                        print "Player has: " + str(playerpts) +" credits."
                        break

            # Feed player cards from available deck until stay or bust            
            elif hit == 'Y' or 'y':
                drawcard = shuffled[int(random.randrange(0,len(shuffled)))]
                player.append(drawcard)
                shuffled.remove(drawcard)
                playerhand = 0

                for card in player:
                    try:
                        playerhand += cardkey[card[0]]
                    except Exception:
                        playerhand += cardkey["10"]

                if playerhand > 21:
                    print "Player Bust"
                    print "Player: " + str(player[0:]) + "(" + str(playerhand) +")"
                    print "Dealer's hand: " + str(dealer[0:])+ "(" + str(dealerhand) +")" +"\n"
                    playerpts -=wager
                    print "Player has: " + str(playerpts) +" credits."
                    stay = True

                else:
                    print "Player: " + str(player[0:]) + "(" + str(playerhand) +")"
                    
# See ya...broke players don't play.
print "You account is now 0. Thank you for playing Console Blackjack."
