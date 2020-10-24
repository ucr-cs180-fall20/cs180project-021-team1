import pandas as pd


class SoccerPlayer:
    def __init__(self, player_id, name, nationality, position,
                 overall, age, hits, potential, team):
        self.player_id = player_id
        self.name = name
        self.nationality = nationality
        self.position = position
        self.overall = overall
        self.age = age
        self.hits = hits
        self.potential = potential
        self.team = team

    def __str__(self) -> str:
        return f"id: {self.player_id}, " \
               f"Name: {self.name}, " \
               f"Nationality: {self.nationality}, " \
               f"position: {self.position}, " \
               f"overall: {self.overall}, " \
               f"age: {self.age}, " \
               f"hits: {self.hits}, " \
               f"potential: {self.potential}, " \
               f"team: {self.team}"


csvPath = r'../FIFA-21Complete.csv'

def readCsv(path):
    DB = open(path, 'r', encoding='utf8')
    myList = DB.readlines()
    return myList

playerList = readCsv(csvPath)
players = []
twoDList = []
for line in playerList:
    elems = line.split(sep=';') # "\"FC Barcelona \"\\n"
    twoDList.append(elems)
    tmpPlayer = SoccerPlayer(elems[0],elems[1],elems[2],elems[3],elems[4],elems[5],elems[6], elems[7], elems[8])
    players.append(tmpPlayer)


df = pd.DataFrame(twoDList, columns=['player_id', 'name', 'nationality', 'position',
                                    'overall', 'age', 'hits', 'potential', 'team'])
#print(df[df['name'] == 'Lionel Messi'])


def searchPlayerName(playerName,dataFrame):
    dataFrame=dataFrame[dataFrame['name'] == playerName]
    print(dataFrame)
    return dataFrame

searchPlayerName('Lionel Messi',df)

print(df)