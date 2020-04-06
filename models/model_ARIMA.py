

import numpy as np
import time

from pmdarima.arima import ARIMA
from BHT_ARIMA.util.utility import get_acc, nrmse

def run_ARIMA(data, param):


      order = param['order'] 
      testsize = param['testsize']

      T = data.shape[-1]
      T_test = int((T * testsize) // 1)
      result_full = np.zeros([data.shape[0], T_test])

      total_time = 0
      n_round = 0


      for i in range(T_test):

        y = data[..., i:T-T_test+i].copy()
        n_round += 1
        start = time.time()

        for j in range(y.shape[0]):
          
          model = ARIMA(order , suppress_warnings = True,enforce_stationarity=True)
          result = model.fit_predict(y[j], n_periods=1)
          result_full[j, i] = result[..., -1]

        end = time.time()
        total_time = total_time + (end - start)

      true_value = data[..., -T_test:]


      stat = {}
      stat['acc'] = get_acc(result_full, true_value)
      stat['nrmse'] = nrmse(result_full, true_value)
      stat['ave_time'] = total_time/n_round


      return(stat)
 
 
