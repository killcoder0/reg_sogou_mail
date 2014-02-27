#!/usr/bin/python
# -*- coding:utf-8 -*-

import wx
import os

class MyDialog(wx.Dialog):
    def __init__(self):
        self.dirname=""
        self.file =""
        wx.Dialog.__init__(self,None,-1,u'LogParserTools',wx.DefaultPosition,wx.Size(700, 500))
        panel=wx.Panel(self,-1)
        self.Center()
        wx.StaticBox(self, -1, 'ParserFailUrl', (5, 30), size=(270, 200)) 
        self.inputText1= wx.TextCtrl(self,-1,"",pos=(80,60),size=(160,20))
        self.button = wx.Button(self,-1,u"..."  ,pos=(250,63),size=(20,20))
        self.Bind(wx.EVT_BUTTON,self.open_logic_path,self.button)
        self.ca = wx.CheckBox(self, -1, 'Show Num', (100, 100))
        self.cb = wx.CheckBox(self, -1, 'Show Info', (100, 120))
        self.cb.SetValue(True)
        self.button1=wx.Button(self,-1,u"check",pos=(100,160),size=(40,25))
        self.Bind(wx.EVT_BUTTON,self.parser_log,self.button1) 
        wx.StaticBox(self,-1,u'Result',(300,16),size=(300, 380))
        self.inputText2= wx.TextCtrl(self,-1,"",pos=(300,30),size=(300,380),style=wx.TE_MULTILINE|wx.HSCROLL)
 
    def open_logic_path(self,event):
        dlg = wx.FileDialog(self, "Choose a file", self.dirname, "", "*.*", wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.filename = dlg.GetFilename()
            self.dirname = dlg.GetDirectory()
            self.file = os.path.join(self.dirname, self.filename)
            self.inputText1.SetValue(self.file)
        dlg.Destroy()

    def parser_log(self,even):
        if self.inputText1.GetValue() =="":
            end_result ="Please Open log!!!"
            self.inputText2.SetValue(end_result) 
        else:
            if self.inputText1.GetValue().find("logic")>0:
                fail_url_list = []
                request_list = []
                try:
                    log=open(self.inputText1.GetValue(),'r')
                    for line in log:
                        mylist = line.split(',')
                    #    url = mylist[7]
                    #    result = url[1:-2]
                    #    URL_error.append(result)
                    #sss = set(URL_error)
                        if mylist[4]=="[{}]"and mylist[5]=="[ParseMediaHTML]" and mylist[6]=="[fail]":
                            url = mylist[7][1:-2]
                            fail_url_list.append(url)
                        elif mylist[4]=="[None]" and mylist[5]=="[Request]" and mylist[6]=="[fail]":
                            request_url = mylist[7][1:-2]
                            request_list.append(request_url)
                        else:
                            continue
                    if self.ca.GetValue() == True and self.cb.GetValue() == False:
                         error_num = len(fail_url_list)
                         error_num_request = len(request_list)
                         end_result = ("the num of parser fail url is=======" +str(error_num)+"\r\n"
                                          +"the num of request timeout is =====" +str(error_num_request)+"\r\n")
                    elif self.ca.GetValue() == False and self.cb.GetValue() == True:
                          end_result = "the parser fail url info is =======" + str(fail_url_list)+"\r\n"
                    elif self.ca.GetValue() == True and self.cb.GetValue() == True:
                         error_num = len(fail_url_list)
                         error_num_request = len(request_list)
                         end_result = ("++++++++++++++++++++++++++++"+"\r\n"
                                        +"++++++++++++++++++++++++++++"+"\r\n"
                                        +"the num of parser fail url is===" 
                                        +str(error_num)+"\r\n"
                                        +"the num of request timeout is==="
                                        +str(error_num_request)+"\r\n"
                                        +"++++++++++++++++++++++++++++"+"\r\n"
                                        +"++++++++++++++++++++++++++++"+"\r\n"
                                        +"the parser fail url info is "+"\r\n"
                                        + str(fail_url_list) )
                    elif self.ca.GetValue() == False and self.cb.GetValue() == False:
                         end_result = "Please check the checkbox!!"
                except Exception,e:
                    end_result = "error!!!\r\n"+"the logFile is not the right one!!\r\n"+str(e)
            else:
                end_result ="Please open the right log txt for logic!!!"

            self.inputText2.SetValue(end_result)

if __name__=='__main__':
    app = wx.App()         
    frame = MyDialog()    
    frame.Show(True)
    app.MainLoop()