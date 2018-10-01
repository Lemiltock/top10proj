# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 07:59:02 2018

@author: lemiltock
"""

import urllib.request as request
import re

# Set browser type to mozilla
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
headers = {'User-Agent': user_agent}

def git_trending():
    '''
    returns a list of tuples that match the trending repo and stars 
    '''
    url = 'https://github.com/trending'
    req = request.Request(url, headers=headers)
    page = request.urlopen(req)
    raw_data = page.read().decode('UTF-8')
    # split pattern into two strings for easy reading
    pattern1 = r'<li class="col-12 d-block width-full py-4 border-bottom" id="[a-zA-Z-]*">.*?<a href="(.*?)"'
    pattern2 = r'.*?<span class="d-inline-block float-sm-right">.*?/svg>\n *(.*?)\n'
    pattern = pattern1 + pattern2
    return re.findall(pattern, raw_data, flags=re.DOTALL)

git_data = git_trending()

print('<tr>\n<th>"REPO"</th>\n<th>"Stars"</th>\n</tr>')
for row in git_data:
    print('<tr>\n<td>'+row[0]+'</td>\n<td>'+row[1]+'</td>\n</tr>')