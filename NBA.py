#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
# NBA season 
year = 2019
# URL page 
url = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html".format(year)
# this is the HTML from the given URL
html = urlopen(url)
soup = BeautifulSoup(html)
#get the column headers
soup.findAll('tr', limit=2)
# extract the text for a list
headers = [th.getText() for th in soup.findAll('tr', limit=2)[0].findAll('th')]
# exclude the first column 
headers = headers[1:]
headers
 # avoid the first header row
rows = soup.findAll('tr')[1:]
player_stats = [[td.getText() for td in rows[i].findAll('td')]
            for i in range(len(rows))]
stats = pd.DataFrame(player_stats, columns = headers)
stats.head(50)


# In[2]:


stats.to_csv(r'Desktop/nba_stats.csv', index = False, sep=',', encoding='utf-8')


# In[ ]:




