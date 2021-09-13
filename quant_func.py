
import numpy as np
import pandas as pd

#%%
import numpy as np
import pandas as pd

def country_spread(df,country_name_str):
    
    
    ## Weight(vp) DataFrame
    weight_list=list(df.columns[list(df.columns.str.contains("voteshare"))])
    weight_list_countries=['country']+weight_list
    weight_df=df[weight_list_countries].groupby('country').mean(numeric_only=False)
    
    ## Voters(likeip) DataFrame
    voter_list=list(df.columns[list(df.columns.str.contains("party"))])
    voter_list_countries=['country']+voter_list
    voter_df=df[voter_list_countries]
    
    ## Calculate spread
    year=df['election_year'].mean()
    vp_cal=weight_df.loc[country_name_str].iloc[0:,].dropna().values
    likeip_cal=voter_df[voter_df['country']==country_name_str].iloc[:,1:len(vp_cal)+1].dropna(axis=0)
    like_bar=likeip_cal.dot(vp_cal*0.01)
    likeip_likeBar=(likeip_cal.T-like_bar).T
    square=likeip_likeBar.apply(np.square).round(2)
    sum_vp_dot_squre=square.dot(vp_cal*0.01)
    spread=np.sqrt(np.array(sum_vp_dot_squre,dtype=np.float64))
    likeip_cal['spread']=spread.round(2)
    Contry_spread=pd.DataFrame(likeip_cal['spread'].describe().round(2)).rename(columns={"spread":country_name_str+' spread description'})
    
    return Contry_spread,str(round(year)),likeip_cal,vp_cal


#%%


#%%
def Data2MAP (df,country_name_str):
    weight_list=list(df.columns[list(df.columns.str.contains("voteshare"))])
    weight_list_countries=['country']+weight_list
    weight_df=df[weight_list_countries].groupby('country').mean(numeric_only=False)
    
    ## Voters(likeip) DataFrame
    voter_list=list(df.columns[list(df.columns.str.contains("party"))])
    voter_list_countries=['country']+voter_list
    voter_df=df[voter_list_countries]
    year=df['election_year'].mean()
    #year=df[df.columns.str.contains("year")].mean()
    freqn=pd.DataFrame()
    Lpi=pd.DataFrame()
    Dpi=pd.DataFrame()
    for i in voter_df.columns[1:]:
        freqn[i]=voter_df[i].value_counts().sort_index()
        Lpi[i]=freqn[i].iloc[-3:]/freqn[i].sum()
        Dpi[i]=freqn[i].iloc[0:3]/freqn[i].sum()
    LP = Lpi.sum(axis=0)
    DP = Dpi.sum(axis=0)
    N=round(df['N'].mean(),2)
    MAP=(LP.dot(DP))/(0.25*N)
        
    return LP,DP,freqn,year,MAP 

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
def MAP (Lpi,Dpi,N):
    MAP_cal=(Lpi.dot(Dpi))/(0.25*N)
    return MAP_cal

#%%
    