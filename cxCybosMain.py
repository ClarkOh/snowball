################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxCybosMain.py
# date        : 2012-08-08 02:45:10
# ver         :
# desc.       :
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import win32gui
import time

from cxCybosInterface   import cxCybosInterface
from cxConsoleThread    import cxConsoleThread
from Queue              import Queue
from cxStockMgr         import cxStockMgr       # for stock information
from cxLog              import cxLog            # for Logging

subscribeLog = cxLog()


class cxCybosMain :

    cybosIF = cxCybosInterface()
    tradeRequestQueue = Queue()     # waiting trade request queue
    nonTradeRequestQueue = Queue()  # waiting non-trade request queue
    subscribeRequestQueue = Queue() # waiting subscribe request queue
    resultQueue = Queue()   # waiting result queue from received event
    reportQueue = Queue()   # waiting report queue from cybosplus objects

    consoleInputQueue = Queue() # waiting key input from console thread
    consoleOutputQueue = None

    _terminate = False

    consoleThread = cxConsoleThread()

    """
    option : 0 -> real trading mode
             1 -> test mode with CybosPlus
             2 -> test mode without CybosPlus
    """
    REAL_TRADE_MODE         = 0
    TEST_MODE_WITH_CP       = 1
    TEST_MODE_WITHOUT_CP    = 2

    option = 0

    loopInterval = 0.05          # 0.1 -> 100 msec.
    monitoringWaitCount = 0
    monitoringWaitSecond = 3    # 10 sec.

    subscribeList = []

    def __init__(self) :
        print "hello cxCybosMain"
        self.stockMgr = cxStockMgr()
        if self.stockMgr.update() > 0 :
            print 'update stockMgr is OK!!'


    def __del__(self) :
        pass

    def setMonitoringInterval(self, monitoringInterval) :
        if isinstance(monitoringInterval, int) is False : return
        if (monitoringInterval <= 0 ) or (monitoringInterval > 100) : return
        self.monitoringWaitSecond = int(monitoringInterval)

    def bUseCP(self) :
        if (self.option == self.REAL_TRADE_MODE ) or (self.option == self.TEST_MODE_WITH_CP ) :
            return True
        else :
            return False

    def init(self, option = 0) :

        self.option = option
        if self.bUseCP() is True :
            self.cybosIF.init(self.resultQueue, self.reportQueue)

        #TODO : set queues
        self.consoleThread.setRequestQueue(self.consoleInputQueue)
        self.consoleOutputQueue = self.consoleThread.getResultQueue()
        self.consoleThread.start()

        self.monitoringWaitCount = ( self.getOneSecondCount() * self.monitoringWaitSecond )

        self.loadSubscribeList()

    def deinit(self) :
        self.consoleThread.join()
        if self.bUseCP() is True :
            self.cybosIF.deinit()

    def terminate(self) :
        self._terminate = True

    def consoleOutput(self,params ) :
        if params is None : return 1
        if self.consoleOutputQueue is None :
            print params
            return 2
        if isinstance(self.consoleOutputQueue, Queue) is False : return 3
        self.consoleOutputQueue.put(params)
        return 0

    def getResultString(self, resultList) :
        if resultList is None : return u''
        if isinstance(resultList, list) :
            resultString = u''
            resultString += u'\tGetDibStatus : %d'%(resultList[0]) + u'\n' #GetDibStatus
            resultString += u'\tGetDibMsg1   : %s'%(resultList[1]) + u'\n' #GetDibMsg1
            resultString += u'\tContinue     : %d'%(resultList[2]) + u'\n' #Continue
            resultString += u'\tTime         : %s'%(resultList[3]) + u'\n' #time
            resultString += u'\tClass Name   : %s'%(resultList[4]) + u'\n' #class name
            if len(resultList[5]) :
                for headerDic in resultList[5] :
                    for key in headerDic.keys() :
                        resultString += u'\t%s : %s'%(headerDic[key][1], headerDic[key][2]) + u'\n'
            if len(resultList[6]) :
                dataList = resultList[6]
                for dataDic in dataList :
                    for key in dataDic.keys() :
                        resultString += u'\t\t%s : %s'%(dataDic[key][1], dataDic[key][2]) + u'\n'

            return resultString
        else : return u''

    def printResult(self, resultList):
        if isinstance(resultList, list) :
            self.consoleOutput( self.getResultString(resultList))

    def setMonitoringIntervale(self, interval ) :
        self.monitoringWaitSecond = interval

    def getSettingValueString(self) :
        settingValueString  = u'\tmon interval  : %d'%self.monitoringWaitSecond + '\n'
        settingValueString += u'\tinput timeout : %d'%self.consoleThread.getInputWaitTimeout() + '\n'
        return settingValueString


    def parsingConsoleInputQueue(self) :

        if self.consoleInputQueue.qsize() == 0 : return 1
        for i in range(0, self.consoleInputQueue.qsize()) :
            request = self.consoleInputQueue.get()
            if request is None : return 2
            #print request
            requestList = request.split()
            #print requestList
            if requestList[0] == 'exit' :
                self.terminate()
            if requestList[0] == 'buy' :
                if len(requestList) != 6 :
                    self.consoleOutput(self.getHelp(requestList))
                else :
                    self.tradeRequestQueue.put(requestList)
            elif requestList[0] == 'sell' :
                if len(requestList) != 6 :
                    self.consoleOutput(self.getHelp(requestList))
                else :
                    self.tradeRequestQueue.put(requestList)
            elif requestList[0] == 'get' :
                if len(requestList) != 2 :
                    self.consoleOutput(self.getHelp(requestList))
                elif requestList[1] == '5331A':
                    self.printResult(self.cybosIF.requestBlockTdNew5331A())
                elif requestList[1] == '0732' :
                    self.printResult(self.cybosIF.requestBlockTd0732())
                elif requestList[1] == '6033' :
                    self.printResult(self.cybosIF.requestBlockTd6033())
                elif requestList[1] == '5339' :
                    self.printResult(self.cybosIF.requestBlockTd5339())

            elif requestList[0] == 'requestStockMst' :
                self.nonTradeRequestQueue.put(requestList)

            elif requestList[0] == 'subscribe' :
                self.subscribeRequestQueue.put(requestList)
            elif requestList[0] == 'unsubscribe' :
                self.subscribeRequestQueue.put(requestList)
            elif requestList[0] == 'request' :
                self.nonTradeRequestQueue.put(requestList)

            elif requestList[0] == 'help' :
                self.consoleOutput(self.getHelp(requestList))
            elif requestList[0] == 'set' :
                if len(requestList) == 1 :
                    self.consoleOutput(self.getSettingValueString())
                if len(requestList) == 4 and \
                        requestList[1] == 'mon' and \
                        requestList[2] == 'interval' :
                    self.setMonitoringInterval(int(requestList[3]))
                    self.consoleOutput(self.getSettingValueString())
                if len(requestList) == 4 and \
                        requestList[1] == 'input' and \
                        requestList[2] == 'timeout' :
                    self.consoleThread.setInputWaitTimeout(int(requestList[3]))
                    self.consoleOutput(self.getSettingValueString())
            elif requestList[0] == 'find' :
                if len(requestList) == 1 :
                    self.consoleOutput(self.getHelp(requestList))
                elif len(requestList) == 2 :
                    self.consoleOutput(self.getFindString(requestList[1]))
                else :
                    self.consoleOutput(self.getHelp(requestList))
            else :
                self.consoleOutput(u'unknown command : %s'%request)

        return 0

    """
    def processRequestQueueTestMode(self) :
        if self.tradeRequestQueue.qsize() != 0 :
            request = self.tradeRequestQueue.get()
            self.consoleOutput(u'tradeRequest : %s'%request)
        if self.nonTradeRequestQueue.qsize() != 0 :
            request = self.nonTradeRequestQueue.get()
            self.consoleOutput(u'nonTradeRequest : %s'%request)
        if self.subscribeRequestQueue.qsize() != 0 :
            request = self.subscribeRequestQueue.get()
            self.consoleOutput(u'subscribeRequest : %s'%request)
        return 0
    """

    def requestBuy( self, request ) :
        if isinstance(request, list ) is False : return 1
        if self.bUseCP() is False :
            string = u'tradeRequest : '
            for i in range(0,len(request) ) :
               string += request[i] + ' '
            string += '\n'
            self.consoleOutput(string)
        else :
            self.cybosIF.requestBuy( request[1],
                                        int(request[2]),
                                        int(request[3]),
                                        int(request[4]),
                                        request[5] )
        return 0

    def requestSell( self, request ) :
        if isinstance(request, list ) is False : return 1
        if self.bUseCP() is False :
            string = u'tradeRequest : '
            for i in range(0,len(request) ) :
               string += request[i] + ' '
            string += '\n'
            self.consoleOutput(string)
        else :
            self.cybosIF.requestSell( request[1],
                                        int(request[2]),
                                        int(request[3]),
                                        int(request[4]),
                                        request[5] )
        return 0

    def requestStockMst(self, stockCode ) :
        if self.bUseCP() is False :
            string = u'stockMst.request : ' + stockCode + u'\n'
            self.consoleOutput(string)
        else :
            self.cybosIF.requestStockMst( stockCode )

    def subscribeStock(self, stockCode ) :
        if self.bUseCP() is False :
            string = u'subscribe request for ' + stockCode + u'\n'
            self.consoleOutput(string)
        else :
            self.cybosIF.subscribeStockCode(stockCode)
            self.cybosIF.subscribeStockJpBid(stockCode)

    def getFindString(self, keyword ) :
        string = u''
        for stockItem in self.stockMgr.searchStockCode( keyword ) :
            string += u'\t' + stockItem[0] + u'\t' + stockItem[1] + u'\n'
        self.consoleOutput(string)

    def getHelp(self, cmd ) :
        helpStr = u''
        if cmd[0] == 'buy' :
            helpStr  = u'\tbuy 종목코드 주문수량 주문단가 주문조건구분코드 주문호가구분코드\n'
            if len(cmd) == 1 : return helpStr
            if cmd[1] != 'more' : return helpStr

            helpStr += u'\t\t종목코드         : string\n'
            helpStr += u'\t\t주문수량         : long\n'
            helpStr += u'\t\t주문조건구분코드 : long \n'
            helpStr += u'\t\t\t 0   : default\n'
            helpStr += u'\t\t\t 1   : IOC\n'
            helpStr += u'\t\t\t 2   : FOK\n'
            helpStr += u'\t\t주문호가구분코드 : string \n'
            helpStr += u'\t\t\t\'01\' : 보통\n'
            helpStr += u'\t\t\t\'02\' : 임의\n'
            helpStr += u'\t\t\t\'03\' : 시장가\n'
            helpStr += u'\t\t\t\'05\' : 조건부지정가\n'
            helpStr += u'\t\t\t\'06\' : 희망대량\n'
            helpStr += u'\t\t\t\'09\' : 자사주\n'
            helpStr += u'\t\t\t\'12\' : 최유리지정가\n'
            helpStr += u'\t\t\t\'13\' : 최우선지정가\n'
            helpStr += u'\t\t\t\'10\' : 스톡옵션자사주\n'
            helpStr += u'\t\t\t\'23\' : 임의시장가\n'
            helpStr += u'\t\t\t\'25\' : 임의조건부지정가\n'
            helpStr += u'\t\t\t\'51\' : 장중대량\n'
            helpStr += u'\t\t\t\'52\' : 장중바스켓\n'
            helpStr += u'\t\t\t\'61\' : 개시전종가\n'
            helpStr += u'\t\t\t\'62\' : 개시전종가대량\n'
            helpStr += u'\t\t\t\'63\' : 개시전시간외바스켓\n'
            helpStr += u'\t\t\t\'67\' : 개시전금전신탁자사주\n'
            helpStr += u'\t\t\t\'69\' : 개시전대량자기\n'
            helpStr += u'\t\t\t\'71\' : 신고대량(전장시가)\n'
            helpStr += u'\t\t\t\'72\' : 시간외대량\n'
            helpStr += u'\t\t\t\'73\' : 신고대량(종가)\n'
            helpStr += u'\t\t\t\'77\' : 금전신탁종가대량\n'
            helpStr += u'\t\t\t\'11\' : 금전신탁자사주\n'
            helpStr += u'\t\t\t\'80\' : 시간외바스켓\n'
            helpStr += u'\t\t\t\'79\' : 시간외대량자기\n'

        elif cmd[0] == 'sell' :
            helpStr  = u'\tsell 종목코드 주문수량 주문단가 주문조건구분코드 주문호가구분코드\n'
            if len(cmd) == 1 : return helpStr
            if cmd[1] != 'more' : return helpStr

            helpStr += u'\t\t종목코드         : string\n'
            helpStr += u'\t\t주문수량         : long\n'
            helpStr += u'\t\t주문조건구분코드 : long \n'
            helpStr += u'\t\t\t 0   : default\n'
            helpStr += u'\t\t\t 1   : IOC\n'
            helpStr += u'\t\t\t 2   : FOK\n'
            helpStr += u'\t\t주문호가구분코드 : string \n'
            helpStr += u'\t\t\t\'01\' : 보통\n'
            helpStr += u'\t\t\t\'02\' : 임의\n'
            helpStr += u'\t\t\t\'03\' : 시장가\n'
            helpStr += u'\t\t\t\'05\' : 조건부지정가\n'
            helpStr += u'\t\t\t\'06\' : 희망대량\n'
            helpStr += u'\t\t\t\'09\' : 자사주\n'
            helpStr += u'\t\t\t\'12\' : 최유리지정가\n'
            helpStr += u'\t\t\t\'13\' : 최우선지정가\n'
            helpStr += u'\t\t\t\'10\' : 스톡옵션자사주\n'
            helpStr += u'\t\t\t\'23\' : 임의시장가\n'
            helpStr += u'\t\t\t\'25\' : 임의조건부지정가\n'
            helpStr += u'\t\t\t\'51\' : 장중대량\n'
            helpStr += u'\t\t\t\'52\' : 장중바스켓\n'
            helpStr += u'\t\t\t\'61\' : 개시전종가\n'
            helpStr += u'\t\t\t\'62\' : 개시전종가대량\n'
            helpStr += u'\t\t\t\'63\' : 개시전시간외바스켓\n'
            helpStr += u'\t\t\t\'67\' : 개시전금전신탁자사주\n'
            helpStr += u'\t\t\t\'69\' : 개시전대량자기\n'
            helpStr += u'\t\t\t\'71\' : 신고대량(전장시가)\n'
            helpStr += u'\t\t\t\'72\' : 시간외대량\n'
            helpStr += u'\t\t\t\'73\' : 신고대량(종가)\n'
            helpStr += u'\t\t\t\'77\' : 금전신탁종가대량\n'
            helpStr += u'\t\t\t\'11\' : 금전신탁자사주\n'
            helpStr += u'\t\t\t\'80\' : 시간외바스켓\n'
            helpStr += u'\t\t\t\'79\' : 시간외대량자기\n'

        elif cmd[0] == 'help' :
            if len(cmd) == 1 :
                helpStr = u'\thelp command [more]\n'
            elif ( len(cmd) == 2 ) or ( len(cmd) == 3 ) :
                helpStr = self.getHelp(cmd[1:])
        elif cmd[0] == 'LTRC' :
            helpStr = u'\tLTRC : Limit Trade-request Remain Count\n'
        elif cmd[0] == 'LNRC' :
            helpStr = u'\tLNRC : Limit Non-trade-request Remain Count\n'
        elif cmd[0] == 'LSRC' :
            helpStr = u'\tLSRC : Limit Subscribe-request Remain Count\n'
        elif cmd[0] == 'LRRT' :
            helpStr = u'\tLRRT : Limit Request Remain Time (sec.)\n'
        elif cmd[0] == 'RM' :
            helpStr = u'\tRM : Real Mode\n'
        elif cmd[0] == 'TWCP' :
            helpStr = u'\tTWCP : Test With Cybos Plus\n'
        elif cmd[0] == 'TOCP' :
            helpStr = u'\tTOCP : Test withOut Cybos Plus\n'
        elif cmd[0] == 'TRQ' :
            helpStr = u'\tTRQ : Trade Request Queue size\n'
        elif cmd[0] == 'NRQ' :
            helpStr = u'\tNRQ : Non-trade Request Queue size\n'
        elif cmd[0] == 'SRQ' :
            helpStr = u'\tSRQ : Subscribe Request Queue size\n'
        elif cmd[0] == 'find' :
            helpStr = u'\tfind keyword\n'
        else :
            helpStr = u'\tunknown command : ' + \
                       ' '.join( unicode(w) for w in cmd ) + '\n'

        return helpStr

    def processRequestQueue(self) :
        if ( self.tradeRequestQueue.qsize() == 0 ) and \
           ( self.nonTradeRequestQueue.qsize() == 0 ) and \
           ( self.subscribeRequestQueue.qsize() == 0 ) :
               return 1

        if self.tradeRequestQueue.qsize() != 0 :
            request = self.tradeRequestQueue.get()

            if   request[0] == 'buy' :
                self.requestBuy( request )
            elif request[0] == 'sell' :
                self.requestSell( request )
            else :
                self.consoleOutput(u'unknown trade request command : %s'%(request[0]))
        # end of tradeRequestQueue

        if self.nonTradeRequestQueue.qsize() != 0 :
            request = self.nonTradeRequestQueue.get()
            if request[0] == 'requestStockMst' :
                self.requestStockMst(request[1])
            else :
                self.consoleOutput(u'this non trade request \'%s\' is not ready yet.'%request[0])
        # end of nonTradeRequestQueue

        if self.subscribeRequestQueue.qsize() != 0 :
            request = self.subscribeRequestQueue.get()
            if request[0] == 'subscribe' :
                if self.subscribeStock(request[1]) == True :
                    self.subscribeList.append(request[1])
            else :
                self.consoleOutput(u'this subscribe request \'%s\' is not ready yet.'%request[0])

        # end of subscribeRequestQueue

        return 0

    def getOneSecondCount(self) :
        return int((1000/(self.loopInterval*1000))-1)

    def getMonitoringMessage(self) :

        optionDic =  { 0 : u'RM', 1 : u'TWCP', 2 : u'TOCP' }

        monitoringMessage =  u'Time   : ' + unicode(time.ctime())

        monitoringMessage += u'\n'
        monitoringMessage += u'Status : ' + \
                             u'LTRC(%d)'%self.cybosIF.getLimitTradeReqRemainCount() + u' ' +\
                             u'LNRC(%d)'%self.cybosIF.getLimitNonTradeReqRemainCount() + u' ' +\
                             u'LSRC(%d)'%self.cybosIF.getLimitSubscribeReqRemainCount() + u' ' +\
                             u'LRRT(%f)'%(self.cybosIF.getLimitRequestRemainTime()/1000) + u' '

        monitoringMessage += u'MODE(%s)'% optionDic[self.option]

        monitoringMessage += u'\n'
        monitoringMessage += u'Queue  : '
        monitoringMessage += u'TRQ(%d)'%self.tradeRequestQueue.qsize() + ' '
        monitoringMessage += u'NRQ(%d)'%self.nonTradeRequestQueue.qsize() + ' '
        monitoringMessage += u'SRQ(%d)'%self.subscribeRequestQueue.qsize() + ' '

        monitoringMessage += u'\n'

        return monitoringMessage

    def loadSubscribeList(self) :
       # self.subscribeList.append('A000660')    # 하이닉스 test mode
       self.subscribeList.append('A005930')    # 삼성전자 test mode

       #for i in range(0,199) :
       #    self.subscribeList.append( self.stockMgr.stockList[i][0] )
       #print len(self.subscribeList)

    def subscribeStockCodes(self) :
        if self.bUseCP() is False :
            string = u'subscribeRequest : '
            for stockCode in self.subscribeList :
                string += stockCode + u' '
            string += u'\n'
            self.consoleOutput(string)
        else :
            for stockCode in self.subscribeList :
                if self.cybosIF.subscribeStockCode(stockCode) == True :
                    self.consoleOutput(u'subscribe : success : \t' + stockCode + u'\n')
                else :
                    self.consoleOutput(u'subscribe : failed : \t' + stockCode + u'\n')

    def unsubscribeStockCodes(self) :
        if self.bUseCP() is False :
            string = u'unsubscribeRequest : '
            for stockCode in self.subscribeList :
                string += stockCode + u' '
            string += u'\n'
            self.consoleOutput(string)
        else :
            print self.subscribeList
            print len(self.subscribeList)
            for stockCode in self.subscribeList :
                if self.cybosIF.unsubscribeStockCode(stockCode) == True :
                    self.consoleOutput(u'unsubscribe : success : \t' + stockCode + u'\n')
                else :
                    self.consoleOutput(u'unsubscribe : failed : \t' + stockCode + u'\n')

    def processResult( self, result ) :
        global subscribeLog

        if result[0] != 0 : return
        if result[4] != 'cxCpStockCur' : return
        logString = result[3] + u'\t'
        dic = result[5][0]
        logString += unicode(dic[0][2]) + u'\t'
        print u'result[5]', len(result[5])
        print u'result[5] is', result[5]
        try :
            dic = result[5][1]                      # IndexError : list index out of range
        except IndexError as e :
            print e
            return
        logString += unicode(dic[1][2]) + u'\t'
        dic = result[5][11]
        logString += unicode(dic[13][2])

        subscribeLog.write(logString)

    def main(self) :
        global subscribeLog

        bFirst = True

        self.subscribeStockCodes()

        while True :
            if self._terminate is True :
                break

            # buy, sell example : ('A005180',1,1,0,'03')
            # 'A000660' 하이닉스

            # parsing consoleInputQueue
            self.parsingConsoleInputQueue()

            # process requestQueues
            self.processRequestQueue()

            win32gui.PumpWaitingMessages()

            for i in range(0, self.reportQueue.qsize()) :
                self.consoleOutput(self.reportQueue.get())

            for i in range(0, self.resultQueue.qsize()) :
                result = self.resultQueue.get()
                self.consoleOutput( self.getResultString(result) )
                self.processResult( result )

            if( self.monitoringWaitCount >= \
                    ( int( self.getOneSecondCount() * self.monitoringWaitSecond ) ) ) :

                self.consoleOutput(self.getMonitoringMessage())
                self.monitoringWaitCount = 0
            else :
                self.monitoringWaitCount += 1

            time.sleep(self.loopInterval)
        # end of while True

        subscribeLog.close()
        self.unsubscribeStockCodes()
        print u'\nexiting cxCybosMain.main'
    # end of cxCybosMain.main()

# end of cxCybosMain


def test_cpMain(option = 0 ) :
    cpMain = cxCybosMain()
    cpMain.init(option)
    cpMain.main()

    if option == 1 :
        print 'reportQueue'
        for i in range(0,cpMain.reportQueue.qsize()) :
            print cpMain.reportQueue.get()

        print 'resultQueue'
        for i in range(0,cpMain.resultQueue.qsize()) :
            cpMain.printResult( cpMain.resultQueue.get() )

    cpMain.deinit()

    del cpMain


def test() :
    #test_cpMain(cxCybosMain.TEST_MODE_WITHOUT_CP)
    test_cpMain(cxCybosMain.TEST_MODE_WITH_CP)


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
