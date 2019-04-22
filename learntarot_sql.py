######################################################################
"""
Load learntarot scrape data to postgresql
"""
######################################################################

import pandas as pd
import sqlalchemy as sql



######################################################################
"""
Load action/subaction tables into database
"""
######################################################################

actions_df = pd.read_csv('db/actions.csv', sep = '|')
actions_df = actions_df.applymap( lambda x: float(x) if type(x) == int else x )
subactions_df = pd.read_csv('db/subactions.csv', sep = '|')
subactions_df = subactions_df.applymap( lambda x: float(x) if type(x) == int else x )

act_values = [ dict(actions_df.loc[row]) for row in actions_df.index]
subact_values = [ dict(subactions_df.loc[row]) for row in subactions_df.index]

engine = sql.create_engine('postgresql://postgres:dbpass@localhost/Tarot')
conn = engine.connect()
meta = sql.MetaData()


actions_table = sql.Table('actions',meta, autoload = True, autoload_with = engine)
actins = actions_table.insert()
subactions_table = sql.Table('subactions',meta, autoload = True, autoload_with = engine)
subactins = subactions_table.insert()

conn.execute(actins, act_values)
conn.execute(subactins, subact_values)

