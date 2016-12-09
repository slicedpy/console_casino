import time
import random
import numpy as np
import csv


global track
global user_choice
global user_bet
global game_on

go_flag = 1
user_wallet = 100.00
track = 100

def welcome_user(cd):
    if cd == 0:
        with open('banner.txt','rb') as banner:
            print banner.read()
            time.sleep(3)
            options_menu=["[S]tart Racing","[H]orse Catalog/Stats","[R]ace Records"]
            for each in options_menu:
                gap = (66-len(each))/2
                print " "*gap + each + " "*gap

            option_choice = raw_input("SELECT>> ",) or "S"
    if cd == 1:
        option_choice = raw_input("SELECT>> ",) or "S"
        

    return option_choice.upper()

def exit_user():
    print "SEE YA....SUCKA!"
    


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


def run_race():

    global user_choice
    global user_bet
    
    stable = load_race_catalog()
        
    end_race = False
    leaderboard = []
    starter_gun = 0

    for each in stable:
        each.show_stats()

    user_choice = raw_input("\nWho do you think is going to win?: ") or "LUCKY DAY"
    user_bet = float(raw_input("How much do you want to bet?: ")) or 5.00


    while end_race == False:
        if starter_gun == 0:
            time.sleep(1)
            print "\nON YOUR MARK..."
            time.sleep(1)
            print "GET SET..."
            time.sleep(1)
            print "GO!"
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
                print tops[0] + "."*(18-len(tops[0])) + str(tops[1])

            print "\n"

    return sorted(leaderboard, key=getKey,reverse=True)

def console_derby(answer):
    if answer == "Q":
        exit_user()
    
    if answer == "S":
        keepgoing = 'y'
        while keepgoing == 'y':

            global user_choice
            global user_bet
            
            leaders = run_race()
            
            first_place = leaders[0]
            second_place = leaders[1]
            third_place = leaders[2]

            print "FIRST PLACE: " + first_place[0]
            print "SECOND PLACE: " + second_place[0]
            print "THIRD PLACE: " + third_place[0] + "\n"

            if user_choice.upper() == first_place[0].upper():
                user_wallet += float(user_bet*1.08)
                print "PLAYER WINS! WALLET:" + str(user_wallet)
            else:
                user_wallet -= float(user_bet)
                print "PLAYER LOSES! WALLET:" + str(user_wallet)
                

            keepgoing = raw_input("Keep going?: ") or 'y'

    elif answer == "H":
        welcome_user(1)

if __name__ == "__main__":
    global game_on
    
    game_on = True
    
    while game_on == True:
        console_derby(welcome_user(0))
    

