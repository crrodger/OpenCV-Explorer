'''
Created on 25 Oct. 2018

@author: craig
'''

import cv2

allOperations = {}

def CannyFunc(image, threshold1=100, threshold2=200, apertureSize=3, L2gradient=False):
    return cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)



allOperations['Canny'] = {
    'Name':'Canny Edge Detection',
    'Function':CannyFunc,
    'ValueChangeEvent':(lambda event: {
            print(event.EventObject.Name)
        }),
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'threshold1', 'Label':'Threshold 1', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'threshold2', 'Label':'Threshold 2', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'apertureSize', 'Label':'Aperture Size', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'L2gradient', 'Label':'L2 Gradient', 'ParamType':'Boolean', 'Value':False, 'control':True}
        ],
    'Returns':[
        {'Returnname':'edges', 'ReturnType':'IntArray'}
        ]
    }