"""                                                       
Created on Mon Jan 22 2019
@author: Ishan Dubey                                                                            
"""                                                                                                
  

class Evaluation_param:

     def __init__(self,predictive_model_object):

          self.inputs=predictive_model_object.inputs
          self.outputs=predictive_model_object.outputs
          self.incpt=predictive_model_object.incpt
          self.cord=predictive_model_object.cord


     def calculate_mean(self): #this function calculates the mean of the outputs dataset values. 
          sum=0
          for x in self.outputs:
               sum=sum+x
          sum=sum/self.inputs.shape[0]
          return sum


     def calc_expval(self,inp): #function that calculates the expected value given the values for the inputs.
          out=0
          for i in range(inp.size):
               out=out+inp[i]*self.cord[i]
          out=out+self.incpt
          return out

     def R_squared(self):
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
    
