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

##############################################################
"""
Section 2: Load cards.htm and scrape card names and links
"""
##############################################################

url = "http://learntarot.com/cards.htm"

page_soup = card_scrape(url)

""" create array of titles to initialize DataFrame """
titles = []
for head in page_soup.findAll('b'):             #loop through each <b> tag
    headstr = str(head)                         #convert the tag to a string
    #print(headstr)
    title_search = re.compile('(?<=\s|\>).+(?=\<)')
    title = title_search.search(headstr)        #return the part of the tag after the > (plus whitespace)
    if(title != None):
        #print(headstr[title.start():title.end()])
        title_text = headstr[title.start():title.end()]
        title_text = title_text.replace('[','')
        title_text = title_text.replace(']','')
        title_text = title_text.replace('-','')
        title_text = title_text.strip()
        title_text = title_text.title()
        titles.append(title_text)


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

##################################################
"""
Load card sites and scrape: keywords,
"""
##################################################
actions=[]
opp_raw=[]
re_raw = []
descs = []
#desc_len = []
"""
loop through each card
"""
actID = 0
sactID = 0

for card in scrape_df['Card ID']:
    if card[0] == 't':
        actions.append('-')
        opp_raw.append('-')
        re_raw.append('-')
        descs.append('-')
    else:
        url = "http://learntarot.com/"+card+".htm"
        page_soup = card_scrape(url)
        tags_u = page_soup.findAll('ul')        # ul tags contain opposing/reinforcing info
        tag_dl = str(page_soup.find('dl'))      # dl tag contains actions(dt) and subactions(dd)

        if len(tags_u) == 1 or card == 'p6':
            opp_raw.append('-')
            re_raw.append('-')
        else:
            opp_raw.append(str(tags_u[1]))        #changed these indices to 0 and 1 bc keywords is no longer in the list; could be wrong
            re_raw.append(str(tags_u[2]))

        tags_p = page_soup.findAll('p')
        no_hit = True
        count = -1
        while no_hit:
            p = tags_p[count]
            tag_search = re.compile('howdesc').search(str(p))
            if tag_search == None:
                count += -1
            else:
                no_hit = False
        p = tags_p[count + 1]

        hr_search = re.compile('\<hr').search(str(p))
        desc_text = str(p)[:hr_search.start()]
        desc_text = bs(desc_text, "html.parser").text
        desc_text = desc_text.replace('\r','')
        desc_text = desc_text.replace('\n','')
        descs.append(desc_text)
        #desc_len.append(len(desc_text))

        tags_dt = re.compile('(?<=dt\\>).+(?=\\<)').findall(tag_dl)[:-1]
        tags_dd = re.compile('(?s)(?<=dd\>(?!\<)).+?(?=\<\/?d)').findall(tag_dl)
        action_row = []
        for i in range(len(tags_dt)):
            action_dict = {}
            actID += 1
            act = tags_dt[i].replace('<b>','')
            action_dict['act'] = act
            
            dd = tags_dd[i]
            dd = dd.replace('\r','')
            dd = dd.replace('<br/>','')
            dd = dd.replace('<p>','')
            dd_split = dd.split('\n')
            subacts = [a for a in dd_split if a != '']
            action_dict['sub'] = subacts

            action_row.append(action_dict)
        actions.append(action_row)

    

opposing = []
reinforcing = []
for i in scrape_df.index:
    card_temp = scrape_df['Card ID'][i]
    opp_soup = bs(opp_raw[i],"html.parser")
    re_soup = bs(re_raw[i],"html.parser")
    opp_search = opp_soup.find_all('a',attrs={'href':re.compile(".htm")})
    re_search = re_soup.find_all('a',attrs={'href':re.compile(".htm")})
    o_row = []
    r_row = []
    for o in opp_search:
        o_title = o.get('href').split(sep='.')[0]
        o_row.append(o_title)
    for r in re_search:
        r_title = r.get('href').split(sep='.')[0]
        r_row.append(r_title)

    opposing.append(o_row)
    reinforcing.append(r_row)

    # if scrape_df['Previous'][i] != '-':
    #     related.append([card_temp, scrape_df['Previous'][i],'previous'])

    # key_soup = bs(scrape_df['Keywords'][i],"html.parser")
    # key_list = key_soup.find_all('b')
    # for key in key_list:
    #     key_search = re.compile('(?<=\>).+(?=\<)').search(str(key))
    #     key_text = str(key)[key_search.start():key_search.end()]
    #     keys.append([card_temp,key_text])

scrape_df['Opposing'] = opposing
scrape_df['Reinforcing'] = reinforcing
scrape_df['Actions'] = actions
scrape_df['Description'] = descs

scrape_cols = ['Card ID','Title','Suit','Links','Small Image','Opposing','Reinforcing','Previous', 'Actions', 'Description']
scrape_df = scrape_df[scrape_cols]

scrape_df.to_json(path_or_buf = 'www/tarot_cards.js', orient='records')
