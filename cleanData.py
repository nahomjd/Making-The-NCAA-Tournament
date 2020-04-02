import pandas as pd

df = pd.read_csv('combinedCBBStatsOriginal.csv')

list1 = []
list2 = []

for i in range(1,31):
    list1.append(str(i))
    list2.append(str(i)+'*')
    
df.replace(to_replace=list2,value=list1)
print(list2)

wins = df['wins'].tolist()
losses = df['losses'].tolist()
Cwins = df['wins_conf'].tolist()
Closses = df['losses_conf'].tolist()
maxRound = df['round_max'].tolist()

row = 0
for i in wins:
    if '*' in i:
        i = i.replace('*','')
        df.loc[row, 'wins'] = i
    row += 1
    
row = 0
for i in losses:
    if '*' in i:
        i = i.replace('*','')
        df.loc[row, 'losses'] = i
    row += 1

row = 0   
for i in Cwins:
    i = str(i)
    if '*' in i:
        i = i.replace('*','')
        df.loc[row, 'wins_conf'] = i
    row += 1
   
row = 0
for i in Closses:
    i = str(i)
    if '*' in i:
        i = i.replace('*','')
        df.loc[row, 'losses_conf'] = i
    row += 1

row = 0    
madeNBT = 1
noNBT = 0
makeTournament = []
for i in maxRound:
    if str(i) != 'nan':
        makeTournament.append(madeNBT)
    else:
        makeTournament.append(noNBT)

df['makeTournament'] = makeTournament
       
df.to_csv('combinedCBBStats.csv')