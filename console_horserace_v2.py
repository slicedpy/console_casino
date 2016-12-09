import time
import random
import numpy as np
import csv


global track

go_flag = 1
user_wallet = 100

track = 234

class racehorse(object):

    def __init__(self,horseNum,horseName,lowStride,highStride,distance):
        self.horseNum = horseNum
        self.horseName = horseName
        self.lowStride = lowStride
        self.highStride = highStride
        self.distance = 0


    def show_stats(self):
        print "Horse No.: #" + str(self.horseNum)
        print "Horse Name: " + self.horseName
        print "Low Stride: " + str(self.lowStride)
        print "High Stride: " + str(self.highStride) +"\n"


def getKey(item):
    return item[1]

def load_race_catalog():
    stable = []
    with open('race_catalog.csv','rb') as race_catalog:
        loaded_catalog = csv.reader(race_catalog,delimiter=',',quotechar='"')
        for entry in loaded_catalog:
            try:
                stable.append(racehorse(str(entry[0]),str(entry[1]),int(entry[2]),int(entry[3]),0))
            except ValueError:
                pass
            
    return stable


keepgoing = 'y'
def run_race():

    stable = load_race_catalog()
        
    end_race = False
    leaderboard = []

    while end_race == False:
        time.sleep(1)
        
        for each in stable:
            each.distance += random.randint(each.lowStride,each.highStride)

            if each.distance >= track:
                end_race = True
            else:
                leaderboard=[]

        for each in stable:
            leaderboard.append([each.horseName,each.distance])

        for tops in sorted(leaderboard, key=getKey,reverse=True):
            print tops[0] + "."*(18-len(tops[0])) + str(tops[1])

        print "\n"

    return sorted(leaderboard, key=getKey,reverse=True)


while keepgoing == 'y':
    leaders = run_race()
    first_place = leaders[0]
    second_place = leaders[1]
    third_place = leaders[2]

    print "FIRST PLACE: " + first_place[0]
    print "SECOND PLACE: " + second_place[0]
    print "THIRD PLACE: " + third_place[0] + "\n"

    keepgoing = raw_input("Keep going?: ") or 'y'



#for each_horse in leaderboard:
    #print str(each_horse[0]) + "."*(18-len(each_horse[0])) + str(each_horse[1])



#print str(len(stable)) + " horses are in the stable."

#horse_1.show_stats()


##while go_flag == 1:
##    print "Start: %s" % time.ctime()
##
##    horse1 = ["Outlandish",0,5,3]
##    horse2 = ["Awesome Aussie",0,7,1]
##
##    all_horses = [horse1,horse2]
##
##    winning_horse = ""
##
##    track = 175
##
##
##    for each_horse in all_horses:
##        print each_horse[0] + " with " + str(each_horse[3]) + ":" + str(each_horse[2]) + " stride."
##
##
##    user_choice = raw_input("\nWho do you think is going to win?: ") or "LUCKY DAY"
##
##    user_bet = raw_input("How much do you want to bet?: ") or 5
##
##    print "\nALL BETS ARE IN!"
##    print user_choice.upper()
##    print user_bet.upper() + "\n"
##        
##
##    def announcer(h1,h2,track):
##        progress = " (" + str(int((np.mean([h1[1],h2[1]])/track)*100)) + "% of race completed)"
##        
##        if h1[1] > h2[1]:
##            #print "(" + str(h1[1]) + ") vs ("+ str(h2[1]) + ") " +
##            print h1[0] + " leads by " + str(h1[1] - h2[1]) + progress
##
##        if h2[1] > h1[1]:
##            #print "(" + str(h1[1]) + ") vs ("+ str(h2[1]) + ") " +
##            print h2[0] + " leads by " + str(h2[1] - h1[1]) + progress
##
##        if h1[1] == h2[1]:
##            if h1[1] >= 100 and h2[1] >= 100:
##                print "IT'S LOOKING LIKE A PHOTO FINISH!"
##                track += 1  
##            else:
##                #print "(" + str(h1[1]) + ") vs ("+ str(h2[1]) + ") " +
##                print h1[0] + " and " + h2[0] + " neck and neck!" + progress
##
##    while horse1[1] <= track and horse2[1] <= track:    
##
##        if horse1[1] == 0 and horse2[1] == 0:
##            time.sleep(1)
##            print "\nON YOUR MARK..."
##            time.sleep(1)
##            print "GET SET..."
##            time.sleep(1)
##            print "GO!"
##            
##            horse1[1] += random.randint(horse1[3],horse1[2]) # 1
##            horse2[1] += random.randint(horse2[3],horse2[2]) # 3
##            
##        else:
##            time.sleep(1)
##
##            announcer(horse1,horse2,track)
##
##            horse1[1] += random.randint(horse1[3],horse1[2])
##            horse2[1] += random.randint(horse2[3],horse2[2])
##            
##                
##
##    if horse1[1] >= track and horse2[1] >= track:
##        if horse1[1] > horse2[1]:
##            print horse1[0] + " WINS!"
##            winning_horse = horse1[0]
##
##        if horse2[1] > horse1[1]:
##            print horse2[0] + " WINS!"
##            winning_horse = horse2[0]
##            
##    elif horse1[1] > horse2[1]:
##        print horse1[0] + " WINS!"
##        winning_horse = horse1[0]
##    else:
##        print horse2[0] + " WINS!"
##        winning_horse = horse2[0]
##
##    print "End time: %s" % time.ctime()+ "\n"
##
##    if user_choice.upper() == winning_horse.upper():
##        print "Player wins!"
##        user_wallet += int(user_bet)
##        print "Player wallet now: " + str(user_wallet) + "\n\n"
##        
##    else:
##        print "Player loses!"
##        user_wallet -= int(user_bet)
##        print "Player wallet now: " + str(user_wallet) + "\n\n"
##
##        
    
