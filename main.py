#from Regression import Linear_Regression_gradient_descent


from DemandSensing.PredictiveModels.LinearModels.Regression import Linear_Regression_gradient_descent
from DemandSensing.DataPrep.FeatureExtraction.featext import FeatureExtration as fx
from DemandSensing.ModelEvaluation.evaluation import Evaluation_param as ep
from DemandSensing.DataIngestion.readCSV import read_file as rf

import sys 
import pandas as pd
from pandas import DataFrame as df


#stock_market=pd.read_csv( 'sample_data.csv') #the example predicts the stock prices for based given dependent varibales like Unemployment rate and Interest Rates

stock_market=rf(sys.argv[1],sys.argv[2]).read_file()

train_data= df(stock_market,columns=[ 'Interest_Rate' ,'Unemployment_Rate' ,'Stock_Index_Price' ])
#The Data is converted to the pandas datafrmae object

X = train_data[['Interest_Rate','Unemployment_Rate']]
#X = train_data[['Interest_Rate']]
Y = train_data['Stock_Index_Price'] 

#print X
#print Y


reg_obj=Linear_Regression_gradient_descent(X,Y,learning_rate=0.03,epochs=1000,logs=True)

print "the type is",type(reg_obj)

print "the return val is",reg_obj.run_grad()
print "the intercept are ",reg_obj.incpt
print "cordinates are ",reg_obj.cord
eval_param=ep(reg_obj)

print "the r squared value is ", eval_param.R_squared()
print "the standard error is ",eval_param.calculate_stder()o

obfx=fx(Y)
ot=obfx.min_max_norm()
#print ot
reg_obj_1=Linear_Regression_gradient_descent(X,ot,learning_rate=0.03,epochs=1000,logs=True)
print "the return val is after Norm is",reg_obj_1.run_grad()
print "the intercept after norm are ",reg_obj_1.incpt
print "cordinates after norm are ",reg_obj_1.cord
 
eval_param_1=ep(reg_obj_1)

print "the r squared value after norm is ", eval_param_1.R_squared()
print "the standard error after norm is ",eval_param_1.calculate_stder()




#print reg_obj.cord, reg_obj.incpt
#import dummy

#dummy.dum(reg_obj)

