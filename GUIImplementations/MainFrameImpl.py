'''
Created on 24 Oct. 2018

@author: craig
'''

import wx
import cv2
from GUILayouts.OpenCVExplorerGUI import MainFrameDefn
from wx.lib.dialogs import openFileDialog
from Utilities.OpenCVOperations import allOperations
from Utilities.OpenCVFunction import OpenCVFunction

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
            self.m_tlFunctions.SetItemData(child, i)

    def layoutFunctionPanel(self, selFunction):
        funcDef = allOperations[self.m_tlFunctions.GetItemData(selFunction)]
        
        self.m_pnlFunc.DestroyChildren()
        self.bszFuncLayout = wx.BoxSizer( wx.VERTICAL )
        self.m_pnlFunc.SetSizer(self.bszFuncLayout)
        
        txtLabel = wx.StaticText(self.m_pnlFunc, id=wx.ID_ANY, label=funcDef['Name'], pos=(0,0),size=(20,20), name="Name")
        self.bszFuncLayout.Add(txtLabel, 0, wx.EXPAND, 3)
        
        for param in funcDef['Parameters']:
            if param['control']:
                func = self.switcher.get(param['ParamType'])
#                 if param['ParamType'] == 'Int':
                res = func(self, self.m_pnlFunc, param, funcDef)
                self.bszFuncLayout.Add(res, 0, wx.EXPAND, 3)
        self.m_pnlFunc.Layout()
                    
            
    
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
            
        self.bmp = self.wxBitmapFromCvImage(img)
        dc = wx.PaintDC(self.m_pnlImageRes)
#         dc = wx.ClientDC(self.m_pnlImage)
        dc.DrawBitmap(self.bmp, 0, 0)
        
        
    def menuAddToLayers(self, event):
        selFunction = self.m_tlFunctions.GetSelection()
        
        funcObject = OpenCVFunction(self.m_tlFunctions.GetItemData(selFunction))
        
        funcDef = allOperations[self.m_tlFunctions.GetItemData(selFunction)]
        
        rootItem = self.m_tlLayers.GetRootItem()
        child = self.m_tlLayers.AppendItem(rootItem, funcDef['Name'], -1, -1, funcObject)
        self.m_tlLayers.SetItemData(child, funcObject)
        self.m_tlLayers.Select(child)
        
        funcObject.layoutFunctionPanel(self.m_pnlFunc)
        
    def OnFuncListContextMenu( self, event ):
        if self.m_tlFunctions.GetSelection() is None:
            return
        
        if not hasattr(self, "popIDAddToLayers"):
            self.popIDAddToLayers = wx.NewIdRef()
            
            self.Bind(wx.EVT_MENU, self.menuAddToLayers, id=self.popIDAddToLayers)
            
        mnu = wx.Menu()
        mnuAdd = mnu.Append(self.popIDAddToLayers, item="Add to Layer", helpString="Add this function to the layer process", kind=wx.ITEM_NORMAL)
        self.PopupMenu(mnu, pos=wx.DefaultPosition)
        
        
    def OnTreelistSelectionChanged( self, event ):
        pass
    
    def OnTreeLayerSelectionChange( self, event ):
        selLayer = self.m_tlLayers.GetSelection()
        funcObject = self.m_tlLayers.GetItemData(selLayer)
        funcObject.layoutFunctionPanel(self.m_pnlFunc)
        
    
    def OnLayerApplyClick( self, event ):
        selLayer = self.m_tlLayers.GetSelection()
        funcObject = self.m_tlLayers.GetItemData(selLayer)
        funcObject.execFunc(self.baseImage)
    
    def OnMenuFileOpenSelect( self, event ):
        fileWildcards = "All files (*.*)|*.*|JPEG files (*.jpg)|*.jpg|TIFF files (*.tif)|*.tif|PNG files (*.png)|*.png"
        with wx.FileDialog(self, "Open Image file", wildcard=fileWildcards,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            pathname = fileDialog.GetPath()
            fileDialog.Hide()
            self.loadBitmap(pathname)
            

        
        
        