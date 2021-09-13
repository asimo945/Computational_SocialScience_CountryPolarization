## try to automatically scan over files
import os
from quant_func import *

#%%

folder_dir='Data with N/Calculate'
cont=[]
y=[]
MAP_=[]

for filename in os.listdir(folder_dir):
    if filename.endswith('.xlsx'):
        df=pd.read_excel(folder_dir+'/'+filename).replace(r'^\s*$', np.nan, regex=True)
        countries= list(df['country'].unique())
        year=[]
        country=[]
        MAP=[]
        for k in countries:
            country.append(k)
            LP,DP,freqn,Y,map_cal = Data2MAP (df,k)
            Y=str(round(Y))
            year.append(Y)
            MAP.append(map_cal)
            cont.append(k)
            y.append(Y)
            MAP_.append(map_cal)
            freqn['MAP']=map_cal
            LP.to_excel(folder_dir+'/Results/'+k+Y+'Lpi.xlsx')
            DP.to_excel(folder_dir+'/Results/'+k+Y+'Dpi.xlsx')
            freqn.to_excel(folder_dir+'/Results/'+k+Y+'freq.xlsx')
            d={'year':year,'country':country,'MAP': MAP}
            overall= pd.DataFrame(d)
            overall.to_excel(folder_dir+'/overall/'+k+Y+'overall.xlsx')
    
    else:
        continue

data=pd.DataFrame({'contry':cont,'year':y,'MAP':MAP_}).sort_values('year').reset_index(drop=True)
data.to_excel('Data with N/'+"overall_MAP_data.xlsx")
    