import pandas as pd

df = pd.read_csv('sportsref_download.csv')

i = 0
CS = df['City, State']
state = ''
for elem in CS:
    state = elem.split(',')[1][1:]
    df.loc[i, 'states'] = state
    i += 1
    
df.to_csv('refernceWithStates.csv')