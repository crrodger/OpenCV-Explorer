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
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_tlFunctions = wx.dataview.TreeListCtrl( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		
		bSizer4.Add( self.m_tlFunctions, 25, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlTools = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_pnlTools.SetScrollRate( 5, 5 )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel4 = wx.Panel( self.m_pnlTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_cbBlur = wx.CheckBox( self.m_panel4, wx.ID_ANY, u"Blur", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer6.Add( self.m_cbBlur, 0, wx.ALL, 5 )
		
		self.m_BlurKernel = wx.Slider( self.m_panel4, wx.ID_ANY, 0, 0, 20, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer6.Add( self.m_BlurKernel, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_txtBlurKernel = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Kernel", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_txtBlurKernel.Wrap( -1 )
		
		bSizer6.Add( self.m_txtBlurKernel, 0, wx.ALL, 5 )
		
		
		self.m_panel4.SetSizer( bSizer6 )
		self.m_panel4.Layout()
		bSizer6.Fit( self.m_panel4 )
		bSizer5.Add( self.m_panel4, 7, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel5 = wx.Panel( self.m_pnlTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_DEFAULT|wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_cbCanny = wx.CheckBox( self.m_panel5, wx.ID_ANY, u"Canny Edge Detection", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer7.Add( self.m_cbCanny, 0, wx.ALL, 5 )
		
		self.m_CannyTh1 = wx.Slider( self.m_panel5, wx.ID_ANY, 0, 0, 500, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer7.Add( self.m_CannyTh1, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_txtTh1Value = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Threshold 1", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_txtTh1Value.Wrap( -1 )
		
		bSizer7.Add( self.m_txtTh1Value, 0, wx.ALL, 5 )
		
		self.m_CannyTh2 = wx.Slider( self.m_panel5, wx.ID_ANY, 0, 0, 500, wx.DefaultPosition, wx.DefaultSize, wx.SL_HORIZONTAL )
		bSizer7.Add( self.m_CannyTh2, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_txtTh2Value = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Threshold 2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_txtTh2Value.Wrap( -1 )
		
		bSizer7.Add( self.m_txtTh2Value, 0, wx.ALL, 5 )
		
		
		self.m_panel5.SetSizer( bSizer7 )
		self.m_panel5.Layout()
		bSizer7.Fit( self.m_panel5 )
		bSizer5.Add( self.m_panel5, 10, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel6 = wx.Panel( self.m_pnlTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		m_lstEdgesChoices = []
		self.m_lstEdges = wx.ListBox( self.m_panel6, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_lstEdgesChoices, 0 )
		bSizer8.Add( self.m_lstEdges, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel6.SetSizer( bSizer8 )
		self.m_panel6.Layout()
		bSizer8.Fit( self.m_panel6 )
		bSizer5.Add( self.m_panel6, 10, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel7 = wx.Panel( self.m_pnlTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_panel7, 10, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel8 = wx.Panel( self.m_pnlTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_panel8, 10, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_pnlTools.SetSizer( bSizer5 )
		self.m_pnlTools.Layout()
		bSizer5.Fit( self.m_pnlTools )
		bSizer4.Add( self.m_pnlTools, 66, wx.EXPAND |wx.ALL, 5 )
		
		
		bszMainContent.Add( bSizer4, 30, wx.EXPAND, 5 )
		
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
		self.m_cbBlur.Bind( wx.EVT_CHECKBOX, self.OnCbBlurChange )
		self.m_BlurKernel.Bind( wx.EVT_SCROLL_CHANGED, self.OnScrollBlurKernelChanged )
		self.m_cbCanny.Bind( wx.EVT_CHECKBOX, self.OnCbCannyChange )
		self.m_CannyTh1.Bind( wx.EVT_SCROLL_CHANGED, self.OnScrollCannyChanged )
		self.m_CannyTh2.Bind( wx.EVT_SCROLL_CHANGED, self.OnScrollCannyChanged )
		self.m_lstEdges.Bind( wx.EVT_LISTBOX, self.OnListBoxContoursSelect )
		self.m_pnlImageOrg.Bind( wx.EVT_PAINT, self.OnPanelPaintOrg )
		self.m_pnlImageRes.Bind( wx.EVT_PAINT, self.OnPanelPaintRes )
		self.Bind( wx.EVT_MENU, self.OnMenuFileOpenSelect, id = self.m_mnuItemFileOpen.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnTreelistSelectionChanged( self, event ):
		event.Skip()
	
	def OnCbBlurChange( self, event ):
		event.Skip()
	
	def OnScrollBlurKernelChanged( self, event ):
		event.Skip()
	
	def OnCbCannyChange( self, event ):
		event.Skip()
	
	def OnScrollCannyChanged( self, event ):
		event.Skip()
	
	
	def OnListBoxContoursSelect( self, event ):
		event.Skip()
	
	def OnPanelPaintOrg( self, event ):
		event.Skip()
	
	def OnPanelPaintRes( self, event ):
		event.Skip()
	
	def OnMenuFileOpenSelect( self, event ):
		event.Skip()
	

