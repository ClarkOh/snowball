################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : RapidSnowBall.py
# date        : 2013-02-12 17:14:33
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

def loadSubscribeStockList() :
    #import os
    subFile = cxFile(u'subStockList.cfg')
    subStockList = [stock.rstrip(u'\r\n') for stock in filter(lambda x : x!=u'\r\n',subFile.readlines())]    
    # os.sep can be used.
    return subStockList
    
def RapidSnowBall() :
    reportQueue = Queue()
    conclusionQueue = Queue()
    resultFile = cxFile()

    cpTdUtil = gCybosPlusClassDic['cxCpTdUtil']
    result = cpTdUtil.TradeInit()

    if result != 0 :
        resultString = u'cpTdUtil.init failed'
        resultFile.write(resultString)
        return

    accountList = cpTdUtil.AccountNumber()
    goodsList = cpTdUtil.GoodsList(accountList[0],3)

    cpConclusion = gCybosPlusClassDic['cxCpConclusion']
    cpConclusion.open()
    cpConclusion.set_result_queue(conclusionQueue)
    cpConclusion.Subscribe()

    cpTd0311 = gCybosPlusClassDic['cxCpTd0311']
    cpTd0311.open()
    cpTd0311.set_result_queue(reportQueue)

    # TODO :initial subscribe
    subscribeStockList = loadSubscribeStockList()

    #if len(subscribeStockList) :
        

    while True :
        #if reportQueue.qsize() != 0 :
            #resultList = reportQueue.get()
            #resultString = getResultStringPortrait(resultList, 1, 1, 1, 1)
            #resultFile.write(resultString)

        # TODO : if it gets some value changes, 
        #           determines whether buy or sell.
        #           determines stockCode, amount, unitPrice, tradeCondition,
        #           tradType also.
        # TODO : if it determines to buy, buy it.
        # TODO : if it determines to sell, sell it.
            
            #cpTd0311.SetInputValue(0, 1 or 2 ) # 1 : sell, 2 : buy
            #cpTd0311.SetInputValue(1, accountList[0])
            #cpTd0311.SetInputValue(2, goodsList[0])
            #cpTd0311.SetInputValue(3, stockCode)       # stockCode
            #cpTd0311.SetInputValue(4, amount)          # amount
            #cpTd0311.SetInputValue(5, unitPrice)       # unitPrice
            #cpTd0311.SetInputValue(7, tradeCondition)  # tradeCondition
            #cpTd0311.SetInputValue(8, tradeType)       # tradeType

            #result = cpTd0311.Request()
            #print 'result', result
            #print 'GetDibStatus', cpTd0311.GetDibStatus()
            #print 'GetDibMsg1', cpTd0311.GetDibMsg1()
            #bContinue = cpTd0311.Continue()
            #print 'Continue', bContinue 
            #if bContinue == 1 :
            #   cpTd0311.Request()

        if conclusionQueue.qsize() != 0 :
            resultList = conclusionQueue.get()
            resultString = getResultStringPortrait(resultList, 1, 1, 1, 1)
            print resultString
            resultFile.write(resultString)
        
        # TODO : check the loop-end conditions.
        #           keystroke or some other conditions.

        win32gui.PumpWaitingMessages()
        #time.sleep(1) 
        time.sleep(0.01) #0.01  for 10 msec.

    resultFile.close()
    cpTd0311.close()

    cpConclusion.Unsubscribe()
    cpConclusion.close()


def test() :
    #RapidSnowBall()
    print loadSubscribeStockList()

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
