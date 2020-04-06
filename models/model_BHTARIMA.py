
# This script is rewriting code from demo of BHT-ARIMA algorithm
#(https://github.com/huawei-noah/BHT-ARIMA) with adding loop to evaluate nrmse



import numpy as np
import time

from BHT_ARIMA import BHTARIMA
from BHT_ARIMA.util.utility import get_acc, nrmse

def run_BHTARIMA(data, param):


      p = param['p'] # p-order
      d = param['d'] # d-order
      q = param['q'] # q-order
      taus = param['taus'] # MDT-rank
      Rs = param['Rs'] # tucker decomposition ranks
      k =  param['k'] # iterations
      tol = param['tol'] # stop criterion
      Us_mode = param['Us_mode'] # orthogonality mode
      testsize = param['testsize']



      T = data.shape[-1]
      T_test = int((T * testsize) // 1)
      result_full = np.zeros([data.shape[0], T_test])

      total_time = 0
      n_round = 0

      for i in range(T_test):

        ts = data[..., i:T-T_test+i].copy()
        n_round += 1
        model = BHTARIMA(ts, p, d, q, taus, Rs, k, tol, verbose=0, Us_mode=Us_mode)
        start = time.time()
        result, _ = model.run()
        end = time.time()
        total_time = total_time + (end - start)
        result_full[..., i] = result[..., -1]

      label = data[..., -T_test:]

      stat = {}
      stat['acc'] = get_acc(result_full, label)
      stat['nrmse'] = nrmse(result_full, label)
      stat['ave_time'] = total_time/n_round

      return(stat)

 



