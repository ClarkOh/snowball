################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : testA005930.py
# date        : 2012-12-28 15:07:20
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

from cxDatabase import cxDatabase

class cxTestA005930 :   #samsung electronics

    def __init__(self) :
        #from cxCybosPlus import gCybosPlusClassDic
        #self.cpClsDic = gCybosPlusClassDic
        pass

    def __del__(self) :
        pass

    def loadDataDirect(self) :
        database = cxDatabase()

        database.updateDataList( 


    def loadDataFromFile(self, fileName) :

        logDataFile = open(fileName)
        lineNum = 0
        tempList = []
        dataList = []
        for line in logDataFile.readlines() :
            if lineNum == 0 :
                lineNum+=1
                continue
            lineNum+=1
            tempList = []
            itemList = []
            for item in line.split() :
                tempList.append(item)
            print tempList
            itemList.append(int(tempList[0]), int(tempList[2]), int(tempList[3]), int(tempList[4]),int(tempList[5]), int(tempList[7]))
            dataList.append(itemList)
        print u'dataList len :', len(dataList)


def update_A005930_LogData(fileName) :
    database = cxDatabase()
    
    chartType = u'day'
    stockCode = u'A005930'
    dataResult = database.update(chartType, stockCode, True, fileName)

    if dataResult.result != u'ok' :
        print u'\n database.update for %s with %s chart type was failed.'%(stockCode, chartType)
    else : 
        print u'\n database.update for %s with %s chart type was written to %s'%(stockCode, chartType, fileName)

    del database
    return dataResult
 
def test() :
    testA005930 = cxTestA005930()
    testA005930.loadDataDirect()

#    fileName = u'A005930_samsung_electronics.data'
#    updateLogDataResult = update_A005930_LogData(fileName)
#    if updateLogDataResult.result != u'ok' :
#        return
#    testA005930 = cxTestA005930()
#    testA005930.loadDataFromFile(fileName)
   


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
