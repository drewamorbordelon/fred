import pandas as pd
import numpy as np
import datetime
import pandas_datareader as pdr
import quandl
import csv
# from .env import quandl_API


# Pulling data from Quandl API 
quandl.ApiConfig.api_key='1mEBe1BeVaAExprr7akA'
df_ism = pd.read_csv('https://www.quandl.com/api/v3/datasets/ISM/MAN_PMI.csv?api_key=1mEBe1BeVaAExprr7akA', index_col=['Date'])
df_ism = df_ism.iloc[::-1]



# Setting up the Start and End time 
# series_code = ['CURRCIR', 'DGS10']
data_source = 'fred'

start = datetime.datetime (1990, 1, 1)      #  (2005, 5, 1)
end = datetime.datetime (2030, 12, 1)


"""
Reading in the data from FRED
"""
df_m2 = pdr.DataReader('CURRCIR', data_source, start, end)
df_m2_vel = pdr.DataReader('M2V', data_source,start, end)
df_yr10 = pdr.DataReader('DGS10', data_source, start, end)
df_vix = pdr.DataReader('VIXCLS', data_source, start, end)
df_headline_cpi = pdr.DataReader('CPIAUCSL', data_source, start, end)
df_core_cpi = pdr.DataReader('CPILFESL', data_source, start, end)
df_gdp = pdr.DataReader('GDPC1', data_source, start, end)


df_qoq = pd.merge(df_gdp, df_headline_cpi, left_index=True, right_index=True)
df_qoq = pd.merge(df_qoq, df_core_cpi, left_index=True, right_index=True)
df_qoq.columns = ['GDP', 'CPI', 'Core_CPI']
# print(df_qoq.head())
# print(df_qoq.tail(10))


"""
Merging all the dataframes and renaming 
the columns MoM with some QoQ (for the most part)
"""
df_mom  = pd.merge(df_m2, df_yr10, on='DATE', how='inner')      #  using `merge` REMOVES all NaN values
df_mom = pd.merge(df_mom, df_ism, left_index=True, right_index=True)
df_mom= pd.merge(df_mom, df_vix, left_index=True, right_index=True)
df_mom = pd.merge(df_mom, df_headline_cpi, left_index=True, right_index=True)
df_mom = pd.merge(df_mom, df_core_cpi, left_index=True, right_index=True)

df_mom = df_mom.join(df_gdp)    #  using `join` will KEEP all NaN values
df_mom = df_mom.join(df_m2_vel)

df_mom.columns = ['M2_supply', 'US10yr_rate', 'ISM_PMI', 'VIX', 'Headline_CPI', 'Core_CPI', 'Real_GDP', 'M2_velocity']

df_mom['ISM_lagged18'] = df_mom['ISM_PMI'].shift(18)
df_mom['US10_pct_yoy'] = df_mom['US10yr_rate'].pct_change(12)
df_mom['Core_pct_yoy_INV'] = df_mom['Core_CPI'].pct_change(12) 

# print(df_mom.shape)
# print(df_mom.head())
# print(df_mom.tail())
# print(df_mom.corr())

fedfunds = pdr.DataReader('FEDFUNDS', data_source, start, end)
pce = pdr.DataReader('PCE', data_source, start, end)




if __name__ == "__main__":
    # print(df_mom.tail(10))
    # print(fedfunds.head(2))
    # print(fedfunds.tail(10))
    print(pce.head())
    print(pce.tail(6))
    # print(df_qoq.tail())
    # print(df_mom.shape)
    # print(df_mom.isnull().sum())
    # print(df_mom.corr())