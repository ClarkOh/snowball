################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxRapidSnowBall.py
# date        : 2013-03-11 15:00:56
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.2 Stackless 3.1b3 060516 (default, Dec 21 2011, 17:08:51) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

from Queue          import Queue
from cxCybosPlus    import gCybosPlusClassDic
import win32gui
import time
from common         import getResultStringPortrait
from cxFile         import cxFile
import pyHook
import sys

def consoleOutput(outputString) :
    sys.stdout.write(outputString)
    #sys.stdout.flush()

class cxRapidSnowBall :

    def __init__(self) :
        print 'cxRapidSnowBall'
        self.inputString = u''
        self.initInputHook()
        self.loadConfig()
        self.loadSubscribeStockList()
        self.exitCondition = False

	def __del__(self) :
		pass

    def loadConfig(self) :
        pass

    def loadSubscribeStockList(self) :
        subFile = cxFile(u'subStockList.cfg')
        self.subStockList = [stock.rstrip(u'\r\n') for stock \
                in filter(lambda x : x!=u'\r\n', subFile.readlines())]

    def onKeyboardEvent(self, event) :
        # 한글이 안되는군..ㅠ_ㅠ
        # back space/delete를 구현해야 할 듯...
        # 한글도 유니코드로 작동만 된다면 가능할 듯.

        #print chr(event.Ascii),
        #sys.stdout.write(u'\r>>')
        if event.Key == 'Return' :
            #print self.inputString
            #sys.stdout.write(u'\r>>'+' '*80)
            #sys.stdout.write(u'\n\r>>')
            #sys.stdout.flush()
            consoleOutput(u'\n\r>>')
            self.processInput(self.inputString)
            del self.inputString
            self.inputString = u''
        else :
            self.inputString += chr(event.Ascii)
            #sys.stdout.write(u'\r>>'+' '*(len(self.inputString)+1))
            #sys.stdout.write(u'\r>>'+self.inputString)
            #sys.stdout.flush()
            consoleOutput(u'\r>>'+self.inputString)
        return True

    def processInput(self, inputString) :
        if inputString == u'exit':
            self.exitCondition = True

    def initInputHook(self) :
        self.hookManager = pyHook.HookManager()
        self.hookManager.KeyDown = self.onKeyboardEvent
        self.hookManager.HookKeyboard()

    def main(self) :

        while self.exitCondition != True :
            win32gui.PumpWaitingMessages()
            time.sleep(0.01)


def test() :
    rapidSnowBall = cxRapidSnowBall()
    print rapidSnowBall.subStockList
    rapidSnowBall.main()
    del rapidSnowBall


def collect_and_show_garbage() :
	"Show what garbage is present."
	print "Collecting..."
	n = gc.collect()
	print "Unreachable objects:", n
	if n > 0 : print "Garbage:"
	for i in range(n):
		print "[%d] %s" % (i, gc.garbage[i])

if __name__ == "__main__" :
	import gc

	gc.set_debug(gc.DEBUG_LEAK)

	print "before"
	collect_and_show_garbage()
	print "testing..."
	print "-"*79

	test()

	print "-"*79
	print "after"
	collect_and_show_garbage()

	raw_input("Hit any key to close this window...")
