# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 07:59:02 2018

@author: lemiltock
"""

import urllib.request as request
import re
import html

def page_scrape(url):
    '''
    Set browser type to mozilla
    url: string of webpage to scrape
    returns raw data of page
    '''
    user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    headers = {'User-Agent': user_agent}
    req = request.Request(url, headers=headers)
    page = request.urlopen(req)
    return page.read().decode('UTF-8')

def git_trending():
    '''
    returns a list of tuples that match the trending repo and stars
    (repo, stars)
    '''
    raw_data = page_scrape('https://github.com/trending')
    # split pattern into two strings for easy reading
    pattern1 = r'<li class="col-12 d-block width-full py-4 border-bottom" id="[a-zA-Z-]*">.*?<a href="(.*?)"'
    pattern2 = r'.*?<span class="d-inline-block float-sm-right">.*?/svg>\n *(.*?)\n'
    pattern = pattern1 + pattern2
    clean_data = html.unescsape(raw_data)
    data = re.findall(pattern, clean_data, flags=re.DOTALL)
    return data[0:10]

def stack_topqs():
    '''
    returns a list of tuples that match the top questions and their views
    (views, question)
    '''
    raw_data = page_scrape('https://stackoverflow.com/')
    # split pattern into two strings for easy reading
    pattern1 = r'<div class="question-summary narrow".*?class="views".*?title="(.*?)"'
    pattern2 = r'.*?class="question-hyperlink">(.*?)</a'
    pattern = pattern1 + pattern2
    clean_data = html.unescape(raw_data)
    data = re.findall(pattern, clean_data, flags=re.DOTALL)
    return data[0:10]

def imdb_popular_tv():
    '''
    returns a list of tuples that match most popular tv and their imdb ranking
    (show, rank)
    '''
    raw_data = page_scrape('https://www.imdb.com/chart/tvmeter')
    #split pattern into two strings for easy reading
    pattern1 = r'<td class="titleColumn">.*?>(.*?)</a>.*?'
    pattern2 = r'<td class="ratingColumn imdbRating">.*?title=(.*?) .*?<td class="ratingColumn">'
    pattern = pattern1 + pattern2
    clean_data = html.unescape(raw_data)
    data = re.findall(pattern, clean_data, flags=re.DOTALL)
    return data[0:10]

#print(git_trending())
#print(stack_topqs())
print(imdb_popular_tv())