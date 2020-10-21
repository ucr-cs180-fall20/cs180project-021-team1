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


# sample player
sc = SoccerPlayer(207650,"Emil Krafth", "Sweden", "RB", 73, 25, 1, 77, "Newcastle United")
# print(sc)

print("Reading in file\n")
csvPath = '../../FIFA-21Complete.csv'

def readCsv(path):
    DB = open(csvPath, 'r', encoding='utf8')
    myList = DB.readlines()
    return myList

playerList = readCsv(csvPath)

for line in playerList:
    print(line)