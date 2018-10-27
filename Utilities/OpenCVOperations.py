'''
Created on 25 Oct. 2018

@author: craig
'''

import cv2

allOperations = {}

def CannyFunc(image, threshold1=100, threshold2=200, apertureSize=3, L2gradient=False):
    return cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)

def GaussianBlurFunc(image, kernelSize, borderType):
    return cv2.GaussianBlur(image, (kernelSize, kernelSize), borderType)

allOperations['Canny'] = {
    'Name':'Canny Edge Detection',
    'Function':CannyFunc,
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

enumBorderTypes = {'CONSTANT':      cv2.BORDER_CONSTANT,
                   'DEFAULT':       cv2.BORDER_DEFAULT,
                   'ISOLATED':      cv2.BORDER_ISOLATED,
                   'REFLECT':       cv2.BORDER_REFLECT,
                   'REFLECT101':    cv2.BORDER_REFLECT101,
                   'REFLECT_101':   cv2.BORDER_REFLECT_101,
                   'REPLICATE':     cv2.BORDER_REPLICATE,
                   'TRANSPARENT':   cv2.BORDER_TRANSPARENT,
                   'WRAP':          cv2.BORDER_WRAP
                   }

allOperations['GaussianBlur'] = {
    'Name':'Gaussian Blur',
    'Function':GaussianBlurFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'kernelSize', 'Label':'Kernel SIze', 'ParamType':'Int', 'Min':0,'Max':10, 'Value':0, 'control':True},
        {'ParamName':'borderType', 'Label':'Border Type', 'ParamType':'Enum', 'EnumValues':enumBorderTypes, 'Min':0,'Max':100, 'Value':0, 'control':True}
        ]
    }