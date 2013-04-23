################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxCybosInterface.py
# date        : 2012-10-06 18:45:35
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

from Queue          import Queue

from cxCybosPlus    import cxCpCybos
from cxCybosPlus    import cxCpTdUtil
from cxCybosPlus    import cxCpTd0311       # for 매수, 매도
from cxCybosPlus    import cxCpTd0313       # for 주문 정정
from cxCybosPlus    import cxCpTd0314       # for 주문 취소
from cxCybosPlus    import cxCpTdNew5331A   # for 예수금 조희
from cxCybosPlus    import cxCpTd0732       # for 최종 결제 예정 예수금 조회 (모의투자)
from cxCybosPlus    import cxCpConclusion   # for Trade Event 수신
from cxCybosPlus    import cxCpTd6033       # for 
from cxCybosPlus    import cxCpTd5339       # for 미체결 잔량 데이터 요청
from cxCybosPlus    import cxCpStockCur     # for subscribing current values of stock
from cxCybosPlus    import cxCpStockMst     # for requesting current values of stock
from cxCybosPlus    import cxCpStockJpBid   # for subscribing current bid of stock
from cxCybosPlus    import constants

from cxCybosPlus    import getCybosPlusClassDic
from cxError        import cxError
"""
cxCybosInterface

    -- resultQueue operations --
    delResultQueue()
    setResultQueue(resultQueue)

    -- reportQueue operations --
    report(params)
    delReportQueue()
    setReportQueue(reportQueue)


"""

class cxCybosInterface :

    cpTdUtil        = cxCpTdUtil()
    cpTd0311        = cxCpTd0311()
    cpTd0313        = cxCpTd0313()
    cpTd0314        = cxCpTd0314()
    cpConclusion    = cxCpConclusion()
    cpCybos         = cxCpCybos()
    cpTdNew5331A    = cxCpTdNew5331A()
    cpTd0732        = cxCpTd0732()
    cpTd6033        = cxCpTd6033()
    cpTd5339        = cxCpTd5339()
    cpStockCur      = cxCpStockCur()
    cpStockMst      = cxCpStockMst()
    cpStockJpBid    = cxCpStockJpBid()

    resultQueue     = None
    reportQueue     = None

    accountList     = None
    goodsList       = None

    resultInitTradeUtil = None
    resultGetAccount    = None

    limitTradeReqRemainCount        = 0
    limitTradeNonReqRemainCount     = 0
    limitSubscribeReqRemainCount    = 0
    limitRequestRemainTime          = 0

    def __init__(self) :
        pass

    def __del__(self) :
        pass

    def getLimitTradeReqRemainCount(self) :
        self.limitTradeReqRemainCount = \
            self.cpCybos.GetLimitRemainCount(constants.LT_TRADE_REQUEST)
        return self.limitTradeReqRemainCount

    def getLimitNonTradeReqRemainCount(self) :
        self.limitNonTradeReqRemainCount = \
            self.cpCybos.GetLimitRemainCount(constants.LT_NONTRADE_REQUEST)
        return self.limitNonTradeReqRemainCount

    def getLimitSubscribeReqRemainCount(self) :
        self.limitSubscribeReqRemainCount = \
            self.cpCybos.GetLimitRemainCount(constants.LT_SUBSCRIBE)
        return self.limitSubscribeReqRemainCount

    def getLimitRequestRemainTime(self) :
        self.limitRequestRemainTime = \
            self.cpCybos.com_cp.LimitRequestRemainTime
        return self.limitRequestRemainTime

    def delResultQueue(self) :
        if self.resultQueue is not None :
            del self.resultQueue
            self.resultQueue = None
            self.cpTd0311.del_result_queue()
            self.cpStockCur.del_result_queue()
            self.cpStockMst.del_result_queue()
            self.cpConclusion.del_result_queue()

    def setResultQueue(self, resultQueue) :
        if resultQueue is None : return 1
        if isinstance(resultQueue, Queue) :
            if self.resultQueue is not None :
                self.delResultQueue()
            self.resultQueue = resultQueue
            self.cpTd0311.set_result_queue(resultQueue)
            self.cpStockCur.set_result_queue(resultQueue)
            self.cpStockMst.set_result_queue(resultQueue)
            self.cpStockJpBid.set_result_queue(resultQueue)
            self.cpConclusion.set_result_queue(resultQueue)
            return 0
        else : return 2

    def delReportQueue(self) :
        if self.reportQueue is not None :
            del self.reportQueue
            self.reportQueue = None
            self.cpTd0311.del_report_queue()
            self.cpStockCur.del_report_queue()
            self.cpStockMst.del_report_queue()
            self.cpStockJpBid.del_report_queue()
            self.cpConclusion.del_report_queue()

    def setReportQueue(self, reportQueue) :
        if reportQueue is None : return 1 
        if isinstance(reportQueue, Queue) :
            if self.reportQueue is not None :
                self.delReportQueue()
            self.reportQueue = reportQueue
            self.cpTd0311.set_report_queue(reportQueue)
            self.cpStockCur.set_report_queue(reportQueue)
            self.cpStockMst.set_report_queue(reportQueue)
            self.cpStockJpBid.set_report_queue(reportQueue)
            self.cpConclusion.set_report_queue(reportQueue)
            return 0
        else : return 2

    def report(self, params) :
        if self.reportQueue is None :
            print params
        elif isinstance(self.reportQueue, Queue ) :
            self.reportQueue.put(params)
        else :
            return 1
        return 0

    def open(self) :
        self.cpTd0311.open()
        self.cpTd0313.open()
        self.cpTd0314.open()
        self.cpStockCur.open()
        self.cpStockMst.open()
        self.cpStockJpBid.open()
        self.cpConclusion.open()

    def close(self) :
        self.cpTd0311.close()
        self.cpTd0313.close()
        self.cpTd0314.close()
        self.cpStockCur.close()
        self.cpStockMst.close()
        self.cpStockJpBid.close()
        self.cpConclusion.close()

    def init(self,resultQueue = None,reportQueue = None) :
        if ( resultQueue is not None ) and ( isinstance(resultQueue, Queue) ) :
            self.setResultQueue(resultQueue)
        if ( reportQueue is not None ) and ( isinstance(reportQueue, Queue) ) :
            self.setReportQueue(reportQueue)

        self.open()


        self.resultInitTradeUtil = self.initTradeUtil()
        self.resultGetAccount = self.getAccount()
        if ( self.resultInitTradeUtil is 0 ) and (self.resultGetAccount is 0 ) : 
            self.cpConclusion.Subscribe()
            return 0
        else : return 1


    def deinit(self) :
        self.cpConclusion.Unsubscribe()
        self.close()

        self.delResultQueue()
        self.delReportQueue()

    def initTradeUtil(self) :
        result = self.cpTdUtil.TradeInit()
        if      result is 0 :
            self.report(u'TradeInit() 초기화 성공')
        elif    result is 1 :
            self.report(u'업무 키 입력 잘못됨')
        elif    result is 2 :
            self.report(u'계좌 비밀 번호 입력 잘못됨')
        elif    result is 3 :
            self.report(u'취소됨')
        else :
            self.report(u'알 수 없는 에러 코드 : %d'%(result))
        return result

    def getAccount(self) :
        if self.resultInitTradeUtil is not 0 : return 1
        self.accountList = self.cpTdUtil.AccountNumber()
        if self.accountList is None : return 3
        if self.accountList[0] == u'000000000' :
            self.report(u'계좌가 없거나, 계좌가 무효화되었습니다.')
            return 2
        else :
            self.report(u'주계좌 번호 : %s'%(self.accountList[0]))
        self.goodsList = self.cpTdUtil.GoodsList(self.accountList[0], 3)
        if self.goodsList is not None :
            if len(self.goodsList) >= 1 :
                self.report(u'주식계좌 : %s'%(self.goodsList[0]))
            if len(self.goodsList) >= 2 :
                self.report(u'선물계좌 : %s'%(self.goodsList[1]))
        return 0

    def request(self, objectName, params ) :
        pass

    def requestBlockTd5339( self, jongMokCode = '', 
                            joomunGuBunCode = 0, jungRyulGuBunCode = 0,  
                            joomunJongGaGuBunCode = 0,
                            yochungGeSu = 20 ) :
        self.cpTd5339.SetInputValue( 0, self.accountList[0] )
        self.cpTd5339.SetInputValue( 1, self.goodsList[0] )
#        self.cpTd5339.SetInputValue( 3, jongMokCode )
#        self.cpTd5339.SetInputValue( 4, joomunGuBunCode )
#        self.cpTd5339.SetInputValue( 5, jungRyulGuBunCode )
#        self.cpTd5339.SetInputValue( 6, joomunJongGaGuBunCode )
        self.cpTd5339.SetInputValue( 7, yochungGeSu )
        self.cpTd5339.BlockRequest()
        resultList = self.cpTd5339.getResult()
        return resultList

    def requestBlockTd6033( self, numRequest = 14 ) :
        self.cpTd6033.SetInputValue( 0, self.accountList[0] )
        self.cpTd6033.SetInputValue( 1, self.goodsList[0] )
        self.cpTd6033.SetInputValue( 2, numRequest )
        self.cpTd6033.BlockRequest()
        resultList = self.cpTd6033.getResult()
        return resultList

    def requestBlockTd0732( self ) :
        self.cpTd0732.SetInputValue( 0, self.accountList[0] )
        self.cpTd0732.SetInputValue( 1, self.goodsList[0] )

        self.cpTd0732.BlockRequest()
        resultList = self.cpTd0732.getResult()
        return resultList


    def requestBlockTdNew5331A( self, 
                                stockCode =u'', 
                                orderAskingPrice='01',
                                unitPrice = 0,
                                unpaidAmountCondition = 'N',
                                searchCode = '1' ) :
        self.cpTdNew5331A.SetInputValue( 0, self.accountList[0] )
        self.cpTdNew5331A.SetInputValue( 1, self.goodsList[0] )
        #self.cpTdNew5331A.SetInputValue( 2, stockCode )
        #self.cpTdNew5331A.SetInputValue( 3, orderAskingPrice )  # 주문호가구분코드 : 01 'default'
        #self.cpTdNew5331A.SetInputValue( 4, unitPrice )         # 주문단가 : 0 'default'
        #self.cpTdNew5331A.SetInputValue( 5, unpaidAmountCondition )
        #self.cpTdNew5331A.SetInputValue( 6, searchCode )

        self.cpTdNew5331A.BlockRequest()
        resultList = self.cpTdNew5331A.getResult()
        return resultList 

                                            # 미수발생증거금 100 퍼센트 징수 여부 코드
                                            # N  : 계좌별증거금 [default]
                                            # Y  : 증거금 100
                                            # 조회구분코드
                                            # '1' : 금액조회 [default]
                                            # '2' : 수량조회
        

    def requestCancel(self, orderID, stockCode, amount = 0 ) :

        self.cpTd0314.SetInputValue(1, orderID )                # 원주문번호
        self.cpTd0314.SetInputValue(2, self.accountList[0] )    # 계좌번호
        self.cpTd0314.SetInputValue(3, self.goodsList[0] )      # 상품관리구분코드
        self.cpTd0314.SetInputValue(4, stockCode )              # 종목코드
        self.cpTd0314.SetInputValue(5, amount )                 # 취소수량 (0 : 가능수량 자동계산됨)
        return self.cpTd0314.Request()

    def requestModify(self, orderID, stockCode, unitPrice, amount = 0 ) :

        self.cpTd0313.SetInputValue(1, orderID )                # 원주문번호
        self.cpTd0313.SetInputValue(2, self.accountList[0] )    # 계좌번호
        self.cpTd0313.SetInputValue(3, self.goodsList[0] )      # 상품관리구분코드
        self.cpTd0313.SetInputValue(4, stockCode )              # 종목코드
        self.cpTd0313.SetInputValue(5, amount )                 # 취소수량 (0 : 가능수량 자동계산됨)
        self.cpTd0313.SetInputValue(6, unitPrice )              # 주문단가
        return self.cpTd0313.Request()


    """
    tradeCondition : 0 -> default, 1 -> IOC (Immediate or Cancel), 2 -> FOK (Fill or Kill)
                     in test mode, only default value is supported.
    tradeType      : '01' -> default, '03' -> 시장가
    """
    def requestBuy(self, stockCode, unitPrice, amount, tradeCondition, tradeType) :
        #TODO : check the type of params.
        self.cpTd0311.SetInputValue(0, 2)                   # 매수 -> 2
        self.cpTd0311.SetInputValue(1, self.accountList[0]) # 계정
        self.cpTd0311.SetInputValue(2, self.goodsList[0])   # 계정 구분 (주식)
        self.cpTd0311.SetInputValue(3, stockCode)           # 종목 코드
        self.cpTd0311.SetInputValue(4, amount)              # 주문 수량
        self.cpTd0311.SetInputValue(5, unitPrice)           # 매수 단가
        self.cpTd0311.SetInputValue(7, tradeCondition)      # 주문 조건 구분
        self.cpTd0311.SetInputValue(8, tradeType)           # 주문 호가 구분
       
        try:
            result = self.cpTd0311.Request()
        except cxError as e :
            print e.dump()
        
        """
        result = self.cpTd0311.BlockRequest()
        print 'result', result
        print 'GetDibStatus',self.cpTd0311.GetDibStatus()
        print 'GetDibMsg1', self.cpTd0311.GetDibMsg1()
        print 'Continue', self.cpTd0311.Continue()

        print self.cpTd0311.get_header_value_list()
        #"""
        return result

    def requestSell(self, stockCode, unitPrice, amount, tradeCondition, tradeType) :
        #TODO : check the type of params.
        self.cpTd0311.SetInputValue(0, 1)                   # 매도 -> 1 
        self.cpTd0311.SetInputValue(1, self.accountList[0])     # 계정
        self.cpTd0311.SetInputValue(2, self.goodsList[0])   # 계정 구분 (주식)
        self.cpTd0311.SetInputValue(3, stockCode)           # 종목 코드
        self.cpTd0311.SetInputValue(4, amount)              # 주문 수량
        self.cpTd0311.SetInputValue(5, unitPrice)           # 매수 단가
        self.cpTd0311.SetInputValue(7, tradeCondition)      # 주문 조건 구분
        self.cpTd0311.SetInputValue(8, tradeType)           # 주문 호가 구분

        return self.cpTd0311.Request()

    def requestStockMst(self, stockCode) :
        try : self.cpStockMst.SetInputValue(0,stockCode)
        except : return False
        try : self.cpStockMst.Request()
        except : return False
        return True

    def subscribeStockCur(self, stockCode) :
        try : self.cpStockCur.SetInputValue(0, stockCode)
        except : return False
        try : self.cpStockCur.Subscribe()
        except : return False
        return True

    def subscribeStockJpBid(self, stockCode) :
        try : self.cpStockJpBid.SetInputValue(0, stockCode)
        except : return False
        try : self.cpStockJpBid.Subscribe()
        except : return False
        return True

    def subscribeStockCode(self, stockCode) :
        if self.subscribeStockCur( stockCode ) == False : return False
        if self.subscribeStockJpBid( stockCode ) == False : return False
        return True

    def unsubscribeStockCur(self, stockCode) :
        try : self.cpStockCur.SetInputValue(0,stockCode)
        except : return False
        try : self.cpStockCur.Unsubscribe()
        except : return False
        return True

    def unsubscribeStockJpBid(self, stockCode) :
        try : self.cpStockJpBid.SetInputValue(0,stockCode)
        except : return False
        try : self.cpStockJpBid.Unsubscribe()
        except : return False
        return True

    def unsubscribeStockCode(self, stockCode) :
        self.unsubscribeStockCur( stockCode )
        self.unsubscribeStockJpBid( stockCode )

# end of cxCybosInterface

def test() :
    test_getCybosPlusClassDic()

def test_getCybosPlusClassDic() :
    import sys
    dic = getCybosPlusClassDic( sys.stdout )
    print dic

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
