# basic imports
import pandas as pd
import random
from mysite.fifa.soccerPlayer import SoccerPlayer

class database:

    def __init__(self):
        self.fifacsvPath = '../FIFA-21Complete.csv'
        self.fifatxtPath = 'fifaCS180.txt'
        self.playerList = []
        self.resetDB()


    def setPlayerList(self, cleanList: list):
        for player in cleanList:
            tempPlayer = SoccerPlayer(player[0],player[1],player[2],player[3],player[4],
                                      player[5],player[6],player[7],player[8])
            self.playerList.append(tempPlayer)


    def resetDB(self):
        csvFile = open(self.fifacsvPath, "r", encoding='utf-8')
        txtFile = open(self.fifatxtPath, "w+", encoding='utf-8')
        cleanList = self.cleanCsv(csvFile.readlines())
        self.setPlayerList(cleanList)
        self.updateDB()
        csvFile.close()
        txtFile.close()

    def updateDB(self):
        txtFile = open(self.fifatxtPath, "w", encoding='utf-8')
        for player in self.playerList:
            txtFile.write(player.toCsvString())

        txtFile.close()

    def cleanCsv(self, rawList: list):
        dataList = []
        for line in rawList:
            elems = line.split(sep=';')
            elems[8] = self.cleanCsvTeam(elems[8])
            dataList.append(elems)
        dataList.pop(0) # remove 1st line of csv file
        return dataList

    def cleanCsvTeam(self, teamString: str):
        return teamString[1:-2].strip()

    def searchEntry(self):
        print("Not implemented")

    def addEntry(self, player_id, name, nationality, position, overall, age, hits, potential, team):
        tempPlayer = SoccerPlayer(player_id, name, nationality, position, overall, age, hits, potential, team)
        self.playerList.append(tempPlayer)

        self.updateDB()

    def modifyEntry(self, player_id, name, nationality, position, overall, age, hits, potential, team):
        tempPlayer = SoccerPlayer(player_id, name, nationality, position, overall, age, hits, potential, team)

        for i in range(len(self.playerList)):
            if player_id == self.playerList[i].player_id:
                print(f"\nChanging player: {self.playerList[i]}\n")
                self.playerList[i] = tempPlayer
                print(f"\nModified player is: {self.playerList[i]}\n")
                break

        self.updateDB()

    def deleteEntry(self, entered_id: str):
        for player in self.playerList:
            if entered_id == player.player_id:
                self.playerList.remove(player)
                print(f"Removed player: {player}")
                break
        self.updateDB()


print("\n\nInitialize db")
db = database()
print("\n")

# for player in db.playerList:
#     print(player)
# print("\nAdding new entry\n")
# rand_id = str(random.randrange(300000,400000))
# db.addEntry(rand_id,"eveveveveveve","USA","CDeezNuts","12","22","1","99","Patriots")
# db.addEntry(rand_id,"jay leno","Korea","CB","122","212","551","9","lmao")

# db.deleteEntry('158023') # kill messi
# db.deleteEntry('200389') # kill Jan Oblak
db.modifyEntry("20801","eveveveveveve","USA","CDeezNuts","12","22","1","99","Patriots")
db.modifyEntry("190871","jay leno","Korea","CB","122","212","551","9","lmao")

for player in db.playerList[:5]:
    print(player)