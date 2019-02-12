from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
from statsmodels.tsa.ar_model import AR

class Time_Based_Models:

    def __init__(self,inputs):
        self.inputs=inputs

    def arima(self):
        model=ARIMA(self.inputs,order=(5,1,0))
        model_fit=model.fit(disp=0)

        return model_fit.summary()

    def arma(self):
        model = sm.tsa.ARMA(self.inputs, (2,0)).fit(disp=False)
        return model.params

    def ar(self):
         model = AR(self.inputs)
         model_fit = model.fit()
         return model_fit.params
