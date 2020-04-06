#!/usr/bin/env python
# -*- coding: utf-8 -*-

csv = 'perf_Us_3'

cfg_dict = {

    'ele_1096':
    
    {
        'dataset': 'ele_1096',
        'p': 3,
        'd': 2,
        'q': 1,
        'taus': [321, 20],
        'Rs': [5, 5],
        'k': 15,
        'tol': 0.001,
        'testsize': 0.1,
        'loop_time': 5,
        'info': 'v2',
        'Us_mode': 1,
        'filename': csv
    },

    'ele_40':
    {
        'dataset': 'ele_40',
        'p': 3,
        'd': 2,
        'q': 1,
        'taus': [321, 20],
        'Rs': [5, 5],
        'k': 15,
        'tol': 0.001,
        'testsize': 0.1,
        'loop_time': 5,
        'info': 'v2',
        'Us_mode': 3,
        'filename': csv
    },

    'traffic_80':
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
        'filename': csv
    },
    
    'traffic_40':
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
        'filename': csv
    }

}