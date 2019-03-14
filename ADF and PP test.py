#unit root test for each of the variables being tested on




import numpy as np
import pandas as pd
from pandas import ExcelWriter
from statsmodels.tsa.stattools import coint, adfuller
import statsmodels.api as sm


def data():
    df = pd.read_excel(r'C:\Users\justi\Documents\DataMatrixDiss.xlsx',sheet_name='matrix', header=0)
    df = pd.DataFrame(df)
   # df['date'] = pd.to_datetime(df.Date_Time, format='%d/%m/%Y %H.%M.%S')
   # df = df.drop(['date'], axis=1)
   # df = df.Date_Time
    return(df)

def ADF_test(X):
    for i in range(1,24):
        ADF = sm.tsa.stattools.adfuller(X.iloc[:,i])
    return(ADF)

X = data()
print(ADF_test(X))