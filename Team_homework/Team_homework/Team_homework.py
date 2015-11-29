#-*- coding: utf-8 -*-
import sqlite3
from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import *


def dataParse(url):
    l = []
    data = urlopen(url)
    soup = BeautifulSoup(data.read(), from_encoding = 'utf-8')
    
    for link in soup('a'):
        if 'href' in dict(link.attrs):
            if link['href'].find('page=') != -1:
                url, t = link['href'].split('page=')
                l.append(t)
    
    page = max(l)
    l = []
    
    for i in range(int(page)):
        urli = url+'page='+str(i+1)
        data = urlopen(urli)
        soup = BeautifulSoup(data.read(), from_encoding = 'utf-8')
        
        print(i+1, '번째 페이지 파싱중')
        for link in soup('a'):
            if 'href' in dict(link.attrs):
                if 'title' in dict(link.attrs):
                    if 'class' not in dict(link.attrs):
                        try:
                            print(link['title'])
                            l.append(link['title'])
                        except:
                            print('unicode Exception')  # ô
                            pass

    insertData(l)

def getDB():
    return sqlite3.connect("test.db")

def init_DB():
    db = getDB()
    cur = db.cursor()
    cur.execute('drop table if exists music;')
    cur.execute('create table music(artist string not null);')
    db.commit()

def insertData(dataList):
    db = getDB()
    cur = db.cursor()
    for item in dataList:
        print(item)
        cur.execute('insert into music(artist) values(?);', [item])
    db.commit()
    db.close()

#init_DB()
#dataParse('http://musicbrainz.org/area/b9f7d640-46e8-313e-b158-ded6d18593b3/artists?page=1')

db = getDB()
cur = db.cursor()
print("****한국 가수이름 데이터베이스입니다.****")
print()
while(1):
    print("찾고자 하는 가수 이름을 입력해 주세요 : " )
    print(" -> " , end = '')
    name = input()
    l = cur.execute('select * from music where artist = ?', [name])
    answer = l.fetchone()
    
    if answer != None:
        print("{0:s}가 데이터베이스에 있습니다.".format(name))
        print()
        #print(answer[0])
    else :
        print("{0:s}가 데이터베이스에 없습니다.".format(name))
        print()
    #print(l.fetchall())