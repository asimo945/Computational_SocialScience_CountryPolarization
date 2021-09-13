## try to automatically scan over fils
import os
from quant_func import *

#%%

folder_dir='Data with N/2006'


for filename in os.listdir(folder_dir):
    if filename.endswith('.xlsx'):
        df=pd.read_excel(folder_dir+'/'+filename).replace(r'^\s*$', np.nan, regex=True)
        countries= list(df['country'].unique())
        probm=[]
        ## This loop is used to detec the problems ##
        for i in countries:
            Contry_spread,year,likeip_cal,vp_cal=country_spread(df,i)
            if Contry_spread.loc['count'].values==0:
                probm.append(i)
        print ('the problem dataset is :', probm)
        
        ## This looop is use to output the results of spread
        overall=pd.DataFrame()
        for k in countries:
            Contry_spread,year,likeip_cal,vp_cal=country_spread(df,k)
            
            # save data ##
            # Contry_spread.to_excel(folder_dir+'/results/'+k+'Contry_spread.xlsx')
            # likeip_cal.to_excel(folder_dir+'/results/'+k+'likeip_cal.xlsx')
            # pd.DataFrame(vp_cal).to_excel(folder_dir+'/results/'+k+'vp_cal.xlsx')
            
            overall['year']=year
            overall[k]=Contry_spread
            
        overall.to_excel(folder_dir+'/overall/'+k+year+'_overall.xlsx')
        
        
    else:
        continue
        
        
