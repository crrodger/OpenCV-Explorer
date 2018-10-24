'''
Created on 24 Oct. 2018

@author: craig
'''

import wx
import cv2
from GUILayouts.OpenCVExplorerGUI import MainFrameDefn
from wx.lib.dialogs import openFileDialog
import Utilities.OpenCVOperations
from Utilities.OpenCVOperations import allOperations

class MainFrameImpl(MainFrameDefn):
    
    bmp = None
    baseImage = None
    
    def __init__(self, parent:MainFrameDefn):
        MainFrameDefn.__init__(self, parent)
        self.loadOperations()

#==============================================================================================================
# Utility functions
#==============================================================================================================
    def loadOperations(self):
        rootItem = self.m_tlFunctions.GetRootItem()
        for i in allOperations:
            funcItem = allOperations[i]
            child = self.m_tlFunctions.AppendItem(rootItem, funcItem['Name'], -1, -1, i)

    
    
    def wxBitmapFromCvImage(self, image):
        if len(image.shape) < 3:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w = image.shape[:2]
        # The following conversion fails on Raspberry Pi.
        bitmap = wx.BitmapFromBuffer(w, h, image)
        return bitmap
    
    def loadBitmap(self, filePath):
        try:
            height, width = self.m_pnlImage.Size
#             self.baseImage = cv2.cvtColor(cv2.imread(filePath), cv2.COLOR_BGR2RGB)
            self.baseImage = cv2.imread(filePath)
            self.m_pnlImage.Refresh()
#             self.bmp = wx.BitmapFromBuffer(width, height, self.baseImage)
#             dc = wx.ClientDC(self.m_pnlImage)
#             dc = wx.BufferedDC(self.m_pnlImage)
#             dc.DrawBitmap(self.bmp, 0, 0)
        except IOError:
            print("Cannot open file '%s'." % filePath)

    
#==============================================================================================================
# Event handlers
#==============================================================================================================
    
    def OnPanelPaint( self, event ):
        print("Painting")
        height, width = self.m_pnlImage.Size
        img = cv2.resize(self.baseImage, (height, width), cv2.INTER_LINEAR)
        self.bmp = self.wxBitmapFromCvImage(img)
        dc = wx.PaintDC(self.m_pnlImage)
#         dc = wx.ClientDC(self.m_pnlImage)
        dc.DrawBitmap(self.bmp, 0, 0)
    
    def OnMenuFileOpenSelect( self, event ):
        fileWildcards = "JPEG files (.jpg)|.jpg|TIFF files (.tif)|.tif|PNG files (.png)|.png"
        with wx.FileDialog(self, "Open Image file", wildcard=fileWildcards,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            pathname = fileDialog.GetPath()
            fileDialog.Hide()
            self.loadBitmap(pathname)
            