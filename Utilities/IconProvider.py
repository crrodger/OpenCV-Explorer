import wx
import os

class IconProvider(wx.ArtProvider):

    def __init__(self):
        wx.ArtProvider.__init__(self)
#         self.log = log

    def CreateBitmap(self, id, client, size):
        if client == "wxART_TOOLBAR_C":
            scriptDir = os.path.dirname(os.path.realpath(__file__))
            imageDir = '../Assets/Icons/'
            bmp = wx.Bitmap(os.path.join(scriptDir, imageDir, id))
            return bmp

#     # optionally override this one as well
#     def CreateIconBundle(self, id, client):
#         
#         # Your implementation of CreateIconBundle here
#         pass
