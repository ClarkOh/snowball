################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxConsoleThread.py
# date        : 2012-10-06 18:51:18
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import time
import sys
import msvcrt
import threading

from Queue          import Queue

class cxClockThread(threading.Thread) :
    _terminate = False
    resultQueue = None
    requestQueue = Queue()

    def __init__(self, interval ) :
        threading.Thread.__init__(self)
        self.daemon = False
        self.interval = interval

    def terminate(self) :
        self._terminate = True

    def setResultQueue(self, resultQueue) :
        if resultQueue is not None :
            self.resultQueue = resultQueue

    def setResult(self, param) :
        if self.resultQueue is not None :
            self.resultQueue.put(param)
        else :
            print param

    def getRequestQueue(self) :
        return self.requestQueue

    def run(self) :
        while True :
            if self._terminate is True :
                print '\nexiting cxClockThread'
                break
            reqQueueSize = self.requestQueue.qsize()
            for i in range(0, reqQueueSize) :
                request = self.requestQueue.get()
                if request == 'exit' :
                    self.terminate()

            result = 'The time is %s'% time.ctime()
            self.setResult(result)
            time.sleep(self.interval)


bKeyboardInputFlag = False

class cxConsoleThread(threading.Thread) :

    _terminate = False
    resultQueue = Queue()   # waiting queue from clockthread result
    requestQueue = None     # request queue to clockthread 

    inputQueue = Queue()    # waiting queue from cxConsoleInputThread

    def __init__(self) :
        threading.Thread.__init__(self)
        self.daemon = False
        self.inputThread = cxConsoleInputThread()

        self.inputThread.setInputQueue(self.getInputQueue())

    def setInputWaitTimeout(self, timeout) :
        self.inputThread.setInputWaitTimeout(timeout)

    def getInputWaitTimeout(self) :
        return self.inputThread.inputWaitTimeout

    def getInputQueue(self) :
        return self.inputQueue

    def setRequestQueue(self, requestQueue ) :
        if requestQueue is not None :
            self.requestQueue = requestQueue

    def setRequest(self, param ) :
        if self.requestQueue is not None :
            self.requestQueue.put(param)

    def getResultQueue(self) :
        return self.resultQueue

    def start(self):
        threading.Thread.start(self)
        self.inputThread.start()

    def terminate(self) :
        self.inputThread.terminate()
        self._terminate = True

    def run(self) :
        global bKeyboardInputFlag

        while True :
            if self._terminate == True :
                print u'\nexiting cxConsoleThread'
                break

            inputString = ''
            if self.inputQueue.qsize() is not 0 :
                inputString = self.inputQueue.get()
                self.setRequest(inputString)

            resultQueueSize = self.resultQueue.qsize()
            for i in range(0, resultQueueSize ) :
                resultString = self.resultQueue.get()
                if bKeyboardInputFlag is False :
                    print resultString

            if inputString == 'exit' :
                self.terminate()
            else : time.sleep(0.2)

        # end of while True
    # end of run()
# end of cxConsoleThread


class cxConsoleInputThread(threading.Thread) :

    _terminate = False
    
    inputQueue = None       # input queue to cxConsoleThread

    inputWaitTimeout = 60 #10

    def __init__(self) :
        threading.Thread.__init__(self)
        self.daemon = False
        self.inputString = u''

    def setInputQueue(self, inputQueue ) :
        if inputQueue is not None :
            self.inputQueue = inputQueue

    def setInput(self, param ) :
        if self.inputQueue is not None :
            self.inputQueue.put(param)

    def terminate(self) :
        self._terminate = True

    def readInput(self, prompt, timeout = 10 ) :
        start_time = time.time()
        sys.stdout.write(u'%s'%prompt)
        inputString = u''
        while True :
            if (time.time() - start_time) > timeout :
                return None
            if msvcrt.kbhit() :
                start_time = time.time()
                ch = msvcrt.getwch()

                if ord(ch) == 13 : # enter key
                    if inputString == 'q' :
                        return None
                    elif len(inputString) == 0 :
                        return None
                    elif len(inputString) > 0 :
                        return inputString
                elif ord(ch) == 8 : # back space
                    inputString = inputString[0:-1]
                else : inputString += ch
                
                try : inputString = unicode(inputString)
                except : 
                    sys.stdout.write(u'\r%s%s'%(prompt,
                                     u'unicode converting error for inputString'))
                    sys.stdout.flush()
                    continue
                
                sys.stdout.write(u'\r%s%s'%(prompt,' '*(len(inputString)*2+1)))
                sys.stdout.write(u'\r%s%s'%(prompt, inputString))
                sys.stdout.flush()
        return None

    def setInputWaitTimeout(self, timeout ) :
        self.inputWaitTimeout = int(timeout)

    def run(self) :
        global bKeyboardInputFlag

        while True :
            if self._terminate is True :
                print u'\nexiting cxConsoleInputThread'
                break
            if msvcrt.kbhit() :
                msvcrt.getch()
                bKeyboardInputFlag = True
                inputString = self.readInput(u'>>', self.inputWaitTimeout)
                print 
                self.setInput(inputString)
                bKeyboardInputFlag = False
                
            time.sleep(0.1)


def test_keyboard_input(option = 0 ) :
    if option == 0 : 
        clockThread = cxClockThread(1)
        consoleThread = cxConsoleThread()

        consoleThread.setRequestQueue(clockThread.getRequestQueue())
        clockThread.setResultQueue(consoleThread.getResultQueue())

        clockThread.start()
        consoleThread.start()
    
        clockThread.join()
        consoleThread.join()

    elif option == 1 :
        queue = Queue()
        clockThread = cxClockThread(1)
        clockThread.setResultQueue(queue)

        clockThread.start()
    
        time.sleep(5)
        clockThread.terminate()
        clockThread.join()
        for i in range(0, queue.qsize()) :
            print queue.get()


def test() :
    pass


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
