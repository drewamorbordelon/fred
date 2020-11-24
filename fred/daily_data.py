import pandas as pd
import numpy as np
import datetime
import pandas_datareader as pdr
import quandl
import csv
import yfinance as yf
import investpy 
# from mom_data import data_source, start, end
# from .env import quandl_API


# Pulling data from Quandl API 
# quandl.ApiConfig.api_key='1mEBe1BeVaAExprr7akA'
# df_ism = pd.read_csv('https://www.quandl.com/api/v3/datasets/ISM/MAN_PMI.csv?api_key=1mEBe1BeVaAExprr7akA', index_col=['Date'])
# df_ism = df_ism.iloc[::-1]

data_source = 'fred'
starttime = datetime.datetime (2000, 1, 1)
endtime = datetime.datetime (2030, 12, 1)

data_source = 'fred'
start = datetime.datetime (2000, 1, 1)     
end = datetime.datetime (2030, 12, 1)


# remove_columns = ['Open', 'High', 'Low', 'Currency', 'Exchange']

# VIX
vix_df = investpy.get_index_historical_data(
    index= 'S&P 500 VIX',
    from_date='01/01/2012', 
    to_date='12/01/2030', 
    country='United States')
vix_df = vix_df.drop(['Open', 'High', 'Low', 'Currency', 'Volume'], axis=1)
# print(vix_df.tail())



# S&P 500
sp_df = pdr.get_data_yahoo(
    "SPY",
    start='2012-01-01', 
    end='2030-12-01')
sp_df = sp_df.drop(['Open', 'High', 'Low', 'Adj Close'], axis=1)
# print(sp_df.head())
# print(sp_df.tail())


#  DXY
dxy_df = pdr.get_data_yahoo(
    "DX-Y.NYB", 
    start="2012-01-01", 
    end="2030-12-01")
df = dxy_df.drop(['High', 'Low', 'Volume', 'Adj Close'], axis=1)
# print(dxy_df.tail())

#  EUR/USD
eur_df = investpy.get_currency_cross_historical_data(
    currency_cross='EUR/USD', 
    from_date='01/01/2012',
    to_date='12/01/2030')
eur_df = eur_df.drop(['High', 'Low', 'Currency'], axis=1) 
# print(eur_df.tail())

#  Gold/Usd
gold_df = pdr.DataReader(
    'GOLDAMGBD228NLBM', 
    data_source, 
    starttime, 
    endtime)
# print(gold_df.tail())

#  Silver/Usd
silver_df = pdr.DataReader(
    'SLVPRUSD', 
    data_source, 
    starttime, 
    endtime)
# print(silver_df.tail())

#  Bitcoin/Usd and BTC_Volume
bitcoin_df = investpy.get_crypto_historical_data(
    crypto='bitcoin', 
    from_date='01/01/2012',
    to_date='12/01/2030')
bitcoin_df = bitcoin_df.drop(['Open', 'High', 'Low', 'Currency'], axis=1)
# print(bitcoin_df.tail())

lite_df = investpy.get_crypto_historical_data(
    crypto='litecoin', 
    from_date='01/01/2012',
    to_date='12/01/2030')
lite_df = lite_df.drop(['Open', 'High', 'Low', 'Currency'], axis=1)
lite_df.columns = ['lite', 'Volume']

lite_df['lite_mean'] = lite_df['lite'].rolling(21).mean()
lite_df['lite_std'] = lite_df['lite'].rolling(21).std()

lite_df['lite_low'] = lite_df['lite_mean'] - lite_df['lite_std'] * 2

lite_df['lite_up']  = lite_df['lite_mean'] + lite_df['lite_std'] * 2
print(lite_df.tail())

con_df = investpy.get_etf_historical_data(
    etf='Consumer Discretionary Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
con_df = con_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(con_df.tail())

fin_df = investpy.get_etf_historical_data(
    etf='Financial Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
fin_df = fin_df.drop(['High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(fin_df.tail())

health_df = investpy.get_etf_historical_data(
    etf='Health Care Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# health_df = health_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(health_df.tail())

tech_df = investpy.get_etf_historical_data(
    etf='Technology Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# tech_df = tech_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(tech_df.tail())

consumerstaples_df = investpy.get_etf_historical_data(
    etf='Consumer Staples Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# consumerstaples_df = consumerstaples_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(consumerstaples_df.tail())

industrial_df = investpy.get_etf_historical_data(
    etf='Industrial Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# industrial_df = industrial_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(industrial_df.tail())

material_df = investpy.get_etf_historical_data(
    etf='Materials Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# material_df = material_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(material_df.tail())

energy_df = investpy.get_etf_historical_data(
    etf='Energy Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# energy_df = energy_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(energy_df.tail())

utilities_df = investpy.get_etf_historical_data(
    etf='Utilities Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# utilities_df = utilities_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(utilities_df.tail())

realestate_df = investpy.get_etf_historical_data(
    etf='Real Estate Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
# realestate_df = realestate_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(realestate_df.tail())

commun_df = investpy.get_etf_historical_data(
    etf='Communication Services Select Sector SPDR',
    country='United States',
    from_date='01/01/2012',
    to_date='12/01/2030')
commun_df = commun_df.drop(['Open', 'High', 'Low', 'Currency', 'Exchange'], axis=1) 
# print(commun_df.tail())




#  Merging all the dataframes
# df = pd.merge(df, eur_df, left_index=True, right_index=True)
df = pd.merge(eur_df, gold_df, left_index=True, right_index=True)
df = pd.merge(df, silver_df, left_index=True, right_index=True)
df = pd.merge(df, bitcoin_df, left_index=True, right_index=True)
df = pd.merge(df, vix_df, left_index=True, right_index=True)
df = pd.merge(df, sp_df, left_index=True, right_index=True)




#  Renaming all columns 
df.columns = ['DXY', 'Eur/Usd', 'Gold/Usd', 'Silver/Usd', 'Bitcoin', 'BTC_Volume', 'VIX', 'SPY', 'SPY_Volume']

# df = df.drop(['BTC_Volume'], axis=1)
# print(df.columns)

# df['BTC_roc7'] = np.log(df['Bitcoin']/df['Bitcoin'].shift(7))
# df['BTC_roc15'] = np.log(df['Bitcoin']/df['Bitcoin'].shift(15))
# df['BTC_roc30'] = np.log(df['Bitcoin']/df['Bitcoin'].shift(30))
# df['BTC_roc90'] = np.log(df['Bitcoin']/df['Bitcoin'].shift(90))

# df['Gold_corr1'] = df['Gold/Usd'].corr(df['DXY'])

# df['Gold_corr7'] = df['Gold/Usd'].rolling(7).corr(df['DXY']) 
# df['Gold_corr15'] = df['Gold/Usd'].rolling(15).corr(df['DXY'])
# df['Gold_corr30'] = df['Gold/Usd'].rolling(30).corr(df['DXY'])

# df['Gold_corr90'] = df['Gold/Usd'].rolling(90).corr(df['DXY'])


#  VIX Baskets
def vix_basket(df):
    if df['VIX'] >= 30:
        return 'Not Investable'
    elif 15 <= df['VIX'] < 30:
        return 'Trade'
    else:
        return 'Invest'

df['VIX_basket'] = df.apply(lambda df: vix_basket(df), axis=1)

df['SPY_pct_chg'] = df['SPY'].pct_change(5)
df['SPY_Vol_chg'] = df['SPY_Volume'].pct_change(5)

# a standard deviation range of 2 (95%)
df['VIX_mean'] = df['VIX'].rolling(21).mean()
df['VIX_std'] = df['VIX'].rolling(21).std()
df['VIX_lowband'] = df['VIX_mean'] - df['VIX_std'] * 1.5
df['VIX_upband']  = df['VIX_mean'] + df['VIX_std'] * 1.5


# a standard deviation range of 2 (95%)
df['SPY_mean'] = df['SPY'].rolling(21).mean()
df['SPY_std'] = df['SPY'].rolling(21).std()
df['SPY_low'] = df['SPY_mean'] - df['SPY_std'] * 2
df['SPY_up']  = df['SPY_mean'] + df['SPY_std'] * 2


# a standard deviation range 2 (95%)
df['BTC_mean'] = df['Bitcoin'].rolling(21).mean()
df['BTC_std'] = df['Bitcoin'].rolling(21).std()

df['BTC_low'] = df['BTC_mean'] - df['BTC_std'] * 2
# df['BTC_lowband'] = (df['BTC_lowband'].shift() + df['BTC_lowband'].shift(2) + df['BTC_lowband'].shift(3)) / 3
df['BTC_up']  = df['BTC_mean'] + df['BTC_std'] * 2
# df['BTC_upband'] = (df['BTC_upband'].shift() + df['BTC_upband'].shift(2) + df['BTC_upband'].shift(3)) / 3
btc = df[['Bitcoin', 'BTC_mean', 'BTC_low', 'BTC_up', 'BTC_std']].copy()

# a standard deviation range of 2 (95%)
df['Gold_mean'] = df['Gold/Usd'].rolling(21).mean()
df['Gold_std'] = df['Gold/Usd'].rolling(21).std()

df['Gold_low'] = df['Gold_mean'] - df['Gold_std'] * 2

df['Gold_up']  = df['Gold_mean'] + df['Gold_std'] * 2
gold = df[['Gold/Usd', 'Gold_mean', 'Gold_low', 'Gold_up', 'Gold_std']].copy()


# a standard deviation range of 2 (95%)
df['Silver_mean'] = df['Silver/Usd'].rolling(21).mean()
df['Silver_std'] = df['Silver/Usd'].rolling(21).std()

df['Silver_low'] = df['Silver_mean'] - df['Silver_std'] * 2

df['Silver_up']  = df['Silver_mean'] + df['Silver_std'] * 2

silver = df[['Silver/Usd', 'Silver_mean', 'Silver_low', 'Silver_up', 'Silver_std']].copy()

df = df.drop(
    ['DXY', 'Eur/Usd', 'Gold/Usd', 
    'VIX_basket', 'SPY_pct_chg', 'SPY_mean', 
    'SPY_std', 'BTC_mean', 'BTC_Volume', 
    'BTC_std', 'Gold_mean', 'Gold_std', 
    'VIX_std', 'VIX_mean'], axis=1)

# #  Renaming all columns 
# df.columns = ['DXY', 'Eur/Usd', 'Gold/Usd', 'Bitcoin', 'BTC_Volume', 'VIX', 'SPY', 'SPY_Volume']



# a standard deviation range 2 (95%)
yr_tr = pdr.get_data_yahoo(
    "^TNX", 
    start="2012-01-01", 
    end="2030-12-01")

yr_tr['yr10_mean'] = yr_tr['Close'].rolling(21).mean()
yr_tr['yr10_std'] = yr_tr['Close'].rolling(21).std()

yr_tr['yr10_lowband'] = yr_tr['yr10_mean'] - yr_tr['yr10_std'] * 2.0
yr_tr['yr10_upband']  = yr_tr['yr10_mean'] + yr_tr['yr10_std'] * 2.0

yr_tr = yr_tr.drop(['High', 'Low', 'Open', 'Volume', 'Adj Close'], axis=1)
yr_tr.columns = ['10yr', '10yr_mean', '10yr_std', '10yr_lower', '10yr_upper']
# yr_tr = yr_tr.drop(['10yr_std'], axis=1)
yr_tr = yr_tr.round(2)
print(yr_tr.tail(6))


#  Mergeing dataframes 
df = pd.merge(df, yr_tr, left_index=True, right_index=True)

# #  Renaming all columns 


df = df.drop(['Bitcoin', 'VIX', 'SPY_Volume', '10yr_mean', 'Silver_mean', '10yr'], axis=1)
df = df.round(2)


if __name__ == "__main__":
    print(gold.tail())
    # print(df.shape)
    # print(df.head())
    # print(df.columns)
    # print(df_silver.tail())


    # print(btc.tail(8))
    # print(gold.tail(8))
    # print(silver.tail(8))
    # print(df.tail(8))