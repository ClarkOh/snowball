################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : testCP.py
# date        : 2012-09-28 17:23:26
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE


def testCpSvrNew7216() :
    from cxCybosPlus import cxCpSvrNew7216

    cpSvrNew7216 = cxCpSvrNew7216()

    stockCode = 'A005180'
   
    cpSvrNew7216.SetInputValue( 0, stockCode )

    cpSvrNew7216.BlockRequest()

    result = cpSvrNew7216.getResult()

    print 'GetDibStatus', result[0]
    print 'GetDibMsg1', result[1]
    print 'Continue?', result[2]
    if result[2] == 1 : print 'Continue'
    elif result[2] == 0 : print 'End'
    print 'time', result[3]
    print 'class', result[4]

    headerList = result[5]
    dataList = result[6]

    print type(headerList),len(headerList)
    print type(dataList),len(dataList)
    
    for dataDic in dataList :
        for key in dataDic.keys() :
            typeName, fieldName, value = dataDic[key]
            print typeName, fieldName, value
        
    """
    for headerDic in headerList :
        key = headerDic.keys()[0]
        print headerDic[key][1], headerDic[key][2]

    num = 0
    for data in dataList :
        num += 1
        print num,
        for dataDic in data :
            #print type(dataDic)
            print dataDic,
            #key = dataDic.keys()[0]
            #print dataDic[key][1], dataDic[key][2]
        print
        #if raw_input() == 'n' : break
    """

    """
    stockCode = cpSvrNew7216.GetHeaderValue(0)
    count = cpSvrNew7216.GetHeaderValue(1)
    dateTime = cpSvrNew7216.GetHeaderValue(2)

    print u'종목코드\t:', stockCode
    print u'카운트\t\t:', count
    print u'조회일자\t:', dateTime

    raw_input()

    for i in range( 0, count ) :
        print u'일자\t\t:', cpSvrNew7216.GetDataValue( 0, i )
        print u'종가\t\t:', cpSvrNew7216.GetDataValue( 1, i )
        flag = cpSvrNew7216.GetDataValue( 2, i )
        print u'전일대비 Flag\t:',
        if   flag == ord(u'1') : print u'상한'
        elif flag == ord(u'2') : print u'상승'
        elif flag == ord(u'3') : print u'보합'
        elif flag == ord(u'4') : print u'하한'
        elif flag == ord(u'5') : print u'하락'
        elif flag == ord(u'6') : print u'기세상한'
        elif flag == ord(u'7') : print u'기세상승'
        elif flag == ord(u'8') : print u'기세하한'
        elif flag == ord(u'9') : print u'기세하락'
        print u'전일대비\t:', cpSvrNew7216.GetDataValue( 3, i )
        print u'전일대비율\t:', cpSvrNew7216.GetDataValue( 4, i )
        print u'거래량\t\t:', cpSvrNew7216.GetDataValue( 5, i )
        print u'기관매매\t:', cpSvrNew7216.GetDataValue( 6, i )
        print u'기관매매 누적\t:', cpSvrNew7216.GetDataValue( 7, i )
        print u'외국인 순매매\t:', cpSvrNew7216.GetDataValue( 8, i )
        print u'외국인 지분율\t:', cpSvrNew7216.GetDataValue( 9, i )

        if raw_input() == 'n' : break
    """

    del cpSvrNew7216

def testStockChart() :
    from cxCybosPlus import cxStockChart
    reqType = u'period'
    #reqType = u'count'
    stockChart = cxStockChart()
    stockChart.SetInputValue(0,u'A000660')
    if reqType == u'period' :
        stockChart.SetInputValue(1,ord(u'1'))   # u'1' : period, u'2' : count
        startTime = u'20121200'
        endTime = u'20121200'
        stockChart.SetInputValue(2,endTime)
        stockChart.SetInputValue(3,startTime)
    elif reqType == u'count' :
        stockChart.SetInputValue(1,ord(u'2'))   # u'1' : period, u'2' : count
        count = 2048
        stockChart.SetInputValue(4,count)
    stockChart.SetInputValue(5, [0,1,2,3,4,5])
    #stockChart.SetInputValue(6,ord(u'D'))
    #stockChart.SetInputValue(6,ord(u'M'))
    stockChart.SetInputValue(6,ord(u'W'))
    stockChart.SetInputValue(8,ord(u'0'))
    stockChart.SetInputValue(9,ord(u'0'))
    stockChart.SetInputValue(10,ord(u'3'))
    stockChart.BlockRequest()
    result = stockChart.getResult()
    print 'GetDibStatus', result[0]
    print 'GetDibMsg1', result[1]
    print 'Continue?', result[2]
    if result[2] == 1 : print 'Continue'
    elif result[2] == 0 : print 'End'
    print 'time', result[3]
    print 'class', result[4]

    headerList = result[5]
    dataList = result[6]

    print 'headerList len :',len(headerList)
    print 'dataList len:',len(dataList)

    for headerDic in headerList :
        key = headerDic.keys()[0]
        print headerDic[key][1], headerDic[key][2]

    print 'dataList type', type(dataList)
    for dataDic in dataList :
        for key in dataDic.keys() :
            typeName, fieldName, value = dataDic[key]
            print typeName, fieldName, value
        #    for value in dataDic[key] :
        #        print value,
        #    print
        print
            #print type(dataDic)
            #key = dataDic.keys()[0]
            #print dataDic[key][1], dataDic[key][2]

    #    if raw_input() == 'n' : break

    print 'len of data', len(dataList)

    del stockChart

def testStockMst(version) :
    
    if version == 1 :
        testStockMst_ver_1()
    elif version == 2 :
        testStockMst_ver_2()
    elif version == 3 :
        testStockMst_ver_3()

def testStockMst_ver_2() :
    from common import testBlockRequest
    from cxFile import cxFile

    stockCode = u'A000660'
    paramList = [ [ 0, stockCode ], ]
    option = 1
    if option == 1 :
        print testBlockRequest('cxCpStockMst', paramList, 1, 1, 0, 0)
    else :
        resultFile = cxFile()
        testBlockRequest( 'cxCpStockMst', paramList, 1, 1, 0, 0,resultFile )
        resultFile.close()

def testFutureMst() :
    "전체 선물 정보를 얻어낸다."
    from cxCybosPlus import gCybosPlusClassDic
    from cxCybosPlus import constants
    from common import testBlockRequest
    from cxFile import cxFile
    import time

    #cpFutureMst = gCybosPlusClassDic['cxFutureMst']
    cpFutureCode = gCybosPlusClassDic['cxCpFutureCode']
    cpCybos = gCybosPlusClassDic['cxCpCybos']

    futureNum = cpFutureCode.GetCount()

    futureList = []

    for i in range(0,futureNum) :
        futureCode = cpFutureCode.GetData(0, i)
        futureName = cpFutureCode.GetData(1, i)
        futureList.append([futureCode, futureName])
        #print futureCode, '"',futureName,'"'

    index = 0

    for futureCode, futureName in futureList :
        paramList = [ [ 0, futureCode],]
        print testBlockRequest('cxFutureMst', paramList, 1, 1, 0, 0 )

        remainCount = cpCybos.GetLimitRemainCount(constants.LT_NONTRADE_REQUEST)
        remainTime = cpCybos.LimitRequestRemainTime()
        print index,'remainCount : %d, remainTime : %d'%(remainCount,remainTime)
        if remainCount <= 0 :
            print 'time.sleep for %d sec.'%((remainTime/1000)+1)
            time.sleep((remainTime/1000) + 1)

        print index, futureCode, futureName
        index+=1

def testOptionMst() :
    "전체 옵션 정보를 얻어낸다."
    from cxCybosPlus import gCybosPlusClassDic
    from cxCybosPlus import constants
    from common import testBlockRequest
    from cxFile import cxFile
    import time

    cpOptionCode = gCybosPlusClassDic['cxCpOptionCode']
    cpCybos = gCybosPlusClassDic['cxCpCybos']

    optionNum = cpOptionCode.GetCount()

    optionList = []

    for i in range(0,optionNum) :
        optionCode = cpOptionCode.GetData(0,i)
        optionName = cpOptionCode.GetData(1,i)
        optionType = cpOptionCode.GetData(2,i)
        optionMonth = cpOptionCode.GetData(3,i)
        optionPrice = cpOptionCode.GetData(4,i)

        optionList.append([optionCode,optionName,optionType,optionMonth,optionPrice])
        print optionCode, optionName, optionType, optionMonth, optionPrice


def testStockMst_ver_3() :
    "전체 주식 정보를 얻어낸다."
    from cxStockMgr  import stockMgr
    from cxCybosPlus import gCybosPlusClassDic
    from cxCybosPlus import constants
    from common import testBlockRequest
    from cxFile import cxFile
    import time

    cpCybos = gCybosPlusClassDic['cxCpCybos']
    stockList = stockMgr.getStockList()
    index = 0

    for stockCode, stockName, stockFullCode in stockList :
        paramList = [ [ 0, stockCode],]
        print testBlockRequest('cxCpStockMst', paramList, 1, 1, 0, 0 )

        remainCount = cpCybos.GetLimitRemainCount(constants.LT_NONTRADE_REQUEST)
        remainTime = cpCybos.LimitRequestRemainTime()
        print index,'remainCount : %d, remainTime : %d'%(remainCount,remainTime)
        index+=1
        if remainCount <= 0 :
            print 'time.sleep for %d sec.'%((remainTime/1000)+1)
            time.sleep((remainTime/1000) + 1)

    del stockMgr


def testStockMst_ver_1() :
    from cxCybosPlus import gCybosPlusClassDic
    stockMst = gCybosPlusClassDic['cxCpStockMst']
    stockMst.SetInputValue(0, u'A000660')
    stockMst.BlockRequest()
    option = 1
    if option == 1 :
        headerValueIndexList = [u'0',u'1',u'2',u'3',4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,
                                19,20,21,22,23,24,25,26,27,28,u'31',32,33,34,u'35',36,37,38,39,
                                40,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,
                                60,61,62,63,64,65,66,67,68,69,70]
        for headerValueIndex in headerValueIndexList :
            print headerValueIndex, stockMst.GetHeaderValue(headerValueIndex)

    else :
        from cxFile import cxFile
        from common import UNI
        resultFile = cxFile()
        for headerValueIndex in stockMst.headerIndexDic.keys() :
            name = stockMst.headerIndexDic[headerValueIndex][1]
            value = stockMst.GetHeaderValue(headerValueIndex)
            #print UNI(name) + u' ' + UNI(value)
            #print name, stockMst.GetHeaderValue(headerValueIndex)
            resultFile.write(UNI(name)+u' : '+UNI(value) + u'\n')
        resultFile.close()

    del stockMst

def testCpCodeMgr() :
    from cxCybosPlus import gCybosPlusClassDic
    from cxCybosPlus import constants
    cpCodeMgr = gCybosPlusClassDic['cxCpCodeMgr']

    code = u'A000660'
    print u'종목명 :', cpCodeMgr.CodeToName(code)
    print u'주식 매수 증거금율 :', cpCodeMgr.GetStockMarginRate(code), u'%'
    print u'주식 매매 거래 단위 주식 수 :', cpCodeMgr.GetStockMemeMin(code)
    print u'증권전산업종코드 :', cpCodeMgr.GetStockIndustryCode(code)
    print u'소속부 :',
    category = cpCodeMgr.GetStockMarketKind(code)
    if category == constants.CPC_MARKET_NULL :
        print u'구분없음'
    elif category == constants.CPC_MARKET_KOSPI :
        print u'거래소'
    elif category == constants.CPC_MARKET_KOSDAQ :
        print u'코스닥'
    elif category == constants.CPC_MARKET_FREEBOARD :
        print u'프리보드'
    elif category == constants.CPC_MARKET_KRX :
        print u'KRX'
    else :
        print u'UNKNOWN'

    print u'감리구분 :',
    controlKind = cpCodeMgr.GetStockControlKind(code)
    if controlKind == constants.CPC_CONTROL_NONE :
        print u'정상'
    elif controlKind == constants.CPC_CONTROL_ATTENTION :
        print u'주의'
    elif controlKind == constants.CPC_CONTROL_WARNING :
        print u'경고'
    elif controlKind == constants.CPC_CONTROL_DANGER_NOTICE :
        print u'위험예고'
    elif controlKind == constants.CPC_CONTROL_DANGER :
        print u'위험'
    else :
        print u'UNKNOWN'

    print u'관리여부 :',
    svKind = cpCodeMgr.GetStockSupervisionKind(code)
    if svKind == constants.CPC_SUPERVISION_NONE :
        print u'일반종목'
    elif svKind == constants.CPC_SUPERVISION_NORMAL :
        print u'관리'
    else : print u'UNKNOWN'

    print u'상태구분 :',
    statusKind = cpCodeMgr.GetStockStatusKind(code)
    if statusKind == constants.CPC_STOCK_STATUS_NORMAL :
        print u'정상'
    elif statusKind == constants.CPC_STOCK_STATUS_STOP :
        print u'거래정지'
    elif statusKind == constants.CPC_STOCK_STATUS_BREAK :
        print u'거래중단'
    else : print u'UNKNOWN'

    print u'자본금규모구분 :',
    capital = cpCodeMgr.GetStockCapital(code)
    if capital == constants.CPC_CAPITAL_NULL :
        print u'제외'
    elif capital == constants.CPC_CAPITAL_LARGE :
        print u'대'
    elif capital == constants.CPC_CAPITAL_MIDDLE :
        print u'중'
    elif capital == constants.CPC_CAPITAL_SMALL :
        print u'소'
    else : print u'UNKNOWN'

    print u'결산기', cpCodeMgr.GetStockFiscalMonth(code)
    print u'계열사 코드', cpCodeMgr.GetStockGroupCode(code)

    """
    cputil.dll 이 안바뀌는 듯, CPC_KOSPI200_CONSTRUCTIONS_MACHINERY 이하 상수들이
    반영이 안됨에도 CybosPlus 서버에서는 변경된 상수들로 값들을 제공하는 것을 보임.
    따라서 아래 상수들을 name base가 아닌 value base로 접근하도록 수정함. 
    """
    print u'KOSPI200 종목 :', 
    kospi200 = cpCodeMgr.GetStockKospi200Kind(code)
    """
    gStockKospi200KindDic = {
        constants.CPC_KOSPI200_NONE     : u'미채용',
        constants.CPC_KOSPI200_MANUFACTURE     : u'제조업',
        constants.CPC_KOSPI200_TELECOMMUNICATION     : u'전기통신업',
        constants.CPC_KOSPI200_CONSTRUCT     : u'건설업',
        constants.CPC_KOSPI200_CURRENCY     : u'유통업',
        constants.CPC_KOSPI200_FINANCE     : u'금융업',
    }
    """
    gStockKospi200KindDic = {
        0 : u'미채용',
        1 : u'건설기계',
        2 : u'조선운송',
        3 : u'철강소재',
        4 : u'에너지화학',
        5 : u'정보통신',
        6 : u'금융',
        7 : u'필수소비재',
        8 : u'자유소비재',
    }
    try:
        print gStockKospi200KindDic[kospi200]
    except BaseException as e :
        print e, kospi200
    """
    if kospi200 == constants.CPC_KOSPI200_NONE :
        print u'미채용'
    elif kospi200 == constants.CPC_KOSPI200_CONSTRUCTIONS_MACHINERY :
        print u'건설기계'
    elif kospi200 == constants.CPC_KOSPI200_SHIPBUILDING_TRANSPORTATION :
        print u'조선운송'
    elif kospi200 == constants.CPC_KOSPI200_STEELS_METERIALS :
        print u'철강소재'
    elif kospi200 == constants.CPC_KOSPI200_ENERGY_CHEMICALS :
        print u'에너지화학'
    elif kospi200 == constants.CPC_KOSPI200_IT :
        print u'정보통신'
    elif kospi200 == constants.CPC_KOSPI200_FINANCE :
        print u'금융'
    elif kospi200 == constants.CPC_KOSPI200_CUSTOMER_STAPLES :
        print u'필수소비재'
    elif kospi200 == constants.CPC_KOSPI200_CUSTOMER_DISCRETIONARY :
        print u'자유소비재'
    else : print u'UNKNOWN'
    """
    

    sectionKind = cpCodeMgr.GetStockSectionKind(code)
    print u'부 구분코드 :',
    gStockSectionKindDic = {
        constants.CPC_KSE_SECTION_KIND_NULL  : u'구분없음',
        constants.CPC_KSE_SECTION_KIND_ST    : u'주권',
        constants.CPC_KSE_SECTION_KIND_MF    : u'투자회사',
        constants.CPC_KSE_SECTION_KIND_RT    : u'부동산투자회사',
        constants.CPC_KSE_SECTION_KIND_SC    : u'선박투자회사',
        constants.CPC_KSE_SECTION_KIND_IF    : u'사회간접자본투융자회사',
        constants.CPC_KSE_SECTION_KIND_DR    : u'주식예탁증서',
        constants.CPC_KSE_SECTION_KIND_SW    : u'신수인수권증권',
        constants.CPC_KSE_SECTION_KIND_SR    : u'신주인수권증서',
        constants.CPC_KSE_SECTION_KIND_ELW   : u'주식워런트증권',
        constants.CPC_KSE_SECTION_KIND_ETF   : u'상장지수펀드',
        constants.CPC_KSE_SECTION_KIND_BC    : u'수익증권',
        constants.CPC_KSE_SECTION_KIND_FETF  : u'해외ETF',
        constants.CPC_KSE_SECTION_KIND_FOREIGN : u'외국주권',
        constants.CPC_KSE_SECTION_KIND_FU    : u'선물',
        constants.CPC_KSE_SECTION_KIND_OP    : u'옵션',
    }
    try:
        print gStockSectionKindDic[sectionKind]
    except BaseException as e :
        print e, sectionKind

    print u'락 구분코드 :',
    lacKind = cpCodeMgr.GetStockLacKind(code)
    gLacKindDic = {
        constants.CPC_LAC_NORMAL             : u'구분없음',
        constants.CPC_LAC_EX_RIGHTS          : u'권리락',
        constants.CPC_LAC_EX_DIVIDEND        : u'배당락',
        constants.CPC_LAC_EX_DISTRI_DIVIDEND : u'분배락',
        constants.CPC_LAC_EX_RIGHTS_DIVIDEND : u'권배락',
        constants.CPC_LAC_INTERIM_DIVIDEND   : u'중간배당락',
        constants.CPC_LAC_EX_RIGHTS_INTERIM_DIVIDEND : u'권리중간배당락',
        constants.CPC_LAC_ETC                : u'기타'
    }
    try :
        print gLacKindDic[lacKind]
    except BaseException as e :
        print e, lacKind

    print u'상장일   :', cpCodeMgr.GetStockListedDate(code)
    print u'상한가   :', cpCodeMgr.GetStockMaxPrice(code)
    print u'하한가   :', cpCodeMgr.GetStockMinPrice(code)
    print u'액면가   :', cpCodeMgr.GetStockParPrice(code)
    print u'기준가   :', cpCodeMgr.GetStockStdPrice(code)
    print u'전일시가 :', cpCodeMgr.GetStockYdOpenPrice(code)
    print u'전일고가 :', cpCodeMgr.GetStockYdHighPrice(code)
    print u'전일저가 :', cpCodeMgr.GetStockYdLowPrice(code)
    print u'전일종가 :', cpCodeMgr.GetStockYdClosePrice(code)
    print u'신용여부 :', 
    if cpCodeMgr.IsStockCreditEnable(code) == 1 :
        print u'Yes'
    else : print u'No'

    print u'액면정보코드 :',
    parPriceCode = cpCodeMgr.GetStockParPriceChageType(code)
    gParPriceCodeDic = {
        constants.CPC_PARPRICE_CHANGE_NONE : u'해당없음',
        constants.CPC_PARPRICE_CHANGE_DIVIDE : u'액면분할',
        constants.CPC_PARPRICE_CHANGE_MERGE : u'액면병합',
        constants.CPC_PARPRICE_CHANGE_ETC : u'기타',
    }
    try :
        print gParPriceCodeDic[parPriceCode]
    except BaseException as e :
        print e, parPriceCode

def testBuy() :
    from Queue          import Queue
    from cxCybosPlus    import gCybosPlusClassDic
    import win32gui
    import time
    from common         import getResultStringPortrait
    from cxFile         import cxFile

    reportQueue = Queue()
    conclusionQueue = Queue()

    cpTdUtil = gCybosPlusClassDic['cxCpTdUtil']
    result = cpTdUtil.TradeInit()

    if result != 0 :
        print 'cpTdUtil.init failed'
        return
    accountList = cpTdUtil.AccountNumber()
    goodsList = cpTdUtil.GoodsList(accountList[0], 3)

    cpConclusion = gCybosPlusClassDic['cxCpConclusion']
    cpConclusion.open()
    cpConclusion.set_result_queue(conclusionQueue)
    cpConclusion.Subscribe()

    cpTd0311 = gCybosPlusClassDic['cxCpTd0311']
    cpTd0311.open()
    cpTd0311.set_result_queue(reportQueue)

    cpTd0311.SetInputValue(0, 2)        # 1 : sell, 2 : buy
    cpTd0311.SetInputValue(1, accountList[0])
    cpTd0311.SetInputValue(2, goodsList[0])

    stockCode = u'A005180'      #빙그레
    amount = 1
    unitPrice = 1
    tradeCondition = 0
    tradeType = '03'

    cpTd0311.SetInputValue(3, stockCode)
    cpTd0311.SetInputValue(4, amount)
    cpTd0311.SetInputValue(5, unitPrice)
    cpTd0311.SetInputValue(7, tradeCondition)
    cpTd0311.SetInputValue(8, tradeType)

#    result = cpTd0311.BlockRequest()
    result = cpTd0311.Request()
    print 'result', result
    print 'GetDibStatus',cpTd0311.GetDibStatus()
    print 'GetDibMsg1', cpTd0311.GetDibMsg1()
    print 'Continue', cpTd0311.Continue()
    #print cpTd0311.get_header_value_list()

    cntConclusion = 0
    resultFile = cxFile()

    while True :
        if reportQueue.qsize() != 0 :
            print reportQueue.qsize()
            resultList = reportQueue.get()
            resultString = getResultStringPortrait(resultList, 1, 1, 1, 1 )
            print resultString
            resultFile.write(resultString)
            print resultList[0]
            print resultList[4]
            if ( resultList[0] == -1 ) and ( resultList[4] == u'cxCpTd0311' ) :
                del resultList
                del resultString
                break
            del resultList
            del resultString

        if conclusionQueue.qsize() != 0 :
            resultList = conclusionQueue.get()
            resultString = getResultStringPortrait(resultList, 1, 1, 1, 1)
            print resultString
            resultFile.write(resultString)
            print resultList[0]
            print resultList[4]

            cntConclusion += 1
            
            if cntConclusion >= 2 :
                break

        win32gui.PumpWaitingMessages()
        time.sleep(0.5)

    resultFile.close()
    cpConclusion.Unsubscribe()
    cpConclusion.close()

def getStockSize() :
    from cxStockMgr import stockMgr
    print 'number of stock : ', len(stockMgr.getStockList())
    print
    # 2129 개

def test() :
    #testCpSvrNew7216()
    #testStockChart()
    #testStockMst(1)
    #testFutureMst()
    #testOptionMst()
    #testCpCodeMgr()
    #testBuy()
    getStockSize()

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
