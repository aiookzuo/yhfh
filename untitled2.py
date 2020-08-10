# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:55:08 2020

@author: gu zhongxiang
"""

from nonebot import on_command, CommandSession
from urllib.request import urlopen
from bs4 import BeautifulSoup

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字
@on_command('news', aliases=('公告', '最新公告', '三国杀公告'), only_to_me = False)
async def weather(session: CommandSession):
    # 从会话状态（session.state）中获取缺人信息（confirmation），如果当前不存在，则询问用户
    confirm = session.get('confirm', prompt='你确定想要获取公告链接吗?若确定，请输入confirm')
    # 获取三国杀官网的公告
    news_report = await scrape_news(confirm)
    # 向用户发送公告
    await session.send(news_report)


async def scrape_news(city: str) -> str:
    html = urlopen('https://www.sanguosha.com')
    soup = BeautifulSoup(html,'html.parser')
    hyperlink = soup.find_all('a')
    for i in hyperlink:
        hh = i.get('href')
        if hh and ('https://www.sanguosha.com/Home/newsInfo/a_id/2020' in hh):
            return hh