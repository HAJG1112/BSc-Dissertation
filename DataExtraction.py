import scipy as sp
import numpy as np
import pandas as pd
from pandas import ExcelWriter
from statsmodels.tsa.stattools import coint, adfuller
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression

def data():
    df = pd.read_excel(r'C:\Users\justi\Documents\DataMatrixDiss.xlsx',sheet_name='matrix', header=0)
    df = pd.DataFrame(df)
   # df['date'] = pd.to_datetime(df.Date_Time, format='%d/%m/%Y %H.%M.%S')
   # df = df.drop(['date'], axis=1)
   # df = df.Date_Time
    return(df)

def check_for_stationarity(X, cutoff=0.01):
    # H_0 in adfuller is unit root exists (non-stationary)
    # We must observe significant p-value to convince ourselves that the series is stationary
    pvalue = adfuller(X)[1]
    if pvalue < cutoff:
        print ('p-value = ' + str(pvalue) + ' The series ' + X.name)# +' is likely stationary.')

        #return True

    else:
        print ('p-value = ' + str(pvalue) + ' The series ' + X.name)#+' is likely non-stationary.'
        #return False
    return


#for loop for stationarity of columns
def get_stationarity(X):
    for i in range(1,24):
        print(check_for_stationarity(X.iloc[:,i]))


def difference(X):
    X = X.diff(periods=1,axis=0)
    return X

###Question:How can i parse the column data and its shifted component through the OLS model?

def dat1(X):
        mean = X.mean(axis=0)
        sigma = np.std(X,axis=0)
        min = (X.min(axis=0))
        max = (X.max(axis=0))
        #AR1 = AR1(X)
        X = pd.concat([mean, sigma, min, max], axis=1)
        return (X)

def print_full(x):
    pd.set_option('display.max_rows', len(x))
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 2000)
    pd.set_option('display.float_format', '{:20,.2f}'.format)
    pd.set_option('display.max_colwidth', -1)
    print(x)
    pd.reset_option('display.max_rows')
    pd.reset_option('display.max_columns')
    pd.reset_option('display.width')
    pd.reset_option('display.float_format')
    pd.reset_option('display.max_colwidth')


X = data()
X1  = difference(data()).drop([0])
mat = pd.concat([X,X1],axis=1)
ADF = get_stationarity(X)


df1 = (dat1(data()))   #parse data() into dat1()
df2 = (dat1(difference(data())))  #parse data() into difference function, then these values parse through dat1

print(ADF)
print (df1)


#writer = pd.ExcelWriter(r"C:\Users\justi\Documents\Neat.xlsx")
#ADF.to_excel(writer, sheet_name='ADF')

#writer.save()
#writer.close()
#use for VAR section
#https://www.slideshare.net/wesm/scipy-2011-time-series-analysis-in-python