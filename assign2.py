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
    returns a list of 10 tuples that match the trending repo and stars
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
    returns a list of 10 tuples that match the top questions and their views
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
    returns a list of 10 tuples that match most popular tv and their imdb ranking
    (show, rank)
    '''
    raw_data = page_scrape('https://www.imdb.com/chart/tvmeter')
    #split pattern into two strings for easy reading
    pattern1 = r'<td class="titleColumn">.*?>(.*?)</a>.*?'
    pattern2 = r'<td class="ratingColumn imdbRating">.*?title="(.*?) .*?<td class="ratingColumn">'
    pattern = pattern1 + pattern2
    clean_data = html.unescape(raw_data)
    data = re.findall(pattern, clean_data, flags=re.DOTALL)
    return data[0:10]

def html_export(image, title, col_label, data, webpage):
    '''
    image: string, link to image
    title: string, table title
    col_label: tuple of column labels
    data: 10 tuples of table data
    webpage: string, source location for data
    returns a multiline string of html code ready for export
    '''
    format_match = {'title': title, 'image': image, 'column1': col_label[0], 'column2': col_label[1],
                    'data1-1': data[0][0], 'data1-2': data[0][1], 'data2-1': data[1][0],
                    'data2-2': data[1][1], 'data3-1': data[2][0], 'data3-2': data[2][1],
                    'data4-1': data[3][0], 'data4-2': data[3][1], 'data5-1': data[4][0],
                    'data5-2': data[4][1], 'data6-1': data[5][0], 'data6-2': data[5][1],
                    'data7-1': data[6][0], 'data7-2': data[6][1], 'data8-1': data[7][0],
                    'data8-2': data[7][1], 'data9-1': data[8][0], 'data9-2': data[8][1],
                    'data10-1': data[9][0], 'data10-2': data[9][1], 'webpage': webpage}
    export = '''<!DOCTYPE html>
<html>
  <title>{title}</title>
  <body>
    <img src="{image}" alt="Image Loading" width="500" height="500">
    <!--Create 3x11 table to display ranked data-->
    <h1>{title}</h1>
    <table>
      <tr>
        <th>Rank</th>
        <th>{column1}</th>
        <th>{column2}</th>
      </tr>
      <tr>
        <td>1</td>
        <td>{data1-1}</td>
        <td>{data1-2}</td>
      </tr>
      <tr>
        <td>2</td>
        <td>{data2-1}</td>
        <td>{data2-2}</td>
      </tr>
      <tr>
        <td>3</td>
        <td>{data3-1}</td>
        <td>{data3-2}</td>
      </tr>
      <tr>
        <td>4</td>
        <td>{data4-1}</td>
        <td>{data4-2}</td>
      </tr>
      <tr>
        <td>5</td>
        <td>{data5-1}</td>
        <td>{data5-2}</td>
      </tr>
      <tr>
        <td>6</td>
        <td>{data6-1}</td>
        <td>{data6-2}</td>
      </tr>
      <tr>
        <td>7</td>
        <td>{data7-1}</td>
        <td>{data7-2}</td>
      </tr>
      <tr>
        <td>8</td>
        <td>{data8-1}</td>
        <td>{data8-2}</td>
      </tr>
      <tr>
        <td>9</td>
        <td>{data9-1}</td>
        <td>{data9-2}</td>
      </tr>
      <tr>
        <td>10</td>
        <td>{data10-1}</td>
        <td>{data10-2}</td>
      </tr>
    </table>
    <!-- Add source location as a hyperlink for tabulated data -->
    This data was sourced from <a href="{webpage}">{webpage}<a/>.
  </body>
</html>'''.format(**format_match)
    print(export)