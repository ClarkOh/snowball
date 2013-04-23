################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : testStockMst.py
# date        : 2013-03-24 19:16:47
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.2 Stackless 3.1b3 060516 (default, Dec 21 2011, 17:08:51) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import common
import os
from cxFile import cxFile

def getAllStockMst() :
    import time

    from cxCybosPlus import constants
    from cxCybosPlus import gCybosPlusClassDic
    from cxStockMgr  import stockMgr
    cpCybos = gCybosPlusClassDic['cxCpCybos']
    stockMst = gCybosPlusClassDic['cxCpStockMst']
    stockList = stockMgr.getStockList()

    sep = u'\t'
    newLine = u'\n'
    
    fileName = u'StockMst.des'
    if common.checkFileExist(fileName) == True :
        os.remove(fileName)
    stockMstFile = cxFile(fileName)
    strLine = u''
    
    for key in stockMst.headerIndexDic.keys() :
        strLine += stockMst.headerIndexDic[key][1] + sep 
    strLine += newLine
    print strLine
    stockMstFile.write(strLine)
   
    #stockList = [[u'A000660',u'SK하이닉스']]
    for stockItem in stockList :
        print stockItem[0]
        stockMst.SetInputValue(u'0',stockItem[0])
        stockMst.BlockRequest()
        result = stockMst.getResult()
        
        print 'getResult (',result[0],')'
        
        if result[0] != 0 :
            print stockItem[0], ': BlockRequest is failed (%d).'%(result[0])
            continue
        
        strLine = u''
        for key in stockMst.headerIndexDic.keys() :
            strLine += unicode(result[5][0][key][2]) + sep
        strLine += newLine
        print strLine
        stockMstFile.write(strLine)
        
        remainCount = cpCybos.GetLimitRemainCount(constants.LT_NONTRADE_REQUEST)
        remainTime = cpCybos.LimitRequestRemainTime()
        print remainCount, remainTime
        if remainCount <= 0 :
            time.sleep((remainTime/1000)+1)

    stockMstFile.close()

def loadAllStockMst() :
    fileName = u'StockMst.des'
    stockFile = cxFile(fileName)
    sep = u'\t'

    lines = stockFile.readlines() 
    print lines[0]


def test() :
    #getAllStockMst()
    loadAllStockMst() 


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
