'''
Created on 25 Oct. 2018

@author: craig
'''

import cv2

allOperations = {}

# ==================================================================================================
# Define any enums before being used
# ==================================================================================================
enumBorderTypes = {
                   'CONSTANT':      cv2.BORDER_CONSTANT,
                   'DEFAULT':       cv2.BORDER_DEFAULT,
                   'ISOLATED':      cv2.BORDER_ISOLATED,
                   'REFLECT':       cv2.BORDER_REFLECT,
                   'REFLECT101':    cv2.BORDER_REFLECT101,
                   'REFLECT_101':   cv2.BORDER_REFLECT_101,
                   'REPLICATE':     cv2.BORDER_REPLICATE,
                   'TRANSPARENT':   cv2.BORDER_TRANSPARENT,
                   'WRAP':          cv2.BORDER_WRAP
               }

enumAdaptiveThresholdTypes = { 
                    'MEAN_C':       cv2.ADAPTIVE_THRESH_MEAN_C,
                    'GAUSSIAN_C':   cv2.ADAPTIVE_THRESH_GAUSSIAN_C
                }

enumThresholdTypes = {
                    'BINARY':       cv2.THRESH_BINARY,
                    'BINARY_INV':   cv2.THRESH_BINARY_INV,
                    'TRUNC':        cv2.THRESH_TRUNC,
                    'TOZERO':       cv2.THRESH_TOZERO,
                    'TOZERO_INV':   cv2.THRESH_TOZERO_INV,
                    'MASK':         cv2.THRESH_MASK,
                    'OTSU':         cv2.THRESH_OTSU,
                    'TRIANGLE':     cv2.THRESH_TRIANGLE
                }

enumColourConversionTypes = {
                    'BGR2GRAY':     cv2.COLOR_BGR2GRAY,
                    'BGR2RGB':      cv2.COLOR_BGR2RGB,
                    'BGRA2RGBA':    cv2.COLOR_BGRA2RGBA,
                    'BGRA2BGR':     cv2.COLOR_BGRA2BGR
    }
# ==================================================================================================
# Functions that match to allOperations entrues that will actually do the work
# ==================================================================================================





# ==================================================================================================
# Mapping of information needed to load and use functions
# Valid fields for Parameters
# ParamName, Label, ParamType, control, Min, Max, Value
# ParamNames should match the named parameters of the functions listed above that are called when this
# OpenCV is executed.
# ==================================================================================================

# ==================================================================================================
# Colour conversion
def ConvertColourFunc(image, code):
    return cv2.cvtColor(image, code)

allOperations['CvtColor'] = {
    'Name':'Convert Colour',
    'Function':ConvertColourFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'code', 'Label':'Colour Code', 'ParamType':'Enum', 'EnumValues':enumColourConversionTypes, 'Value':0, 'control':True}
        ]
    }



# ==================================================================================================
# Canny edge detection

def CannyFunc(image, threshold1=100, threshold2=200, apertureSize=5, L2gradient=False):
    return cv2.Canny(image, threshold1, threshold2)
#     return cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)


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

def GaussianBlurFunc(image, kernelSize, borderType):
    return cv2.GaussianBlur(image, (kernelSize, kernelSize), borderType)

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

def BlurFunc(image, ksize, anchorx, anchory, borderType):
    return cv2.blur(image, (ksize, ksize), (anchorx,anchory))
# return cv2.blur(image, (ksize, ksize), (anchorx, anchory), borderType)

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

def MedianBlurFunc(image, ksize):
    return cv2.medianBlur(image, ksize)

allOperations['MedianBlur'] = {
    'Name':'Median Blur',
    'Function':MedianBlurFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'ksize', 'Label':'Kernel Size', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True}
        ]
    }

# ==================================================================================================
# Bilateral Filter

def BilateralFilterFunc(image, d, sigmaColor, sigmaSpace):
    return cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

allOperations['BilateralFilter'] = {
    'Name':'Bilateral Filter',
    'Function':BilateralFilterFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'d', 'Label':'Pix Diam.', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'sigmaColor', 'Label':'Sigma Colour.', 'ParamType':'Double', 'Min':0,'Max':100, 'Value':0.0, 'control':True},
        {'ParamName':'sigmaSpace', 'Label':'Sigma Space', 'ParamType':'Double', 'Min':0,'Max':100, 'Value':0.0, 'control':True}
        ]
    }

# ==================================================================================================
# Simple Threshold

def SimpleThresholdFunc(image, thresh, maxval, thresholdType):
    x, newImg = cv2.threshold(image, thresh, maxval, thresholdType)
    return newImg

allOperations['SimpleThreshold'] = {
    'Name':'Simple Threhold',
    'Function':SimpleThresholdFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'thresh', 'Label':'Threshold.', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'control':True},
        {'ParamName':'maxval', 'Label':'Max Value', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'control':True},
        {'ParamName':'thresholdType', 'Label':'Threshold Type', 'ParamType':'Enum', 'EnumValues':enumThresholdTypes, 'Value':6, 'control':True}
        ]
    }

# ==================================================================================================
# Adaptive Threshold

def AdaptiveThresholdFunc(image, maxValue, adaptiveMethod, thresholdType, blockSize, c):
    return cv2.adaptiveThreshold(image, maxValue, adaptiveMethod, thresholdType, blockSize, c)

allOperations['AdaptiveThreshold'] = {
    'Name':'Adaptive Threshold',
    'Function':AdaptiveThresholdFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'maxValue', 'Label':'Max Value', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'adaptiveMethod', 'Label':'Adapt Method', 'ParamType':'Enum', 'EnumValues':enumAdaptiveThresholdTypes, 'Value':0, 'control':True},
        {'ParamName':'thresholdType', 'Label':'Threshold Type', 'ParamType':'Enum', 'EnumValues':enumThresholdTypes, 'Value':0, 'control':True},
        {'ParamName':'blockSize', 'Label':'Block Size', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'c', 'Label':'c', 'ParamType':'Double', 'Min':-100,'Max':100, 'Value':0.0, 'control':True}
        ]
    }

