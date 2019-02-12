"""                                                                                                
Created on Mon Jan 22 2019                                                                         
@author: Ishan Dubey                                                                              
"""          

import numpy as np
import pandas as pd
import tsfresh as ts

class FeatureExtration:
    
    def __init__(self,table):
        #the given from which the features needs to be extracted
        self.tables=table.values
        self.outputs=np.zeros(self.tables.size,dtype=np.float32)
    def rolling_average(self,window=3): 
        #code for the rolling average of the given column and retrun the output table with same no ofrows
        #self.window=window
        suma=0
        for x in range(self.tables.size):
            #try:
            if x >= (window-1):
                for y in range(window):
                    suma=suma+float(self.tables[x-y])
                suma=(suma/window)
                self.outputs[x]=float(suma)
                #print "the value of x is ",x
                suma=0
            #except:
            else:
                #print "executed"
                
                self.outputs[x]=float(self.tables[x])
                
        #values=np.zeros(self.outputs.size,dtype=np.float)
        col=pd.DataFrame({'col':self.outputs})
        return col
    def min_max_norm(self):
        #code for the normalization of the given column and return the output table with the same no of rows
        mina=np.amin(self.tables)
        #print "the man is ", mina
        maxa=np.amax(self.tables)
        #print "the max is ",maxa
        
        for x in range(self.tables.size):
            self.outputs[x]=float(self.tables[x]-mina)/(maxa-mina)
            #print "for the intital is ",self.tables[x]
            #print mina
            #print maxa
        col=pd.DataFrame({'col':self.outputs})
        return col
        
    def log_transform(self):
        
        for x in range(self.tables.size):
            self.outputs[x]=math.log10(self.tables[x])
        col=pd.DataFrame({'col':self.outputs})
        return col


    def calc_mean(self):
        mean=0
        for x in range(self.tables.size):
            mean=mean+self.tables[x]
        mean=mean/self.tables.size
        return mean
    def calc_deviation(self):
        mean=calc_mean()
        dev=0
        for x in range(self.tables.size):
            dev=dev+((self.tables[x]-mean)*(self.tables[x]-mean))
        dev=dev/self.tables.size
        dev=(dev)**0.5
        return dev
    
    def standaradization(self):

        dev=calc_deviation()
        mean=calc_mean()
        for x in range(self.tables.size):
            self.outputs[x]=(self.tables[x]-mean)/dev

        col=pd.DataFrame({'col':self.outputs})
        return col

    def lag_features(self,lag_len):

        for x in range(self.tables.size):
            self.outputs[x+lag_len]=self.tables[x]

        
        col=pd.DataFrame({'col':self.outputs})
        return col
