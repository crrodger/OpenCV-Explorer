'''
Created on 25 Oct. 2018

@author: craig
'''

import cv2
import numpy as np

allOperations = {}

# ==================================================================================================
# Define any enums before being used
# ==================================================================================================
enumInterpolationTypes = {
                'LINEAR':       cv2.INTER_LINEAR,
                'NEAREST':      cv2.INTER_NEAREST,
                'CUBIC':        cv2.INTER_CUBIC,
                'AREA':         cv2.INTER_AREA,
                'LANCZOS4':     cv2.INTER_LANCZOS4,
                'LINEAR_EXACT': cv2.INTER_LINEAR_EXACT,
                'MAX':          cv2.INTER_MAX,
                'FILL_OUTLIERS': cv2.WARP_FILL_OUTLIERS,
                'INVERSE_MAP':  cv2.WARP_INVERSE_MAP
                }


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
                    'OTSU_BINARY':  cv2.THRESH_OTSU + cv2.THRESH_BINARY,
                    'OTSU_BIN_INV': cv2.THRESH_OTSU + cv2.THRESH_BINARY_INV,
                    'TRIANGLE':     cv2.THRESH_TRIANGLE
                }

enumColourConversionTypes = {
                    'BGR2GRAY':     cv2.COLOR_BGR2GRAY,
                    'BGR2RGB':      cv2.COLOR_BGR2RGB,
                    'BGRA2RGBA':    cv2.COLOR_BGRA2RGBA,
                    'BGRA2BGR':     cv2.COLOR_BGRA2BGR
                }

enumMorphologyOperations = {
                    'MORPH_ERODE':  cv2.MORPH_ERODE,
                    'MORPH_DILATE ':cv2.MORPH_DILATE,
                    'MORPH_OPEN ':  cv2.MORPH_OPEN,
                    'MORPH_CLOSE ': cv2.MORPH_CLOSE,
                    'MORPH_GRADIENT ':cv2.MORPH_GRADIENT,
                    'MORPH_TOPHAT': cv2.MORPH_TOPHAT,
                    'MORPH_BLACKHAT':cv2.MORPH_BLACKHAT,
                    'MORPH_HITMISS':cv2.MORPH_HITMISS
                }

enumMorphologyOperationsShapes = {
                    'MORPH_CROSS':  cv2.MORPH_CROSS,
                    'MORPH_ELIPSE': cv2.MORPH_ELLIPSE,
                    'MORPH_RECT':   cv2.MORPH_RECT
                }
# ==================================================================================================
# Functions that match to allOperations entrues that will actually do the work
# ==================================================================================================


# ==================================================================================================
# Mapping of information needed to load and use functions
# Valid fields for Parameters
# ParamName, Label, ParamType, control, Min, Max, Value
# ParamNames should match the named parameters of the 'stub' functions that then call
# the OpenCV function. This makes it possible to do some processing before calling an OpenCV
# function. 
# OpenCV is executed.
# ==================================================================================================

# ==================================================================================================
# Extract region of image
def ImageSubregionFunc(image, xStartPerc, xEndPerc, yStartPerc, yEndPerc):
    shp = image.shape
    
    xStart = int(xStartPerc/100 * shp[1])
    xEnd = int(xEndPerc/100 * shp[0])
    yStart = int(yStartPerc/100 * shp[0])
    yEnd = int(yEndPerc/100 * shp[1])
        
    if len(shp) == 2:
        image = image[yStart:yEnd, xStart:xEnd]
        
    if len(shp) == 3: # Not sure if there are differences in future
        image = image[yStart:yEnd, xStart:xEnd, :]
        
    return image

allOperations['ExtractRegion'] = {
    'Name':'Extract Region',
    'Group':'',
    'Function':ImageSubregionFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'xStartPerc', 'Label':'X Start %', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'xEndPerc', 'Label':'X End %', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'yStartPerc', 'Label':'Y Start %', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'yEndPerc', 'Label':'Y End %', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True}
        ]
    }



# ==================================================================================================
# Colour conversion
def ConvertColourFunc(image, code):
    return cv2.cvtColor(image, code)

allOperations['CvtColor'] = {
    'Name':'Convert Colour',
    'Group':'',
    'Function':ConvertColourFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'code', 'Label':'Colour Code', 'ParamType':'Enum', 'EnumValues':enumColourConversionTypes, 'Value':enumColourConversionTypes['BGR2GRAY'], 'control':True}
        ]
    }


# ==================================================================================================
# Downscale image - help to make processing faster (can then disable for full check)

def DownScaleImageFunc(image, heightPerc, widthPerc, interpolation=cv2.INTER_LINEAR):
    shp = image.shape
    
    newHeight = int(heightPerc/100 * shp[0])
    newWidth = int(widthPerc/100 * shp[1])
    
    return cv2.resize(image, (newHeight, newWidth), interpolation)

allOperations['Downscale'] = {
    'Name':'Downscale',
    'Group':'',
    'Function':DownScaleImageFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'heightPerc', 'Label':'height %', 'ParamType':'IntSpin', 'Min':0,'Max':100, 'Value':50, 'control':True},
        {'ParamName':'widthPerc', 'Label':'width %', 'ParamType':'IntSpin', 'Min':0,'Max':100, 'Value':50, 'control':True},
        {'ParamName':'interpolation', 'Label':'Interp. Type', 'ParamType':'Enum', 'EnumValues':enumInterpolationTypes, 'Min':0,'Max':100, 'Value':enumInterpolationTypes['LINEAR'], 'control':True}
        ]
    }


# ==================================================================================================
# Canny edge detection

def CannyFunc(image, threshold1=100, threshold2=200, apertureSize=5, L2gradient=False):
    return cv2.Canny(image, threshold1, threshold2)
#     return cv2.Canny(image, threshold1, threshold2, apertureSize, L2gradient)


allOperations['Canny'] = {
    'Name':'Canny Edge Detection',
    'Group':'',
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
    'Group':'',
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
    'Group':'',
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
    'Group':'',
    'Function':MedianBlurFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'ksize', 'Label':'Kernel Size', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':11, 'control':True}
        ]
    }

# ==================================================================================================
# Bilateral Filter

def BilateralFilterFunc(image, d, sigmaColor, sigmaSpace):
    return cv2.bilateralFilter(image, d, sigmaColor, sigmaSpace)

allOperations['BilateralFilter'] = {
    'Name':'Bilateral Filter',
    'Group':'',
    'Function':BilateralFilterFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'d', 'Label':'Pix Diam.', 'ParamType':'Int', 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'sigmaColor', 'Label':'Sigma Colour.', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'Step':0.5, 'control':True},
        {'ParamName':'sigmaSpace', 'Label':'Sigma Space', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'Step':0.5, 'control':True}
        ]
    }

# ==================================================================================================
# Simple Threshold

def SimpleThresholdFunc(image, thresh, maxval, thresholdType):
    x, newImg = cv2.threshold(image, thresh, maxval, thresholdType)
    return newImg

allOperations['SimpleThreshold'] = {
    'Name':'Simple Threhold',
    'Group':'',
    'Function':SimpleThresholdFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'thresh', 'Label':'Threshold.', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'Step':0.5, 'control':True},
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
    'Group':'',
    'Function':AdaptiveThresholdFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'maxValue', 'Label':'Max Value', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':10, 'control':True},
        {'ParamName':'adaptiveMethod', 'Label':'Adapt Method', 'ParamType':'Enum', 'EnumValues':enumAdaptiveThresholdTypes, 'Value':0, 'control':True},
        {'ParamName':'thresholdType', 'Label':'Threshold Type', 'ParamType':'Enum', 'EnumValues':enumThresholdTypes, 'Value':0, 'control':True},
        {'ParamName':'blockSize', 'Label':'Block Size', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'c', 'Label':'c', 'ParamType':'Double', 'Min':-255,'Max':255, 'Value':0.0, 'Step':0.5, 'control':True}
        ]
    }

# ==================================================================================================
# Morphological gradient

def MorphologicalGradientFunc(image, op, ksizex, ksizey, shape):
    kernel = cv2.getStructuringElement(shape, (ksizex, ksizey))
    return cv2.morphologyEx(image, op, kernel)
    

allOperations['MorphologicalGradient'] = {
    'Name':'Morphological Gradient',
    'Group':'',
    'Function':MorphologicalGradientFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'op', 'Label':'Operation', 'ParamType':'Enum', 'EnumValues':enumMorphologyOperations, 'Value':0, 'control':True},
        {'ParamName':'ksizex', 'Label':'k Size X', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'ksizey', 'Label':'k Size Y', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'shape', 'Label':'Shape', 'ParamType':'Enum', 'EnumValues':enumMorphologyOperationsShapes, 'Value':0, 'control':True},
        ]
    }

# ==================================================================================================
# Histogram equalisation

def equalizeHistFunc(image):
    return cv2.equalizeHist(image)
    

allOperations['EqualiseHistogram'] = {
    'Name':'Equalise Histogram',
    'Group':'',
    'Function':equalizeHistFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False}
        ]
    }

# ==================================================================================================
# Create border

def CreateBorderFunc(image, borderSizeTop, borderSizeBottom, borderSizeLeft, borderSizeRight, borderType, colorValue):
    return cv2.copyMakeBorder(image, borderSizeTop, borderSizeBottom, borderSizeLeft, borderSizeRight, borderType, value=[colorValue, colorValue, colorValue])
    
allOperations['CopyCreateBorder'] = {
    'Name':'Copy Create Border',
    'Group':'Miscellaneous',
    'Function':CreateBorderFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'borderSizeTop', 'Label':'Top Border', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'borderSizeBottom', 'Label':'Bot Border', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'borderSizeLeft', 'Label':'Lft  Border', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'borderSizeRight', 'Label':'Rght Border', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'colorValue', 'Label':'Colour Code', 'ParamType':'IntSpin', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'borderType', 'Label':'Border Type', 'ParamType':'Enum', 'EnumValues':enumBorderTypes, 'Min':0,'Max':100, 'Value':0, 'control':True}
        ]
    }

# ==================================================================================================
# Find lines in the image

def HoughLinesFunc(image, rho, theta, threshold, srn=0, stn=0, min_theta=0, max_theta = 3.141592653589636, line_width=2, colour_constant=128 ):
    lines = cv2.HoughLines(image, rho, theta, threshold, srn, stn, min_theta, max_theta)
    if not lines is None and len(lines) > 0:
        for line in lines:
            rho,theta = line[0]
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 10000*(-b))
            y1 = int(y0 + 10000*(a))
            x2 = int(x0 - 10000*(-b))
            y2 = int(y0 - 10000*(a))
            cv2.line(image,(x1,y1),(x2,y2),(colour_constant, colour_constant, colour_constant),line_width)
    return image
    
allOperations['HoughLines'] = {
    'Name':'Hough Lines',
    'Group':'Find Features',
    'Function':HoughLinesFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'rho', 'Label':'Rho', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':1.0, 'Step':0.5, 'control':True},
        {'ParamName':'theta', 'Label':'Theta', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.05, 'Step':0.01, 'control':True},
        {'ParamName':'threshold', 'Label':'Threshold', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':150, 'control':True},
        {'ParamName':'srn', 'Label':'srn', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'Step':0.1, 'control':True},
        {'ParamName':'stn', 'Label':'stn', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'Step':0.1, 'control':True},
        {'ParamName':'min_theta', 'Label':'Min Theta', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':0.0, 'control':True},
        {'ParamName':'max_theta', 'Label':'Max Theta', 'ParamType':'Double', 'Min':0,'Max':255, 'Value':1.0, 'control':True},
        {'ParamName':'line_width', 'Label':'Line Width', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':5, 'control':True},
        {'ParamName':'colour_constant', 'Label':'Colour Val', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':128, 'control':True}
        ]
    }

# ==================================================================================================
# Find corners in the image

def CornerHarrisFunc(image, blockSize, ksize, k, borderType, drawThreshold, drawRadius=10, colour=128, thickness=3 ):
    corners = cv2.cornerHarris(image, blockSize, ksize, k, borderType)
    
    corners_norm = np.empty(corners.shape, dtype=np.float32)
    cv2.normalize(corners, corners_norm, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    dst_norm_scaled = cv2.convertScaleAbs(corners_norm)
    
    # Drawing a circle around corners
    for i in range(corners_norm.shape[0]):
        for j in range(corners_norm.shape[1]):
            if int(corners_norm[i,j]) > drawThreshold:
                cv2.circle(image, (j,i), drawRadius, (colour), thickness)

    
    return image
    
allOperations['CornerHarris'] = {
    'Name':'Harris Corner Detector',
    'Group':'Find Features',
    'Function':CornerHarrisFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'blockSize', 'Label':'Block Size', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'ksize', 'Label':'K Size', 'ParamType':'Int', 'Min':0,'Max':31, 'Value':1, 'control':True},
        {'ParamName':'k', 'Label':'Harris Param', 'ParamType':'Double', 'Min':0,'Max':1, 'Value':0.0, 'Step':0.01, 'control':True},
        {'ParamName':'borderType', 'Label':'Border Type', 'ParamType':'Enum', 'EnumValues':enumBorderTypes, 'Min':0,'Max':100, 'Value':0, 'control':True},
        {'ParamName':'drawThreshold', 'Label':'Draw Thresh', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':1, 'control':True},
        {'ParamName':'drawRadius', 'Label':'Draw Radius', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':1, 'control':True},
        {'ParamName':'colour', 'Label':'Colour', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':1, 'control':True},
        {'ParamName':'thickness', 'Label':'Thickness', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':1, 'control':True}
        ]
    }

# ==================================================================================================
# Find 'Good Features/ in the image

def GoodFeaturesToTrackFunc(image, maxCorners, qualityLevel, minDistance, blockSize, useHarris, k=0.04, drawRadius=10, colour=128, thickness=3):
    
    corners = cv2.goodFeaturesToTrack(image, maxCorners, qualityLevel, minDistance, None, None, blockSize, useHarris,k)
    
    corners = np.int0(corners)

    for i in corners:
        x,y = i.ravel()
        cv2.circle(image,(x,y),drawRadius, (colour), thickness)

    
    return image
    
allOperations['GoodFeatures'] = {
    'Name':'Good Features to Track',
    'Group':'Find Features',
    'Function':GoodFeaturesToTrackFunc,
    'Parameters':[
        {'ParamName':'image', 'Label':'Image', 'ParamType':'FloatArray', 'control':False},
        {'ParamName':'maxCorners', 'Label':'Max n Corners', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'qualityLevel', 'Label':'Quality Level', 'ParamType':'Double', 'Min':0,'Max':1, 'Value':0.0, 'Step':0.01, 'control':True},
        {'ParamName':'minDistance', 'Label':'Min Distance', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'blockSize', 'Label':'Block Size', 'ParamType':'Int', 'Min':0,'Max':255, 'Value':0, 'control':True},
        {'ParamName':'useHarris', 'Label':'Use Harris', 'ParamType':'Boolean', 'Value':False, 'control':True},
        {'ParamName':'k', 'Label':'Harris Param', 'ParamType':'Double', 'Min':0,'Max':1, 'Value':0.0, 'Step':0.01, 'control':True},
        {'ParamName':'drawRadius', 'Label':'Draw Radius', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':1, 'control':True},
        {'ParamName':'colour', 'Label':'Colour', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':1, 'control':True},
        {'ParamName':'thickness', 'Label':'Thickness', 'ParamType':'Int', 'Min':0,'Max':500, 'Value':1, 'control':True}
        ]
    }
