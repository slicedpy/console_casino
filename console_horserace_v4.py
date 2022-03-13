#Title: Console Derby
#Date: Dec 2016
#Contributors: slicedpy (https://github.com/slicedpy)
#Purpose: Exploratory scripting to stay sharp with python in general, nothing fancy, just fun.
#-----------------------------------------------------------------------------
#
#

# Import needed packages()
# time : simulates game play
# random: simulates/adds chance
# csv: Allows the import of 'data' files--can be easily subbed for odbc
# os: Allows the manipulation of the window to fit the banners
#

# Dependencies
# race_catalog.csv - consist of the horses and horse attributes.
# race_record.csv - csv appended after the race
#
#

import time
import random
import csv
import os


# Global Variables()
# Track - refers to the distance of the race (sort of like 100 = 100m)
# user_choice - refers to who the user believe will win
# user_bet - refers to the how much the user wants to wager for their choice
# user_wallet - refers to user's virtual credits (dollars); not a global variable (not sure why I did that, may change it)
# game_on - refers to whether or not the player is still playing (or if they 'can')
#
#


global track
global user_choice
global user_bet
global game_on

go_flag = 1
user_wallet = 1000.00
track = 100

os.system("mode con cols=100 lines=40")

# Classes()
#
# racehorse - each horse has attributes associated
#
#   Not to be made - the racehorse class gets rebuild each race--that can be good and bad in some cases
#   wasted resource recreating objects BUT if the support files were to change, the rebuild would be
#   able to catch up on the fly instead of having to reload the script--something to think about
#
#   The only function besides initiating is the show_stats; pretty nifty and used in a for loop
#   later down the line. Still needs some adjustment to be a little more automation friendly
#
#

class racehorse(object):

    def __init__(self,horseNum,horseName,lowStride,highStride,age,sex,lbs,org,trainer,distance):
        self.horseNum = horseNum
        self.horseName = horseName
        self.lowStride = lowStride
        self.highStride = highStride
        self.age = age
        self.sex = sex
        self.lbs = lbs
        self.org = org
        self.trainer = trainer
        self.distance = 0

    def show_stats(self):
            
        listing = [str(self.horseNum),self.horseName,str(self.lowStride)+"/"+str(self.highStride),\
                   str(self.age),str(self.sex),str(self.lbs),str(self.org),str(self.trainer)]
        listing_gaps = [12,16,7,7,7,7,7,9] 
        listing_str = ""

        for each,gap in zip(listing,listing_gaps):
            listing_str += each + " "*(gap-len(each)) + "| "

        print(listing_str)


     
# Functions ()
#
# console_derby():
#   Basically, the answer board for the rest of the functions--allows the script to be in a continues interactive loop
#   Can simply add options and shortcuts here for the user to access (call other functions)
#
#

    
# create_banner(banner_file="banner.txt",whichMenu="start"):
#   Creates the welcome ASCII banner from the text file--defaulted to save a little headache if parameters are passed
#   for whatever reason. ASCII credit to http://patorjk.com
#
#

   
# exit_game():
#   The exact opposite of the welcome screen; breaks the go_flag loop when the player wants to quit ("cash out") or
#   runs out of money in their user_wallet
#
#


# gameClaim():
#   Similar to a dealer collecting chips; game claim functions present the winner circle and declares the user
#   a winner or a loser (including adjusting the user_wallet to reflect respectively). Have yet to figure odds
#   and what not so the winnings are currently hardcoded (at 8% the last I checked). Eventually, with more tracks
#   odds and side bets, this will be adjusted to take all of those aspects into consideration
#
#   This function allows returns a 1 to the go_flag to continue--the onle instance where that is not the case is
#   when the wallet amounts to 0 (signifying that the user can't play anymore if they wanted to.
#


# getKey(item):
#   This was a nifty little function I found on StackOverflow to handling the sorting of the leaderboard. IIRC, it
#   it allows the sort function to sort ont he first indice of a list
#
#


# load_race_catalog():
#   Loads the race_catalog.csv in read-only; returns a list of racehorse() objects to iterate through during the run_race()
#   funciton
#
#


# run_race():
#   Function to increment the distance attribute to the track value using the listed objects from the load_race_catalog function.
#   Values increment randomly based on a number between the low stride and high stride of the horse. Ideally, horses with a
#   higher stride will also have chances to have a low stride. For example, a high stride of 9 will usually come with a low stride
#   of 1 or 2. So a horse at 1/9 can produce increment of (9+7+1) against a 4/7 horse (6+5+7).
#
#   Prints out the progress of the race 1 sec at a time to keep the player updated on the progress of the race. Have yet to
#   to figure out how to clear the previous print to simply appear to be updating the distance. That' okay for now.
#
#   Returns the leaderboard in descending order to declare the winner in the gameClaim() function.
#
#


# showHorseCatalog():
#   Basically a formatting function to show the attributes of the race horses (ie Horsename, LS/HS).
#
#

# showRaceRecords():
#   A formatting function that reads and calculates from the race_record.csv--definitely can be improved using
#   data analysis tools. Would for sure be updated when migrated/upcoded to python 3.x
#
#

# validateFunds():
#   Takes user input for which horse they want to bet on (defaulted to 'Lucky Day') and how much they want to bet
#   (defaulted at $50.00). Might actually have a redudant filter for an empty wallet. Still need to code logic
#   to tell the user that the horse they chose does exist. For now, if the user wants to back a horse that doesn't
#   exist, they can just (and will) just lose). This includes misspelling the horses name (working on a spellchecker
#   in another project--custom spell checking).
#
#

# user_selection():
#   This function runs the cursor that is presented to the user before and after a race. It does have logic
#   to not allow the user to enter invalid options. Anything other than valid is returned as an 'X' which
#   runs through and repeats the selection function.
#
#

def create_banner(banner_file="banner.txt",whichMenu="start"):
    options_menu=["[S]tart Racing","[H]orse Catalog/Stats","[R]ace Records","[A]bout"]

    if whichMenu == "start":
        with open(banner_file,'r') as banner:
            print(banner.read())
            time.sleep(2)
            for each in options_menu:
                gap = int((66-len(each))/2)
                print(" "*gap + each + " "*gap)
                
    if whichMenu == "continue":
        print("SELECT AN OPTION:")
        print("=-" * 12)
        for each in options_menu:
            print(each)
        print("\n")

    if whichMenu == "end":
        with open(banner_file,'rb') as banner:
            print(banner.read())
            
def exit_game():
    global go_flag
    create_banner("credit_banner.txt","end")

    go_flag = 0


def load_race_catalog():
    stable = []
    with open('race_catalog.csv','r') as race_catalog:
        loaded_catalog = csv.reader(race_catalog,delimiter=',',quotechar='"')
        for entry in loaded_catalog:
            try:
                stable.append(racehorse(str(entry[0]),str(entry[1]),int(entry[2]),\
                                        int(entry[3]),int(entry[4]),str(entry[5]),\
                                        int(entry[6]),str(entry[7]),str(entry[8]),0))
            except ValueError:
                pass
            
    return stable


def validateFunds():

    global user_bet
    global user_choice
    global user_wallet
    
    user_choice = input("\nWho do you think is going to win?: ") or "LUCKY DAY"
    user_bet = float(input("How much do you want to bet?: ") or 50.00)


    if user_wallet <= 0:
        print("Looks like you're out of funds!")
        exit_game()
            
    while user_wallet < user_bet:
        user_bet = float(input("You can't bet more than you have--How much do you want to bet?: ") or 50.00)
        

    
def user_selection():
    option_choice = input("\nSTART RACE? [S] >> ",).upper() or "S"

    if len(option_choice)>=2:
        option_choice ='X'

    try:
        if int(option_choice):
            option_choice='X'
    except:
        pass

    return option_choice.upper()

 
def getKey(item):
    return item[1]


def run_race():

    global user_choice
    global user_bet
        
    end_race = False
    leaderboard = []
    starter_gun = 0

    stable = load_race_catalog()

    validateFunds()

    print("\nALL BETS ARE IN!")
    print(user_choice.upper())
    print("$" + str(("%.2f" % user_bet)).upper() + "\n")
    print("Start: %s" % time.ctime())

    while end_race == False:
        if starter_gun == 0:
            time.sleep(1)
            print("\nON YOUR MARK...")
            time.sleep(1)
            print("GET SET...")
            time.sleep(1)
            print("GO!")
            starter_gun += 1
            
        elif starter_gun > 0:
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
                print(tops[0] + "."*(18-len(tops[0])) + str(tops[1]))

            print("\n")
            
    print("End time: %s" % time.ctime()+ "\n")

    return sorted(leaderboard, key=getKey,reverse=True)

def gameClaim():
    global user_choice
    global user_bet
    global user_wallet
    
    leaders = run_race()
    winners_circle = [["1st Place: ", leaders[0][0].upper()],\
                   ["2nd Place: ",leaders[1][0].upper()],\
                   ["3rd Place: ", leaders[2][0].upper()]]

    with open('race_record.csv','a+') as race_record:
        for winner in winners_circle:
            print(winner[0] + winner[1])
            race_record.write(str(winner[0][0])+","+str(winner[1])+"\n")

    print("\n")

    if user_choice.upper() == winners_circle[0][1]:
        user_wallet += float(user_bet*1.08)
        print("$^$"*10)
        print("\nPLAYER WINS! WALLET: $" + str(("%.2f" % user_wallet)) +'\n')
        print("$^$"*10 + "\n")
        
    else:
        user_wallet -= float(user_bet)
        
        if user_wallet <= 0:
            print("Looks like you're out of funds!")
            exit_game()
            return 0
        
        print("@X@"*10)
        print("\nPLAYER LOSES! WALLET: $" + str(("%.2f" % user_wallet)) + '\n')
        print("@X@"*10 + "\n")

    return 1
    

def showRaceRecords():
    board = []
    race_stats = []

    with open('race_record.csv','rb') as loaded_record:
        race_record = csv.reader(loaded_record,delimiter=',',quotechar='"')
        header_check = 0
        
        for entry in race_record:
            if header_check == 0:
                header_check += 1
                pass
            else:
                try:
                    board.index(entry[1])
                except ValueError:
                    board.append(entry[1])
                    
        header_check = 0

    with open('race_record.csv','rb') as loaded_record:
        race_record = csv.reader(loaded_record,delimiter=',',quotechar='"')
        header_check = 0

        for horse in board:
            race_stats.append([horse,0,0,0])

        for entry in race_record:
            if header_check == 0:
                header_check += 1
                pass
            else:
                for each in race_stats:
                    if str(entry[1]) == str(each[0]):
                        each[int(entry[0])] += 1

    head_tags = ["Horse Name","1ST","2ND","3RD"]
    gap = 18
    head_line = "-"*(gap+1)*len(head_tags) + "\n"

    for each in head_tags:
        spacer = gap - len(each)
        head_line += str(each) + " "*spacer + "|"

    print("\n" + "/"*(gap*2) + "RACE RECORDS" + "/"*(gap*2))
    print(head_line)


    for i in race_stats:
        line_made = ""
        for cell in i:
            if len(str(cell)) <= 3:
                line_made += " "*((gap/2)-len(str(cell))) + str(cell) + " "*(gap/2) + "|"
            else:
                line_made += str(cell) + " "*(gap-len(str(cell)))+ "|"
                
        print(line_made)

def showHorseCatalog():
    headers = ["Horse No.","Horse Name","L/H","Age","M/F","LBS","ORG","TRAINER"]
    headers_gaps = [12,16,7,7,7,7,7,9] 
    header_str = ""

    for each,gap in zip(headers,headers_gaps):
        header_str += each + " "*(gap-len(each)) + "| "

    print(header_str)

    for each in load_race_catalog():
        each.show_stats()
    
 
def console_derby():
    go_flag = 1
    
    while go_flag == 1:
        answer = user_selection()

        if answer == 'S':
            go_flag == gameClaim()

        if answer == 'H':
            showHorseCatalog()

        if answer == 'R':
            showRaceRecords()

        if answer == 'Q' or len(answer)>16:
            exit_game()


if __name__ == "__main__":
    create_banner()
    console_derby()
