import pandas as pd
import numpy as np 
from pandas import DataFrame as df
import logging


#linear regression class using the gradient descent.  
class Linear_Regression_gradient_descent:

    def __init__(self,inputs,outputs,learning_rate=0.01,epochs=1000,logs=False,log_file='logger.log'): #intialization of the Gradient Descent where x is the input parameters and y is the output parameter, inputs and outputs need to be passed as the pandas DataFrames

        self.logs=logs
        self.log_file=log_file
        if self.logs==True:
            logging.basicConfig(filename=self.log_file,format = '%(asctime)s %(levelname)-10s %(name)s %(message)s',level=logging.DEBUG)
            self.log=logging.getLogger()

        try:
            self.inputs=inputs.values  #converts the input dataframes into the Numpy data 
            self.outputs=outputs.values 
        except:
            self.log.exception("The Input and Output needs to be Pandas Data Frames")
            

        self.learning_rate=learning_rate 
        self.epochs=epochs

        if type(epochs) is not int:
            self.log.error("EPOCH VALUE NEEDS TO BE INTEGER")
            
        self.cord=np.ones(self.inputs[0].size)  #creates the dummy values for the coordinates and intercept as 1
        self.incpt=1
        self.cord_nu=np.ones(self.inputs[0].size)
        self.incpt_nu=1
        

    def calc_expval(self,inp): #function that calculates the expected value given the values for the inputs.
        out=0
        for i in range(inp.size):
           out=out+inp[i]*self.cord[i]
        out=out+self.incpt
        return out


    def calc_gradients(self,grad_cof): #this function calculates the gradient of the coefficients 
        i=0
        dum=0
        for x in self.inputs:
            dum=dum+(self.calc_expval(x)-self.outputs[i])*x[grad_cof]
            i=i+1
        dum=dum*2/(self.inputs.shape[0])
        return dum
    

    def calc_gradients_incpt(self):#this function calculates the gradient of the intercept 
        i=0
        dum=0
        for x in self.inputs:
            dum=dum+(self.calc_expval(x)-self.outputs[i])
            i=i+1
        dum=dum*2/(self.inputs.shape[0])
        return dum

    def calculate_mean(self): #this function calculates the mean of the outputs dataset values. 
        sum=0
        for x in self.outputs:
            sum=sum+x
        sum=sum/self.inputs.shape[0]
        return sum


    def calculate_rsqu(self):#this function is for the calculation of R squared values 
        num=0
        den=0
        mean=self.calculate_mean()
        for x in self.inputs:
            num=num+((self.calc_expval(x)-mean)*(self.calc_expval(x)-mean))
        for a in self.outputs:
            den=den+((a-mean)*(a-mean))
        return num/den
        
    def calculate_stder(self): #this function is for the calculation of the standard error 
        num=0
        mean=self.calculate_mean()
        for x in self.inputs:
            num=num+((self.calc_expval(x)-mean)*(self.calc_expval(x)-mean))
        return (num/self.inputs.shape[0])**0.5
        
    def calculate_cost(self): #function to calculate the quadratic cost value
        i=0
        su=0
        for x in self.inputs:
            su=su+(self.calc_expval(x)-self.outputs[i])*(self.calc_expval(x)-self.outputs[i])
        su=su/self.inputs.shape[0]
        return su

    
    def run_grad(self): #this function runs the Gradient descent on the given inputs and outputs
        try:
            for i in range(self.epochs):
                self.incpt_nu=self.incpt-self.learning_rate*self.calc_gradients_incpt()
                for a in range(self.inputs[0].size):
                    self.cord_nu[a]=self.cord[a]-self.learning_rate*self.calc_gradients(a)
                self.incpt=self.incpt_nu
                self.cord=self.cord_nu
                if self.logs==True:
                   self.log.info("EPOCH "+str(i) + "   r^2-->"+str(self.calculate_rsqu())+"   S-->"+str(self.calculate_stder())+"   Intercept-->"+str(self.incpt)+"   Coefficients-->"+str(self.cord)+"   Quad Cost-->"+str(self.calculate_cost()))
            return 1
        
        except:
            if self.logs==True:
                self.log.exception("The Gradient Descent Didn't execute")
            return 0





