import numpy as np
import pandas as pd
from quant_func import*

#%%
def N(v):
    V = np.array(v)
    A = V
    pi = np.array([i**2 for i in A])
    sigma_pi = sum(pi)
    p_square = sum(A)**2
    n = p_square/sigma_pi 


    return n, sigma_pi

#%%
def Lpi_Dpi (df,country_name_str):
    voter_df, weight_df=data_extraction(df,country_name_str)
    freqn=pd.DataFrame()
    Lpi=pd.DataFrame()
    Dpi=pd.DataFrame()
    for i in voter_df.columns[1:]:
        freqn[i]=voter_df[i].value_counts().sort_index()
        Lpi[i]=freqn[i].iloc[-3:]/freqn[i].sum()
        Dpi[i]=freqn[i].iloc[0:3]/freqn[i].sum()
    return Lpi.sum(axis=0),Dpi.sum(axis=0),freqn 


#%%
def MAP (Lpi,Dpi,N):
    MAP_cal=(Lpi.dot(Dpi))/(0.25*N)
    return MAP_cal
    
#%%
S=[140,94,93,5,14,0,3,3,4,2,2,2]
Voter=[5.694,4.516,4.187,0.873,0.728,0.223,0.139,0.102,0.102,0.101,0.075,0.0335]

#%%
file_dir='Data with N/2011/2011 TURKEY miss.xlsx'

df=pd.read_excel(file_dir)

lpi,dpi,freqn=Lpi(df,'Turkey')

N = df['N'].mean()
MAP_countru = MAP(lpi,dpi,N)

#%%
# Nv,sigma_pi_v=N(Voter)
# Ns,sigma_pi_s=N(S)

dot_test=lpi.dot(dpi)
