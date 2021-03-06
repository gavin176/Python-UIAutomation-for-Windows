#!python3
# -*- coding: utf-8 -*-
# hide windows with hotkey Ctrl+1, show the hidden windows with hotkey Ctrl+2
import os
import sys
import time
import subprocess
from typing import List

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # not required after 'pip install uiautomation'
import uiautomation as auto

WindowsWantToHide = ('Warcraft III', 'Valve001', 'Counter-Strike', 'Notepad')


def hide(stopEvent: 'threading.Event', handles: List[int]):
    #_uiobj = auto.UIAutomationInitializerInThread()
    # Hide doesn't call any COM methods, so it doesn't need an UIAutomationInitializerInThread
    for handle in handles:
        win = auto.ControlFromHandle(handle)
        win.Hide(0)


def show(stopEvent: 'threading.Event', handle: List[int]):
    #_uiobj = auto.UIAutomationInitializerInThread()
    # Show doesn't call any COM methods, so it doesn't need an UIAutomationInitializerInThread
    for handle in handles:
        win = auto.ControlFromHandle(handle)
        win.Show(0)
        if auto.IsIconic(handle):
            win.ShowWindow(auto.SW.Restore, 0)


if __name__ == '__main__':
    for i in range(2):
        subprocess.Popen('notepad.exe')
        time.sleep(1)
        notepad = auto.WindowControl(searchDepth=1, ClassName='Notepad')
        notepad.MoveWindow(i * 400, 0, 400, 300)
        notepad.SendKeys('notepad {}'.format(i + 1))
    auto.SetConsoleTitle('Hide: Ctrl+1, Show: Ctrl+2, Exit: Ctrl+D')
    auto.Logger.ColorfullyWriteLine('Press <Color=Green>Ctr+1</Color> to hide the windows\nPress <Color=Green>Ctr+2</Color> to show the windows\n')
    handles = [win.NativeWindowHandle for win in auto.GetRootControl().GetChildren() if win.ClassName in WindowsWantToHide]
    auto.RunByHotKey({(auto.ModifierKey.Control, auto.Keys.VK_1): lambda event: hide(event, handles),
                      (auto.ModifierKey.Control, auto.Keys.VK_2): lambda event: show(event, handles),
                      })

