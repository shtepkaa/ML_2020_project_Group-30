
import numpy as np
import pickle

dataset_traffic_40 = np.load('input/datasets_from_paper/traffic_40.npy').T 

hyperparam_traffic_40 = {

  'BHTARIMA':

    {
        'dataset': 'traffic_40',
        'p': 3,
        'd': 2,
        'q': 1,
        'taus': [228, 5],
        'Rs': [20, 5],
        'k': 15,
        'tol': 0.001,
        'testsize': 0.1,
        'loop_time': 5,
        'info': 'v2',
        'Us_mode': 3,
    },


  'ARIMA':

    {   'testsize': 0.1,
        'order': [3, 1, 1]
    },

    'VAR':

    {
         'p' : 100,
         'testsize': 0.2
      
    },

      'Prophet':

    {

        'testsize': 0.1,
        'start' : '2017-1',
        'freq' : 'D'

    }
    




}