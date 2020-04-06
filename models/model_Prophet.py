import numpy as np
import pandas as pd
import time

from fbprophet import Prophet
from BHT_ARIMA.util.utility import get_acc, nrmse

def run_Prophet(data, param):


      testsize = param['testsize']
      start = '2017-3'
      freq = 'D'


      T = data.shape[-1]
      T_test = int((T * testsize) // 1)
      result_full = np.zeros([data.shape[0], T_test])

      total_time = 0
      n_round = 0

      time_st = pd.period_range(start=start, periods=T, freq=freq).to_timestamp()


      for i in range(T_test):

        y = data[..., i:T-T_test+i+1].copy()
        n_round += 1
        ds = time_st[i:T-T_test+i+1].copy()
        

        start = time.time()

        for j in range(y.shape[0]):


          DF_ts = pd.DataFrame()
          DF_ts['ds'] = ds.copy()
          DF_ts['y'] = y[j].copy()



          model = Prophet()
          model.fit(DF_ts[i:T-T_test+i])

          result = model.predict(DF_ts[['ds']].iloc[[-1]])['yhat'][0]
          result_full[j, i] = result

        end = time.time()
        total_time = total_time + (end - start)

      true_value = data[..., -T_test:]


      stat = {}
      stat['acc'] = get_acc(result_full, true_value)
      stat['nrmse'] = nrmse(result_full, true_value)
      stat['ave_time'] = total_time/n_round


      return(stat)
 



