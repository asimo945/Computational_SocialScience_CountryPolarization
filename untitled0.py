import numpy as np
import pandas as pd
from quant_func import*


file_dir='Data with N/2011/2011 TURKEY miss.xlsx'

df=pd.read_excel(file_dir)

voter_df, weight_df=data_extraction(df,'Turkey')
freqn=pd.DataFrame()
Lpi=pd.DataFrame()
Dpi=pd.DataFrame()
for i in voter_df.columns[1:]:
    freqn[i]=voter_df[i].value_counts().sort_index()
    Lpi[i]=freqn[i].iloc[-3:]/freqn[i].sum()
    Dpi[i]=freqn[i].iloc[0:3]/freqn[i].sum()

Lp=Lpi.sum(axis=0)
Dp=Dpi.sum(axis=0)

result=pd.DataFrame({'Lp':Lp,'Dp':Dp})
result['lpi*dpi']=result['Lp']*result['Dp']
sum_=result['lpi*dpi'].sum()
N = df['N'].mean()
result['MAP'] = sum_ /(N*0.25)

MAP=(Lp.dot(Dp))/(0.25*N)
