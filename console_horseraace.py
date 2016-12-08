import time
import random
import numpy as np

global track

go_flag = 1

while go_flag == 1:
    print "Start: %s" % time.ctime()

    horse1 = ["Lucky Day",0,5,3]
    horse2 = ["Dear Aunt Sally",0,7,1]

    all_horses = [horse1,horse2]

    winning_horse = ""

    track = 175

    user_wallet = 100

    for each_horse in all_horses:
        print each_horse[0] + " with " + str(each_horse[3]) + ":" + str(each_horse[2]) + " stride."


    user_choice = raw_input("\nWho do you think is going to win?: ") or "LUCKY DAY"

    user_bet = raw_input("How much do you want to bet?: ") or 5

    print "\nALL BETS ARE IN!"
    print user_choice.upper()
    print user_bet.upper() + "\n"
        

    def announcer(h1,h2,track):
        progress = " (" + str(int((np.mean([h1[1],h2[1]])/track)*100)) + "% of race completed)"
        
        if h1[1] > h2[1]:
            #print "(" + str(h1[1]) + ") vs ("+ str(h2[1]) + ") " +
            print h1[0] + " leads by " + str(h1[1] - h2[1]) + progress

        if h2[1] > h1[1]:
            #print "(" + str(h1[1]) + ") vs ("+ str(h2[1]) + ") " +
            print h2[0] + " leads by " + str(h2[1] - h1[1]) + progress

        if h1[1] == h2[1]:
            if h1[1] >= 100 and h2[1] >= 100:
                print "IT'S LOOKING LIKE A PHOTO FINISH!"
                track += 10  
            else:
                #print "(" + str(h1[1]) + ") vs ("+ str(h2[1]) + ") " +
                print h1[0] + " and " + h2[0] + " neck and neck!" + progress

    while horse1[1] <= track and horse2[1] <= track:    

        if horse1[1] == 0 and horse2[1] == 0:
            time.sleep(1)
            print "\nON YOUR MARK..."
            time.sleep(1)
            print "GET SET..."
            time.sleep(1)
            print "GO!"
            
            horse1[1] += random.randint(horse1[3],horse1[2]) # 1
            horse2[1] += random.randint(horse2[3],horse2[2]) # 3
            
        else:
            time.sleep(1)

            announcer(horse1,horse2,track)

            horse1[1] += random.randint(horse1[3],horse1[2])
            horse2[1] += random.randint(horse2[3],horse2[2])
            
                

    if horse1[1] >= track and horse2[1] >= track:
        if horse1[1] > horse2[1]:
            print horse1[0] + " WINS!"

        if horse2[1] > horse1[1]:
            print horse2[0] + " WINS!"
            
    elif horse1[1] > horse2[1]:
        print horse1[0] + " WINS!"
        winning_horse = horse1[0]
    else:
        print horse2[0] + " WINS!"
        winning_horse = horse2[0]

    print "End time: %s" % time.ctime()+ "\n"

    if user_choice.upper() == winning_horse.upper():
        print "Player wins!"
        user_wallet += int(user_bet)
        print "Player wallet now: " + str(user_wallet) + "\n\n"
        
    else:
        print "Player loses!"
        user_wallet -= int(user_bet)
        print "Player wallet now: " + str(user_wallet) + "\n\n"



##        if horse1 > horse2:
##            print "(" + str(horse1) + ") vs ("+ str(horse2) + ") horse1 leads by " + str(horse1 - horse2)
##
##        if horse2 > horse1:
##            print "(" + str(horse1) + ") vs ("+ str(horse2) + ") horse2 leads by " + str(horse2 - horse1)
##
##        if horse2 == horse1:
##            if horse2 >= 100 and horse1 >= 100:
##                print "PHOTO FINISH!"
##                track += 10
##                
##            else:
##                print "(" + str(horse1) + ") vs ("+ str(horse2) + ") horse1 and horse2 neck and neck"
##

    
        
    
