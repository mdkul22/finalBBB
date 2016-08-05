import wx
from datetime import datetime
from threading import RLock, Thread
from screen_gui.py2uart import Logger
__author__ = "Mayunk Kulkarni"
global sensor_val, log, mpptdict, mcdict, gendict, batdict, thread, lock
sensor_val = {}
mpptdict = {}
mcdict = {}
gendict = {}
batdict = {}
lock = RLock()
log = Logger()


def serial_reading_function():
    while True:
        try:
            lock.acquire()
            log.checkr(log.readr())
        finally:
            lock.release()


class My_App(wx.App):

    def OnInit(self):
        self.frame = MyFrame(None)
        self.frame.Show()
        self.SetTopWindow(self.frame)
        return True

    def return_dict(self):
        return self.imp_dict

    def OnExit(self):
        print('Dying ...')


class MyFrame(wx.Frame):

    """initializing threads and locks"""

    def __init__(self, image, parent=None, id=-1,
                 title='Generic Title', pos=wx.DefaultPosition):

        size = (800, 480)
        wx.Frame.__init__(self, parent, id, 'GUI', pos, size)

        self.sizer_h = wx.BoxSizer(wx.HORIZONTAL)
        log = Logger()
        # thread
        thread = Thread(target=serial_reading_function())
        thread.start()

        self.imp_dict = log.checkr(log.readr())
        self.panel0 = MyPanel(self)
        self.sizer_h.Add(self.panel0, 1, wx.EXPAND)

        self.panel1 = MyPanel1(self)
        self.sizer_h.Add(self.panel1, 1, wx.EXPAND)

        self.panel2 = MyPanel2(self)
        self.sizer_h.Add(self.panel2, 1, wx.EXPAND)

        self.panel3 = MyPanel3(self)
        self.sizer_h.Add(self.panel3, 1, wx.EXPAND)

        self.SetSizer(self.sizer_h)
        self.panel0.Hide()
        self.panel1.Hide()
        self.panel2.Hide()
        self.panel3.ShowYourself()

    def ShutDown(self):
        self.Destroy()

        # Add a panel so it looks correct on all platforms


class MyPanel(wx.Panel):

    """Battery panel panel"""

    def __init__(self, parent, id=-1):
        """Constructor"""
        wx.Panel.__init__(self, parent, id, size=(800, 480))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        # dictionary update
        self.batupdater = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.DictUpdater, self.batupdater)
        self.batupdater.Start(100)
        # warning timer
        self.timerx = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.BatteryWarn, self.timerx)
        self.timerx.Start(10)
        # label updaters
        # 1
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatetq1, self.timer1)
        self.timer1.Start(10)
        # 2
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatetq2, self.timer2)
        self.timer2.Start(10)
        # 3
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatetq3, self.timer3)
        self.timer3.Start(10)
        # 4
        self.timer4 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatetq4, self.timer4)
        self.timer4.Start(10)
        # 5
        self.timer5 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemaxdc, self.timer5)
        self.timer5.Start(10)
        # 6
        self.timer6 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemindc, self.timer6)
        self.timer6.Start(10)
        # 7
        self.timer7 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemaxc, self.timer7)
        self.timer7.Start(10)
        # dictionary of lists
        self.imp_dict = {}
        # title
        title = wx.StaticText(self, -1, 'Battery')
        title.SetFont(wx.Font(24, wx.DEFAULT, wx.BOLD, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour('white')
        # label declarations
        self.labelOne = wx.StaticText(
            self, -1, 'Battery (NE) Temperature  :   ' + str(self.btq1))
        self.labelTwo = wx.StaticText(
            self, -1, 'Battery (NW) Temperature  :   ' + str(self.btq2))
        self.labelThree = wx.StaticText(
            self, -1, 'Battery (SE) Temperature  :   ' + str(self.btq3))
        self.labelFour = wx.StaticText(
            self, -1, 'Battery (SW) Temperature  :   ' + str(self.btq4))
        self.labelFive = wx.StaticText(
            self, -1, 'Max. Discharge Current  :   ' + str(self.maxdisc))
        self.labelSix = wx.StaticText(
            self, -1, 'Min. Discharge Current  :   ' + str(self.mindisc))
        self.labelSeven = wx.StaticText(
            self, -1, 'Battery (SW) Temperature  :   ' + str(self.maxc))
        # the label describers
        self.labelOne.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelOne.SetForegroundColour('white')
        self.labelTwo.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelTwo.SetForegroundColour('white')
        self.labelThree.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelThree.SetForegroundColour('white')
        self.labelFour.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelFour.SetForegroundColour('white')
        self.labelFive.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelFive.SetForegroundColour('white')
        self.labelSix.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelSix.SetForegroundColour('white')
        self.labelSeven.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelSeven.SetForegroundColour('white')

        # image button creation
        self.wbutton0 = wx.Button(
            self, -1, '-            M P P T               -')
        self.wbutton1 = wx.Button(
            self, -1, '-             B M S                -')
        self.wbutton2 = wx.Button(
            self, -1, '-           M O T O R              -')
        self.wbutton3 = wx.Button(
            self, -1, '-          G E N E R A L           -')

        imageFile = "mppt.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MPPTBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                  pos=(10, 20),
                                  size=(image1.GetWidth()+10,
                                        image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnMPPT, MPPTBtn)

        imageFile = "battery.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        BatteryBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                     pos=(10, 20),
                                     size=(image1.GetWidth()+10,
                                           image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, None, BatteryBtn)

        imageFile = "motor.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MotorBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                   pos=(10, 20),
                                   size=(image1.GetWidth()+10,
                                         image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnMotor, MotorBtn)

        imageFile = "general.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        GenBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                 pos=(10, 20),
                                 size=(image1.GetWidth()+10,
                                       image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnGeneral, GenBtn)

        # generating sizers
        topSizer = wx.BoxSizer(wx.VERTICAL)
        toolBtn = wx.BoxSizer(wx.HORIZONTAL)
        toolBtn_h = wx.BoxSizer(wx.VERTICAL)
        warnSizer = wx.BoxSizer(wx.HORIZONTAL)
        warnSizer_h = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFiveSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputSixSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputSevenSizer = wx.BoxSizer(wx.HORIZONTAL)

        # adding toolbar
        toolBtn.Add(MPPTBtn, 0, wx.ALL, 5)
        toolBtn.Add(BatteryBtn, 0, wx.ALL, 5)
        toolBtn.Add(MotorBtn, 0, wx.ALL, 5)
        toolBtn.Add(GenBtn, 0, wx.ALL, 5)
        # adding them in a vertical sizer to center them completely
        toolBtn_h.Add(toolBtn, 0, wx.CENTER, 5)
        # same done for warnsizers
        warnSizer.Add(self.wbutton0, 0, wx.ALL, 5)
        warnSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        warnSizer.Add(self.wbutton1, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton2, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton3, 0, wx.ALL, 5)

        warnSizer_h.Add(warnSizer, 0, wx.CENTER, 5)

        titleSizer.Add(title, 0, wx.ALL, 5)
        inputOneSizer.Add(self.labelOne, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.labelTwo, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.labelThree, 0, wx.ALL, 5)
        inputFourSizer.Add(self.labelFour, 0, wx.ALL, 5)
        inputFiveSizer.Add(self.labelFive, 0, wx.ALL, 5)
        inputSixSizer.Add(self.labelSix, 0, wx.ALL, 5)

        topSizer.Add(toolBtn_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(warnSizer_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputOneSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputTwoSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputThreeSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputFourSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputFiveSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputSixSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputSevenSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(topSizer)
        topSizer.Fit(self)

        self.Raise()
        self.SetPosition((0, 0))
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # value declarations

        self.btq1 = 0
        self.btq2 = 0
        self.btq3 = 0
        self.btq4 = 0
        self.maxdisc = 0
        self.mindisc = 0
        self.maxc = 0

    def DictUpdater(self, event):
        self.imp_dict = log.return_bat()

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        start_image1 = wx.Image("solarcar.jpg")
        start_image1.Rescale(1310, 800)
        bmp = wx.BitmapFromImage(start_image1)
        dc.DrawBitmap(bmp, 0, 0)

    def closeProgram(self):
        self.Destroy()

    def BatteryWarn(self, event):
        """warner for all seven values"""
        if self.GetParent().panel0.IsShown():
            self.wbutton1.SetBackgroundColour('white')
            if self.btq1 > 65:
                self.labelOne.SetForegroundColour('red')
            else:
                self.labelOne.SetForegroundColour('white')
            if self.btq2 > 65:
                self.labelTwo.SetForegroundColour('red')
            else:
                self.labelTwo.SetForegroundColour('white')
            if self.btq3 > 65:
                self.labelThree.SetForegroundColour('red')
            else:
                self.labelThree.SetForegroundColour('white')
            if self.btq4 > 65:
                self.labelFour.SetForegroundColour('red')
            else:
                self.labelFour.SetForegroundColour('white')
            if self.maxdisc > 600:
                self.labelFive.SetForegroundColour('red')
            else:
                self.labelFive.SetForegroundColour('white')
            if self.mindisc < 500:
                self.labelSix.SetForegroundColour('red')
            else:
                self.labelSix.SetForegroundColour('white')
            if self.maxc > 600:
                self.labelTwo.SetForegroundColour('red')
            else:
                self.labelTwo.SetForegroundColour('white')

        elif (self.btq1, self.btq2, self.btq2, self.btq4) > 65 or (self.maxc, self.maxdisc) > 600 or self.mindisc < 500:
            self.wbutton1.SetBackgroundColour('red')
            self.GetParent().panel1.wbutton1.SetBackgroundColour('red')
            self.GetParent().panel2.wbutton1.SetBackgroundColour('red')
            self.GetParent().panel3.wbutton1.SetBackgroundColour('red')

    def updatetq1(self, event):
        """battery NE quadrant temperature"""
        self.btq1 = self.imp_dict["btq1"][len(self.imp_dict["btq1"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq1.txt', 'a')
        txt.write(str(self.btq1) + "," + t + "\n")
        self.labelOne.SetLabel('Temperature  : ' + str(self.btq1) + ' C')
        self.Refresh()

    def updatetq2(self, event):
        """battery NW quadrant temperature"""
        self.btq2 = self.imp_dict["btq2"][len(self.imp_dict["btq2"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq2.txt', 'a')
        txt.write(str(self.btq2) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.btq2) + ' C')
        self.Refresh()

    def updatetq3(self, event):
        """battery SE quadrant temperature"""
        self.btq3 = self.imp_dict["btq3"][len(self.imp_dict["btq3"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq3.txt', 'a')
        txt.write(str(self.btq3) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.btq3) + ' C')
        self.Refresh()

    def updatetq4(self, event):
        """battery SW quadrant temperature"""
        self.btq4 = self.imp_dict["btq4"][len(self.imp_dict["btq4"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq4.txt', 'a')
        txt.write(str(self.btq4) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.btq4) + ' C')
        self.Refresh()

    def updatemaxdc(self, event):
        """max. discharge current"""
        self.maxdisc = self.imp_dict["maxdiscC"][
            len(self.imp_dict["maxdiscC"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('maxdiscC.txt', 'a')
        txt.write(str(self.maxdisc) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.maxdisc) + ' A')
        self.Refresh()

    def updatemindc(self, event):
        """min. discharge current"""
        self.mindisc = self.imp_dict["mindiscC"][
            len(self.imp_dict["mindiscC"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mindiscC.txt', 'a')
        txt.write(str(self.mindisc) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.mindisc) + ' A')
        self.Refresh()

    def updatemaxc(self, event):
        """max current"""
        self.maxc = self.imp_dict["btq3"][len(self.imp_dict["btq3"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('battery_current.txt', 'a')
        txt.write(str(self.maxc) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.maxc) + ' A')
        self.Refresh()

    def ShowYourself(self):
        l = self.GetParent().GetSize()
        self.SetSize(l)
        self.Raise()
        self.SetPosition((0, 0))
        self.Show()

    def OnMPPT(self, event):
        self.Hide()
        self.GetParent().panel1.ShowYourself()

    def OnMotor(self, event):
        self.Hide()
        self.GetParent().panel2.ShowYourself()

    def OnGeneral(self, event):
        self.Hide()
        self.GetParent().panel3.ShowYourself()


class MyPanel1(wx.Panel):

    """MPPT panel class"""

    def __init__(self, parent, id=-1):
        """Constructor"""
        wx.Panel.__init__(self, parent, id, size=(800, 480))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        # dictionary update
        self.mpptupdater = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.DictUpdater, self.mpptupdater)
        self.mpptupdater.Start(100)
        # warning timer
        self.timerx = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MPPTWarn, self.timerx)
        self.timerx.Start(10)
        # label updater
        # 1
        self.timer = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemppt2bat(), self.timer1)
        self.timer1.Start(10)
        # 2
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatesp2mppt(), self.timer2)
        self.timer2.Start(10)
        # dictionary of lists

        # buttons and labels
        title = wx.StaticText(self, -1, 'MPPT')
        title.SetFont(
            wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.BOLD, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour('white')
        # label declarations
        self.labelOne = wx.StaticText(
            self, -1, 'Panels to MPPT : ' + str(self.sp2mppt))
        self.labelTwo = wx.StaticText(
            self, -1, 'MPPT to Battery : ' + str(self.mppt2bat))
        # label describers
        self.labelOne.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelTwo.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelTwo.SetForegroundColour('white')

        self.wbutton0 = wx.Button(
            self, -1, '-            M P P T              -')
        self.wbutton1 = wx.Button(
            self, -1, '-             B M S                -')
        self.wbutton2 = wx.Button(
            self, -1, '-           M O T O R              -')
        self.wbutton3 = wx.Button(
            self, -1, '-          G E N E R A L           -')

        imageFile = "battery.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        BatteryBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                     pos=(10, 20),
                                     size=(image1.GetWidth()+10,
                                           image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnBattery, BatteryBtn)

        imageFile = "mppt.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MPPTBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                  pos=(10, 20),
                                  size=(image1.GetWidth()+10,
                                        image1.GetHeight()+10))

        imageFile = "motor.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MotorBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                   pos=(10, 20),
                                   size=(image1.GetWidth()+10,
                                         image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnMotor, MotorBtn)

        self.Bind(wx.EVT_BUTTON, None, MPPTBtn)

        imageFile = "general.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        GenBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                 pos=(10, 20),
                                 size=(image1.GetWidth()+10,
                                       image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnGeneral, GenBtn)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        toolBtn = wx.BoxSizer(wx.HORIZONTAL)
        toolBtn_h = wx.BoxSizer(wx.VERTICAL)
        warnSizer = wx.BoxSizer(wx.HORIZONTAL)
        warnSizer_h = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)

        toolBtn.Add(MPPTBtn, 0, wx.ALL, 5)
        toolBtn.Add(BatteryBtn, 0, wx.ALL, 5)
        toolBtn.Add(MotorBtn, 0, wx.ALL, 5)
        toolBtn.Add(GenBtn, 0, wx.ALL, 5)
        toolBtn_h.Add(toolBtn, 0, wx.CENTER, 5)

        warnSizer.Add(self.wbutton0, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton1, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton2, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton3, 0, wx.ALL, 5)
        warnSizer_h.Add(warnSizer, 0, wx.CENTER, 5)

        titleSizer.Add(title, 0, wx.ALL, 5)
        inputOneSizer.Add(self.labelOne, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.labelTwo, 0, wx.ALL, 5)

        topSizer.Add(toolBtn_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(warnSizer_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputOneSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputTwoSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(topSizer)
        topSizer.Fit(self)

        self.Raise()
        self.SetPosition((0, 0))
        self.Hide()
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)

    def DictUpdater(self, event):
        self.imp_dict = log.return_mppt()

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        start_image1 = wx.Image("solarcar.jpg")
        start_image1.Rescale(1310, 800)
        bmp = wx.BitmapFromImage(start_image1)
        dc.DrawBitmap(bmp, 0, 0)

    def MPPTWarn(self, event):
        """warner for two values"""
        if self.GetParent().panel1.IsShown():
            self.wbutton0.SetBackgroundColour('white')
            if self.sp2mppt > 9:
                self.labelOne.SetForegroundColour('red')
            else:
                self.labelOne.SetForegroundColour('white')
            if self.mppt2bat > 22:
                self.labelTwo.SetForegroundColour('red')
            else:
                self.labelTwo.SetForegroundColour('white')
        elif self.mppt2bat > 9 or self.sp2mppt > 22:
            self.wbutton0.SetBackgroundColour('red')
            self.GetParent().panel0.wbutton0.SetBackgroundColour('red')
            self.GetParent().panel2.wbutton0.SetBackgroundColour('red')
            self.GetParent().panel3.wbutton0.SetBackgroundColour('red')

    def onOK(self, event):
        # Do something
        print('onOK handler')

    def onCancel(self, event):
        self.closeProgram()

    def closeProgram(self):
        self.Destroy()

    def updatemppt2bat(self, event):
        """MPPT to battery"""
        self.mppt2bat = self.imp_dict["mppt2bat"][
            len(self.imp_dict["mppt2bat"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mppt2bat.txt', 'a')
        txt.write(str(self.mppt2bat) + "," + t + "\n")
        self.labelOne.SetLabel(
            'MPPT to Battery  : ' + str(self.mppt2bat) + ' A')
        self.Refresh()

    def updatesp2mppt(self, event):
        """Solar Panels to MPPT"""
        self.sp2mppt = self.imp_dict["sp2mppt"][
            len(self.imp_dict["mppt2bat"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('sp2mppt.txt', 'a')
        txt.write(str(self.sp2mppt) + "," + t + "\n")
        self.labelOne.SetLabel('Panels to MPPT  : ' + str(self.sp2mppt) + ' A')
        self.Refresh()

    def ShowYourself(self):
        l = self.GetParent().GetSize()
        self.SetSize(l)
        self.Raise()
        self.SetPosition((0, 0))
        self.Show()

    def OnMotor(self, event):
        self.Hide()
        self.GetParent().panel2.ShowYourself()

    def OnBattery(self, event):
        self.Hide()
        self.GetParent().panel0.ShowYourself()

    def OnGeneral(self, event):
        self.Hide()
        self.GetParent().panel3.ShowYourself()


class MyPanel2(wx.Panel):

    """Motor controller panel"""

    def __init__(self, parent, id=-1):
        """Constructor"""
        wx.Panel.__init__(self, parent, id, size=(800, 480))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        # timer for updating dictionary
        self.mcupdater = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.DictUpdater, self.mcupdater)
        # timer for warning
        self.timerx = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.MotorWarn, self.timerx)
        self.timerx.Start(10)
        # timer
        # 1
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemtl, self.timer1)
        self.timer1.Start(10)
        # 2
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemtr, self.timer2)
        self.timer2.Start(10)
        # 3
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemct, self.timer3)
        self.timer3.Start(10)
        # 4
        self.timer4 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemc2mrc, self.timer4)
        self.timer4.Start(10)
        # 5
        self.timer5 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemc2mlc, self.timer5)
        self.timer5.Start(10)
        # 6
        self.timer6 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatemc2bc, self.timer6)
        self.timer6.Start(10)

        # title
        title = wx.StaticText(self, -1, 'Motor Controller')
        title.SetFont(
            wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.BOLD, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour('white')
        # label declarations
        self.labelOne = wx.StaticText(self, -1, 'Motor Controller Temp. : ')
        self.labelTwo = wx.StaticText(self, -1, 'Motor(L) Temp. : ')
        self.labelThree = wx.StaticText(self, -1, 'Motor(R) Temp. : ')
        self.labelFour = wx.StaticText(self, -1, 'MC to Motor(L) : ')
        self.labelFive = wx.StaticText(self, -1, 'MC to Motor(R) : ')
        self.labelSix = wx.StaticText(self, -1, 'MC to BMS : ')
        # label describers
        self.labelOne.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelOne.SetForegroundColour('white')
        self.labelTwo.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelTwo.SetForegroundColour('white')
        self.labelThree.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelThree.SetForegroundColour('white')
        self.labelFour.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelFour.SetForegroundColour('white')
        self.labelFive.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelFive.SetForegroundColour('white')
        self.labelSix.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelSix.SetForegroundColour('white')
        # button creators
        self.wbutton0 = wx.Button(
            self, -1, '-            M P P T               -')
        self.wbutton1 = wx.Button(
            self, -1, '-             B M S                -')
        self.wbutton2 = wx.Button(
            self, -1, '-           M O T O R              -')
        self.wbutton3 = wx.Button(
            self, -1, '-          G E N E R A L           -')
        # image button declaration
        imageFile = "mppt.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MPPTBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                  pos=(10, 20),
                                  size=(image1.GetWidth()+10,
                                        image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnMPPT, MPPTBtn)

        imageFile = "battery.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        BatteryBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                     pos=(10, 20),
                                     size=(image1.GetWidth()+10,
                                           image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnBattery, BatteryBtn)

        imageFile = "motor.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MotorBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                   pos=(10, 20),
                                   size=(image1.GetWidth()+10,
                                         image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, None, MotorBtn)

        imageFile = "general.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        GenBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                 pos=(10, 20),
                                 size=(image1.GetWidth()+10,
                                       image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnGeneral, GenBtn)
        # sizer generators
        topSizer = wx.BoxSizer(wx.VERTICAL)
        toolBtn = wx.BoxSizer(wx.HORIZONTAL)
        toolBtn_h = wx.BoxSizer(wx.VERTICAL)
        warnSizer = wx.BoxSizer(wx.HORIZONTAL)
        warnSizer_h = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFiveSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputSixSizer = wx.BoxSizer(wx.HORIZONTAL)

        toolBtn.Add(MPPTBtn, 0, wx.ALL, 5)
        toolBtn.Add(BatteryBtn, 0, wx.ALL, 5)
        toolBtn.Add(MotorBtn, 0, wx.ALL, 5)
        toolBtn.Add(GenBtn, 0, wx.ALL, 5)
        toolBtn_h.Add(toolBtn, 0, wx.CENTER, 5)

        warnSizer.Add(self.wbutton0, 0, wx.ALL, 5)
        warnSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        warnSizer.Add(self.wbutton1, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton2, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton3, 0, wx.ALL, 5)
        warnSizer_h.Add(warnSizer, 0, wx.CENTER, 5)

        titleSizer.Add(title, 0, wx.ALL, 5)
        inputOneSizer.Add(self.labelOne, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.labelTwo, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.labelThree, 0, wx.ALL, 5)
        inputFourSizer.Add(self.labelFour, 0, wx.ALL, 5)
        inputFiveSizer.Add(self.labelFive, 0, wx.ALL, 5)
        inputSixSizer.Add(self.labelSix, 0, wx.ALL, 5)

        topSizer.Add(toolBtn_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(warnSizer_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputOneSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputTwoSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputThreeSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputFourSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputFiveSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputSixSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(topSizer)
        topSizer.Fit(self)

        self.Raise()
        self.SetPosition((0, 0))
        self.Hide()
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # value declarations

        self.mct = 0
        self.mtl = 0
        self.mtr = 0
        self.mc2bc = 0
        self.mc2mlc = 0
        self.mc2mrc = 0

    def DictUpdater(self, event):
        self.imp_dict = log.return_mc()

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        start_image1 = wx.Image("solarcar.jpg")
        start_image1.Rescale(1310, 800)
        bmp = wx.BitmapFromImage(start_image1)
        dc.DrawBitmap(bmp, 0, 0)

    def MotorWarn(self, event):
        """warner for all six values"""
        if self.GetParent().panel0.IsShown():
            self.wbutton1.SetBackgroundColour('white')
            if self.mct > 45:
                self.labelOne.SetForegroundColour('red')
            else:
                self.labelOne.SetForegroundColour('white')
            if self.mtl > 65:
                self.labelTwo.SetForegroundColour('red')
            else:
                self.labelTwo.SetForegroundColour('white')
            if self.mtr > 65:
                self.labelThree.SetForegroundColour('red')
            else:
                self.labelThree.SetForegroundColour('white')
            if self.mc2mlc > 350:
                self.labelFour.SetForegroundColour('red')
            else:
                self.labelFour.SetForegroundColour('white')
            if self.mc2mrc > 350:
                self.labelFive.SetForegroundColour('red')
            else:
                self.labelFive.SetForegroundColour('white')
            if self.mc2bc < 250:
                self.labelSix.SetForegroundColour('red')
            else:
                self.labelSix.SetForegroundColour('white')

        elif self.mct > 45 or (self.mtl, self.mtr) > 65 or (self.mc2mrc, self.mc2mlc) > 350 or self.mc2bc > 250:
            self.wbutton1.SetBackgroundColour('red')
            self.GetParent().panel1.wbutton1.SetBackgroundColour('red')
            self.GetParent().panel2.wbutton1.SetBackgroundColour('red')
            self.GetParent().panel3.wbutton1.SetBackgroundColour('red')

    def closeProgram(self):
        self.Destroy()

    def updatemct(self, event):
        """motor controller temperature"""
        self.mct = self.imp_dict["mct"][len(self.imp_dict["mct"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mct.txt', 'a')
        txt.write(str(self.mct) + "," + t + "\n")
        self.labelOne.SetLabel('Motor Controller Temp. : ' + str(self.btq2) + ' C')
        self.Refresh()

    def updatemtr(self, event):
        """left motor temperature"""
        self.mtr = self.imp_dict["mtl"][len(self.imp_dict["mtl"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mtl.txt', 'a')
        txt.write(str(self.mtl) + "," + t + "\n")
        self.labelThree.SetLabel('Motor(R) Temp. : ' + str(self.mtl) + ' C')
        self.Refresh()

    def updatemc2mlc(self, event):
        """motor controller to left motor current"""
        self.mtr = self.imp_dict["mc2mlc"][len(self.imp_dict["mc2mlc"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mc2mlc.txt', 'a')
        txt.write(str(self.mc2mlc) + "," + t + "\n")
        self.labelFour.SetLabel('MC to Motor(L) : ' + str(self.mc2mlc) + ' A')
        self.Refresh()

    def updatemtl(self, event):
        """left motor temperature"""
        self.mtl = self.imp_dict["mtl"][len(self.imp_dict["mtl"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mtl.txt', 'a')
        txt.write(str(self.mtl) + "," + t + "\n")
        self.labelThree.SetLabel('Motor(L) Temp. : ' + str(self.mtr) + ' C')
        self.Refresh()

    def updatemc2mrc(self, event):
        """Motor controller to Motor(R)"""
        self.mc2mrc = self.imp_dict["mc2mrc"][len(self.imp_dict["mc2mrc"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mc2mrc.txt', 'a')
        txt.write(str(self.mc2mrc) + "," + t + "\n")
        self.labelFive.SetLabel('MC to Motor(R) : ' + str(self.mc2mrc) + ' A')
        self.Refresh()

    def updatemc2bc(self, event):
        """motor controller to BMS"""
        self.mc2bc = self.imp_dict["mc2bc"][len(self.imp_dict["mc2bc"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('mc2bc.txt', 'a')
        txt.write(str(self.mc2bc) + "," + t + "\n")
        self.labelSix.SetLabel('MC to BMS : ' + str(self.mc2bc) + ' A')
        self.Refresh()

    def ShowYourself(self):
        l = self.GetParent().GetSize()
        self.SetSize(l)
        self.Raise()
        self.SetPosition((0, 0))
        self.Show()

    def OnMPPT(self, event):
        self.Hide()
        self.GetParent().panel1.ShowYourself()

    def OnBattery(self, event):
        self.Hide()
        self.GetParent().panel0.ShowYourself()

    def OnGeneral(self, event):
        self.Hide()
        self.GetParent().panel3.ShowYourself()


class MyPanel3(wx.Panel):
    """General Panel class"""

    def __init__(self, parent, id=-1):
        """Constructor"""
        wx.Panel.__init__(self, parent, id, size=(800, 480))
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        # timer for updating dictionary
        self.genupdater = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.genupdater, self.genupdater)
        # timers
        # 1
        self.timer1 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatesoc, self.timer1)
        self.timer1.Start(10)
        # 2
        self.timer2 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatespeedfl, self.timer2)
        self.timer2.Start(10)
        # 3
        self.timer3 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatespeedfr, self.timer3)
        self.timer3.Start(10)
        # 4
        self.timer4 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatespeedbl, self.timer4)
        self.timer4.Start(10)
        # 5
        self.timer5 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updatespeedbr, self.timer5)
        self.timer5.Start(10)
        # 6
        self.timer6 = wx.Timer(self)
        self.Bind(wx.EVT_TIMER, self.updateoiltemp, self.timer6)
        self.timer6.Start(9)

        # title creator
        title = wx.StaticText(self, -1, 'General')
        title.SetFont(
            wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.BOLD, wx.FONTWEIGHT_BOLD))
        title.SetForegroundColour('white')
        # label declarations
        self.labelOne = wx.StaticText(self, -1)
        self.labelOne.SetLabel('Car Speed (FR FL) : ')
        self.labelTwo = wx.StaticText(self, -1)
        self.labelTwo.SetLabel('Car speed (BR BL) : ')
        self.labelThree = wx.StaticText(self, -1)
        self.labelThree.SetLabel('Ambient Temperature :')
        self.labelFour = wx.StaticText(self, -1)
        self.labelFour.SetLabel('Oil temperature : ')
        self.labelFive = wx.StaticText(self, -1)
        self.labelFive.SetLabel('State of Charge : ')
        # label describers
        self.labelOne.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelOne.SetForegroundColour('white')
        self.labelTwo.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelTwo.SetForegroundColour('white')
        self.labelThree.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelThree.SetForegroundColour('white')
        self.labelFour.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelFour.SetForegroundColour('white')
        self.labelFive.SetFont(
            wx.Font(20, wx.FONTFAMILY_DECORATIVE, wx.BOLD, wx.FONTWEIGHT_BOLD))
        self.labelFive.SetForegroundColour('white')
        # image buttons
        self.wbutton0 = wx.Button(
            self, -1, '-            M P P T               -')
        self.wbutton1 = wx.Button(
            self, -1, '-             B M S                -')
        self.wbutton2 = wx.Button(
            self, -1, '-           M O T O R              -')
        self.wbutton3 = wx.Button(
            self, -1, '-          G E N E R A L           -')

        imageFile = "battery.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        BatteryBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                     pos=(10, 20),
                                     size=(image1.GetWidth() + 10,
                                           image1.GetHeight() + 10))

        self.Bind(wx.EVT_BUTTON, self.OnBattery, BatteryBtn)

        imageFile = "mppt.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MPPTBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                  pos=(10, 20),
                                  size=(image1.GetWidth() + 10,
                                        image1.GetHeight() + 10))
        self.Bind(wx.EVT_BUTTON, self.OnMotor, MPPTBtn)

        imageFile = "motor.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        MotorBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                   pos=(10, 20),
                                   size=(image1.GetWidth()+10,
                                         image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, self.OnMotor, MotorBtn)

        imageFile = "general.png"
        image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        GenBtn = wx.BitmapButton(self, id=-1, bitmap=image1,
                                 pos=(10, 20),
                                 size=(image1.GetWidth()+10,
                                       image1.GetHeight()+10))

        self.Bind(wx.EVT_BUTTON, None, GenBtn)

        topSizer = wx.BoxSizer(wx.VERTICAL)
        toolBtn = wx.BoxSizer(wx.HORIZONTAL)
        toolBtn_h = wx.BoxSizer(wx.VERTICAL)
        warnSizer = wx.BoxSizer(wx.HORIZONTAL)
        warnSizer_h = wx.BoxSizer(wx.VERTICAL)
        titleSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputOneSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputTwoSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputThreeSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFourSizer = wx.BoxSizer(wx.HORIZONTAL)
        inputFiveSizer = wx.BoxSizer(wx.HORIZONTAL)

        toolBtn.Add(MPPTBtn, 0, wx.ALL, 5)
        toolBtn.Add(BatteryBtn, 0, wx.ALL, 5)
        toolBtn.Add(MotorBtn, 0, wx.ALL, 5)
        toolBtn.Add(GenBtn, 0, wx.ALL, 5)
        toolBtn_h.Add(toolBtn, 0, wx.CENTER, 5)

        warnSizer.Add(self.wbutton0, 0, wx.ALL, 5)
        warnSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        warnSizer.Add(self.wbutton1, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton2, 0, wx.ALL, 5)
        warnSizer.Add(self.wbutton3, 0, wx.ALL, 5)
        warnSizer_h.Add(warnSizer, 0, wx.CENTER, 5)

        titleSizer.Add(title, 0, wx.ALL, 5)
        inputOneSizer.Add(self.labelOne, 0, wx.ALL, 5)
        inputTwoSizer.Add(self.labelTwo, 0, wx.ALL, 5)
        inputThreeSizer.Add(self.labelThree, 0, wx.ALL, 5)
        inputFourSizer.Add(self.labelFour, 0, wx.ALL, 5)
        inputFiveSizer.Add(self.labelFive, 0, wx.ALL, 5)

        topSizer.Add(toolBtn_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(warnSizer_h, 0, wx.ALL | wx.EXPAND | wx.CENTER, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(titleSizer, 0, wx.CENTER)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputOneSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputTwoSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputThreeSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputFourSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(inputFiveSizer, 0, wx.ALL | wx.EXPAND, 5)
        topSizer.Add(wx.StaticLine(self), 0, wx.ALL | wx.EXPAND, 5)

        self.SetSizer(topSizer)
        topSizer.Fit(self)
        self.Raise()
        self.SetPosition((0, 0))
        self.Hide()
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
        # value declarations
        self.speedfl = 0
        self.speedfr = 0
        self.speedbr = 0
        self.speedbl = 0
        self.oiltemp = 0
        self.soc = 0

    def DictUpdater(self, event):
        self.imp_dict = log.return_general()

    def OnEraseBackground(self, evt):
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        start_image1 = wx.Image("solarcar.jpg")
        start_image1.Rescale(1310, 800)
        bmp = wx.BitmapFromImage(start_image1)
        dc.DrawBitmap(bmp, 0, 0)

    def updatetq1(self, event):
        """battery NE quadrant temperature"""
        self.btq1 = self.imp_dict["btq1"][len(self.imp_dict["btq1"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq1.txt', 'a')
        txt.write(str(self.btq1) + "," + t + "\n")
        self.labelOne.SetLabel('Temperature  : ' + str(self.btq1) + ' C')
        self.Refresh()

    def update(self, event):
        """battery NW quadrant temperature"""
        self.btq2 = self.imp_dict["btq2"][len(self.imp_dict["btq2"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq2.txt', 'a')
        txt.write(str(self.btq2) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.btq2) + ' C')
        self.Refresh()

    def updatetq3(self, event):
        """battery SE quadrant temperature"""
        self.btq3 = self.imp_dict["btq3"][len(self.imp_dict["btq3"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq3.txt', 'a')
        txt.write(str(self.btq3) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.btq3) + ' C')
        self.Refresh()

    def updatetq4(self, event):
        """battery SW quadrant temperature"""
        self.btq4 = self.imp_dict["btq4"][len(self.imp_dict["btq4"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('btq4.txt', 'a')
        txt.write(str(self.btq4) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.btq4) + ' C')
        self.Refresh()

    def updatemaxdc(self, event):
        """max. discharge current"""
        self.maxdisc = self.imp_dict["maxdiscC"][
            len(self.imp_dict["maxdiscC"]) - 1]
        t = datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y")
        txt = open('maxdiscC.txt', 'a')
        txt.write(str(self.maxdisc) + "," + t + "\n")
        self.labelTwo.SetLabel('Battery Current : ' + str(self.maxdisc) + ' A')
        self.Refresh()

    def closeProgram(self):
        self.Destroy()

    def ShowYourself(self):
        l = self.GetParent().GetSize()
        self.SetSize(l)
        self.Raise()
        self.SetPosition((0, 0))
        self.Show()

    def OnMotor(self, event):
        self.Hide()
        self.GetParent().panel2.ShowYourself()

    def OnMPPT(self, event):
        self.Hide()
        self.GetParent().panel1.ShowYourself()

    def OnBattery(self, event):
        self.Hide()
        self.GetParent().panel0.ShowYourself()


def main(val):
    app = My_App(redirect=False, sensor_dict=val)
    app.MainLoop()

if __name__ == '__main__':
    main()
