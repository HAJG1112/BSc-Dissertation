import numpy as np
import pandas as pd
from statsmodels.tsa.api import VAR


def data():
    df = pd.read_excel(r'C:\Users\justi\Documents\DataMatrixDiss.xlsx',sheet_name='matrix', header=0)
    df = pd.DataFrame(df)
   # df['date'] = pd.to_datetime(df.Date_Time, format='%d/%m/%Y %H.%M.%S')
   # df = df.drop(['date'], axis=1)
   # df = df.Date_Time
    return(df)

def get_data(X):
    for i in range(1,20):
        columns = X.iloc[:,:i]
    return (columns)

print(get_data(data()))

