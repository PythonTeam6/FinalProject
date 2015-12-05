import sqlite3


class DBControl:
    def __getDB(self):
        return sqlite3.connect("test.db")

    def init_DB(self):
        self.db = __getDB()
        self.cur = self.db.cursor()
        self.cur.execute('drop table if exists music;')
        self.cur.execute('create table music(artist string not null);')
        self.db.commit()
        self.db.close()

    def insertDataList(self, dataList):
        self.db = __getDB()
        self.cur = self.db.cursor()
        for self.item in dataList:
            print(self.item)
            self.cur.execute('insert into music(artist) values(?);', [self.item])
        self.db.commit()
        self.db.close()

    def getDataList(self):
        self.db = self.__getDB()
        self.cur = self.db.cursor()
        self.list = self.cur.execute('select * from music')
        self.reList = self.list.fetchall()
        self.db.close()
        return self.reList

    def findArtist(self, name):
        self.db = self.__getDB()
        self.cur = self.db.cursor()
        self.cur.execute('select * from music where artist = ?', [name])
        self.db.close()