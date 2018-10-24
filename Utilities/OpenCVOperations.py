'''
Created on 25 Oct. 2018

@author: craig
'''


allOperations = {}
allOperations['Canny'] = {
    'Name':'Canny Edge Detection',
    'Parameters':[
        {'ParamName':'image', 'ParamType':'FloatArray'},
        {'ParamName':'threshold1', 'ParamType':'Float'},
        {'ParamName':'threshold2', 'ParamType':'Float'},
        {'ParamName':'apertureSize', 'ParamType':'Int'},
        {'ParamName':'L2gradient', 'ParamType':'Boolean'}
        ],
    'Returns':[
        {'Returnname':'edges', 'ReturnType':'IntArray'}
        ]
    }