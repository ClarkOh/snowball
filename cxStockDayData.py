################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxStockDayData.py
# date        : 2012-11-05 15:43:05
# ver         :
# desc.       :
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import sys
import common
from cxStockLogData import cxStockLogData
from cxStockMgr     import cxStockMgr
from cxFile         import cxFile

"""
cxStockDayData
    void loadLogData(void)
        : cxStockLogData로 저장되어 있는 파일의 데이터를 Load하여,
          모든 현물 주식에 대해 [ stockCode, [ 날짜,고가,저가,종가,거래량,거래대금 ] ]
          의 data list를 저장한다.
    list loadLogDataFromFile(fileName)
    bool saveLogDataToFile(fileName,option)
"""
class cxStockDayData :

    def __init__(self) :
        self.data = []
        self.fileName = u'cxStockDayData.dat'

    def __del__(self) :
        pass

    """
    실패함. Memory Error. data size가 커서...
    메모리가 큰 컴퓨터에서 해 볼 필요는 있는데...
    WIN7의 8기가 이상의 컴퓨터에서 나중에 포팅하면서 해봐야 할 듯...

    def save(self) :
        import cPickle
        dataFile = open(self.fileName,'w')
        cPickle.dump(self.data, dataFile)
        dataFile.close()

    def load(self) :
        import cPickle
        dataFile = open(self.fileName,'r')
        self.data = cPickle.load(dataFile)
        dataFile.close()
    """

    def loadLogData(self) :
        stockMgr = cxStockMgr()

        if stockMgr.update() < 0 :
            sys.stderr.write('cxStockDayData.loadLogData { stockMgr.update : failed }\n')
            del stockMgr
            return None

        stockList = stockMgr.getStockList()

        """
        for item in stockList :
            print item[0],      #stockCode
            print item[1],      #stockName
            print

        print len(stockList)    #2135
        """

        stockLogData = cxStockLogData()

        for stockCode,stockName,stockFullCode in stockList :
            dayLogData = []
            #sys.stdout.write('cxStockDayData.loadLogData { loading "%s ( %s )" daily logs.'\
            #                  %( stockCode, stockName ) )

            dayLogData = stockLogData.loadLogData( stockCode, u'Day' )

            if dayLogData == None :
                sys.stderr.write('cxStockDayData.loadLogData { "%s (%s)" daily log : failed. }\n'\
                                    %( stockCode, stockName ) )
            else :
                dataList = []
                for i in range( 0, len(dayLogData) ) :
                    dataList.append( [ int(dayLogData[i][0]), #날짜
                                       int(dayLogData[i][2]), #고가
                                       int(dayLogData[i][3]), #저가
                                       int(dayLogData[i][4]), #종가
                                       int(dayLogData[i][5]), #거래량
                                       int(dayLogData[i][6])  #거래대금
                                      ] )
                self.data.append( [ stockCode, dataList ] )

        sys.stdout.write('cxStockDayData.loadLogData { total len of data : %d }\n'\
                          %( len(self.data) ) )

        del stockLogData
        del stockMgr

        return self.data

    def loadLogDataFromFile(self, fileName=u'stockDayData.txt') :
        #import time
        """
        dataList = [ [ 'A000660', [ [ 19970101, 5434,5434,5435 ],
                                    [ 19970102, 3434,3434,3434 ] ] ],
                   ]
        """
        itemList = []
        dataList = []
        stockList = []
        historyList = []
        stockCode = u''

        #print 'begin'
        #startTime = time.time()
        for line in open(fileName) :
            strDataList = line.split()
            if len(strDataList) == 1 :
                if stockCode != strDataList[0] :
                    if len(historyList) > 0 :
                        stockList.append([stockCode,historyList])
                        stockCode = strDataList[0]
                        historyList = []
                    else :
                        stockCode = strDataList[0]
            else :
                for strData in strDataList :
                    item = int(strData)
                    itemList.append(item)
                historyList.append(itemList)
                itemList = []

        #endTime = time.time()
        #print 'end', endTime - startTime

        return stockList

    def saveLogDataToFile(  self,
                            fileName = u'stockDayData.txt',
                            condition = 19910100) :

        if ( self.data == None ) or ( len(self.data) == 0 ) :
            return False
        try:
            dataFile = cxFile(fileName)
        except BaseException as e :
            print e
            return False

        for stockCode, dayLog in self.data :
            dataFile.write('%s\n'%stockCode)
            for date,highPrice,lowPrice,currentPrice,tradingVolumn,tradingCost in dayLog :
                if date >= condition :
                    dataFile.write('\t%d %d %d %d %d %d\n'\
                                    %( date,
                                       highPrice,
                                       lowPrice,
                                       currentPrice,
                                       tradingVolumn,
                                       tradingCost ) )
        dataFile.close()

        return True

def save() :
    stockDayData = cxStockDayData()
    dataList = stockDayData.loadLogData()

    collect_and_show_garbage()

    for i in range(0,5):
        print dataList[i][0]
        for j in range(0,5) :
            print '\t',dataList[i][1][j]

    print 'saving'
    stockDayData.saveLogDataToFile( condition = 20000100 )
    print 'saved'
    del dataList
    del stockDayData

def load() :
    stockDayData = cxStockDayData()
    print stockDayData.data

    dataList = stockDayData.loadLogDataFromFile()

    for stockIndex in range(0,5):
        print dataList[stockIndex][0]
        for dayIndex in range(0,5) :
            print '\t',dataList[stockIndex][1][dayIndex]

    del stockDayData


def test() :
    save()
    #load()


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
