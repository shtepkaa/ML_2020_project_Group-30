
import numpy as np
import pickle

with open('input/datasets_from_paper/traffic_80.npy', 'rb') as file:
      dataset_traffic_80 = pickle.load(file).T

hyperparam_traffic_80 = {

  'BHTARIMA':

    {
        'dataset': 'traffic_80',
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

    {  
        'testsize': 0.1,
        'order': [3, 1, 1]
    },


  'Prophet':

    {

        'testsize': 0.1,
        'start' : '2017-1',
        'freq' : 'D'

    }
    


}