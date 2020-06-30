# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 09:54:56 2020

@author: Marcin Lubszczyk

"""
class komfovent:
    import requests
    from bs4 import BeautifulSoup
    
    def __init__(self, ipAddress, password='user'):        
        self.ipAddress = 'http://'+ ipAddress
        self.password = password
        self.tempInlet = 0
        self.tempOutlet = 0
        self.tempIndoor = 0
        self.tempOutdoor = 0
        self.humidity = 0
        self.flowOutLoad = 0
        self.flowInLoad = 0
        self.filterStatus = 0
        self.powerConsumption = 0
        self.RAWWebData = ''
        self.connect()
        self.update()
        self.status()
        
       
        
        
        
    
    def connect(self):
        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Content-Length': '19',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': self.ipAddress,
            'Origin': self.ipAddress,
            'Referer': self.ipAddress,
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'
    
        }
        self.login_data = {
                '1': 'user',
                '2': self.password,
        }
        with self.requests.Session() as s:
            self.RAWWebData = s.post(self.ipAddress, data = self.login_data, headers=self.headers)
            #print(self.RAWWebData.content)
        
        
    def update(self):
        content = self.requests.get(self.ipAddress)
        soup = self.BeautifulSoup(content.text, features="lxml")
        self.temp = self.BeautifulSoup(str(soup.select('#ai0')),features="lxml").span.text   
        self.tempInlet = self.BeautifulSoup(str(soup.select('#ai0')),features="lxml").span.text
        self.tempIndoor = self.BeautifulSoup(str(soup.select('#ai1')),features="lxml").span.text
        self.tempOutdoor = self.BeautifulSoup(str(soup.select('#ai2')),features="lxml").span.text
        self.flowOutLoad = self.BeautifulSoup(str(soup.select('#eaf')),features="lxml").span.text
        self.flowInLoad = self.BeautifulSoup(str(soup.select('#saf')),features="lxml").span.text
        self.filterStatus = self.BeautifulSoup(str(soup.select('#fcg')),features="lxml").span.text
        self.powerConsumption = self.BeautifulSoup(str(soup.select('#ec3')),features="lxml").span.text
        
        content = self.requests.get(self.ipAddress+'/det.html')
        soup = self.BeautifulSoup(content.text, features="lxml")
        self.tempOutlet = self.BeautifulSoup(str(soup.select('#v_et')),features="lxml").td.text
        self.humidity = self.BeautifulSoup(str(soup.select('#v_ph1')),features="lxml").td.text
       
    def status(self):
        print('Panel Temperature: '+self.tempIndoor)
        print('Inlet Air Temperature: '+self.tempInlet)
        print('Outlet Air Temperature: '+self.tempOutlet)
        print('Panel Humidity: '+self.humidity)
        print('Filter Dirty: '+self.filterStatus)
        print('In Fan Speed: '+self.flowInLoad)
        print('Out Fan Speed: '+self.flowOutLoad)
        
        pass
        

