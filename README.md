# indian-news-analysis-app

# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 12:57:58 2019

@author: Shahid iqbal
"""
import time
import os
import requests
from bs4 import BeautifulSoup

channel_name='www.ndtv.com'
categories=['india-news','business','education','science',
            'entertainment','opinion','world-news']
"""categories=['cricket','football','formula-1','kabaddi',
            'tennis','golf','chess','badminton','boxing',
            'athletics','swimming','shooting','wrestling']"""
categories_files=os.listdir()
t1=time.perf_counter()
for category in categories:
    filename=category+'.txt'
    if filename in categories_files:
        mode='a'
    else:
        mode='w'
        
    if mode=='a':
        with open(filename,'r') as titles:
            title_list=[]
            for title in titles:
                title_,_=title.split('\n')
                if title_ not in title_list:
                    title_list.append(title_)
                    
    with open(filename,mode) as f:
        url='https://'+channel_name+'/'+category
        counter=1
        status=True
        resp_url=''
        while status and resp_url!='https://'+channel_name+'/':
            resp=requests.get(url)
            soup=BeautifulSoup(resp.text,'html.parser')
            links=[]
            for link in soup.find_all('a',href=True):
                temp_link=link['href']
                if channel_name in temp_link \
                    and '/'+category in temp_link \
                    and '/video' not in temp_link \
                    and '/photos' not in temp_link:
                        if '?' in temp_link:
                            link,_=temp_link.split('?')
                        else:
                            link=temp_link
                        title=link.split('/')[-1]
                        title_list=title.split('-')
                        if len(title_list)>3:
                            if link not in links:
                                if mode=='a':
                                    if link not in title_list:
                                        f.write(link)
                                        f.write('\n')
                                else:
                                    f.write(link)
                                    f.write('\n')
                                links.append(link)
            url='https://'+channel_name+'/'+category+'/'+'page-'+str(counter)
            counter+=1
            status=resp.ok
            resp_url=resp.url
        print(f'All links from {category} category extracted')
