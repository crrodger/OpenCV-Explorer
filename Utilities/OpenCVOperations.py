'''
Created on 25 Oct. 2018

@author: craig
'''

import cv2

allOperations = {}

# ==================================================================================================
# Define any enums before being used
# ==================================================================================================
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

# ==================================================================================================
# Functions that match to allOperations entrues that will actually do the work
# ==================================================================================================
def CannyFunc(image, threshold1=100, threshold2=200, apertureSize=5, L2gradient=False):
    return cv2.Canny(image, threshold1, threshold2)
#     return cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)

def GaussianBlurFunc(image, kernelSize, borderType):
    return cv2.GaussianBlur(image, (kernelSize, kernelSize), borderType)

def BlurFunc(image, ksize, anchorx, anchory, borderType):
    return cv2.blur(image, (ksize, ksize), (anchorx,anchory))
# return cv2.blur(image, (ksize, ksize), (anchorx, anchory), borderType)

def MedianBlurFunc(image, ksize):
    return cv2.medianBlur(image, ksize)

# ==================================================================================================
# Mapping of information needed to load and use functions
# Valid fields for Parameters
# ParamName, Label, ParamType, control, Min, Max, Value
# ParamNames should match the named parameters of the functions listed above that are called when this
# OpenCV is executed.
# ==================================================================================================

# ==================================================================================================
# Canny edge detection
allOperations['Canny'] = {
    'Name':'Canny Edge Detection',
    'Function':CannyFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'threshold1', 'Label':'Threshold 1', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':0, 'control':True},
        {'ParamName':'threshold2', 'Label':'Threshold 2', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':0, 'control':True},
        {'ParamName':'apertureSize', 'Label':'Aperture Size', 'ParamType':'Int', 'Min':3,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'L2gradient', 'Label':'L2 Gradient', 'ParamType':'Boolean', 'Value':False, 'control':True}
        ]
    }

# ==================================================================================================
# Gaussian Blur
allOperations['GaussianBlur'] = {
    'Name':'Gaussian Blur',
    'Function':GaussianBlurFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'kernelSize', 'Label':'Kernel Size', 'ParamType':'Int', 'Min':3,'Max':101, 'Value':0, 'control':True},
        {'ParamName':'borderType', 'Label':'Border Type', 'ParamType':'Enum', 'EnumValues':enumBorderTypes, 'Min':0,'Max':100, 'Value':0, 'control':True}
        ]
    }

# ==================================================================================================
# Blur
allOperations['Blur'] = {
    'Name':'Blur',
    'Function':BlurFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'ksize', 'Label':'Kernel Size', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'anchorx', 'Label':'Anchor-X', 'ParamType':'Int', 'Min':-1,'Max':100, 'Value':-1, 'control':True},
        {'ParamName':'anchory', 'Label':'Anchor-Y', 'ParamType':'Int', 'Min':-1,'Max':100, 'Value':-1, 'control':True},
        {'ParamName':'borderType', 'Label':'Border Type', 'ParamType':'Enum', 'EnumValues':enumBorderTypes, 'Min':0,'Max':100, 'Value':0, 'control':True}
        ]
    }

# ==================================================================================================
# Median Blur
allOperations['MedianBlur'] = {
    'Name':'Median Blur',
    'Function':MedianBlurFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'ksize', 'Label':'Kernel Size', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True}
        ]
    }
