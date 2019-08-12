#!/usr/bin/env python
# coding: utf-8

# In[21]:


#import Libraries
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

# pull espn  source code
url ='http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/1'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

#create column names
header = soup.find("tr", attrs= {"class": "colhead"})
#extract column names
columns = [col.get_text() for col in header.find_all("td")]

#create dataframe
final_df = pd.DataFrame(columns=columns)
final_df


# In[22]:


#pull espn source code
url = 'http://www.espn.com/mlb/history/leaders/_/breakdown/season/year/2019/start/()'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')

# pull players stats
players = soup.find_all("tr", attrs ={"class":re.compile("row player-10-")})
for player in players:
    
    #get stats for players
    stats = [stat.get_text() for stat in player.find_all("td")]
    
    #dataframe for player stats
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    
    #Combine player stats with dataset
    final_df = pd.concat([final_df,temp_df], ignore_index= True)
final_df


# In[23]:


final_df.to_csv(r"Desktop/mlb_stats.csv")


# In[ ]:




