import numpy as np
import pandas as pd

#%%
class MAP:
    def __init__(self,data,country):
        self.data=data
        self.country=country
        
    ## Data clean
    def data_extraction(self):
        ## Weight(vp) DataFrame
        weight_list=list(self.data.columns[list(self.data.columns.str.contains("voteshare"))])
        weight_list_countries=[self.country]+weight_list
        weight_df=self.data[weight_list_countries].groupby(self.country).mean(numeric_only=False)
        weight_df=weight_df.loc[country_name_str].iloc[0:,]
        ## Voters(likeip) DataFrame
        voter_list=list(df.columns[list(df.columns.str.contains("party"))])
        voter_list_countries=['country']+voter_list
        voter_df=df[voter_list_countries]
        voter_df=voter_df[voter_df['country']==country_name_str]
    
    
    return voter_df, weight_df

    
    ## calculate N
    
        
        
