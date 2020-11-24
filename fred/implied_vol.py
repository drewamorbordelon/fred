from math import sqrt, exp, log, pi
from scipy.stats import norm
import datetime
import numpy as np

#  Option parameters
sigma = 0.15
S = 586.08    # current stock price
K = 585.0   # strike price
r = 0.01   # FED Fund's Rate  .25
t = (datetime.date(2014,10,18) - datetime.date(2014,9,8)).days / 365. / 365.0   # in years
c0 = 1.50   # call price

def d(sigma, S, K, r, t):
    d1 = 1 / (sigma * sqrt(t)) * (log(S/K) + (r + sigma**2/2) * t)
    d2 = d1 - sigma * sqrt(t)
    return d1, d2

def call_price(sigma, S, K, r, t, d1, d2):
    C = norm.cdf(d1) * S - norm.cdf(d2) * K * exp(-r * t)
    return C


# print(d(0.15, S, K, r, t))
# d1, d2 = (d(0.15, S, K, r, t))
# print(call_price(sigma, S, K, r, t, d1, d2))


#  Tolerances
tol = 1e-3
epsilon = 1

count = 0
max_iteration = 1000

vol = 0.50  # initial guess to get things started

while epsilon > tol:
    count += 1
    # print(count)
    if count >= max_iteration:
        print('Breaking on count')
        break;

    orig_vol = vol

    d1, d2 = d(vol, S, K, r, t)
    function_value = call_price(vol, S, K, r, t, d1, d2) - c0

    vega = S * norm.pdf(d1) * sqrt(t)   #  vega == the derivative
    vol = -function_value / vega + vol

    epsilon = abs((vol - orig_vol) / orig_vol)  # epsilon == 

print('sigma = ', vol)
print(count, 'iterations')


# PUTS
def f(x):
    return np.exp(x) - 5 * x

def fddx(x):
    return np.exp(x) - 5





# def find_vol(target_value, call_put, S, K, T, r):
#     MAX_ITERATIONS = 250
#     PRECISION = 1.0e-3

#     sigma = 0.5
#     for i in range(0, MAX_ITERATIONS):
#         price = bs_price(call_put, S, K, T, r, sigma)
#         vega = bs_vega(call_put, S, K, T, r, sigma)

#         price = price
#         diff = target_value - price  # our root

#         print(i, sigma, diff)

#         if (abs(diff) < PRECISION):
#             return sigma
#         sigma = sigma + diff/vega # f(x) / f'(x)

#     # value wasn't found, return best guess so far
#     return sigma


# n = norm.pdf
# N = norm.cdf

# def bs_price(cp_flag,S,K,T,r,v,q=0.0):
#     d1 = (log(S/K)+(r+v*v/2.)*T)/(v*sqrt(T))
#     d2 = d1-v*sqrt(T)
#     if cp_flag == 'c':
#         price = S*exp(-q*T)*N(d1)-K*exp(-r*T)*N(d2)
#     else:
#         price = K*exp(-r*T)*N(-d2)-S*exp(-q*T)*N(-d1)
#     return price

# def bs_vega(cp_flag,S,K,T,r,v,q=0.0):
#     d1 = (log(S/K)+(r+v*v/2.)*T)/(v*sqrt(T))
#     return S * sqrt(T)*n(d1)


# V_market = 17.5
# K = 585
# t = (datetime.date(2014,10,18) - datetime.date(2014,9,8)).days / 365.
# S = 586.08
# r = 0.0002
# c0 = 'c' # call option

# implied_vol = find_vol(V_market, c0, S, K, t, r)

# print('Implied vol: %.2f%%' % (implied_vol * 100))

# print('Market price = %.2f' % V_market)
# print('Model price = %.2f' % bs_price(c0, S, K, t, r, implied_vol))


