from mom_data import *


df = df_qoq

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


