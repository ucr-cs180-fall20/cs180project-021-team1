# basic imports
import pandas as pd


class database:

    def __init__(self):
        self.fifacsvPath = '../../FIFA-21Complete.csv'
        self.fifatxtPath = 'fifaCS180.txt'

    def resetDB(self):
        # f = open(self.fifacsvPath, 'r', encoding='utf-8')
        print("Not implemented")

    def updateDB(self):
        print("Not implemented")

    def cleanCsv(self, rawList: list):
        # for line in list:
        #     elems = line.split(sep=';')
        print("Not implemented")

    def cleanCsvTeam(self, teamString: str):
        """remove quotations from team name string """
        # print(f"Received: {teamString} \nreturning: ->{teamString[1:-2]}<-")
        return teamString[1:-2]

    def searchEntry(self):
        print("Not implemented")

    def addEntry(self):
        print("Not implemented")

    def modifyEntry(self):
        print("Not implemented")

    def deleteEntry(self):
        print("Not implemented")


# database testing
db = database()

teamStr = "\"FC Barcelona \""
print(f"team is {teamStr}")

db.cleanCsvTeam(teamStr)
