import numpy as np
import time

from sklearn.model_selection import GridSearchCV
from xgboost import XGBRegressor
from BHT_ARIMA.util.utility import get_acc, nrmse

def run_XGB(data, test_size):


      T_test = test_size
      result_full = np.zeros([data.shape[0], T_test])
      parameters = {'max_depth':(3,4,5,6,7,8,9,10), 
              'subsample':[0.5,0.6, 0.7, 0.8, 0.9],
               'lambda' :[0, 0.25, 0.5, 0.75, 1]}
      clf = GridSearchCV(XGBRegressor(), parameters, verbose = False, cv = 5)
      X = data[..., :-T_test-1]
      y = data[..., -T_test-1]
      clf.fit(X, y)
      for i in range(T_test):
        X_test = data[..., i+1:-T_test+i]
        result = clf.predict(X_test)
        result_full[..., i] = result

      label = data[..., -T_test:]

      stat = {}
      stat['acc'] = get_acc(result_full, label)
      stat['nrmse'] = nrmse(result_full, label)

      return(stat)

 



