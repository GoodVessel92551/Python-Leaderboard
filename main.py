from replit import db
import random
import time
def database():
    choice = input("Do set or get >>> ").lower()
    if choice == "set":
        try:
            getnum = db.prefix("leaderboard")
            int(getnum[-1][-1])
        except:
            getnum = -1
        else:
            getnum = db.prefix("leaderboard")
            getnum = int(getnum[-1][-1])
        name = input("Input you name >>> ").title()
        num =  random.randint(100,10000)
        print("You have "+str(num)+" points")
        value = str(num)+"#"+name
        db["leaderboard"+str(getnum+1)] = value
        database()
    elif choice == "del":
        delit()
    else:
        matches = db.prefix("leaderboard")
        leaderboard = []
        for i in range(len(matches)):
            value = db[matches[i]]
            leaderboard.append(value)
        leaderboard.sort(reverse=True)

        def printlead():
            print("Position".ljust(20) + "Username".center(20) + "Points".rjust(20))
            for i in range(len(leaderboard)):
                for j in range(len(leaderboard[i])):
                    letter = leaderboard[i][j]
                    if letter == "#":
                        points = leaderboard[i][0:j]
                        username = leaderboard[i][j+1:]
                        position = str(i+1)
                print(position.ljust(20) + username.center(20) + points.rjust(20))
                time.sleep(0.5)
        printlead()
        database()

def delit():
    keys = db.prefix("lead")
    print(keys)
    for i in range(len(keys)):
        del db[keys[i]]
    print(db.keys())


database()
