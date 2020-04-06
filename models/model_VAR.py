

import numpy as np
import time

from statsmodels.tsa.api import VAR
from BHT_ARIMA.util.utility import get_acc, nrmse

def run_VAR(data, param):


      p = param['p']
      testsize = param['testsize']

      T = data.shape[-1]
      T_test = int((T * testsize) // 1)
      result_full = np.zeros([data.shape[0], T_test])

      total_time = 0
      n_round = 0

      for i in range(T_test):

        ts = data[..., i:T-T_test+i].copy()
        n_round += 1
        model = VAR(ts)
        start = time.time()
        result = model.fit(p).forecast(ts, 1)
        end = time.time()
        total_time = total_time + (end - start)
        result_full[..., i] = result[..., -1]

      label = data[..., -T_test:]

      stat = {}
      stat['acc'] = get_acc(result_full, label)
      stat['nrmse'] = nrmse(result_full, label)
      stat['ave_time'] = total_time/n_round

      return(stat)



