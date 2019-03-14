import pandas as pd
import numpy as np
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.tsa.stattools import coint, adfuller


def data():
    df = pd.read_excel(r'C:\Users\justi\Documents\DataMatrixDiss.xlsx',sheet_name='matrix', header=0)\

    df = pd.DataFrame(df)
    return(df)

def dat1(X):
        mean = X.mean(axis=0)
        sigma = np.std(X, axis=0)
        min = (X.min(axis=0))
        max = (X.max(axis=0))
        # AR1 = AR1(X)
        X = pd.concat([mean, sigma, min, max], axis=1)
        return (X)

def get_data(X):
    for i in range(1,20):

        columns = X.iloc[:,:i]
    return (columns)


def check_for_stationarity(X, cutoff=0.01):
    # H_0 in adfuller is unit root exists (non-stationary)
    # We must observe significant p-value to convince ourselves that the series is stationary
    pvalue = adfuller(X,maxlag=20,autolag = 't-stat' ,regression='ct')[1]
    ADF = adfuller(X,maxlag=20, autolag = 't-stat', regression='ct')[0]
    lag_n = adfuller(X,maxlag=20, autolag = 't-stat', regression='ct')[2]
    if pvalue < cutoff:
        print ('p-value = ' + str(pvalue) + ' The series ' + X.name +' is likely stationary.'+'ADF =' + str(ADF) + ' number of lags = '+str(lag_n))

    else:
        print ('p-value = ' + str(pvalue) + ' The series ' + X.name+' is likely non-stationary.'+'ADF =' + str(ADF)+' number of lags = '+str(lag_n))

    return

def get_stationarity_IG(X):
    for i in range(1,16):
        print(check_for_stationarity(X.iloc[:,i]))

def get_stationarity_HY(X):
    for i in range(16,19):
        print(check_for_stationarity(X.iloc[:,i]))

def VAR1():
    mdata=X[[]]
X=get_data(data())
X1 = data()
print(get_stationarity_IG(X))

