'''
Created on 24 Oct. 2018

@author: craig
'''
import wx
from GUIImplementations.MainFrameImpl import MainFrameImpl

class opencv_exp():
    
    def __init__(self):
        self.m_mainFrame = MainFrameImpl(None)

    def showMainFrame(self):
        self.m_mainFrame.Show(show=True)


if __name__ == "__main__":
    theApp = wx.App()
    m:opencv_exp = opencv_exp()
    m.showMainFrame()
    #m.showTestFrame()
    theApp.MainLoop()