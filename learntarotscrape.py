# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 17:34:39 2018

@author: bahar
"""

from bs4 import BeautifulSoup as bs
import urllib.request as ulr
import pandas as pd
import re

"""
Section 1: function definitions
"""
def card_scrape(url):
    page_html = ulr.urlopen(url)
    page_soup = bs(page_html, "html.parser")
    return page_soup

"""
Section 2: Load cards.htm and scrape card names and links
"""
url = "http://learntarot.com/cards.htm"

page_soup = card_scrape(url)

""" create array of titles to initialize DataFrame """
titles = []
for head in page_soup.findAll('b'):             #loop through each <b> tag
    headstr = str(head)                         #convert the tag to a string
    #print(headstr)
    title_search = re.compile('(?<=\s|\>)\w+')  
    title = title_search.search(headstr)        #return the part of the tag after the > (plus whitespace)
    if(title != None):
        #print(headstr[title.start():title.end()])
        titles.append(headstr[title.start():title.end()])


titles[24:38] = [(title + " of Wands") for title in titles[24:38]]
titles[39:53] = [(title + " of Cups") for title in titles[39:53]]
titles[54:68] = [(title + " of Swords") for title in titles[54:68]]
titles[69:83] = [(title + " of Pentacles") for title in titles[69:83]]


scrape_df = pd.DataFrame(data=titles,columns=['Title'])

""" populate main scrape data """


scrape_df['Links'] = [link.get('href') for link in page_soup.findAll('a', attrs={'href': re.compile(".htm")})][2:-5]
# remove first 2 links (how-to) and last 5 links (navigation)

scrape_df['Card ID'] = [link.split(sep='.')[0] for link in scrape_df['Links']]

suit_dic = {'m':'Major','t':'Suit','w':'Wands','c':'Cups','s':'Swords','p':'Pentacles'}
scrape_df['Suit'] = [suit_dic[card[0]] for card in scrape_df['Card ID']]

scrape_df['Previous'] = [scrape_df['Card ID'][i-1] if (i > 0 and scrape_df['Suit'][i] == scrape_df['Suit'][i-1]) else '-' for i in scrape_df.index]

scrape_df['Small Image'] = [card + 's.gif' if card[0]!='t' else '-' for card in scrape_df['Card ID']]

"""
Load card sites and scrape: keywords,
"""
keywords=[]
opposing=[]
reinforcing = []
descs = []
for link in scrape_df['Links']:
    if link[0] == 't':
        keywords.append('-')
        opposing.append('-')
        reinforcing.append('-')
        descs.append('-')
    else:
        url = "http://learntarot.com/"+link
        page_soup = card_scrape(url)
        tags_u = page_soup.findAll('ul')

        if len(tags_u) == 1 or link == 'p6.htm':
            keywords.append(str(tags_u[0]))
            opposing.append('-')
            reinforcing.append('-')
        else:
            keywords.append(str(tags_u[0]))
            opposing.append(str(tags_u[1]))
            reinforcing.append(str(tags_u[2]))
        
        tags_p = page_soup.findAll('p')
        for p in tags_p:
            p_search = re.compile('\<p\>(?!=\<)').search(str(p))
            p_text = str(p)[p_search.start():p_search.end()]
            descs.append('-')

scrape_df['Keywords'] = keywords   
scrape_df['Opposing'] = opposing
scrape_df['Reinforcing'] = reinforcing 

scrape_cols = ['Card ID','Title','Suit','Links','Small Image','Keywords','Opposing','Reinforcing','Previous']  
scrape_df = scrape_df[scrape_cols]
                
#scrape_df.to_csv('learntarotscrape_df.csv')

cards_cols = ['Card ID','Title','Suit']
cards_df = scrape_df[cards_cols]

related = []
card_desc = []
for i in scrape_df.index:
    card_temp = scrape_df['Card ID'][i]
    opp_soup = bs(scrape_df['Opposing'][i],"html.parser")
    re_soup = bs(scrape_df['Reinforcing'][i],"html.parser")  
    opp_search = opp_soup.find_all('a',attrs={'href':re.compile(".htm")})
    re_search = re_soup.find_all('a',attrs={'href':re.compile(".htm")})   
    for o in opp_search:
        o_title = o.get('href').split(sep='.')[0]
        related.append([card_temp,o_title,'opposing'])
    for r in re_search:
        r_title = r.get('href').split(sep='.')[0]
        related.append([card_temp,r_title,'reinforcing'])
    if scrape_df['Previous'][i] != '-':
        related.append([card_temp, scrape_df['Previous'][i],'previous'])
    
    key_soup = bs(scrape_df['Keywords'][i],"html.parser")
    key_list = key_soup.find_all('b')
    for key in key_list:
        key_search = re.compile('(?<=\>).+(?=\<)').search(str(key))
        key_text = str(key)[key_search.start():key_search.end()]
        card_desc.append([card_temp,key_text,'Keyword'])
    
rel_df = pd.DataFrame(related)    
rel_df.columns = ['Root Card','Related Card','Relationship'] 
desc_df = pd.DataFrame(card_desc)
desc_df.columns = ['Root Card','Desc','Desc Type']

print(cards_df.head())
