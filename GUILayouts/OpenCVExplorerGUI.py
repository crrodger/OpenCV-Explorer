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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"OpenCV Explorer", pos = wx.DefaultPosition, size = wx.Size( 1071,774 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		bszMain = wx.BoxSizer( wx.VERTICAL )
		
		self.m_spltMain = wx.SplitterWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_3DBORDER|wx.SP_3DSASH|wx.SP_BORDER )
		self.m_spltMain.SetSashSize( 5 )
		self.m_spltMain.Bind( wx.EVT_IDLE, self.m_spltMainOnIdle )
		
		self.m_pnlFunctionsLeft = wx.Panel( self.m_spltMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bszTree = wx.BoxSizer( wx.VERTICAL )
		
		self.m_tlFunctions = wx.dataview.TreeListCtrl( self.m_pnlFunctionsLeft, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_tlFunctions.AppendColumn( u"Operations", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		
		bszTree.Add( self.m_tlFunctions, 50, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlFeedback = wx.Panel( self.m_pnlFunctionsLeft, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer8 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_txtFeedback = wx.TextCtrl( self.m_pnlFeedback, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_MULTILINE|wx.TE_WORDWRAP )
		bSizer8.Add( self.m_txtFeedback, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_pnlFeedback.SetSizer( bSizer8 )
		self.m_pnlFeedback.Layout()
		bSizer8.Fit( self.m_pnlFeedback )
		bszTree.Add( self.m_pnlFeedback, 50, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_pnlFunctionsLeft.SetSizer( bszTree )
		self.m_pnlFunctionsLeft.Layout()
		bszTree.Fit( self.m_pnlFunctionsLeft )
		self.m_pnlMainContentRight = wx.Panel( self.m_spltMain, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bszMainContent = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_spltImagesAndLayers = wx.SplitterWindow( self.m_pnlMainContentRight, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D|wx.SP_3DBORDER|wx.SP_3DSASH )
		self.m_spltImagesAndLayers.SetSashGravity( 0.7 )
		self.m_spltImagesAndLayers.SetSashSize( 5 )
		self.m_spltImagesAndLayers.Bind( wx.EVT_IDLE, self.m_spltImagesAndLayersOnIdle )
		
		self.m_pnlImages = wx.Panel( self.m_spltImagesAndLayers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bszPanels = wx.BoxSizer( wx.VERTICAL )
		
		self.m_pnlImageOrg = wx.Panel( self.m_pnlImages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.FULL_REPAINT_ON_RESIZE|wx.TAB_TRAVERSAL )
		bszPanels.Add( self.m_pnlImageOrg, 50, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlImageRes = wx.Panel( self.m_pnlImages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bszPanels.Add( self.m_pnlImageRes, 50, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_pnlImages.SetSizer( bszPanels )
		self.m_pnlImages.Layout()
		bszPanels.Fit( self.m_pnlImages )
		self.m_pnlLayersAndMessages = wx.Panel( self.m_spltImagesAndLayers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer6 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_spltLayersMessages = wx.SplitterWindow( self.m_pnlLayersAndMessages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.SP_3D )
		self.m_spltLayersMessages.Bind( wx.EVT_IDLE, self.m_spltLayersMessagesOnIdle )
		
		self.m_pnlLayers = wx.Panel( self.m_spltLayersMessages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer15 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_tlLayers = wx.dataview.TreeListCtrl( self.m_pnlLayers, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.dataview.TL_DEFAULT_STYLE )
		self.m_tlLayers.AppendColumn( u"Layers", wx.COL_WIDTH_DEFAULT, wx.ALIGN_LEFT, wx.COL_RESIZABLE )
		
		bSizer15.Add( self.m_tlLayers, 60, wx.EXPAND |wx.ALL, 5 )
		
		self.m_pnlLayerTools = wx.Panel( self.m_pnlLayers, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,40 ), wx.TAB_TRAVERSAL )
		bszLayerButtons = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_pbApply = wx.Button( self.m_pnlLayerTools, wx.ID_ANY, u"Apply", wx.DefaultPosition, wx.DefaultSize, 0 )
		bszLayerButtons.Add( self.m_pbApply, 0, wx.ALL, 5 )
		
		
		self.m_pnlLayerTools.SetSizer( bszLayerButtons )
		self.m_pnlLayerTools.Layout()
		bSizer15.Add( self.m_pnlLayerTools, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_pnlLayers.SetSizer( bSizer15 )
		self.m_pnlLayers.Layout()
		bSizer15.Fit( self.m_pnlLayers )
		self.m_pnlTools = wx.ScrolledWindow( self.m_spltLayersMessages, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_pnlTools.SetScrollRate( 5, 5 )
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_pnlFunc = wx.Panel( self.m_pnlTools, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.BORDER_SIMPLE|wx.TAB_TRAVERSAL )
		bSizer5.Add( self.m_pnlFunc, 5, wx.EXPAND |wx.ALL, 5 )
		
		
		self.m_pnlTools.SetSizer( bSizer5 )
		self.m_pnlTools.Layout()
		bSizer5.Fit( self.m_pnlTools )
		self.m_spltLayersMessages.SplitHorizontally( self.m_pnlLayers, self.m_pnlTools, 0 )
		bSizer6.Add( self.m_spltLayersMessages, 1, wx.EXPAND, 5 )
		
		
		self.m_pnlLayersAndMessages.SetSizer( bSizer6 )
		self.m_pnlLayersAndMessages.Layout()
		bSizer6.Fit( self.m_pnlLayersAndMessages )
		self.m_spltImagesAndLayers.SplitVertically( self.m_pnlImages, self.m_pnlLayersAndMessages, 500 )
		bszMainContent.Add( self.m_spltImagesAndLayers, 1, wx.EXPAND, 5 )
		
		
		self.m_pnlMainContentRight.SetSizer( bszMainContent )
		self.m_pnlMainContentRight.Layout()
		bszMainContent.Fit( self.m_pnlMainContentRight )
		self.m_spltMain.SplitVertically( self.m_pnlFunctionsLeft, self.m_pnlMainContentRight, 300 )
		bszMain.Add( self.m_spltMain, 10, wx.EXPAND, 5 )
		
		
		self.SetSizer( bszMain )
		self.Layout()
		self.m_mnubarMain = wx.MenuBar( 0 )
		self.m_mnuFile = wx.Menu()
		self.m_mnuItemFileOpen = wx.MenuItem( self.m_mnuFile, wx.ID_ANY, u"Open", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_mnuFile.Append( self.m_mnuItemFileOpen )
		
		self.m_mnubarMain.Append( self.m_mnuFile, u"File" ) 
		
		self.SetMenuBar( self.m_mnubarMain )
		
		self.m_tbMain = self.CreateToolBar( wx.TB_HORIZONTAL, wx.ID_ANY ) 
		self.m_tbImageOpen = self.m_tbMain.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( "ImageOpen.png", wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Open source image file", u"Open image file", None ) 
		
		self.m_tbPipelineOpen = self.m_tbMain.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( "PipelineOpen.png", wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Save current layer definitions as a pipline of operations", wx.EmptyString, None ) 
		
		self.m_tbPipelineSave = self.m_tbMain.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( "PipelineSave.png", wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_NORMAL, u"Load a pipeline of operations from a file", wx.EmptyString, None ) 
		
		self.m_tbInteractiveUpdate = self.m_tbMain.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( "InteractiveUpdate.png", wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_CHECK, u"Toggle interactive update of output (off requires apply to be clicked)", wx.EmptyString, None ) 
		
		self.m_tbStretchFit = self.m_tbMain.AddLabelTool( wx.ID_ANY, u"tool", wx.ArtProvider.GetBitmap( "StretchFit.png", wx.ART_TOOLBAR ), wx.NullBitmap, wx.ITEM_CHECK, u"Stretch output image to fit window (otherwise maintain aspect ratio)", wx.EmptyString, None ) 
		
		self.m_tbMain.Realize() 
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_tlFunctions.Bind( wx.dataview.EVT_TREELIST_ITEM_CONTEXT_MENU, self.OnFuncListContextMenu )
		self.m_tlFunctions.Bind( wx.dataview.EVT_TREELIST_SELECTION_CHANGED, self.OnTreelistSelectionChanged )
		self.m_pnlImageOrg.Bind( wx.EVT_PAINT, self.OnPanelPaintOrg )
		self.m_tlLayers.Bind( wx.dataview.EVT_TREELIST_ITEM_CONTEXT_MENU, self.OnLayerListContextMenu )
		self.m_tlLayers.Bind( wx.dataview.EVT_TREELIST_SELECTION_CHANGED, self.OnTreeLayerSelectionChange )
		self.m_pbApply.Bind( wx.EVT_BUTTON, self.OnLayerApplyClick )
		self.Bind( wx.EVT_MENU, self.OnMenuFileOpenSelect, id = self.m_mnuItemFileOpen.GetId() )
		self.Bind( wx.EVT_TOOL, self.tbImageOpenClicked, id = self.m_tbImageOpen.GetId() )
		self.Bind( wx.EVT_TOOL, self.tbPipelineOpenClick, id = self.m_tbPipelineOpen.GetId() )
		self.Bind( wx.EVT_TOOL, self.tbPipelineSaveClick, id = self.m_tbPipelineSave.GetId() )
		self.Bind( wx.EVT_TOOL, self.tbInteractiveUpdateClick, id = self.m_tbInteractiveUpdate.GetId() )
		self.Bind( wx.EVT_TOOL, self.tbStretchOutputClick, id = self.m_tbStretchFit.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFuncListContextMenu( self, event ):
		event.Skip()
	
	def OnTreelistSelectionChanged( self, event ):
		event.Skip()
	
	def OnPanelPaintOrg( self, event ):
		event.Skip()
	
	def OnLayerListContextMenu( self, event ):
		event.Skip()
	
	def OnTreeLayerSelectionChange( self, event ):
		event.Skip()
	
	def OnLayerApplyClick( self, event ):
		event.Skip()
	
	def OnMenuFileOpenSelect( self, event ):
		event.Skip()
	
	def tbImageOpenClicked( self, event ):
		event.Skip()
	
	def tbPipelineOpenClick( self, event ):
		event.Skip()
	
	def tbPipelineSaveClick( self, event ):
		event.Skip()
	
	def tbInteractiveUpdateClick( self, event ):
		event.Skip()
	
	def tbStretchOutputClick( self, event ):
		event.Skip()
	
	def m_spltMainOnIdle( self, event ):
		self.m_spltMain.SetSashPosition( 300 )
		self.m_spltMain.Unbind( wx.EVT_IDLE )
	
	def m_spltImagesAndLayersOnIdle( self, event ):
		self.m_spltImagesAndLayers.SetSashPosition( 500 )
		self.m_spltImagesAndLayers.Unbind( wx.EVT_IDLE )
	
	def m_spltLayersMessagesOnIdle( self, event ):
		self.m_spltLayersMessages.SetSashPosition( 0 )
		self.m_spltLayersMessages.Unbind( wx.EVT_IDLE )
	

