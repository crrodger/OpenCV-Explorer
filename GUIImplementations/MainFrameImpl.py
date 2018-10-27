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
            self.m_tlFunctions.SetItemData(child, i)

    def IntSlider(self, parent, config, funcDef):
        tmpPanel = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
        tmpSizer = wx.BoxSizer( wx.HORIZONTAL )
        tmpSlider = wx.Slider( tmpPanel, wx.ID_ANY, 0, config['Min'], config['Max'], wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL|wx.SL_LABELS|wx.SL_VALUE_LABEL, name=config['ParamName'] )
        tmpSlider.Bind(wx.EVT_SCROLL_THUMBRELEASE, funcDef['ValueChangeEvent'])
        tmpSizer.Add( tmpSlider, 1, wx.ALL|wx.EXPAND, 5 )
        tmpStaticText = wx.StaticText( tmpPanel, wx.ID_ANY, config['Label'], wx.DefaultPosition, wx.DefaultSize, 0 , name=config['ParamName'])
        tmpSizer.Add( tmpStaticText, 0, wx.ALL, 5 )
        tmpPanel.SetSizer(tmpSizer)
        tmpPanel.Layout()

        return tmpPanel

    def FloatEditor(self, parent, config, funcDef):
        return 'y'
    
    def BooleanEditor(self, parent, config, funcDef):
        tmpPanel = wx.Panel(parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
        tmpSizer = wx.BoxSizer( wx.HORIZONTAL )
        tmpCheckBox = wx.CheckBox( tmpPanel, wx.ID_ANY, config['Label'], wx.DefaultPosition, wx.DefaultSize, 0 , name=config['ParamName'])
        tmpSizer.Add( tmpCheckBox, 0, wx.ALL, 5 )
        
        tmpPanel.Layout()
        return tmpPanel

    switcher = {
        'Int':IntSlider,
        'Float':FloatEditor,
        'Boolean':BooleanEditor
        }

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
        funcDef = allOperations[self.m_tlFunctions.GetItemData(selFunction)]
        
        rootItem = self.m_tlLayers.GetRootItem()
        child = self.m_tlLayers.AppendItem(rootItem, funcDef['Name'], -1, -1, funcDef)
        self.m_tlFunctions.SetItemData(child, funcDef)
        self.m_tlLayers.Select(child)
        
        self.layoutFunctionPanel(selFunction)
        
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
        
    
    def OnMenuFileOpenSelect( self, event ):
        fileWildcards = "All files (*.*)|*.*|JPEG files (*.jpg)|*.jpg|TIFF files (*.tif)|*.tif|PNG files (*.png)|*.png"
        with wx.FileDialog(self, "Open Image file", wildcard=fileWildcards,style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return
            
            pathname = fileDialog.GetPath()
            fileDialog.Hide()
            self.loadBitmap(pathname)
            

        
        
        