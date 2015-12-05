from bs4 import BeautifulSoup
from urllib.request import urlopen
from tkinter import *


class DataParser:
    def parse_MusicBrain(self):
        self.url = 'http://musicbrainz.org/area/b9f7d640-46e8-313e-b158-ded6d18593b3/artists?page=1'
        self.l = []
        self.data = urlopen(self.url)
        self.soup = BeautifulSoup(self.data.read(), from_encoding = 'utf-8')
    
        for self.link in self.soup('a'):
            if 'href' in dict(self.link.attrs):
                if self.link['href'].find('page=') != -1:
                    self.url, self.t = self.link['href'].split('page=')
                    self.l.append(self.t)
    
        self.page = max(self.l)
        self.l = []
    
        for self.i in range(int(self.page)):
            self.urli = self.url+'page='+str(self.i+1)
            self.data = urlopen(self.urli)
            self.soup = BeautifulSoup(self.data.read(), from_encoding = 'utf-8')
        
            print(self.i+1, '번째 페이지 파싱중')
            for self.link in self.soup('a'):
                if 'href' in dict(self.link.attrs):
                    if 'title' in dict(self.link.attrs):
                        if 'class' not in dict(self.link.attrs):
                            try:
                                print(self.link['title'])
                                self.l.append(self.link['title'])
                            except:
                                print('unicode Exception')  # ô
                                pass
        return self.l