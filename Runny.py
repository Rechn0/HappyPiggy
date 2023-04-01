import pygame
import PySimpleGUI as Fs
import sys
import time

from PyGaMeeRunny import PyGaMeeRunny


class Runny:
    def __init__(self):
        self.UserList = [
            {"账号": "PAPA", "密码": "REC"},
            {"账号": "MAMA", "密码": "HZQ"}
        ]

        Fs.theme_border_width(30)
        Fs.theme_button_color("purple")
        Fs.theme_text_element_background_color("pink")
        Fs.theme_background_color("pink")
        Fs.theme_slider_border_width(50)
        Fs.theme_text_color("black")
        Fs.theme_slider_border_width(50)
        Fs.theme_slider_color("yellow")
        self.layout = [
            [Fs.Txt("你好，我是快乐小猪，你是谁呀？")],
            [Fs.Txt("我是你的", size=(8, 1)), Fs.InputText("", tooltip="你是爸爸还是妈妈？", key="-user-", size=(8, 1))],
            [Fs.Txt("我的名字是", size=(8, 1)),
             Fs.InputText("", tooltip="你叫什么名字？", password_char="*", key="-pwd-", size=(8, 1))],
            [Fs.Button("告诉小猪", size=(8, 1))]
        ]

    def running(self):
        global msg
        window = Fs.Window("你是谁呀？><", self.layout)
        while True:
            event, values = window.read()
            if event == "告诉小猪":
                for user in self.UserList:
                    if values["-user-"].upper() == user["账号"] and values["-pwd-"].upper() == user["密码"]:
                        msg = "原来是爸爸妈妈^*^"
                        Fs.Popup(msg)
                        window.close()
                        pygame.init()
                        PyGaMeeRunny(values["-user-"]).running()
                        pygame.quit()
                        break
                else:
                    msg = "我不认识你！"
                    Fs.Popup(msg)
            if event is None:
                break
        window.close()
