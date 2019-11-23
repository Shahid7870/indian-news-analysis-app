# -*- coding: utf-8 -*-

import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image
st.sidebar.title('Indian News Analysis App')
categories=['india-news','business','education','science',
            'entertainment','opinion','world-news']

def FetchTitle(soup):
    body_text=soup.find(class_='ins_headline')
    text_1=body_text.find_all('h1')
    text_2=text_1[0].find_all('span')
    title=text_2[0].contents[0]
    return title

def FetchDate(soup):
    try:
        body_text=soup.find(class_='ins_dateline')
        filtered_text=body_text.find_all('span')
        return filtered_text[2].contents
    except:
        return '23-11-2019'
st.sidebar.title('NDTV')
val=st.sidebar.selectbox('Select Category to See the Details',categories)
category=val
st.title(f'All News From {category.capitalize()} Category')
st.sidebar.multiselect('Select Multiple Categories to See the News',categories)
filename=category+'.txt'
with open(filename,'r') as f:
    for url in f:
        url=url.split('\n')[0]
        response=requests.get(url)
        soup=BeautifulSoup(response.text,'html.parser')
        title=FetchTitle(soup)
        date=FetchDate(soup)
        st.markdown(f'#### {date}')
        st.markdown(f'### [{title}]({url})')
        #st.markdown(f'### [{title}]({url})')
        