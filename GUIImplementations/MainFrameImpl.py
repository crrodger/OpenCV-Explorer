'''
Created on 24 Oct. 2018

@author: craig
'''

import wx
import cv2
from GUILayouts.OpenCVExplorerGUI import MainFrameDefn
from wx.lib.dialogs import openFileDialog
from Utilities.OpenCVOperations import allOperations

class MainFrameImpl(MainFrameDefn):
    
    bmp = None
    baseImage = None
    blur = False
    canny = False
    plotContour = None
    
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
            child = self.m_tlFunctions.AppendItem(rootItem, funcItem['Name'], -1, -1, funcItem)

    
    
    def wxBitmapFromCvImage(self, image):
        if len(image.shape) < 3:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        h, w = image.shape[:2]
        bitmap = wx.BitmapFromBuffer(w, h, image)
        return bitmap
    
    def loadBitmap(self, filePath):
        try:
            self.baseImage = cv2.imread(filePath)
            self.m_pnlImageOrg.Refresh()
        except IOError:
            print("Cannot open file '%s'." % filePath)

    
#==============================================================================================================
# Event handlers
#==============================================================================================================
    
    def OnPanelPaintOrg( self, event ):
        if self.baseImage is None:
            return
        height, width = self.m_pnlImageOrg.Size
        img = cv2.resize(self.baseImage, (height, width), cv2.INTER_LINEAR)
        self.bmp = self.wxBitmapFromCvImage(img)
        dc = wx.PaintDC(self.m_pnlImageOrg)
#         dc = wx.ClientDC(self.m_pnlImage)
        dc.DrawBitmap(self.bmp, 0, 0)
    
    def OnPanelPaintRes( self, event ):
        if self.baseImage is None:
            return
        height, width = self.m_pnlImageRes.Size
        img = cv2.resize(self.baseImage, (height, width), cv2.INTER_LINEAR)
        
        if self.blur and self.m_BlurKernel.Value >= 2:
            val = self.m_BlurKernel.Value
            img = cv2.medianBlur(img, val)
        
        if self.canny:
            valTh1 = self.m_CannyTh1.Value
            valTh2 = self.m_CannyTh2.Value
            img = cv2.Canny(img, valTh1, valTh2)
            im2, contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            lstItems = [str(x).replace("\n","") for x in contours]
            self.m_lstEdges.InsertItems(lstItems, self.m_lstEdges.GetCount())
        
        if not self.plotContour is None:
            plotContour = eval(self.plotContour)
            img = cv2.drawContours(img, plotContour, -1, (0,255,0))
             
            
        self.bmp = self.wxBitmapFromCvImage(img)
        dc = wx.PaintDC(self.m_pnlImageRes)
#         dc = wx.ClientDC(self.m_pnlImage)
        dc.DrawBitmap(self.bmp, 0, 0)
        
        
        
    def OnListBoxContoursSelect( self, event ):
        nitem = self.m_lstEdges.GetSelection()
        cnt = self.m_lstEdges.GetString(nitem)
        self.plotContour = cnt
        self.m_pnlImageRes.Refresh()
        
    
    def OnMenuFileOpenSelect( self, event ):
        fileWildcards = "All files (*.*)|*.*|JPEG files (*.jpg)|*.jpg|TIFF files (*.tif)|*.tif|PNG files (*.png)|*.png"
        with wx.FileDialog(self, "Open Image file", wildcard=fileWildcards,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            pathname = fileDialog.GetPath()
            fileDialog.Hide()
            self.loadBitmap(pathname)
            
    def OnCbBlurChange( self, event ):
        if self.m_cbBlur.Value:
            self.blur = True
        else:
            self.blur = False
        self.m_pnlImageRes.Refresh()
        
    def OnScrollBlurKernelChanged( self, event ):
        valKernel = self.m_BlurKernel.Value
        self.m_txtBlurKernel.SetLabel("Kernel {0}".format(valKernel))
        self.m_pnlImageRes.Refresh()
            
    def OnCbCannyChange( self, event ):
        if self.m_cbCanny.Value:
            self.canny = True
        else:
            self.canny = False
        self.m_pnlImageRes.Refresh()
        
    def OnScrollCannyChanged( self, event ):
        valTh1 = self.m_CannyTh1.Value
        valTh2 = self.m_CannyTh2.Value
        self.m_txtTh1Value.SetLabel("Threshold 1 {0}".format(valTh1))
        self.m_txtTh2Value.SetLabel("Threshold 2 {0}".format(valTh2))
        self.m_pnlImageRes.Refresh()