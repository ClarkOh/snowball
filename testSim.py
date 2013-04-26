################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : testSim.py
# date        : 2013-03-13 16:00:48
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.2 Stackless 3.1b3 060516 (default, Dec 21 2011, 17:08:51) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE
from common import getFieldDataList

def testSaveStockData() :
    from cxDatabase     import cxDatabase

    DB = cxDatabase()
    DB.install()


def testGetFieldDataList() :
    from cxFile import cxFile
    fileName = u'database\day\A000020.data'
    dataFile = cxFile(fileName)
    dataLines = dataFile.readlines()
    fieldDataList = getFieldDataList(dataLines[1])
    print fieldDataList
    dataFile.close()

def cal_mean_and_variance( dataList ) :
    from math import pow, log
    mean = 0.0
    variance = 0.0
    num = len(dataList)
    for data in dataList :
        if type(data) != int and type(data) != float :
            print 'invalid type for mean and variance :', type(data)
            return [] 
        mean += data
    mean = mean/num

    for data in dataList :
        variance += pow((data-mean),2)

    variance = log(variance/num)
    return [mean, variance]

def test_cal_mean_and_variance( ) :
    testList = [ 5,2,-7,-10,9,10]
    result = cal_mean_and_variance(testList)
    print result
    assert result == [1.5, 4.053233173979669], 'incorrect result'

def getDayVariance(code) :
    if type(code) != str and type(code) != unicode :
        print 'invalid code type', type(code)
        return None
    #dataPath = u'database\\day\\'
    dataPath = u'D:\\user\\clark\\MyWork\\codes\\RapidSnowBall\\database\\day\\'
    #dataPath = u'D:\\user\\MyProject_old\\codes\\RapidSnowBall\\database\\day\\'
    fileName = dataPath + code + u'.data'
    #fileName = u'D:\\user\\MyProject_old\\codes\\RapidSnowBall\\database\\day\\A000020.data'
    from cxFile import cxFile
    try :
        dataFile = cxFile(fileName)
    except :
        print 'file open failed :', fileName
        return None

    lines = dataFile.readlines()
    if len(lines) == 0 :
        print 'no data in %s'%(code)
        return None
    
    dataList = []
    from common import getFieldDataList

    for index in range(1,len(lines)) :
        dataList.append(int(getFieldDataList(lines[index])[6]))

    result = cal_mean_and_variance(dataList) 
    print result
    return result

def getRelationships() :
    return

def testCalculateStochaostic() :
    from cxFile import cxFile
    dataPath = u'database\\day\\'
    data1FileName = u'A005930.data' #u'A000660.data' #u'A000020.data'
    data2FileName = u'A000660.data' #u'A005930.data' #u'A000060.data'
    #print dataPath + data1FileName
    #print 'what\'s happened'
    data1File = cxFile(dataPath + data1FileName)
    data2File = cxFile(dataPath + data2FileName)
    data1Lines = data1File.readlines()
    data2Lines = data2File.readlines()

    print len(data1Lines), len(data2Lines)
    #print data1Lines[1]
    #print data2Lines[1]

    #print data1Lines[0]
    
    srcDic = {}
    cmpDic = {}

    for i in range(1, len(data1Lines)) :
        data1FieldDataList = getFieldDataList(data1Lines[i])
        srcDic[data1FieldDataList[0]] = i

    for i in range(1, len(data2Lines)) :
        data2FieldDataList = getFieldDataList(data2Lines[i])
        cmpDic[data2FieldDataList[0]] = i

    #print srcDic
    #print cmpDic
    intersectionKeyList = list(set(srcDic.keys()) & set(cmpDic.keys()))
    #print len(intersectionKeyList)

    if len(intersectionKeyList) == 0 :
        print 'no intersection period'
        return
    #print intersectionKeyList
    intersectionKeyList.sort()
    #print intersectionKeyList

    srcAcc = 0
    cmpAcc = 0
    amount = 0
    UpUp = 0
    UpDown = 0
    DownUp = 0
    DownDown = 0


    for i in range(1, len(intersectionKeyList) ) :
        srcDate = intersectionKeyList[i-1]
        cmpDate = intersectionKeyList[i]
        srcIndex = srcDic[srcDate]
        cmpIndex = cmpDic[cmpDate]
        srcValue = int(getFieldDataList(data1Lines[srcIndex])[6])
        cmpValue = int(getFieldDataList(data2Lines[cmpIndex])[6])
        srcAcc += srcValue
        cmpAcc += cmpValue
        amount += 1

        #print srcDate, srcValue, u'|', cmpDate, cmpValue

        if srcValue > 0 and cmpValue > 0 :
            UpUp += 1
        elif srcValue < 0 and cmpValue > 0 :
            DownUp += 1
        elif srcValue > 0 and cmpValue < 0 :
            UpDown += 1
        elif srcValue < 0 and cmpValue < 0 :
            DownDown += 1

    print float(srcAcc)/amount, amount, u'A000660', u'A005930',
    print intersectionKeyList[0], u'~', intersectionKeyList[-1]
    print u'UpUp', UpUp, float(UpUp)/amount
    print u'DownUp', DownUp, float(DownUp)/amount
    print u'UpDown', UpDown, float(UpDown)/amount
    print u'DownDown', DownDown, float(DownDown)/amount

    """
    for date in intersectionKeyList :
        srcIndex = srcDic[date]
        cmpIndex = cmpDic[date]
        srcValue = int(getFieldDataList(data1Lines[srcIndex])[6])
        cmpValue = int(getFieldDataList(data2Lines[cmpIndex])[6])
        srcAcc += srcValue
        cmpAcc += cmpValue
        print date, srcValue, cmpValue

    print srcAcc, cmpAcc
    print intersectionKeyList[0], u'~', intersectionKeyList[-1]
    """
    return

    #print data1FieldDataList[6] #전일대비
    #print data2FieldDataList[6] #전일대비
    

    #for 아이템1 에 대해 (전체 주식아이템 리스트 중)
        #해당 아이템1의 파일을 읽는다.
        #for 아이템2 에 대해 (아이템1을 제외한 리스트 중)
            #해당 아이템2의 파일을 읽는다.
            #for yesterdayValue (전날의 전일대비값) in 아이템1 리스트
                # todayValue = 아이템2의 오늘의 전일대비값
                #if yesterdayValue > 0 and todayValue > 0 :
                # 아이템1이 어제 올랐을 때, 아이템2가 오늘 올랐다. 
                # 정확히는 아이템1이 오늘 올랐을 때, 내일 아이템2가 오를 확률은?의 뜻이다.
                #   데이타[아이템1][아이템2][UpUp] += 1
                #elif yesterdayValue > 0 and todayValue < 0 :
                # 아이템1이 어제 올랐을 때, 아이템2가 오늘 내렸다.
                # 정확히는 아이템1이 오늘 올랐을 때, 내일 아이템2가 내릴 확률은?의 뜻이다.
                #   데이타[아이템1][아이템2][UpDown] += 1
                #elif yesterdayValue < 0 and todayValue > 0 :
                # 아이템1이 어제 내렸을 때, 아이템2가 오늘 올랐다.
                # 정확히는 아이템1이 오늘 내렸을 때, 내일 아이템2가 오를 확률은?의 뜻이다.
                #   데이타[아이템1][아이템2][DownUp] += 1
                #elif yesterdayValue < 0 and todayValue > 0 :
                # 아이템1이 어제 내렸을 때, 아이템2가 오늘 내렸다.
                # 정확히는 아이템1이 오늘 내렸을 때, 내일 아이템2가 내릴 확률은?의 뜻이다.
                #   데이타[아이템1][아이템2][DownDown] += 1
                #elif => y = 0 and t = 0, y = 0 and t < 0, y = 0 and t > 0, 
                #     => y > 0 and t = 0, y < 0 and t = 0, y = 0 and t = 0.
                # 이 부분들이 어떤 의미가 있을까? 생략해도 될 듯...
                #전체 카운트 증가.
            #아이템2의 파일을 닫는다
        #해당 

    from cxStockMgr     import stockMgr
    stockList = stockMgr.getStockList()
    dataPath = u'database\\day\\'
    srcStockFileName = u''
    cmpStockFileName = u''
    fileType = u'.data'
    for srcStockCode, srcStockName, srcStockFullCode in stockList :
        srcStockFileName = dataPath + srcStockCode + fileType
        srcStockFile = cxFile(srcStockFileName)
        srcDataLines = srcStockFile.readlines()
        srcStockFile.close()
        del srcStockFile
        for cmpStockCode, cmpStockName, cmpStockFullCode in stockList :
            if srcStockCode == cmpStockCode :
                continue
            cmpStockFileName = dataPath + cmpStockCode + fileType
            cmpStockFile = cxFile(cmpStockFileName)
            cmpDataLines = cmpStockFile.readlines()
            cmpStockFile.close()
            del cmpStockFile
            # find starting offset time for comparing each other.
            # or
            # travel reverse order from recent day time to most old day time.
            #for day in dayList[startingDay, lastDay] :
            srcFieldDataList = []
            cmpFieldDataList = []
            if len(srcDataLines) >= len(cmpDataLines) :
                numLines = len(cmpDataLines)
            else : numLines = len(srcDataLines)
            # src >= cmp , cmp
            # src < cmp, src

            # +++++++++++++++++++++++++++                       (src)
            #                 ++++++++++++++++++++++++++++++    (cmp)
            #                 |         |
            #                 Offset    (Offset+num) 


            #              ++++++++++++++++++++++++++++++++     (src)
            # ++++++++++++++++++++++++                          (cmp)
            #              |         |
            #              Offset    (Offset+num)


            #              +++++++++++++++++                    (src)
            # ++++++++++++++++++++++++++++++++++++++            (cmp)
            #              |               |
            #              Offset          (Offset+num)


            for i in range(1, numLines) :
                srcFieldDataList.append([ data for data in filter(lambda x : x!= u'\n', \
                                                            srcDataLines[i].split(u' '))])
                cmpFieldDataList.append([ data for data in filter(lambda x : x!= u'\n', \
                                                            cmpDataLines[i].split(u' '))])
            offset = 0
            num = 0
            i = 0
            minLen = numLines - 1

            while i < minLen :
                if int(srcFieldDataList[i][0]) > int(cmpFieldDataList[i][0]) :
                    for j in range(i, numLines) :
                        if int(srcFieldDataList[i][0]) == int(cmpFieldDataList[j][0]) :
                            offset = j
                            i = j
                            break
                elif int(srcFieldDataList[i][0]) < int(cmpFieldDataList[i][0]) :
                    for j in range(i, numLines) :
                        if int(srcFieldDataList[j][0]) == int(cmpFieldDataList[i][0]) :
                            offset = j
                            i = j
                            break
                else : num += 1
                i += 1

            print offset, num + offset
            for i in range(offset, offset + num) :
                print srcFieldDataList[i][0], cmpFieldDataList[i][0],
                if srcFieldDataList[i][0] != cmpFieldDataList[i][0] :
                    print 'Different!!'
                else : print



def test() :
    #testSaveStockData()
    #testCalculateStochaostic()
    #testGetFieldDataList()
    #result = getDayVariance(u'A000020')
    #print result
    #print result[0], result[1]
    test_cal_mean_and_variance()

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
