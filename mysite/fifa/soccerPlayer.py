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

    def toCsvString(self):
        return f"{self.player_id};{self.name};{self.nationality};{self.position};" \
               f"{self.overall};{self.age};{self.hits};{self.potential};{self.team}\n"

    def toArray(self):
        player = []
        player.append(self.player_id)
        player.append(self.name)
        player.append(self.nationality)
        player.append(self.position)
        player.append(self.overall)
        player.append(self.age)
        player.append(self.hits)
        player.append(self.potential)
        player.append(self.team)

        return player

class SoccerTeam:

    def __init__(self, teamname:str, numplayers:int, ratingaverage:float):
        self.teamname = teamname
        self.numplayers = numplayers
        self.ratingaverage = ratingaverage

    def __str__(self) -> str:
        return f"teamname: {self.teamname}, " \
               f"numplayers: {self.numplayers}, " \
               f"ratingaverage: {self.ratingaverage}"


class Map:

    def __init__(self, playername:str, playernationality:str, xcoord:float, ycoord:float):
        self.playername = playername
        self.playernationality = playernationality
        self.xcoord = xcoord
        self.ycoord = ycoord

    def __str__(self) -> str:
        return f"playername: {self.playername}, " \
               f"playernationality: {self.playernationality}," \
               f"xcoord: {self.xcoord}," \
               f"ycoord: {self.ycoord}"


# instead of http response, have a render and pass 2-d list of all filtered results
# modify get search back, and get attributes back

class Nation:

    def __init__(self, nationname:str, numplayers:int):
        self.nationname = nationname
        self.numplayers = numplayers


    def __str__(self) -> str:
        return f"Nationality: {self.nationname}, " \
               f"numplayers: {self.numplayers}, "

