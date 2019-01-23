import pandas as pd
from pandas import DataFrame as df 

class read_file:
    def __init__(self,file_name,file_type):
        self.fil=file_name
        self.typ=file_type

    def read_file(self):
        try:
            if self.typ=='CSV':
                #print "in hereeee",self.fil
                fyil=pd.read_csv(self.fil)
                return fyil
        except:
            print "ERROR: File Not Present"
        #elif file_type='EXCEL':
         #   return None
