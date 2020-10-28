# basic imports
import pandas as pd


class database:

    def __init__(self):
        self.fifacsvPath = '../../FIFA-21Complete.csv'
        self.fifatxtPath = 'fifaCS180.txt'
        self.df = ''
        self.resetDB()

    def setDataFrame(self, dataList: str):
        df = pd.DataFrame(dataList, columns=['player_id', 'name', 'nationality', 'position',
                                            'overall', 'age', 'hits', 'potential', 'team'])
        return df

    def resetDB(self):
        f1 = open(self.fifacsvPath, "r", encoding='utf-8')
        f2 = open(self.fifatxtPath, "w+", encoding='utf-8') #"""here """
        cleanList = self.cleanCsv(f1)
        self.df = self.setDataFrame(cleanList)

        #for line in f1: """here """
        #    f2.write(line)
        #print(self.df)
        csvString = self.df.to_csv(sep=';')
        f2.write(csvString)
        #print(csvString)
        f1.close()
        f2.close()

    def updateDB(self):
        f = open(self.fifatxtPath, "a", encoding='utf-8')
        print("Not implemented")

    def cleanCsv(self, rawList: list):
        dataList = []
        for line in rawList:
            elems = line.split(sep=';')
            elems[8] = self.cleanCsvTeam(elems[8])
            dataList.append(elems)
        return dataList

    def cleanCsvTeam(self, teamString: str):
        #"""remove quotations from team name string """
        #print(f"Received: {teamString} \nreturning: ->{teamString[1:-2].strip()}<-")
        return teamString[1:-2].strip()

    def searchEntry(self):
        print("Not implemented")

    def addEntry(self, ):
        f = open(self.fifatxtPath, "a+", encoding='utf-8')
        newEntry = player_id + ';' + name + ';' + nationality + ';' + position + ';' + overall + ';' + age + ';' + hits + ';' + potential + ';' + team + ' \n'
        f.write(newEntry)
        f.close()

    def modifyEntry(self):
        print("Not implemented")

    def deleteEntry(self):
        print("Not implemented")


# database testing
db = database()

teamStr = "\"FC Barcelona \""
print(f"team is {teamStr}")


#db.addEntry("158023", "Lionel Messi", "Argentina", "ST|CF|RW", "94", "33", "299", "94", "FC Barcelona")

db.cleanCsvTeam(teamStr)


