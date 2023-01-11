# import wx
#
# APP_EXIT = 1
#
#
# class AppFrame(wx.Frame):
#     def __init__(self, parent, title, size):
#         super().__init__(parent, title=title, size=size)
#
#         panel = wx.Panel(self)
#         vbox = wx.BoxSizer(wx.VERTICAL)
#         url_hbox = wx.BoxSizer(wx.HORIZONTAL)
#         info1_hbox = wx.BoxSizer(wx.HORIZONTAL)
#         desc_hbox = wx.BoxSizer(wx.HORIZONTAL)
#
#         st1 = wx.StaticText(panel, label='URL видео:')
#         video_tc = wx.TextCtrl(panel)
#         chck_btn = wx.Button(panel, label='Проверить ссылку', size=(150, 25))
#
#         url_hbox.Add(st1, flag=wx.RIGHT, border=8)
#         url_hbox.Add(video_tc, proportion=1)
#         url_hbox.Add(chck_btn, flag=wx.LEFT, border=5)
#
#         st2 = wx.StaticText(panel, label='Информация о видео')
#         info_tc = wx.TextCtrl(panel)
#
#         info1_hbox.Add(info_tc, flag=wx.TE_READONLY, proportion=1)
#
#         desc = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(250, 250))
#
#         desc_hbox.Add(desc, flag=wx.TE_READONLY, border=5)
#
#         vbox.Add(url_hbox, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=10)
#         vbox.Add(st2, flag=wx.LEFT, border=8)
#         vbox.Add(info1_hbox, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=10)
#         vbox.Add(desc_hbox, flag=wx.EXPAND | wx.RIGHT | wx.LEFT | wx.TOP, border=10)
#
#         panel.SetSizer(vbox)
#
#
# app = wx.App()
#
# frame = AppFrame(None, title='Youtube downloader', size=(600, 600))
# frame.Show()
#
# app.MainLoop()
import appform
import wx

if __name__ == '__main__':
    app = wx.App()
    frame = appform.MainFrame(None)
    frame.Show()

    app.MainLoop()
