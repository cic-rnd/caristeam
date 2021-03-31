import time
import ctypes
import uiautomation as auto
import subprocess


subprocess.Popen('TextExe.exe')

#form1 = auto.WindowControl(searchDepth=1, Name='Form1')
form1 = auto.PaneControl(searchDepth=1, ClassName='Chrome_WidgetWin_1')

#form1 = auto.WindowControl(searchDepth=1, ClassName='ThunderRT6FormDC')

#form1 = auto.WindowControl(searchDepth=1, ClassName='Progman')

if not form1.Exists(3, 1):
    print('Can not find Zoom window')
    exit(0)
# inputbox1 = form1.EditControl(foundIndex=1)
# inputbox1.Click()
# inputbox1.SendKeys('{Del}{Del}{Del}{Del}{Del}')
# inputbox1.SendKeys('Hi')
# time.sleep(1)
#
# inputbox2 = form1.EditControl(foundIndex=2)
# inputbox2.Click()
# inputbox2.SendKeys('{Del}{Del}{Del}{Del}{Del}')
# inputbox2.SendKeys('World')
# time.sleep(1)

# inputbox3 = form1.EditControl(foundIndex=3)
# inputbox3.Click()
# inputbox3.SendKeys('{Del}{Del}{Del}{Del}{Del}')
# inputbox3.SendKeys('Hello')
# time.sleep(1)