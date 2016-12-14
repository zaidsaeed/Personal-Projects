# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

#Zaid Saeed
#Student Number: 8621155
#Date : 30/10/2016
#Assignment #3
import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     human=[]

     for d in range (0, len(deck), 2):  #This function is appending one element(card) to one list(hand) and another element(card) to another list(hand)
         dealer.append(deck[d])     #This distributing function is assuming that there are only 2 players playing this game (dealer = computer and human = human)
     for h in range (1, (len(deck)-1), 2):
         human.append(deck[h])

     return (dealer, human)
 


def remove_pairs(l):
    i = 0
    '''
     (list of str)-> (list of str)

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    l.sort()
    while i < (len(l)-1):
        if l[i][1] == 0 and l[i+1][1] == 0:
            l.remove(l[i])
            l.remove(l[i])
        elif l[i][0] == l[i+1][0]:
            l.remove(l[i])
            l.remove(l[i])
        elif l[i] != l[i+1]:
            i = i + 1
    no_pairs  = l
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for i in deck:
        print(i, end = " ")
    
def get_valid_input(n):
     '''
     (int) -> int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     try:
         u = 0
         while u < 1 or u > n:
            u = int(input("Enter a number greater than or equal to 1 and less than " + str(n+1) + ":"))
         return u
     except ValueError:
        u = 0
        while u < 1 or u > n:
            u = int(input("Enter a number greater than or equal to 1 and less than " + str(n+1) + ":"))
        return u
def trade_cards(dealer,human):
    ''' (list , list) --> list,list
    This function takes in two lists and simulates the trading a card per hnd and removing potential pairs experience in the Old Maid.
    At the the end, this function will return, an empty list (the deck of the winner) and a list with the queen (the deck of the loser). '''
    i = 0
    try:
        while not(len(dealer) <= 1 and len(human) <= 1):
            print ('Your Turn \n')
            print ('Your current deck of cards is: \n')
            print (human, '\n')
            aug = 'I have '+ str(len(dealer))+ ' cards. If 1 stands for my first card and ' + str(len(dealer)) + ' for my last card, which of my cards would you like?:'
            print(aug)
            u = get_valid_input(len(dealer))
            if u == 1:
                print ('You asked for my ', str(u)+'st card.')
            elif u == 2:
                print ('You asked for my ', str(u)+'nd card.')
            elif u == 3:
                print ('You asked for my ', str(u)+'rd card.')
            else:
                print ('You asked for my ', str(u)+'th card.')
            print('Here it is. It is '+ dealer[u-1]+ '\n')
            print('With '+ dealer[u-1]+ ' added. Your current deck is:')
            human.append(dealer[u-1])
            print(human)
            dealer.remove(dealer[u-1]) #We don't add to the value of i, because the remove function decreases the number of elements in the list.
            remove_pairs(human)
            print('And after discarding pairs and shuffling, your deck is: \n')
            shuffle_deck(human)
            print(human)
            wait_for_player()
            print('*********************************************************** \n')
            print('My turn')
            v = random.randint(1,len(human))
            if v == 1:
                print ('I took your '+ str(v)+ '\'st card. Here it is ' + human[v-1])
            elif v == 2:
                print ('I took your '+ str(v)+'\'nd card. Here it is ' + human[v-1])
            elif v == 3:
                print ('I took your '+ str(v)+'\'rd card. Here it is ' + human[v-1])
            else:
                print ('I took your '+ str(v)+'\'th card. Here it is ' + human[v-1])
            dealer.append(human[v-1])
            human.remove(human[v-1])
            remove_pairs(dealer)
        return (dealer,human)
        wait_for_player()
    except:
        return (dealer,human)
        
        


def determine_winner(dealer,human):
    ''' (list,list) --> String
    This function looks at which list is empty and states who the winner of the game is.'''
    if len(dealer)==0:
        print('I win!')
    elif len(human) == 0:
        print('Congratulations! You, human, win.')
        
def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     print('***********************************************************')
     trade_cards(dealer,human)
     dealer = trade_cards(dealer,human)[0]
     human = trade_cards(dealer,human)[1]
     determine_winner(dealer,human)
	 

# main
play_game()
