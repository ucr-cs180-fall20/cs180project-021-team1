from os import path
from geopy.geocoders import Nominatim
import pycountry
import flag
import time
import random
import unittest
from fifa.soccerPlayer import SoccerPlayer, SoccerTeam,Map,Nation


class database:
    # playerList type hint (helps autocomplete)

    def __init__(self,reset=True):
        self.fifacsvPath = '../FIFA-21Complete.csv'
        self.fifatxtPath = 'fifaCS180.txt'
        self.playerList = []
        self.team_dict = {}
        self.team_list = []
        self.nation_dict={}
        self.location_dict={}
        self.icon_dict = self.setIconDict()

        # whenever new players are added they go here
        self.teamAverageUpdateList = []
        self.topRatedUpdateList = []
        self.lowestRatedUpdateList = []

        # values set to false when new players are added,
        # values set to true after analytic recalculations finish
        self.teamAverageUpToDate = False
        self.topRatedUpToDate = False
        self.lowestRatedUpToDate = False

        if(reset):
            self.resetDB()
        else:
            self.setTextFile()

    def setflagsfalse(self):
        print("Setting update flags to False\n")
        self.teamAverageUpToDate = False
        self.topRatedUpToDate = False
        self.lowestRatedUpToDate = False

    def addToUpdateLists(self,newplayer:SoccerPlayer):
        print(f"Adding {newplayer.name} to update lists..\n")
        self.teamAverageUpdateList.append(newplayer)
        self.topRatedUpdateList.append(newplayer)
        self.lowestRatedUpdateList.append(newplayer)

    # dictionary with key-pair <'country_name','icon'>
    def setIconDict(self):
        dict1 = {}
        for country in pycountry.countries:
            dict1[country.name] = flag.flag(country.alpha_2)
        return dict1

    def setPlayerList(self, cleanList: list):
        for player in cleanList:
            tempPlayer = SoccerPlayer(player[0],player[1],player[2],player[3],player[4],
                                      player[5],player[6],player[7],player[8], icon=self.getIcon(player[2]))
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
            elems[8] = elems[8].strip()
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

        txtfile = open(self.fifatxtPath, "a", encoding='utf-8')
        txtfile.writelines([tempPlayer.toCsvString()])
        txtfile.close()
        self.setflagsfalse()
        self.addToUpdateLists(tempPlayer)

    def modifyEntry(self, player_id, name, nationality, position, overall, age, hits, potential, team):
        tempPlayer = SoccerPlayer(player_id, name, nationality, position, overall, age, hits, potential, team)

        for i in range(len(self.playerList)):
            if player_id == self.playerList[i].player_id:
                self.playerList[i] = tempPlayer
                break

        self.updateDB()

    def deleteEntry(self, entered_id: str):
        for player in self.playerList:
            if entered_id == player.player_id:
                self.playerList.remove(player)
                break
        self.updateDB()

    def getIcon(self, nationality:str):
        return self.icon_dict.get(nationality,'⚽')

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
                    #print(f"Adding {player.name} to list")

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

        # for num in resultList:
        #     print(num)
        return resultList

    def mostCommonAge(self):
        age_counter = {}
        age_list = []
        for player in self.playerList:
            if player.age.lower() in age_counter:
                age_counter[player.age.lower()] += 1
            else:
                age_counter[player.age.lower()] = 1

        popular_age = sorted(age_counter, key = age_counter.get, reverse = True)
        top_3 = popular_age[:3]
        for i in top_3:
            #age_list.append(self.searchEntry('age', i))
            return (self.searchEntry('age', i))

    def topAndLowestRated(self, limit=100, top=True):
        return sorted(self.playerList, key=lambda x:x.overall, reverse=top)[:limit]

    def bestHits(self, limit=10, top=True):
        data= sorted(self.playerList, key=lambda x:int(x.hits), reverse=top)[:limit]
        return data

    def setTeamDict(self):
        dict1 = {}
        if bool(self.team_dict):
            dict1 = self.team_dict
        else:
            for player in self.playerList:
                if not player.team in dict1:
                    dict1[player.team] = [player]
                else:
                    dict1[player.team].append(player)
            self.team_dict = dict1

    def setNationDict(self):
        dict2 = {}
        if bool(self.nation_dict):
            dict2 = self.nation_dict
        else:
            for player in self.playerList:
                if not player.nationality in dict2:
                    dict2[player.nationality] = [player]
                else:
                    dict2[player.nationality].append(player)
            self.nation_dict = dict2

    def teamAverageRating(self, limit=10):
        self.setTeamDict()

        if not bool(self.team_list):
            for key in self.team_dict:
                team_name = key
                num_players = len(self.team_dict[key])
                rating_total = 0
                for player in self.team_dict[key]:
                    rating_total += int(player.overall)
                avg = rating_total / num_players
                self.team_list.append(SoccerTeam(team_name, num_players, round(avg, 2)))
            self.teamAverageUpToDate = True
        elif not self.teamAverageUpToDate:
            # factor in all newly added players
            toupdate = []
            print("\nAdding players from update list: ")
            for player in self.teamAverageUpdateList:
                print(f"player: {player.name} from team: {player.team}")
                if player.team in self.team_dict:
                    print(f"Appending {player.name} to team_dict")
                    self.team_dict[player.team].append(player)
                else:
                    print(f"Adding player: {player.name}'s team: {player.team} to team_dict")
                    self.team_dict[player.team] = [player]
                    newTeam = SoccerTeam(player.team,1,round(int(player.overall),2))
                    print(f"Adding {player.team} to team_list")
                    self.team_list.append(newTeam)
                toupdate.append(player.team)
            for i, team in enumerate(self.team_list):
                if team.teamname in toupdate:
                    print(f"\nFound {team.teamname} in toupdate")
                    num_players = len(self.team_dict[team.teamname])
                    rating_total = 0
                    for playr in self.team_dict[team.teamname]:
                        rating_total+= int(playr.overall)
                    avg = rating_total / num_players
                    # print(f"Reassigning the following team: {team}")
                    team.numplayers = len(self.team_dict[team.teamname])
                    team.ratingaverage = round(avg,2)

            # flip uptodate bool
            # empty update list
            print("Setting update flag to True")
            self.teamAverageUpToDate = True
            self.teamAverageUpdateList = []
            print('Finished recalculating teams')
        return sorted(self.team_list, key=lambda team: team.ratingaverage, reverse=True)[:limit]

    def coordOffset(self,coord:tuple):
        x = coord[0]
        y = coord[1]
        xoffset = random.uniform(-1, 1)
        yoffset = random.uniform(-1, 1)

        return (x+xoffset, y+yoffset)

    def jsonData(self, limit=100):
        jsonList = []
        locator = Nominatim(user_agent="myGeocoder")
        for player in self.playerList[:limit]:
            if player.nationality not in self.location_dict:
                location = locator.geocode(player.nationality)
                x = 69.6969 if (location is None) else location.longitude
                y = 69.6969 if (location is None) else location.latitude
                self.location_dict.update({player.nationality: (x, y)})
            x, y = self.coordOffset(self.location_dict[player.nationality])
            tempMap = Map(player.name, player.nationality, x, y)
            jsonList.append(tempMap)
        return jsonList

    def testGeo(self):
        locator = Nominatim(user_agent="myGeocoder")
        for player in self.playerList:
            location = locator.geocode(player.nationality)
            #location = locator.geocode("South Korea")
            print("player nationality: \n", player.nationality)
            print("Latitude = {}, Longitude = {}".format(location.latitude, location.longitude))

    def setNationDict(self):
        dict2 = {}
        if bool(self.nation_dict):
            dict2 = self.nation_dict
        else:
            for player in self.playerList:
                if not player.nationality in dict2:
                    dict2[player.nationality] = [player]
                else:
                    dict2[player.nationality].append(player)
            self.nation_dict = dict2

    def PopularNation(self, limit=10, top=True):

        self.setNationDict()
        nation = []
        for player in self.nation_dict:
            nationname=player
            num_players = len(self.nation_dict[player])
            nation.append(Nation(nationname,num_players))
        return sorted(nation, key=lambda x:x.numplayers, reverse=top)[:limit]

        # for player in self.playerList:
        #     player_nationality=player.nationality
        #     num_players = len(self.team_dict[player])
        #
        #     if player_nationality not in unique:
        #         unique.append(player_nationality)
        #
        # for player in unique:
        #     temp=player
        #     nation.append(Nation(temp))
        #
        # return nation




db = database(reset=False)

#for player in db.playerList:
#    print(player.icon)

# for item in db.jsonData():
#     print(item)
#     print()
# for player in db.playerList:
#     print(player.team)
#
# teamList = db.teamAverageRating()
#
# for team in teamList:
#     print(team)

# for team in db.teamAverageRating():
#     if len(team) > 2:
#         print(team)



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

#print("here it is: ", db.mostCommonAge())
#db.mostCommonAge()
# print("\n\n\n")
# print("BEST AND WORST: ")
# #db.topAndLowestRated(True)
#
#
# for player in db.mostCommonAge():
#     print("HELOOOOOOO")
#     print(player)
#     print("HELOOOOOOO")
# for player in db.topAndLowestRated():
#     print(player)

# print("BEST GOALAZOL")
# for player in db.Map():
#     print(player)


# t0 = time.time()
# print(f"t0 is {t0}")
# print("Running db update")
# db.updateDB()
# t1 = time.time()
# print(f"t1 is {t1}")
# print(f"elapsed time is: {t1-t0}")

# mylist=db.PopularNation()
#
# for player in mylist:
#     print(player.nationname)
