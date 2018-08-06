def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line
def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    
    i=0
    score=0
    av=0 
    totalscore=0
    
    while sum(x for x in hand.values()) > 0:
        print("current Hand:"+displayHand(hand))
        
        word=str(input("enter a word, or a"+" "+ "." +" "+" to indicate that you are finished:"+" ")).lower()
        if word=='.':
            print("good Bye Total Score:"+" "+str(score))
            break

        
        if isValidWord(word,hand,wordList)!=True:
                 print()
            
                 print("invalid word plese try again")
    
        else:
                
                hand=updateHand(hand,word)
                score=getWordScore(word,n)
                totalscore+=score
                print(str(word)+" "+"earned"+" "+str(score)+" "+"points."+" "+"Total:"+str(totalscore))
                

        
    print()
    print("Run out of letters."+" "+ "Total score  :"+" "+str(score))