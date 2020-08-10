# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 11:04:38 2020

@author: gu zhongxiang
"""
import nonebot
from nonebot import on_command, CommandSession
from urllib.request import urlopen
from bs4 import BeautifulSoup

@on_command ('news', aliases = ('公告', '最新公告'))
async def news(session: CommandSession):
    html = urlopen('https://www.sanguosha.com')
    soup = BeautifulSoup(html,'html.parser')
    hyperlink = soup.find_all('a')
    for i in hyperlink:
        hh = i.get('href')
        if hh and ('https://www.sanguosha.com/Home/newsInfo/a_id/2020' in hh):
            await(hh) 

async 