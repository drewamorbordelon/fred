from mom_data import *


# df = df_qoq

df_m2_vel = pdr.DataReader('M2V', data_source,start, end)
df_m2_vel = pd.DataFrame(df_m2_vel).fillna(nan_value)
df_gdp = pdr.DataReader('GDPC1', data_source, start, end)
df_gdp = pd.DataFrame(df_gdp).fillna(nan_value)
df_headline_cpi = pdr.DataReader('CPIAUCSL', data_source, start, end)
df_headline_cpi = pd.DataFrame(df_headline_cpi).fillna(nan_value)
df_core_cpi = pdr.DataReader('CPILFESL', data_source, start, end)
df_core_cpi = pd.DataFrame(df_core_cpi).fillna(nan_value)


df = pd.merge(df_gdp, df_headline_cpi, left_index=True, right_index=True)
df = pd.merge(df, df_core_cpi, left_index=True, right_index=True)
df.columns = ['GDP', 'CPI', 'Core_CPI']

df['GDP_roc_q2q'] = (np.log(df['GDP']).diff(4))   #  log diff/rate of change one quarter to same quarter of previous year
df['GDP_roc_q2q'] = df['GDP_roc_q2q'] * 100  
df['GDP_roc_q2q'] = (df['GDP_roc_q2q']) - (df['GDP_roc_q2q'].shift(1))    #  `Rate of Change` and the `first difference` * 100 == BPS
df['GDP_roc_q2q'] = df['GDP_roc_q2q'] * 100

# df['CoreCPI_roc_q2q'] = (np.log(df['Core_CPI']).diff(4))   #  log diff/rate of change one quarter to same quarter of previous year
# df['CoreCPI_roc_q2q'] = df['CoreCPI_roc_q2q'] * 100  
# df['CoreCPI_roc_q2q'] = (df['CoreCPI_roc_q2q'])  - (df['CoreCPI_roc_q2q'].shift(1))  #  `Rate of Change` and the `first difference` * 100 == BPS
# df['CoreCPI_roc_q2q'] = df['CoreCPI_roc_q2q']  * 100


df['HeadCPI_roc_q2q'] = (np.log(df['CPI']).diff(4))   #  log diff/rate of change one quarter to same quarter of previous year
df['HeadCPI_roc_q2q'] = df['HeadCPI_roc_q2q'] * 100  
df['HeadCPI_roc_q2q'] = (df['HeadCPI_roc_q2q']) - (df['HeadCPI_roc_q2q'].shift(1))    #  `Rate of Change` and the `first difference` * 100 == BPS
df['HeadCPI_roc_q2q'] = df['HeadCPI_roc_q2q']  * 100


conditions = [
    (df['GDP_roc_q2q'] >= 0.000) & (df['HeadCPI_roc_q2q'] < 0.000),
    (df['GDP_roc_q2q'] >= 0.000) & (df['HeadCPI_roc_q2q'] > 0.000),
    (df['GDP_roc_q2q'] <= 0.000) & (df['HeadCPI_roc_q2q'] > 0.000),
    (df['GDP_roc_q2q'] <= 0.000) & (df['HeadCPI_roc_q2q'] < 0.000)
    ]

values = ['Regime 1', 'Regime 2', 'Regime 3', 'Regime 4']
df['Regimes'] = np.select(conditions, values)

df = df.dropna()
if __name__ =="__main__":
    # print(df.tail(4))
    print(df.shape)
    print(df.head())
    


