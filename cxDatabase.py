################################################################################
# -*- coding: utf-8 -*-

# Author      : Jinwon Oh (jinwon.clark.oh@gmail.com)
# File name   : cxDatabase.py
# Date        : 2012.11.28. 13:39
# Ver         : 0.0.1
# Desc.       : install & maintain the stock log data.
# Tab Size    : set sw=4, ts=4
# Python Ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]
# License     : (c) 2012 Jinwon Oh. All rights reserved.

# ADD CODES FROM HERE
# 음...데이타베이스를 사용할까?
# 무언가 용이하게 데이타들을 다루기 위해서는 데이타베이스가 필요하긴 한데...
# 쉽게 다룬다는 것은 그만큼 여러가지 테스트를 해보고 싶다는 뜻?
# 너무 광범위하기는 하다.
# 데이타베이스 구축은 다루기 나름이라 구축하는데 시간이 얼마나 걸릴지 모르지만
# 구축 이후 query 처리 속도가 걱정되기는 한다.
# 그렇다고 Database Like한 기능의 File based object를 만드는 것은
# 구현 시간도 시간이기도 하고 ...
# 하지만 내가 입맛대로 구현할 수 있는 장점도 있고...
# 어지간한 데이타들은 다 넣어서 실행 속도에 대한 최적화도 내가 할 수도 있고...
# 기왕 이렇게 된 거 그냥 여기다 다 넣어버리자.

# 이 코드를 짜는 이유는 좀 더 데이타를 쉽게 다루고 싶어서다.
# 기존의 코드는 터틀에 맞추어서 급하게 처리하다보니, 다른 데이타를 
# 얻기 위해 코드를 다시 작성해야 했다. 리스트의 인덱스를 다시 보고 파악하기가 
# 정말 힘들었다.
# 그래서 쉽게 코드를 파악하고 수정이 쉽게 하는 목적으로 작성중이다.
# 그리고 메모리의 사용 대신에 파일로의 처리를 우선시 한다.
# 처리 속도는 떨어지더라도 컴퓨터의 메모리가 많지 않는 이유이기도 하고,
# 무한정 메모리를 필요로 하는 것도 비현실적이다.

# Examples
# stockDatabase.getChartType('Day')'Month','Week','Minute','Time','Tick'
# stockDatabase.install()
# stockDatabase.update()
# 아래는 미정...
# resultfilename = stockDatabase.query('select
#                       date, maxPrice, minPrice, closingPrice' )

import common
from cxStockMgr     import stockMgr
from common         import cxReturnValue
from cxFile import cxFile
"""
cxDatabase

__init__(argPath=u'database\\')

getChartType(argChartType=[u'month'|u'week'|u'day'|u'time'|u'tick'])
    cxReturnValue([u'M'|u'W'|u'D'|u'm'|u'T'],u'ok')

getChartDir(argChartType=[u'M'|u'W'|u'D'|u'm'|u'T'])
    cxReturnValue(u'[month|week|day|time|tick]',u'ok')

getPath(argChartType=[u''|u'month'|u'week'|u'day'|u'time'|u'tick'])
    cxReturnValue(u'database\\[month|week|day|time|tick]',u'ok')

getFileName(argChartType=[u'month'|u'week'|u'day'|u'time'|u'tick'],
            argStockCode=u'A000660')
    cxReturnValue(fileName,u'ok')

getFieldList(argFieldList=[u'날짜',u'시간',u'시가',u'고가',u'저가',u'종가',...])
    cxReturnValue([0,1,2,3,4,5,...],u'ok')

updateDataList(argChartType=[u'month'|u'week'|u'day'|u'time'|u'tick'],
               argRequestType=[u'period'|u'count'],
               argRequestArg=[list|int],
               argCorrPriceType=[0|1],
               argFieldList=list,
               argStockCode=u'A00060')
    cxReturnValue(resultList,u'ok')

update(argChartType=[u'month'|u'week'|u'day'|u'time'|u'tick'],
       argStockCode=u'A000660',
       argClear=[True|False],
       argFileName=u'')
    cxReturnValue(fileName,u'ok')

install(void)
    None or cxReturnValue(fileName,u'ok')
"""
class cxDatabase :
    chartType = { u'month' : u'M',
                  u'week'  : u'W',
                  u'day'   : u'D',
                  u'minute': u'm',
                  u'tick'  : u'T' }
    fieldDic = { u'날짜'                : 0,
                 u'시간'                : 1,
                 u'시가'                : 2,
                 u'고가'                : 3,
                 u'저가'                : 4,
                 u'종가'                : 5,
                 u'전일대비'            : 6,
                 u'거래량'              : 8,
                 u'거래대금'            : 9,
                 u'누적체결매도수량'    : 10,
                 u'누적체결매수수량'    : 11,
                 u'상장주식수'          : 12,
                 u'시가총액'            : 13,
                 u'외국인주문한도수량'  : 14,
                 u'외국인주문가능수량'  : 15,
                 u'외국인현보유수량'    : 16,
                 u'외국인현보유비율'    : 17,
                 u'수정주가일자'        : 18,
                 u'수정주가비율'        : 19,
                 u'기관순매수'          : 20,
                 u'기관누적순매수'      : 21,
                 u'등락주선'            : 22,
                 u'등락비율'            : 23,
                 u'예탁금'              : 24,
                 u'주식회전율'          : 25,
                 u'거래성립률'          : 26,
                 u'대비부호'            : 37
                 }

    def __init__(self, argPath=u'database\\') :
        from cxCybosPlus    import gCybosPlusClassDic
        import os
        self.cpClsDic = gCybosPlusClassDic
        if argPath[-1:] != u'\\' :
            self.basePath = argPath + u'\\'
        else :
            self.basePath = argPath
        if os.path.exists(self.basePath) == False :
            os.makedirs(self.basePath)
        for subdir in self.chartType.keys() :
            subpath = self.basePath + subdir + u'\\'
            if os.path.exists(subpath) == False :
                os.makedirs(subpath)

    def __del__(self) :
        pass

    def getChartType(self, argChartType) :
        chartType = argChartType.lower()
        if chartType in self.chartType.keys() :
            return cxReturnValue(self.chartType[chartType])
        if argChartType in self.chartType.values() :
            return cxReturnValue(argChartType)
        if argChartType == u'w' :
            return cxReturnValue(u'W')
        elif argChartType == u'd' :
            return cxReturnValue(u'd')
        elif argChartType == u'Time' or argChartType == u'time' :
            return cxReturnValue(u'm')
        elif argChartType == u't' :
            return cxReturnValue(u'T')
        else :
            return cxReturnValue(u'',
                                 u'failed to find chart type for "%s"'%argChartType)

    def getChartDir(self, argChartType) :
        if argChartType == u'' :
            return cxReturnValue(u'',u'argChartType is null')
        chartType = argChartType.lower()
        if chartType in self.chartType.keys() :
            return cxReturnValue(common.UNI(chartType))
        if argChartType in self.chartType.values() :
            for item in self.chartType.items() :
                if item[1] == argChartType :
                    return cxReturnValue(common.UNI(item[0]))
        if argChartType == u'w' :
            return cxReturnValue(u'week')
        elif argChartType == u'd' :
            return cxReturnValue(u'day')
        elif argChartType == u'Time' or argChartType == u'time' :
            return cxReturnValue(u'minute')
        elif argChartType == u't' :
            return cxReturnValue(u'tick')
        else :
            return cxReturnValue(u'',
                                 u'failed to find chart type for "%s"'%argChartType)

    def getPath(self, argChartType=u'') :
        if argChartType == u'' :
            return cxReturnValue(self.basePath)
        subDir = self.getChartDir(argChartType)
        if subDir.result != u'ok' :
            return cxReturnValue(subDir.value, subDir.result)
        return cxReturnValue(self.basePath+subDir.value+u'\\')

    def getFileName(self, argChartType, argStockCode) :
        if argStockCode == u'' or argStockCode == None :
            return cxReturnValue(u'',u'invalid argStockCode')
        cpStockCode = self.cpClsDic['cxCpStockCode']
        stockName = cpStockCode.CodeToName(argStockCode)
        if stockName == u'' :
            return cxReturnValue(u'',
                                 u'failed to find stock name of "%s"'%argStockCode)
        path = self.getPath(argChartType)
        if path.result != u'ok' :
            return cxReturnValue(path.value,path.result)
        fileName = path.value + argStockCode + u'.data'
        return cxReturnValue(fileName)

    def getFieldList(self, argFieldList ) :
        fieldList = []
        if argFieldList == [] or argFieldList == None :
            return cxReturnValue(None, u'invalid argFieldList')
        for fieldName in argFieldList :
            if fieldName in self.fieldDic.keys() :
                fieldList.append(self.fieldDic[fieldName])
            else :
                return cxReturnValue(None,
                                     u'failed to find field index(%s)'%fieldName)
        return cxReturnValue(fieldList, u'ok')

    def updateDataList(self,
                       argChartType,        #[u'M',u'W',u'D',u'm',u'T']
                       argRequestType,      #요청방식:기간요청(u'period'),
                                            #         갯수요청(u'count')
                       argRequestArg,       #요청방식이 기간요청일 경우, list
                       argCorrPriceType,    #수정 주가 여부 [0,1]
                       argFieldList,
                       argStockCode ):

        chartTypeResult = self.getChartType(argChartType)
        if chartTypeResult.result != u'ok':
            return cxReturnValue(None, u'invalid argChartType "%s"'%argChartType)
        chartType = ord(chartTypeResult.value)

        #if argChartType in self.chartType.values() :
        #    chartType = ord(argChartType)
        #else :
        #    return cxReturnValue(None,
        #                         u'invalid argChartType "%s"'%argChartType)

        if argRequestType == u'P' or    \
            argRequestType == u'p' or   \
            argRequestType == u'Period' or  \
            argRequestType == u'period' :
            requestType = ord(u'1')
        elif argRequestType == u'C' or  \
            argRequestType == u'c' or   \
            argRequestType == u'Count' or \
            argRequestType == u'count'  :
            requestType = ord(u'2')
        else :
            return cxReturnValue(None,
                                 u'invalid argRequestType "%s"'%argRequestType)
        if requestType == ord(u'1') :
            if isinstance(argRequestArg,list) == False :
                return cxReturnValue(None,
                                    u'invalid argRequestArg : not list')
            else :
                startTime = argRequestArg[0]
                endTime = argRequestArg[1]
                #print '(',startTime,'-',endTime,')'
                #print type(startTime),type(endTime)
        if requestType == ord(u'2') :
            if isinstance(argRequestArg,int) == False :
                return cxReturnValue(None,
                                    u'invalid argReqeustArg : not int')
            else :
                count = argRequestArg
        if argCorrPriceType in [0, 1] :
            corrPriceType = ord(unicode(argCorrPriceType))
        else :
            return cxReturnValue(None,
                                 u'invalid argCorrPriceType "%d"'%argCorrPriceType)
        if argFieldList == [] or argFieldList == None :
            return cxReturnValue(None, u'invalid argFieldList')
        fieldList = self.getFieldList(argFieldList)
        if fieldList.result != u'ok' :
            return cxReturnValue(None, fieldList.value, fieldList.result)
        paramList = []
        if requestType == ord(u'1') :   #period
            paramList = [
                [ 0, argStockCode   ],
                [ 1, requestType    ],
                [ 2, endTime        ],
                [ 3, startTime      ],
                [ 5 ] + fieldList.value,
                [ 6, chartType      ],
                #[ 7, 1              ],  # 주기 (default - 1)
                [ 8, ord('0')       ],  # 갭보정여부 ('0'-갭무보정,'1'-갭보정)
                [ 9, corrPriceType  ],
                [10, ord(u'3')      ],  # 시간외 거래량 모두 제외
            ]
        else :  #requestType == ord('2')  #count
            paramList = [
                [ 0, argStockCode   ],
                [ 1, requestType    ],
                [ 4, count          ],
                [ 5 ] + fieldList.value,
                [ 6, chartType      ],
                #[ 7, 1              ],  # 주기 (default - 1)
                [ 8, ord('0')       ],  # 갭보정여부 ('0'-갭무보정,'1'-갭보정)
                [ 9, corrPriceType  ],
                [10, ord(u'3')      ],  # 시간외 거래량 모두 제외
            ]
        #print paramList
        #print 'argChartType=',argChartType
        stockChart = self.cpClsDic['cxStockChart']
        resultList = common.templateBlockRequest(stockChart, paramList)
        if resultList == None :
            return cxReturnValue(None, u'templateBlockRequest result is None')
        if len(resultList) == 0 :
            return cxReturnValue(None, u'templateBlockRequest result is []')

        return cxReturnValue(resultList, u'ok')

    def update(self, argChartType, argStockCode, argClear=False, argFileName=u'') :
        # filtering chart type
        chartType = self.getChartType(argChartType)
        if chartType.result != u'ok' :
        #{
            return cxReturnValue(chartType.value, chartType.result)
        #}

        # filtering file name or set default file name
        fileName = u''
        if argFileName == u'' : # if there aren't specific file name
        #{
            dataFileName = self.getFileName(chartType.value, argStockCode)
            if dataFileName.result != u'ok' :
            #{
                return cxReturnValue(dataFileName.value, dataFileName.result)
            #}
            fileName = dataFileName.value
        #}
        else :  # specific file name are given.
        #{
            fileName = argFileName
        #}

        # filtering argClear
        if chartType.value == u'M' or chartType.value == u'W':
            argClear = True    

        dataFile = cxFile(fileName) 

        if argClear == True :   # delete file and update file
            if dataFile.isExist() == True :
                dataFile.delete()
            dataFile = cxFile(fileName)

        # call updateDataList
        import time

        if dataFile.isEmpty() == False :    # not empty
            # get last date time info from file
            lastDate = 19900101
            lastLine = dataFile.getLastLine()
            #####print u"'"+lastLine+u"'"
            #####print lastLine.split()
            if lastLine != None and lastLine != u'' :
                parsedDate = lastLine.split()[0]
                if parsedDate.isdigit() == True :
                    lastDate = common.getOneDayPlus(int(parsedDate))
            # request data from last date time to today.
            today = int(time.strftime('%Y%m%d'))
            todayTime = int(time.strftime('%H%M%S'))

            if (today > lastDate) or (today == lastDate and todayTime > 153000) :
                #오후 3시까지가 장 시간이지만,
                #데이타 정리가 될 때까지 기다리는 시간을 감안하여
                #오후 3시 30분까지 기다렸다가 update하려 함.
                requestArg = [lastDate, today]
                print '(',lastDate,'-',today,')',
                result = self.updateDataList( chartType.value,
                                              u'period',
                                              requestArg,
                                              0,
                                              self.fieldDic.keys(),
                                              argStockCode )
            else :
                result = cxReturnValue(None, u'invalid period (%d-%d)'%(lastDate,today))

            bFirstWrite = False

        else :  # empty file means new file
            # update all. (from 1900 ~ )
            reqType = u'period'
            requestArg = [19900101,int(time.strftime('%Y%m%d'))]
            
            if chartType.value == u'M' or chartType.value == u'W' :  # month
                reqType = u'count'
                requestArg = 2048
            
            print requestArg,
            result = self.updateDataList( chartType.value,
                                          reqType,
                                          requestArg,
                                          0,
                                          self.fieldDic.keys(),
                                          argStockCode )
            bFirstWrite = True

        # writing result to file

        if result.result != u'ok' :
            dataFile.close()
            del dataFile
            return cxReturnValue(result.value, result.result)
        else :
            fieldNameList = []
            lineList = []
            bFirst = True
            for resultList in result.value :
                #print common.getResultStringPortrait( resultList, 1, 1, 1, 1 )
                for itemDic in resultList[6] :
                    valueList = []
                    for key in itemDic.keys() :
                        if bFirst == True :
                            fieldNameList.append(itemDic[key][1])
                        valueList.append(itemDic[key][2])
                    lineList.append(valueList)
                    if bFirst == True :
                        bFirst = False

            if len(lineList) == 0 :
                dataFile.close()
                del dataFile
                return cxReturnValue(None,u'no data')

            print len(lineList),

            if bFirstWrite == True :
                for fieldName in fieldNameList :
                    dataFile.write(common.UNI(fieldName)+u' ')
                dataFile.write(u'\n')
                bFirstWrite = False

            for i in range(len(lineList)-1,-1,-1) :
                for value in lineList[i] :
                    dataFile.write(common.UNI(value) + u' ')
                dataFile.write(u'\n')

        # write results to file with reverse order.
        dataFile.close()
        del dataFile
        return cxReturnValue(fileName)

    def install(self) :
        import time
        from cxCybosPlus import constants
        cpCybos = self.cpClsDic['cxCpCybos']
        self.updateFailedStockList = []
        stockList = stockMgr.getStockList()

        updateFailedStockCodeListFileName = self.basePath + u'updateFailedStockCodeList.txt'
        updateFailedStockCodeListFile = cxFile(updateFailedStockCodeListFileName)

        for chartType in self.chartType.keys() :
        #{
            for code, name, fullcode in stockList :
            #{
                print chartType, code, name,
                resultList = self.update(chartType,code)

                if resultList.result != u'ok' :
                #{
                    failedString = common.UNI(code) + u' ' + \
                                   common.UNI(name) + u' ' + \
                                   common.UNI(chartType) + u' ' + \
                                   common.UNI(resultList.result) + u'\n'
                    print failedString
                    updateFailedStockCodeListFile.write(failedString)
                    self.updateFailedStockList.append([ chartType, code, name ])
                #}

                remainCount = cpCybos.GetLimitRemainCount(constants.LT_NONTRADE_REQUEST)
                remainTime = cpCybos.LimitRequestRemainTime()
                print '\tremainCount : %d, remainTime : %d'%(remainCount, remainTime)

                if remainCount <= 0 :
                #{
                    print '\ttime.sleep for %d msec. [%d sec.]'%(remainTime, (remainTime/1000)+1 )
                    time.sleep((remainTime/1000) + 1)
                #}
            #}
        #}

        updateFailedStockCodeListFile.close()
        
        if len(self.updateFailedStockList) > 0 :
        #{
            print 'update failed stock list'
            for chartType, code, name in self.updateFailedStockList :
                print chartType, code, name
        #} 
        
        return True


#END OF CLASS 'cxDatabase'
        
def test_cxReturnValue() :
    returnValue = cxReturnValue()
    print returnValue.func_name, returnValue.value, returnValue.result
    returnValue2 = cxReturnValue(['a','b'])
    print returnValue2.func_name, returnValue2.value, returnValue2.result
    returnValue3 = cxReturnValue(u'',u'invalid value')
    print returnValue3.func_name, '"',returnValue3.value,'"', returnValue3.result

def test_getChartType(obj) :
    print common.__function_name__()
    testList = [ [ u'month', u'M'],
                 [ u'Month', u'M'],
                 [ u'M',     u'M'],
                 [ u'Week',  u'W'],
                 [ u'week',  u'W'],
                 [ u'W',     u'W'],
                 [ u'w',     u'W'],
                 [ u'Day',   u'D'],
                 [ u'day',   u'D'],
                 [ u'D',     u'D'],
                 [ u'd',     u'd'],
                 [ u'Minute',u'm'],
                 [ u'minute',u'm'],
                 [ u'm',     u'm'],
                 [ u'Time',  u'm'],
                 [ u'time',  u'm'],
                 [ u'T',     u'T'],
                 [ u't',     u'T'],
                 [ u'Tick',  u'T'],
                 [ u'tick',  u'T'] ]
    for testSet in testList :
        result = obj.getChartType(testSet[0])
        if result.value != testSet[1] :
            print testSet, result.dump()

def test_getPath(obj) :
    print common.__function_name__()
    testList = [ [ u'',      u'database\\'],
                 [ u'month', u'database\\month\\'],
                 [ u'Month', u'database\\month\\'],
                 [ u'week',  u'database\\week\\'],
                 [ u'Week',  u'database\\week\\'],
                 [ u'day',   u'database\\day\\'],
                 [ u'Day',   u'database\\day\\'],
                 [ u'Minute',u'database\\minute\\'],
                 [ u'minute',u'database\\minute\\'],
                 [ u'Tick',  u'database\\tick\\'],
                 [ u'tick',  u'database\\tick\\'],
                 [ u'M',     u'database\\month\\'],
                 [ u'W',     u'database\\week\\'],
                 [ u'w',     u'database\\week\\'],
                 [ u'D',     u'database\\day\\'],
                 [ u'd',     u'database\\day\\'],
                 [ u'm',     u'database\\minute\\'],
                 [ u'T',     u'database\\tick\\'],
                 [ u't',     u'database\\tick\\'] ]
    for testSet in testList :
        result = obj.getPath(testSet[0])
        if result.value != testSet[1] :
            print testSet,resultList.dump()

def test_getFileName(obj) :
    print common.__function_name__()
    testList = [ [ u'day',u'A000660',
                  [u'getFileName', u'database\\day\\A000660.data', u'ok'] ],
                 [ u'month',u'A000000',
                  [u'getFileName', u'', u'failed to find stock name of "A000000"'] ],
                 [ u'time',u'',
                  [u'getFileName', u'', u'invalid argStockCode'] ] ]
    for testSet in testList :
        result = obj.getFileName(testSet[0],testSet[1])
        if result.getList() != testSet[2] :
            print testSet, result.dump()

def test_updateDataList(obj):
    print common.__function_name__()
    chartType = obj.getChartType(u'day')
    requestType = u'count'  #period
    requestArg = 4 
    corrPriceType = 0
    fieldList = [u'날짜',u'시가',u'고가',u'저가',u'종가',u'전일대비',u'거래량',
                 u'거래대금',u'시가총액',u'외국인현보유수량',u'외국인현보유비율',
                 u'수정주가일자',u'수정주가비율',u'기관순매수']
    stockCode = u'A000660'
    result = obj.updateDataList( chartType.value, requestType, requestArg, corrPriceType,
                                 fieldList, stockCode )
    if result.result != u'ok' :
        print result.result
    else :
        """
        # 그닥 찍을만한 내용이 없는 듯.
        for resultList in result.value :
            for itemDic in resultList[5] :  # header list
                for key in itemDic.keys() :
                    print itemDic[key][1], itemDic[key][2]
                print
        """
        
        bFirstPrint = True
        fieldNameList = []
        valueList = []
        for resultList in result.value :
            for itemDic in resultList[6] :  # data list
                for key in itemDic.keys() :
                    if bFirstPrint == True :
                        fieldNameList.append(itemDic[key][1])
                        valueList.append(itemDic[key][2])
                    else :
                        print itemDic[key][2],
                if bFirstPrint == True :
                    for fieldName in fieldNameList :
                        print fieldName,
                    print
                    for value in valueList :
                        print value,
                    bFirstPrint = False
                print
    return

def test_update(obj) :
    testChartType=[u'month',u'week',u'day',u'time',u'tick']
    for chartType in testChartType :
        result = obj.update( chartType, u'A000660') #, argFileName = u'A000660.data')
    # time, day, tick 은 성공했는데...
    # month는 왜 안되는지...
        if result.result != u'ok' :
            print result.result

def test_install(obj) :
    result = obj.install()
    if result.result != u'ok' :
        print result.result

def test() :
    database = cxDatabase()
    #test_getChartType(database)
    #test_getPath(database)
    #test_getFileName(database)
    #database.install()
    test_updateDataList(database)    
    #test_update(database)
    #test_install(database)
    del database
    #test_cxReturnValue()
    
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
