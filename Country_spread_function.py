#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


## load file

df=pd.read_excel('Clean files/1996/1996 COUNTRIES WITH 3.xlsx')
df=df.replace(r'^\s*$', np.nan, regex=True)
    

# In[2]:
## The funciton calculate the spread of a target country ##

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
    
    vp_cal=weight_df.loc[country_name_str].iloc[0:,].dropna().values
    likeip_cal=voter_df[voter_df['country']==country_name_str].iloc[:,1:len(vp_cal)+1].dropna(axis=0)
    like_bar=likeip_cal.dot(vp_cal*0.01)
    likeip_likeBar=(likeip_cal.T-like_bar).T
    square=likeip_likeBar.apply(np.square).round(2)
    sum_vp_dot_squre=square.dot(vp_cal*0.01)
    spread=np.sqrt(np.array(sum_vp_dot_squre,dtype=np.float64))
    likeip_cal['spread']=spread.round(2)
    Contry_spread=pd.DataFrame(likeip_cal['spread'].describe().round(2)).rename(columns={"spread":country_name_str+' spread description'})
        
    return Contry_spread,likeip_cal,vp_cal


# In[ ]:
## The funciton split the original Data for further processing    
    
def likeip_vp_df_split(country_name_str):

    ## Weight(vp) DataFrame
    weight_list=list(df.columns[-9:])
    weight_list_countries=['E1006_NAM']+weight_list
    weight_df=df[weight_list_countries].groupby('E1006_NAM').mean(numeric_only=False)
    weight_df_ctry=pd.DataFrame(weight_df.loc[country_name_str])
    ## Voters(likeip) DataFrame
    voter_list=list(df.columns[2:-9])
    voter_list_countries=['E1006_NAM']+voter_list
    voter_df=df[voter_list_countries]
    voter_df_ctry=voter_df[voter_df['E1006_NAM']==country_name_str]
    
    voter_df_ctry.to_excel(country_name_str+' likeip_original.xlsx')
    weight_df_ctry.to_excel(country_name_str+' weight_origional.xlsx')
    
    return voter_df_ctry,weight_df_ctry


## test function 
def country_spread_test(file_path_str,country_name_str):
    
    ## Load File ##
    file_dir=file_path_str
    df=pd.read_excel(file_dir)
    df=df.replace(r'^\s*$', np.nan, regex=True)
    
    ## Weight(vp) DataFrame
    weight_list=list(df.columns[-9:])
    weight_list_countries=['E1006_NAM']+weight_list
    weight_df=df[weight_list_countries].groupby('E1006_NAM').mean(numeric_only=False)
    ## Voters(likeip) DataFrame
    voter_list=list(df.columns[2:-9])
    voter_list_countries=['E1006_NAM']+voter_list
    voter_df=df[voter_list_countries]
    
    ## Calculate spread
    
    vp_cal=weight_df.loc[country_name_str].iloc[0:,].dropna().values
    likeip_cal=voter_df[voter_df['E1006_NAM']==country_name_str].iloc[:,1:len(vp_cal)+1].dropna(axis=0)
    like_bar=likeip_cal.dot(vp_cal*0.01)
    likeip_likeBar=(likeip_cal.T-like_bar).T
    square=likeip_likeBar.apply(np.square).round(2)
    sum_vp_dot_squre=square.dot(vp_cal*0.01)
    spread=np.sqrt(np.array(sum_vp_dot_squre,dtype=np.float64))
    likeip_cal['spread']=spread.round(2)
    Contry_spread=pd.DataFrame(likeip_cal['spread'].describe().round(2)).rename(columns={"spread":country_name_str+' spread description'})
    
    ## save data ##
    Contry_spread.to_excel(country_name_str+' Contry_spread.xlsx')
    likeip_cal.to_excel(country_name_str+' likeip_cal.xlsx')
    weight_df.to_excel(country_name_str+' weight_df.xlsx')
    
    return Contry_spread,likeip_cal,vp_cal



