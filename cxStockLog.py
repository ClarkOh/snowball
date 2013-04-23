################################################################################
# -*- coding: utf-8 -*-

# Author      : Jinwon Oh (jinwon.clark.oh@gmail.com)
# File name   : cxStockLog.py
# Date        : 2012.11.26
# Ver         : 
# Desc.       : 
# Tab Size    : set sw=4, ts=4
# Python Ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]
# License     : (c) 2012 Jinwon Oh. All rights reserved.

# ADD CODES FROM HERE

"""
class name : cxStockLog
class desc.: 
methods
    getChartTypeParam(chartType) : return 'M','W','D','m','T' or ''
    update(stockCode, chartType, fileName)
"""

E_BASE                          = -100
E_FIND_STOCK_NAME               = E_BASE -1
E_FIND_CHART_TYPE               = E_BASE -2
E_BLOCKREQUEST_RESULT_NONE      = E_BASE -3
E_BLOCKREQUEST_RESULT_BLANK     = E_BASE -4
E_DIB_STATUS                    = E_BASE -5
W_FILE_EXIST                    = E_BASE -99

class cxStockLog :
    def __init__(self) :
        from cxCybosPlus    import getCybosPlusClassDic
        self.cpClsDic = getCybosPlusClassDic()
        
    def getChartTypeParam(self, argChartType) :
        if  argChartType == u'Day'  or  \
            argChartType == u'D'    or  \
            argChartType == u'd'    or  \
            argChartType == u'day'      \
            :
            chartType = u'D'
        elif argChartType == u'Week'   or  \
            argChartType == u'W'       or  \
            argChartType == u'w'       or  \
            argChartType == u'week'        \
            :
            chartType = u'W'
        elif argChartType == u'Month'   or  \
            argChartType == u'month'    or  \
            argChartType == u'M'            \
            :
            chartType = u'M'
        elif argChartType == u'Minute'  or  \
            argChartType == u'm'        or  \
            argChartType == u'minute'   or  \
            argChartType == u'time'     or  \
            argChartType == u'Time'     or  \
            :
            chartType = u'm'
        elif argChartType == u'Tick'    or  \
            argChartType == u'tick'     or  \
            argChartType == u't'        or  \
            argChartType == u'T'            \
            :
            chartType = u'T'
        else :
            chartType = u''
        return chartType
    
    def updateData(self,
                    argStockCode,
                    argChartType,
                    argFileName = u'') :
        import common
        import os
        cpStockCode = self.cpClsDic['cxCpStockCode']
        stockName = cpStockCode.CodeToName(argStockCode)
        if stockName == u'' :
            return E_FIND_STOCK_NAME
        chartType = self.getChartTypeParam(argChartType)
        if chartType == u'' :
            return E_FIND_CHART_TYPE
        if argFileName == u'' :
            path = u'log\\%s\\'%(chartType.lower())
            if os.path.exists(path) == False :
                os.makedirs(path)
            fileName = u'%s%s_%s.log' %\
                        ( path,
                          argStockCode,
                          stockName )
        else :
            fileName = argFileName
        if common.checkFileExist(fileName) == True :
            os.remove(fileName)
            #return W_FILE_EXIST
        
        fieldList = [
            0,  # 날짜
            1,  # 시간
            3,  # 고가
            4,  # 저가
            5,  # 종가
            8,  # 거래량
            9,  # 거래대금
        ]   # refer to CybosPlus manual
        
        paramList = [
            [   0,  argStockCode    ],
            [   1,  ord(u'1')       ],  # 기간요청
            [   3,  19500101        ],  # 1950.01.01 ~
#            [   3,  20121124        ],  # 1950.01.01 ~
            [   4,  len(fieldList)  ],
            [5] + fieldList          ,  # Field List
            [   6,  ord(chartType)  ],  # Chart Type
            [   9,  ord(u'1')       ],  # 수정주가
            [   10, ord(u'3')       ],  # 시간외 거래량 모두 제외
        ]
        stockChart = self.cpClsDic[u'cxStockChart']
        resultList = common.templateBlockRequest( stockChart,
                                                  paramList )
        if resultList == None :
            return E_BLOCKREQUEST_RESULT_NONE
        if len(resultList) == 0 :
            return E_BLOCKREQUEST_RESULT_BLANK
        
        
        #print common.dumpList(resultList)
        bFirstLoop = True
        dataNum = 0
        fieldNameList = []
        fileHeader = []
        fileData = []
        for result in resultList :
            #print common.getResultStringLandscape( result,
            #                                      statusOption=1,
            #                                      headerValue=1,
            #                                      dataValue=1,
            #                                      titleOption=1 )
            dibStatus = common.getResultDibStatus(result)
            if dibStatus != 0 :
                return E_DIB_STATUS
            dataList = common.getResultDataList(result)
            
            for dataDic in dataList :
                tempList = []
                for key in dataDic.keys() :
                    tempList.append(dataDic[key][2])
                    if bFirstLoop == True :
                        fieldNameList.append(dataDic[key][1])
                fileData.append(tempList)
                bFirstLoop = False
            fileHeader.append(fieldNameList)
        #end of 'for result in resultList :'
        #print common.dumpList(fieldNameList)
        #print common.dumpList(fileData)
        """
        [0] : field list
        [1] ~ : data
        """

        from cxFile import cxFile
        dataLogFile = cxFile(fileName)
        
        fieldNameString = u''
        for fieldName in fieldNameList :
            fieldNameString += fieldName + u' '
        fieldNameString += u'\n'
        dataLogFile.write(fieldNameString)
        #print fieldNameString
        
        for i in range(len(fileData)-1,-1,-1):
            itemString = u''
            itemList = fileData[i]
            for item in itemList :
                itemString += common.UNI(item) + u' '
            itemString += u'\n'
            dataLogFile.write(itemString)
            #print itemString
        dataLogFile.close()
        return 0 

def test() :
    stockLog = cxStockLog()
    result = stockLog.updateData(u'A000660',u'day')
    print result
    del stockLog

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

    #raw_input("Hit any key to close this window...")
