import wx
import wx.xrc


###########################################################################
# Class MainFrame
###########################################################################

class MainFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Youtube downloader", pos=wx.DefaultPosition,
                          size=wx.Size(650, 400), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)

        mainSizer = wx.BoxSizer(wx.VERTICAL)

        self.panel = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(600, 400), wx.TAB_TRAVERSAL)
        vbox = wx.BoxSizer(wx.VERTICAL)

        url = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText1 = wx.StaticText(self.panel, wx.ID_ANY, u"URL видео:", wx.DefaultPosition, wx.Size(-1, 14), 0)
        self.m_staticText1.Wrap(-1)

        url.Add(self.m_staticText1, 0, wx.ALL, 8)

        self.m_textCtrl1 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(375, 25), 0)
        url.Add(self.m_textCtrl1, 0, wx.ALL, 5)

        self.chckvideo_btn = wx.Button(self.panel, wx.ID_ANY, u"Проверить видео", wx.DefaultPosition, wx.Size(150, 25),
                                       0)
        url.Add(self.chckvideo_btn, 0, wx.ALL | wx.LEFT, 5)

        vbox.Add(url, 1, wx.ALL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        info1 = wx.BoxSizer(wx.VERTICAL)

        info1.SetMinSize(wx.Size(600, 25))
        self.m_staticText3 = wx.StaticText(self.panel, wx.ID_ANY, u"Информация о видео:", wx.DefaultPosition,
                                           wx.DefaultSize, 0)
        self.m_staticText3.Wrap(-1)

        info1.Add(self.m_staticText3, 0, wx.ALL, 5)

        self.m_textCtrl3 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(600, 25), 0)
        info1.Add(self.m_textCtrl3, 0, wx.ALL, 5)

        vbox.Add(info1, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        descr = wx.BoxSizer(wx.HORIZONTAL)

        self.preview_image = wx.StaticBitmap(self.panel, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition,
                                             wx.Size(250, 150), 0)
        descr.Add(self.preview_image, 0, wx.ALL, 5)

        self.m_textCtrl4 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(350, 150),
                                       wx.TE_MULTILINE | wx.TE_READONLY)
        descr.Add(self.m_textCtrl4, 0, wx.ALL, 5)

        vbox.Add(descr, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        save = wx.BoxSizer(wx.HORIZONTAL)

        self.m_staticText5 = wx.StaticText(self.panel, wx.ID_ANY, u"Сохранить в:", wx.DefaultPosition, wx.Size(-1, 25),
                                           0)
        self.m_staticText5.Wrap(-1)

        save.Add(self.m_staticText5, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        self.m_textCtrl5 = wx.TextCtrl(self.panel, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(375, 25), 0)
        save.Add(self.m_textCtrl5, 0, wx.ALL, 5)

        self.savepath_btn = wx.Button(self.panel, wx.ID_ANY, u"Выбрать", wx.DefaultPosition, wx.Size(150, 25), 0)
        save.Add(self.savepath_btn, 0, wx.ALL, 5)

        vbox.Add(save, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        status = wx.BoxSizer(wx.HORIZONTAL)

        self.save_btn = wx.Button(self.panel, wx.ID_ANY, u"Сохранить", wx.DefaultPosition, wx.Size(125, 25), 0)
        status.Add(self.save_btn, 0, wx.ALL, 5)

        self.m_gauge1 = wx.Gauge(self.panel, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(350, 25), wx.GA_HORIZONTAL)
        self.m_gauge1.SetValue(0)
        status.Add(self.m_gauge1, 0, wx.ALL, 5)

        self.m_staticText4 = wx.StaticText(self.panel, wx.ID_ANY, u"Завершено", wx.DefaultPosition, wx.Size(-1, 25), 0)
        self.m_staticText4.Wrap(-1)

        status.Add(self.m_staticText4, 0, wx.ALIGN_BOTTOM | wx.ALL, 5)

        vbox.Add(status, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        self.panel.SetSizer(vbox)
        self.panel.Layout()
        mainSizer.Add(self.panel, 1, wx.ALL | wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 5)

        self.SetSizer(mainSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.chckvideo_btn.Bind(wx.EVT_BUTTON, self.checkvideo_click)
        self.savepath_btn.Bind(wx.EVT_BUTTON, self.saveas_click)
        self.save_btn.Bind(wx.EVT_BUTTON, self.download_click)

    def __del__(self):
        pass

    # Virtual event handlers, override them in your derived class
    def checkvideo_click(self, event):
        event.Skip()

    def saveas_click(self, event):
        event.Skip()

    def download_click(self, event):
        event.Skip()
