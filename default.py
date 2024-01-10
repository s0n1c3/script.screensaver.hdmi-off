import sys
import xbmcaddon
import xbmcgui
import xbmc
import os

Addon = xbmcaddon.Addon('script.screensaver.xbian-hdmioff')

__scriptname__ = Addon.getAddonInfo('name')
__path__ = Addon.getAddonInfo('path')


class Screensaver(xbmcgui.WindowXMLDialog):

    class ExitMonitor(xbmc.Monitor):

        def __init__(self, exit_callback):
            self.exit_callback = exit_callback

        def onScreensaverDeactivated(self):
            self.exit_callback()

    def onInit(self):
        self.monitor = self.ExitMonitor(self.exit)

    def exit(self):
        self.close()


if __name__ == '__main__':
    os.system('xrandr --output HDMI1 --off')
    screensaver_gui = Screensaver(
            'script-%s-main.xml' % __scriptname__,
            __path__,
            'default',
        )
    screensaver_gui.doModal()
    os.system('xrandr --output HDMI1 --auto')
    del screensaver_gui
    sys.modules.clear()
