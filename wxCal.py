# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class cal
###########################################################################

class cal ( wx.Frame ):
    
    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"CAL", pos = wx.DefaultPosition, size = wx.Size( 420,386 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
        
        self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
        
        bSizer2 = wx.BoxSizer( wx.VERTICAL )
        
        self.txtIn = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 400,-1 ), wx.TE_RIGHT )
        bSizer2.Add( self.txtIn, 0, wx.ALL, 5 )
        
        gSizer2 = wx.GridSizer( 6, 4, 5, 5 )
        
        self.btn_fraction = wx.Button( self, wx.ID_ANY, u"1/x", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_fraction, 0, wx.ALL, 5 )
        
        self.btn_squared = wx.Button( self, wx.ID_ANY, u"x²", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_squared, 0, wx.ALL, 5 )
        
        self.btn_Clear = wx.Button( self, wx.ID_ANY, u"C", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_Clear, 0, wx.ALL, 5 )
        
        self.btn_del = wx.Button( self, wx.ID_ANY, u"←", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_del, 0, wx.ALL, 5 )
        
        self.btn_posNneg = wx.Button( self, wx.ID_ANY, u"+/-", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_posNneg, 0, wx.ALL, 5 )
        
        self.btn_root = wx.Button( self, wx.ID_ANY, u"√x", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_root, 0, wx.ALL, 5 )
        
        self.btn_dat = wx.Button( self, wx.ID_ANY, u".", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_dat, 0, wx.ALL, 5 )
        
        self.btn_mul = wx.Button( self, wx.ID_ANY, u"×", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_mul, 0, wx.ALL, 5 )
        
        self.btn_7 = wx.Button( self, wx.ID_ANY, u"7", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_7, 0, wx.ALL, 5 )
        
        self.btn_8 = wx.Button( self, wx.ID_ANY, u"8", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_8, 0, wx.ALL, 5 )
        
        self.btn_9 = wx.Button( self, wx.ID_ANY, u"9", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_9, 0, wx.ALL, 5 )
        
        self.btn_div = wx.Button( self, wx.ID_ANY, u"÷", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_div, 0, wx.ALL, 5 )
        
        self.btn_4 = wx.Button( self, wx.ID_ANY, u"4", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_4, 0, wx.ALL, 5 )
        
        self.btn_5 = wx.Button( self, wx.ID_ANY, u"5", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_5, 0, wx.ALL, 5 )
        
        self.btn_6 = wx.Button( self, wx.ID_ANY, u"6", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_6, 0, wx.ALL, 5 )
        
        self.btn_sub = wx.Button( self, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_sub, 0, wx.ALL, 5 )
        
        self.btn_1 = wx.Button( self, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_1, 0, wx.ALL, 5 )
        
        self.btn_2 = wx.Button( self, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_2, 0, wx.ALL, 5 )
        
        self.btn_3 = wx.Button( self, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_3, 0, wx.ALL, 5 )
        
        self.btn_add = wx.Button( self, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_add, 0, wx.ALL, 5 )
        
        self.btn_left = wx.Button( self, wx.ID_ANY, u"(", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_left, 0, wx.ALL, 5 )
        
        self.btn_0 = wx.Button( self, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_0, 0, wx.ALL, 5 )
        
        self.btn_right = wx.Button( self, wx.ID_ANY, u")", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_right, 0, wx.ALL, 5 )
        
        self.btn_cal = wx.Button( self, wx.ID_ANY, u"=", wx.DefaultPosition, wx.DefaultSize, 0 )
        gSizer2.Add( self.btn_cal, 0, wx.ALL, 5 )
        
        bSizer2.Add( gSizer2, 1, wx.EXPAND, 5 )
        
        
        self.SetSizer( bSizer2 )
        self.Layout()
        
        self.Centre( wx.BOTH )
        
        # Connect Events
        self.btn_fraction.Bind( wx.EVT_BUTTON, self.onFraction )
        self.btn_fraction.SetBackgroundColour(wx.Colour(153,255,102,0))
        self.btn_squared.Bind( wx.EVT_BUTTON, self.onSquared )
        self.btn_squared.SetBackgroundColour(wx.Colour(153,255,102,0))
        self.btn_Clear.Bind( wx.EVT_BUTTON, self.onClear )
        self.btn_Clear.SetBackgroundColour(wx.Colour(255,102,102,0))
        self.btn_del.Bind( wx.EVT_BUTTON, self.onDelete )
        self.btn_del.SetBackgroundColour(wx.Colour(255,102,102,0))
        self.btn_posNneg.Bind( wx.EVT_BUTTON, self.onPosNeg )
        self.btn_posNneg.SetBackgroundColour(wx.Colour(153,255,102,0))
        self.btn_root.Bind( wx.EVT_BUTTON, self.onRoot )
        self.btn_root.SetBackgroundColour(wx.Colour(153,255,102,0))
        self.btn_dat.Bind( wx.EVT_BUTTON, self.onDat )
        self.btn_dat.SetBackgroundColour(wx.YELLOW)
        self.btn_mul.Bind( wx.EVT_BUTTON, self.onMul )
        self.btn_mul.SetBackgroundColour(wx.Colour(153,153,204,0))
        self.btn_7.Bind( wx.EVT_BUTTON, self.onSeven )
        self.btn_7.SetBackgroundColour(wx.YELLOW)
        self.btn_8.Bind( wx.EVT_BUTTON, self.onEight )
        self.btn_8.SetBackgroundColour(wx.YELLOW)
        self.btn_9.Bind( wx.EVT_BUTTON, self.onNine )
        self.btn_9.SetBackgroundColour(wx.YELLOW)
        self.btn_div.Bind( wx.EVT_BUTTON, self.onDiv )
        self.btn_div.SetBackgroundColour(wx.Colour(153,153,204,0))
        self.btn_4.Bind( wx.EVT_BUTTON, self.onFour )
        self.btn_4.SetBackgroundColour(wx.YELLOW)
        self.btn_5.Bind( wx.EVT_BUTTON, self.onFive )
        self.btn_5.SetBackgroundColour(wx.YELLOW)
        self.btn_6.Bind( wx.EVT_BUTTON, self.onSix )
        self.btn_6.SetBackgroundColour(wx.YELLOW)
        self.btn_sub.Bind( wx.EVT_BUTTON, self.onSub )
        self.btn_sub.SetBackgroundColour(wx.Colour(153,153,204,0))
        self.btn_1.Bind( wx.EVT_BUTTON, self.onOne )
        self.btn_1.SetBackgroundColour(wx.YELLOW)
        self.btn_2.Bind( wx.EVT_BUTTON, self.onTwo )
        self.btn_2.SetBackgroundColour(wx.YELLOW)
        self.btn_3.Bind( wx.EVT_BUTTON, self.onThree )
        self.btn_3.SetBackgroundColour(wx.YELLOW)
        self.btn_add.Bind( wx.EVT_BUTTON, self.onAdd )
        self.btn_add.SetBackgroundColour(wx.Colour(153,153,204,0))
        self.btn_left.Bind( wx.EVT_BUTTON, self.onLeft )
        self.btn_left.SetBackgroundColour(wx.YELLOW)
        self.btn_0.Bind( wx.EVT_BUTTON, self.onZero )
        self.btn_0.SetBackgroundColour(wx.YELLOW)
        self.btn_right.Bind( wx.EVT_BUTTON, self.onRight )
        self.btn_right.SetBackgroundColour(wx.YELLOW)
        self.btn_cal.Bind( wx.EVT_BUTTON, self.onCal )
        self.btn_cal.SetBackgroundColour(wx.Colour(255,102,102,0))
    
    def __del__( self ):
        pass
    
    #############
    def display(self,event):
        if self.txtIn.GetLineText(0)=='0':
            self.txtIn.SetValue('')
        self.txtIn.AppenText(event.GetEventObject().GetLabel())
        event.Skipt()
    
    # Virtual event handlers, overide them in your derived class
    def onFraction( self, event ):
        data = eval('1/'+self.txtIn.GetValue())
        self.txtIn.SetValue(str(data))
        event.Skip()
    
    def onSquared( self, event ):
        data=eval(self.txtIn.GetValue()+'*'+self.txtIn.GetValue())
        self.txtIn.SetValue(str(data))
        event.Skip()
    
    def onClear( self, event ):
        self.txtIn.Clear()
        event.Skip()
    
    def onDelete( self, event ):
        back = self.txtIn.GetValue()
        # self.txtIn.Clear()
        self.txtIn.SetValue(back[:-1])
        event.Skip()
    
    def onPosNeg( self, event ):
        self.txtIn.AppendText('-')
        event.Skip()
    
    def onRoot( self, event ):
        data=eval(self.txtIn.GetValue()+'**0.5')
        self.txtIn.SetValue(str(data))
        event.Skip()
    
    def onDat( self, event ):
        self.txtIn.AppendText(".")
        event.Skip()
    
    def onMul( self, event ):
        self.txtIn.AppendText("*")
        event.Skip()
    
    def onSeven( self, event ):
        self.txtIn.AppendText("7")
        event.Skip()
    
    def onEight( self, event ):
        self.txtIn.AppendText("8")
        event.Skip()
    
    def onNine( self, event ):
        self.txtIn.AppendText("9")
        event.Skip()
    
    def onDiv( self, event ):
        self.txtIn.AppendText("/")
        event.Skip()
    
    def onFour( self, event ):
        self.txtIn.AppendText("4")
        event.Skip()
    
    def onFive( self, event ):
        self.txtIn.AppendText("5")
        event.Skip()
    
    def onSix( self, event ):
        self.txtIn.AppendText("6")
        event.Skip()
    
    def onSub( self, event ):
        self.txtIn.AppendText("-")
        event.Skip()
    
    def onOne( self, event ):
        self.txtIn.AppendText("1")
        event.Skip()
    
    def onTwo( self, event ):
        self.txtIn.AppendText("2")
        event.Skip()
    
    def onThree( self, event ):
        self.txtIn.AppendText("3")
        event.Skip()
    
    def onAdd( self, event ):
        self.txtIn.AppendText("+")
        event.Skip()
    
    def onLeft( self, event ):
        self.txtIn.AppendText("(")
        event.Skip()
    
    def onZero( self, event ):
        self.txtIn.AppendText("0")
        event.Skip()
    
    def onRight( self, event ):
        self.txtIn.AppendText(")")
        event.Skip()
    
    def onCal( self, event ):
        result = eval(self.txtIn.GetLineText(0))
        self.txtIn.SetValue(str(result))
        event.Skip()
    
#######메인#########################################
if __name__ == '__main__':
    app=wx.App()
    frame=cal(parent=None)
    frame.Show()
    app.MainLoop()
    
