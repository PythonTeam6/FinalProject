import sqlite3


class DBControl:
    def __init__(self):
        self.db = self.__getDB()

    def __del__(self):
        self.db.close()

    def __getDB(self):
        return sqlite3.connect("test.db")

    def init_DB(self):
        self.cur = self.db.cursor()
        self.cur.execute('drop table if exists music;')
        self.cur.execute('create table music(artist string not null);')
        self.db.commit()

    def insertDataList(self, dataList):
        self.cur = self.db.cursor()
        for self.item in dataList:
            print(self.item)
            self.cur.execute('insert into music(artist) values(?);', [self.item])
        self.db.commit()

    def getDataList(self):
        self.cur = self.db.cursor()
        self.list = self.cur.execute('select * from music')
        self.reList = self.list.fetchall()
        return self.reList

    def findArtist(self, name):
        self.cur = self.db.cursor()
        self.cur.execute('select * from music where artist = ?', [name])