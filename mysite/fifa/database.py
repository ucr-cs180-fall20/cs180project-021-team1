# basic imports
from os import path
import random

from fifa.soccerPlayer import SoccerPlayer
class database:

    def __init__(self,reset=False):
        self.fifacsvPath = '../FIFA-21Complete.csv'
        self.fifatxtPath = 'fifaCS180.txt'
        self.playerList = []
        if(reset):
            self.resetDB()
        else:
            self.setTextFile()


    def setPlayerList(self, cleanList: list):
        for player in cleanList:
            tempPlayer = SoccerPlayer(player[0],player[1],player[2],player[3],player[4],
                                      player[5],player[6],player[7],player[8])
            self.playerList.append(tempPlayer)

    def setTextFile(self):
        if not path.exists(self.fifatxtPath):
            self.resetDB()
            return
        txtFile = open(self.fifatxtPath, "r", encoding='utf-8')
        cleanList = self.cleanTxt(txtFile.readlines())
        self.setPlayerList(cleanList)
        self.updateDB()
        txtFile.close()


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

    def cleanTxt(self, rawList: list):
        dataList = []
        for line in rawList:
            if line=='\n':
                continue
            elems = line.split(sep=';')
            dataList.append(elems)
        return dataList


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

    def searchEntry(self, attrType:str, searchStr:str):
        #print(f'\n\nRecieved search type: {attrType} and searched for {searchStr}\n\n')

        if searchStr== '':
            raise NotImplemented("ERROR: Passed in empty string to searchEntry()")
        elif searchStr[0] == ' ' or searchStr[-1:] == ' ':
            raise NotImplemented("ERROR: Too much whitespace passed to searchEntry()")
        resultList = []
        if attrType == 'player_name':
            for player in self.playerList:
                if searchStr.lower() in player.name.lower():
                    resultList.append(player)
                    print(f"Adding {player.name} to list")

        elif attrType == 'age':
            for player in self.playerList:
                if searchStr.lower() in player.age.lower():
                    resultList.append(player)
                    # print(f"Adding {player.name} to list")
        elif attrType == 'nationality':
            for player in self.playerList:
                if searchStr.lower() in player.nationality.lower():
                    resultList.append(player)
                    # print(f"Adding {player.name} to list")
        elif attrType == 'club':
            for player in self.playerList:
                if searchStr.lower() in player.team.lower():
                    resultList.append(player)
                    # print(f"Adding {player.name} to list")
        elif attrType == 'rating':
            for player in self.playerList:
                if searchStr.lower() in player.overall.lower():
                    resultList.append(player)
                    # print(f"Adding {player.name} to list")
        elif attrType == 'position':
            for player in self.playerList:
                if searchStr.lower() in player.position.lower():
                    resultList.append(player)
                    # print(f"Adding {player.name} to list")
        elif attrType == 'potential':
            for player in self.playerList:
                if searchStr.lower() in player.potential.lower():
                    resultList.append(player)
                    # print(f"Adding {player.name} to list")
        elif attrType == 'player_id':
            for player in self.playerList:
                if searchStr.lower() in player.player_id.lower():
                    resultList.append(player)
                    return resultList
                    # print(f"Adding {player.name} to list")
        else:
            print("\n\nERROR: ATTRIBUTE NOT FOUND")
            raise ValueError("ERROR: ATTRIBUTE NOT FOUND")


        if len(resultList)==0:
            print("No search results!")
            print("Returning empty list...")

        for num in resultList:
            print(num)
        return resultList



# print("\n\nInitialize db")
# db = database()
# print("\n")

# for player in db.playerList:
#     print(player)
# print("\nAdding new entry\n")
# rand_id = str(random.randrange(300000,400000))
# db.addEntry(rand_id,"eveveveveveve","USA","CDeezNuts","12","22","1","99","Patriots")
# db.addEntry(rand_id,"jay leno","Korea","CB","122","212","551","9","lmao")

# db.deleteEntry('158023') # kill messi
# db.deleteEntry('200389') # kill Jan Oblak
# db.modifyEntry("20801","eveveveveveve","USA","CDeezNuts","12","22","1","99","Patriots")
# db.modifyEntry("190871","jay leno","Korea","CB","122","212","551","9","lmao")
#
# for player in db.playerList[:5]:
#     print(player)

# myList = db.searchEntry('age','22')
#
# for player in myList:
#     print(player)
