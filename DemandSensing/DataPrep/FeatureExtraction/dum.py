from featext import FeatureExtration as fx 

import numpy as np


import pandas as pd
from pandas import DataFrame as df


stock_market=pd.read_csv('sample.csv')





train_data= df(stock_market,columns=[ 'Interest_Rate' ,'Unemployment_Rate' ,'Stock_Index_Price' ])
#The Data is converted to the pandas datafrmae object

#X = train_data[['Interest_Rate','Unemployment_Rate']]
#X = train_data[['Interest_Rate']]
Y = train_data['Stock_Index_Price'] 


print Y



obj=fx(Y)
print obj.rolling_average()