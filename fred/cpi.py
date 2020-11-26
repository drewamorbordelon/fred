from mom_data import *
from qoq_data import *
# import mom_data
# import qoq_data
import yfinance as yf
import pandas as pd
import numpy as np
import datetime
import pandas_datareader as pdr

# Setting up the Start and End time 
# series_code = ['CURRCIR', 'DGS10']
data_source = 'fred'
start = datetime.datetime (1990, 1, 1)      #  (2005, 5, 1)
end = datetime.datetime (2030, 12, 1)

#  6 TOTAL
#  NSA Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
uscpi_urban_nsa = pdr.DataReader('CPIAUCNS', data_source, start, end)
# uscpi_urban_nsa = uscpi_urban_nsa.pct_change(12)
# uscpi_urban_nsa = uscpi_urban_nsa - uscpi_urban_nsa.shift()
# uscpi_urban_nsa = uscpi_urban_nsa * 100


#  NSA Consumer Price Index for All Urban Consumers: All Items Less Food and Energy in U.S. City Average
uscpi_food_ener_nsa = pdr.DataReader('CPILFENS', data_source, start, end)
# uscpi_food_ener_nsa = uscpi_food_ener_nsa.pct_change(12)
# uscpi_food_ener_nsa = uscpi_food_ener_nsa - uscpi_food_ener_nsa.shift()
# uscpi_food_ener_nsa = uscpi_food_ener_nsa * 100


#  NSA Consumer Price Index for All Urban Consumers: Energy in U.S. City Average 
uscpi_ener_nsa = pdr.DataReader('CPIENGNS', data_source, start, end)
# uscpi_ener_nsa = uscpi_ener_nsa.pct_change(12)
# uscpi_ener_nsa = uscpi_ener_nsa - uscpi_ener_nsa.shift() 
# uscpi_ener_nsa = uscpi_ener_nsa * 100

#  SA Cleveland FED Median Consumer Price Index
uscpi_median_nsa = pdr.DataReader('MEDCPIM158SFRBCLE', data_source, start, end)
# uscpi_median_nsa = uscpi_median_nsa - uscpi_median_nsa.shift(12)  #  this one needs fixing .5 is what I'm looking for

#  NSA Consumer Price Index for All Urban Consumers: Commodities Less Food and Energy Commodities in U.S. City Average
uscpi_commodity_lessFE = pdr.DataReader('CUUR0000SACL1E', data_source, start, end)
# uscpi_commodity_lessFE = uscpi_commodity_lessFE.pct_change(12)
# uscpi_commodity_lessFE = uscpi_commodity_lessFE - uscpi_commodity_lessFE.shift()
# uscpi_commodity_lessFE = uscpi_commodity_lessFE * 100

#  NSA Consumer Price Index for All Urban Consumers: Services Less Energy Services in U.S. City Average
uscpi_services_nsa = pdr.DataReader('CUSR0000SASLE', data_source, start, end)
# uscpi_services_nsa = uscpi_services_nsa.pct_change(12)
# uscpi_services_nsa = uscpi_services_nsa - uscpi_services_nsa.shift()
# uscpi_services_nsa = uscpi_services_nsa * 100




#  merged CPI dataframes 
cpi_data = pd.merge(uscpi_urban_nsa, uscpi_food_ener_nsa, left_index=True, right_index=True)
cpi_data = pd.merge(cpi_data, uscpi_ener_nsa, left_index=True, right_index=True)
cpi_data = pd.merge(cpi_data, uscpi_median_nsa, left_index=True, right_index=True)
cpi_data = pd.merge(cpi_data, uscpi_commodity_lessFE, left_index=True, right_index=True)
cpi_data = pd.merge(cpi_data, uscpi_services_nsa, left_index=True, right_index=True)


cpi_data.columns = [
    'CPI ALL', 
    'CPI All Less F&E',
    'CPI Energy',
    'Clev FED Median CPI',
    'CPI Commod Less F&E',
    'CPI Serv Less Energy'
    ]


cpi_data['CPI_all_firstdiff'] = (np.log(cpi_data['CPI ALL']).diff(12))   #   log diff/rate of change one quarter to same quarter of previous year
cpi_data['CPI_all_firstdiff'] = cpi_data['CPI_all_firstdiff']  * 100
cpi_data['CPI_all_firstdiff'] = cpi_data['CPI_all_firstdiff'] - cpi_data['CPI_all_firstdiff'].shift(1)    #  `Rate of Change` and the `first difference` * 100 == BPS
cpi_data['CPI_all_firstdiff'] = cpi_data['CPI_all_firstdiff']  * 100

cpi_data['CPI All Less_fd'] = (np.log(cpi_data['CPI All Less F&E']).diff(12))   #   log diff/rate of change one quarter to same quarter of previous year
cpi_data['CPI All Less_fd'] = cpi_data['CPI All Less_fd']  * 100
cpi_data['CPI All Less_fd'] = cpi_data['CPI All Less_fd'] - cpi_data['CPI All Less_fd'].shift(1)    #  `Rate of Change` and the `first difference` * 100 == BPS
cpi_data['CPI All Less_fd'] = cpi_data['CPI All Less_fd']  * 100

cpi_data['CPI Energy_fd'] = (np.log(cpi_data['CPI Energy']).diff(12))   #   log diff/rate of change one quarter to same quarter of previous year
cpi_data['CPI Energy_fd'] = cpi_data['CPI Energy_fd']  
cpi_data['CPI Energy_fd'] = cpi_data['CPI Energy_fd'] - cpi_data['CPI Energy_fd'].shift(1)    #  `Rate of Change` and the `first difference` * 100 == BPS
cpi_data['CPI Energy_fd'] = cpi_data['CPI Energy_fd']  * 100

cpi_data['Clev_fd'] = (np.log(cpi_data['Clev FED Median CPI']).diff(12))   #   log diff/rate of change one quarter to same quarter of previous year
cpi_data['Clev_fd'] = cpi_data['Clev_fd']  
cpi_data['Clev_fd'] = cpi_data['Clev_fd'] - cpi_data['Clev_fd'].shift(1)    #  `Rate of Change` and the `first difference` * 100 == BPS
cpi_data['Clev_fd'] = cpi_data['Clev_fd']  * 100

cpi_data['CPI Commod Less F&E_fd'] = (np.log(cpi_data['CPI Commod Less F&E']).diff(12))   #   log diff/rate of change one quarter to same quarter of previous year
cpi_data['CPI Commod Less F&E_fd'] = cpi_data['CPI Commod Less F&E_fd']  
cpi_data['CPI Commod Less F&E_fd'] = cpi_data['CPI Commod Less F&E_fd'] - cpi_data['CPI Commod Less F&E_fd'].shift(1)    #  `Rate of Change` and the `first difference` * 100 == BPS
cpi_data['CPI Commod Less F&E_fd'] = cpi_data['CPI Commod Less F&E_fd']  * 100

cpi_data['CPI Serv Less Energy_fd'] = (np.log(cpi_data['CPI Serv Less Energy']).diff(12))   #   log diff/rate of change one quarter to same quarter of previous year
cpi_data['CPI Serv Less Energy_fd'] = cpi_data['CPI Serv Less Energy_fd']  
cpi_data['CPI Serv Less Energy_fd'] = cpi_data['CPI Serv Less Energy_fd'] - cpi_data['CPI Serv Less Energy_fd'].shift(1)    #  `Rate of Change` and the `first difference` * 100 == BPS
cpi_data['CPI Serv Less Energy_fd'] = cpi_data['CPI Serv Less Energy_fd']  * 100

drop = ['CPI ALL', 'CPI ALL Less F&E', 'CPI Energy', 'Clev FED Median CPI', 'CPI Commod Less F&E', 'CPI Serv Less Energy']
cpi_data = cpi_data.drop(['CPI ALL', 'CPI All Less F&E', 'CPI Energy', 'Clev FED Median CPI', 'CPI Commod Less F&E', 'CPI Serv Less Energy'], axis=1)
# cpi_data = cpi_data.round(2)

fedfunds = pdr.DataReader('FEDFUNDS', data_source, start, end)
fedfunds = pd.DataFrame(fedfunds)

gold_mon = pdr.DataReader('GOLDAMGBD228NLBM', data_source, start, end)
gold_mon = pd.DataFrame(gold_mon)
silver_mon = quandl.get("LBMA/SILVER", authtoken="1mEBe1BeVaAExprr7akA")
silver_mon = pd.DataFrame(silver_mon)
silver_mon = silver_mon.drop(['GBP', 'EURO'], axis=1)
silver_mon.columns = ['Silver']
print(silver_mon)
# gold_mon.rename(columns = {"Col_1":"Mod_col"})
gold_mon.columns = ['Gold']

gold_silver = pd.merge(silver_mon, gold_mon, left_index=True, right_index=True)
gold_silver['gold/silver'] = gold_silver['Gold'] / gold_silver['Silver']


def roc4(df):
    df1 = df.copy()
    df1 = df1.diff(4) 
    df1 = df1 - (df1.shift(1))
    # df1 = df1 * 100
    return df1


# gold_silver['GS_roc'] = roc4(gold_silver['gold/silver'])
# gold_silver['gold_roc'] = roc4(gold_silver['Gold']) 
# gold_silver['silver_roc'] = roc4(gold_silver['Silver']) 

# gold_silver['g/s_roc'] = gold_silver['gold_roc'] / gold_silver['silver_roc']


# gs_dfs = [gold_silver, gold_mon, silver_mon]
# goldsilver_df = pd.concat(gs_dfs, join='outer', axis=1).dropna()

# gold_mon['roc'] = (np.log(gold_mon).diff(12))   #  log diff/rate of change one quarter to same quarter of previous year
# gold_mon['roc'] = gold_mon['roc'] * 100  
# print(gold_mon)
# gold_mon['rod_fd'] = gold_mon - gold_mon.shift(1)


# Pulling this from mom_data.py 
# Merging these 2 modified DataFrames
ism_lagged18 = pd.DataFrame(df_mom['ISM_lagged18'])
core_inv = pd.DataFrame(df_mom['Core_pct_yoy_INV'])
ism_core = pd.merge(ism_lagged18, core_inv, left_index=True, right_index=True)
gold_ism_core = pd.merge(ism_core, gold_silver, left_index=True, right_index=True)
factors_4 = pd.merge(gold_ism_core, fedfunds, left_index=True, right_index=True)
#  Merging ism_core_df with cpi_data DataFrame in order to build my inflation model
# factors_6 = pd.merge(factors_4, fedfunds, left_index=True, right_index=True)

# Pulling data from Quandl API 
# quandl.ApiConfig.api_key='1mEBe1BeVaAExprr7akA'
# df_ism = pd.read_csv('https://www.quandl.com/api/v3/datasets/ISM/MAN_PMI.csv?api_key=1mEBe1BeVaAExprr7akA', index_col=['Date'])
# df_ism = df_ism.iloc[::-1]


copper = pdr.DataReader('WPUSI019011', data_source, start, end)
copper.columns = ['Copper/Prod']
iron_steel = pdr.DataReader('WPU101', data_source, start, end)
iron_steel.columns = ['Iron/Steel']
chemical_man = pdr.DataReader('PCU325325', data_source, start, end)
chemical_man.columns = ['ChemMan']
con_mach_eq = pdr.DataReader('WPS112', data_source, start, end)
con_mach_eq.columns = ['ConMachEq']


dfs = [copper, iron_steel, chemical_man, con_mach_eq]
nan_value =  0
commodities = pd.concat(dfs, join='outer', axis=1).dropna()    #   fillna(nan_value)
commodities_new = commodities.pct_change(12)
commodities_new.columns = ['Copper/Prod_yoy%', 'Iron/Steel_yoy%', 'ChemMan_yoy%', 'ConMachEq_yoy%']
# df['HeadCPI_roc_q2q'] = (np.log(df['CPI']).diff(4))   #  log diff/rate of change one quarter to same quarter of previous year
# df['HeadCPI_roc_q2q'] = df['HeadCPI_roc_q2q'] * 100  
# df['HeadCPI_roc_q2q'] = (df['HeadCPI_roc_q2q']) - (df['HeadCPI_roc_q2q'].shift(1))    #  `Rate of Change` and the `first difference` * 100 == BPS
# df['HeadCPI_roc_q2q'] = df['HeadCPI_roc_q2q']  * 100



commodities['Copper/Prod_roc'] = roc4(commodities['Copper/Prod'])
commodities['Iron/Steel_roc'] = roc4(commodities['Iron/Steel'])
commodities['ChemMan_roc'] = roc4(commodities['ChemMan'])
commodities['ConMachEq_roc'] = roc4(commodities['ConMachEq'])


fin_dfs = [commodities, commodities_new]
tot_commodity = pd.concat(fin_dfs, join='outer', axis=1).dropna()
tot_commodity = tot_commodity.round(4)



metal_factors4 = [tot_commodity, factors_4]
factors = pd.concat(metal_factors4, join='outer', axis=1)


factors = factors.iloc[37:]
factors = (factors.ffill()+factors.bfill())/2
factors = factors.bfill().ffill()
# factors = factors.dropna()
# factors=factors.fillna(factors.mean())
factors = factors.round(3)

factors_inflation = [factors, cpi_data]
factors_cpi = pd.concat(factors_inflation, join='outer', axis=1)
factors_cpi = factors_cpi.dropna()



if __name__ == "__main__":

    # print(cpi_data.head(10))
    # print(cpi_data.tail())
    # print(cpi_data.shape)
    # print(cpi_data.isnull().sum())
    print(factors_cpi.head())
    print(factors_cpi.tail())
    print(factors_cpi.shape)
    print(factors_cpi.columns)

    # print(df.isnull().sum())

    # print(factors.isnull().sum())
    # print(factors.head())
    # print(factors.tail())
    # print(factors.shape)
    # print(factors.columns)

    # print(df_mom.shape)