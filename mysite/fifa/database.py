# basic imports
import pandas as pd


class database:

    def __init__(self):
        self.fifacsvPath = '../../FIFA-21Complete.csv'
        self.fifatxtPath = 'fifaCS180.txt'
        self.df = pd.DataFrame()
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
        f = open(self.fifatxtPath, "w", encoding='utf-8')
        f.write(self.df.to_csv(sep=';'))
        f.close()

    def cleanCsv(self, rawList: list):
        dataList = []
        for line in rawList:
            elems = line.split(sep=';')
            elems[8] = self.cleanCsvTeam(elems[8])
            dataList.append(elems)
        dataList.pop(0)
        return dataList

    def cleanCsvTeam(self, teamString: str):
        #"""remove quotations from team name string """
        #print(f"Received: {teamString} \nreturning: ->{teamString[1:-2].strip()}<-")
        return teamString[1:-2].strip()

    def searchEntry(self):
        print("Not implemented")

    def addEntry(self, player_id, name, nationality, position, overall, age, hits, potential, team):
        newEntry = [player_id, name, nationality, position, overall, age, hits, potential, team]
        self.df.index = self.df.index + 1
        self.df.loc[len(self.df) + 1] = newEntry
        self.df = self.df.sort_index()
        # tempDf = pd.DataFrame(newEntry, columns=['player_id', 'name', 'nationality', 'position','overall', 'age', 'hits', 'potential', 'team'])
        # print(newEntry)
        # print('\n\n\n')
        # print(self.df.index)
        # print('\n\n\n')
        # print(tempDf)
        # print('\n\n\n')
        # self.df.append(tempDf, ignore_index=True)
        # print(self.df)
        # print('\n\n\n')
        self.updateDB()

    def modifyEntry(self, player_id, name, nationality, position, overall, age, hits, potential, team):
        
        print("Not implemented")

    def deleteEntry(self, entered_id: str):
        id_column = 'player_id'
        self.df = self.df.drop(index=self.df[self.df[id_column] == entered_id].index)
        self.updateDB()


# database testing
db = database()

db.deleteEntry("190871")



#teamStr = "\"FC Barcelona \""
#print(f"team is {teamStr}")
#db.addEntry()

# db.addEntry("158023", "NEWGUY", "NEVERLAND", "ST|CF|RW", "94", "33", "299", "94", "FC Barcelona")

#db.cleanCsvTeam(teamStr)


