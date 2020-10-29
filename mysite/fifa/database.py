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
        f2 = open(self.fifatxtPath, "w+", encoding='utf-8')
        cleanList = self.cleanCsv(f1)
        self.df = self.setDataFrame(cleanList)

        csvString = self.df.to_csv(sep=';')
        f2.write(csvString)
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
        return teamString[1:-2].strip()

    def searchEntry(self):
        print("Not implemented")

    def addEntry(self, player_id, name, nationality, position, overall, age, hits, potential, team):
        newEntry = [player_id, name, nationality, position, overall, age, hits, potential, team]
        self.df.index = self.df.index + 1
        self.df.loc[len(self.df) + 1] = newEntry
        self.df = self.df.sort_index()
        self.updateDB()

    def modifyEntry(self, player_id, name, nationality, position, overall, age, hits, potential, team):
        myIndex = self.df[self.df['player_id'] == player_id].index

        self.df.at[myIndex, 'name'] = name
        self.df.at[myIndex, 'nationality'] = nationality
        self.df.at[myIndex, 'position'] = position
        self.df.at[myIndex, 'overall'] = overall
        self.df.at[myIndex, 'age'] = age
        self.df.at[myIndex, 'hits'] = hits
        self.df.at[myIndex, 'potential'] = potential

        self.updateDB()

    def deleteEntry(self, entered_id: str):
        id_column = 'player_id'
        self.df = self.df.drop(index=self.df[self.df[id_column] == entered_id].index)
        self.updateDB()


# database testing
db = database()

# db.modifyEntry("190871","Neymar Sr","xd","pos|ition","420","35","69","9999","SD Chargers")
db.resetDB()
