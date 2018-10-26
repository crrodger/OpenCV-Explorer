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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OpenCV Explorer", pos = wx.DefaultPosition, size = wx.Size( 781,693 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bszMain = wx.BoxSizer( wx.VERTICAL )
		
		bszMainContent = wx.BoxSizer( wx.HORIZONTAL )
		
		bszTree = wx.BoxSizer( wx.VERTICAL )
		
		self.m_tlFunctions = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_tlFunctions.AppendColumn( u"Function", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		
		bszTree.Add( self.m_tlFunctions, 50, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlTools = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_pnlTools.SetScrollRate( 5, 5 )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_pnlFunc = wx.Panel( self.m_pnlTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_pnlFunc, 5, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_pnlTools.SetSizer( bSizer5 )
		self.m_pnlTools.Layout()
		bSizer5.Fit( self.m_pnlTools )
		bszTree.Add( self.m_pnlTools, 30, wx.EXPAND |wx.ALL, 5 )
		
		
		bszMainContent.Add( bszTree, 30, wx.EXPAND, 5 )
		
		bszPanels = wx.BoxSizer( wx.VERTICAL )
		
		self.m_pnlImageOrg = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		bszPanels.Add( self.m_pnlImageOrg, 50, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlImageRes = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bszPanels.Add( self.m_pnlImageRes, 50, wx.EXPAND |wx.ALL, 5 )
		
		
		bszMainContent.Add( bszPanels, 70, wx.EXPAND, 5 )
		
		
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
		self.m_tlFunctions.Bind( wx.dataview.EVT_TREELIST_SELECTION_CHANGED, self.OnTreelistSelectionChanged )
		self.m_pnlImageOrg.Bind( wx.EVT_PAINT, self.OnPanelPaintOrg )
		self.m_pnlImageRes.Bind( wx.EVT_PAINT, self.OnPanelPaintRes )
		self.Bind( wx.EVT_MENU, self.OnMenuFileOpenSelect, id = self.m_mnuItemFileOpen.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTreelistSelectionChanged( self, event ):
		event.Skip()
	
	def OnPanelPaintOrg( self, event ):
		event.Skip()
	
	def OnPanelPaintRes( self, event ):
		event.Skip()
	
	def OnMenuFileOpenSelect( self, event ):
		event.Skip()
	

