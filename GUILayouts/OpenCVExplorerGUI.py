# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.dataview

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OpenCV Explorer", pos = wx.DefaultPosition, size = wx.Size( 781,574 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bszMain = wx.BoxSizer( wx.VERTICAL )
		
		self.m_toolBar1 = wx.ToolBar( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,40 ), wx.TB_HORIZONTAL ) 
		self.m_tbbtnFileOpen = wx.BitmapButton( self.m_toolBar1, wx.ID_ANY, wx.Bitmap( u"../Assets/Icons/icons8-opened-folder-50.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 24,24 ), 0 )
		
		self.m_tbbtnFileOpen.SetBitmap( wx.Bitmap( u"../Assets/Icons/icons8-opened-folder-50.png", wx.BITMAP_TYPE_ANY ) )
		self.m_toolBar1.AddControl( self.m_tbbtnFileOpen )
		self.m_toolBar1.Realize() 
		
		bszMain.Add( self.m_toolBar1, 0, wx.EXPAND, 5 )
		
		bszMainContent = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_tlFunctions = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		
		bszMainContent.Add( self.m_tlFunctions, 25, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlImage = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bszMainContent.Add( self.m_pnlImage, 50, wx.EXPAND |wx.ALL, 50 )
		
		m_lbALayersChoices = []
		self.m_lbALayers = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lbALayersChoices, 0 )
		bszMainContent.Add( self.m_lbALayers, 25, wx.ALL|wx.EXPAND, 5 )
		
		
		bszMain.Add( bszMainContent, 15, wx.EXPAND, 5 )
		
		
		self.SetSizer( bszMain )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

