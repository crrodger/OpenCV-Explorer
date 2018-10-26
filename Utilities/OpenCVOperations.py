'''
Created on 25 Oct. 2018

@author: craig
'''


allOperations = {}
allOperations['Canny'] = {
    'Name':'Canny Edge Detection',
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'threshold1', 'Label':'Threshold 1', 'ParamType':'Int', 'Min':0,'Max':100, 'control':True},
        {'ParamName':'threshold2', 'Label':'Threshold 2', 'ParamType':'Int', 'Min':0,'Max':100, 'control':True},
        {'ParamName':'apertureSize', 'Label':'Aperture Size', 'ParamType':'Int', 'Min':0,'Max':100, 'control':True},
        {'ParamName':'L2gradient', 'Label':'L2 Gradient', 'ParamType':'Boolean', 'control':True}
        ],
    'Returns':[
        {'Returnname':'edges', 'ReturnType':'IntArray'}
        ]
    }