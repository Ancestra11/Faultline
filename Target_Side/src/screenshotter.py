import base64
import win32api
import win32con
import win32gui
import win32ui

class Screenshotter() :
    def __init__(self) :
        self.Count = 1

    def get_dimensions(self):
        width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
        height = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
        left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
        top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
        return (width, height, left, top)

    def screenshot(self, name='screenshot'):
        hdesktop = win32gui.GetDesktopWindow()
        width, height, left, top = self.get_dimensions()

        desktop_dc = win32gui.GetWindowDC(hdesktop)
        img_dc = win32ui.CreateDCFromHandle(desktop_dc)
        mem_dc = img_dc.CreateCompatibleDC()

        screenshot = win32ui.CreateBitmap()
        screenshot.CreateCompatibleBitmap(img_dc, width, height)
        mem_dc.SelectObject(screenshot)
        mem_dc.BitBlt((0,0), (width, height), img_dc, (left, top), win32con.SRCCOPY)

        self.File_Path = '../data/Screenshots/' + name + str(self.Count) + '.bmp'
        Saved_File = screenshot.SaveBitmapFile(mem_dc, self.File_Path)

        mem_dc.DeleteDC()
        win32gui.DeleteObject(screenshot.GetHandle())

        self.Count += 1 
        return Saved_File

    def getFilePath(self) :
        return self.File_Path

    def run(self):
        screenshot()
        with open('screenshot.bmp') as f:
            img = f.read()
        return img