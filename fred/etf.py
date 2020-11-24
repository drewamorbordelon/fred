import pandas as pd
import numpy as np
import datetime
import pandas_datareader as pdr
import quandl
import csv
import yfinance as yf
import investpy 


con_df = investpy.get_etf_historical_data(
    etf='Consumer Discretionary Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
con_df = con_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(con_df.tail())

fin_df = investpy.get_etf_historical_data(
    etf='Financial Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
fin_df = fin_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(fin_df.tail())

health_df = investpy.get_etf_historical_data(
    etf='Health Care Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
health_df = health_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(health_df.tail())

tech_df = investpy.get_etf_historical_data(
    etf='Technology Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
tech_df = tech_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(tech_df.tail())

consumerstaples_df = investpy.get_etf_historical_data(
    etf='Consumer Staples Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
consumerstaples_df = consumerstaples_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(consumerstaples_df.tail())

industrial_df = investpy.get_etf_historical_data(
    etf='Industrial Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
industrial_df = industrial_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(industrial_df.tail())

material_df = investpy.get_etf_historical_data(
    etf='Materials Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
material_df = material_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(material_df.tail())

energy_df = investpy.get_etf_historical_data(
    etf='Energy Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
energy_df = energy_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(energy_df.tail())

utilities_df = investpy.get_etf_historical_data(
    etf='Utilities Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
utilities_df = utilities_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(utilities_df.tail())

realestate_df = investpy.get_etf_historical_data(
    etf='Real Estate Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
realestate_df = realestate_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(realestate_df.tail())

commun_df = investpy.get_etf_historical_data(
    etf='Communication Services Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
commun_df = commun_df.drop(['Open', 'High', 'Low', 'Volume', 'Currency', 'Exchange'], axis=1) 
# print(commun_df.tail())

sp_df = pdr.get_data_yahoo(
    "SPY",
    start='2012-01-01', 
    end='2030-12-01')
sp_df = sp_df.drop(['Open', 'High', 'Low', 'Volume', 'Adj Close'], axis=1)

#  Merging all the dataframes
etf_df = pd.merge(con_df, fin_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, health_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, tech_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, consumerstaples_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, industrial_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, material_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, energy_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, utilities_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, realestate_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, commun_df, left_index=True, right_index=True)
etf_df = pd.merge(etf_df, sp_df, left_index=True, right_index=True)

etf_df.columns = ['ConsumerDiscretionary(XLY)', 'Financial(XLF)', 'Health(XLV)','Tech(XLK)', 'ConsumerStaples(XLP)', 'Industrial(XLI)', 'Material(XLB)', 'Energy(XLE)', 'Utilities(XLU)', 'RealEstate(XLRE)', 'Communications(XLC)', 'SPY']
# print(etf_df.head())
# print(etf_df.tail())

etf_pct_chg = (etf_df - etf_df.shift(1))/etf_df.shift(1) * 100
etf_pct_chg = etf_pct_chg.tail(1)
# print(etf_pct_chg.tail(1))

etf_pct_chg_m = (etf_df - etf_df.shift(21))/etf_df.shift(21) * 100
etf_pct_chg_m = etf_pct_chg_m.tail(1)
# print(etf_pct_chg_m.tail(1))

etf_pct_chg_q = (etf_df - etf_df.shift(63))/etf_df.shift(63) * 100
etf_pct_chg_q = etf_pct_chg_q.tail(1)
# print(etf_pct_chg_q.tail(1))

etf_pct_chg_y = (etf_df - etf_df.shift(252))/etf_df.shift(252) * 100
etf_pct_chg_y = etf_pct_chg_y.tail(1)
# print(etf_pct_chg_y.tail(1))


frames = [etf_pct_chg, etf_pct_chg_m, etf_pct_chg_q, etf_pct_chg_y]

etf_pctchanges = pd.concat(frames)
etf_current_price = etf_df.tail(1)

frame1 = [etf_current_price, etf_pctchanges]
etf_table = pd.concat(frame1)
etf_table.index = ['Price', 'D% Chg', 'M% Chg', 'Q% Chg', 'YTD% Chg']


etf_tidy = etf_table.T
etf_tidy = etf_tidy.round(2)
print(etf_tidy)
