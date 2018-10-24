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
## Class MainFrameDefn
###########################################################################

class MainFrameDefn ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OpenCV Explorer", pos = wx.DefaultPosition, size = wx.Size( 781,574 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bszMain = wx.BoxSizer( wx.VERTICAL )
		
		bszMainContent = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_tlFunctions = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_tlFunctions.AppendColumn( u"Functions", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		
		bszMainContent.Add( self.m_tlFunctions, 25, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlImage = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bszMainContent.Add( self.m_pnlImage, 70, wx.EXPAND |wx.ALL, 5 )
		
		m_lbALayersChoices = []
		self.m_lbALayers = wx.ListBox( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lbALayersChoices, 0 )
		bszMainContent.Add( self.m_lbALayers, 25, wx.ALL|wx.EXPAND, 5 )
		
		
		bszMain.Add( bszMainContent, 15, wx.EXPAND, 5 )
		
		
		self.SetSizer( bszMain )
		self.Layout()
		self.m_mnubarMain = wx.MenuBar( 0 )
		self.m_mnuFile = wx.Menu()
		self.m_mnuItemFileOpen = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_mnuItemFileOpen )
		
		self.m_mnubarMain.Append( self.m_mnuFile, u"File" ) 
		
		self.SetMenuBar( self.m_mnubarMain )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_pnlImage.Bind( wx.EVT_PAINT, self.OnPanelPaint )
		self.Bind( wx.EVT_MENU, self.OnMenuFileOpenSelect, id = self.m_mnuItemFileOpen.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnPanelPaint( self, event ):
		event.Skip()
	
	def OnMenuFileOpenSelect( self, event ):
		event.Skip()
	

###########################################################################
## Class AlgoFrameDefn
###########################################################################

class AlgoFrameDefn ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 608,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

