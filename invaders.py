import itertools
import collections  
import pandas as pd
import os
  
lInvaders = ["".join(seq) for seq in itertools.product("10", repeat=15)] # all binary combinations of 0s and 1s and length 15

# now we can see how many invaders have what rank (number of times '1' occurs in an invader string)
lRanks = []
for i in range(0,len(lInvaders)):    
    lRanks.append(lInvaders[i].count('1'))

# blocks string and rank into dataframe
oDataFrame = pd.DataFrame({'block_string': lInvaders, 'rank': lRanks})
oDataFrame = oDataFrame.sort_values(by=['rank'], ascending=True)
oDataFrame.to_json('data/all_data.json', orient='records')

# json for each rank
for i, x in oDataFrame.groupby('rank'):
    x.to_json(os.getcwd() + "/data/data_rank_{}.json".format(i), orient='records')

# print for counts of each rank
# counter=collections.Counter(lRanks) 
# print(counter)