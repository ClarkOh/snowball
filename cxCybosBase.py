################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxCybosBase.py
# date        : 2012-08-10 13:14:01
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import common
from win32com.client import Dispatch, DispatchWithEvents, constants
from cxChannel import cxChannel
from cxError import cxError
from Queue import Queue
import pythoncom
import time
import win32gui

"""
cxCybosBase
    private: DO NOT CALL THESE METHODS FROM OUTSIDE
        __init__
        __del__
    public:

using error code :
    pythoncom.com_error in __init__
"""

class cxCybosBase :
    #com_cp = None

    def __init__(self,com_cp_str):
        self.com_cp = None

        try:
            self.com_cp = Dispatch(com_cp_str)
        except pythoncom.com_error, (hr, msg, exc, arg) :
            raise cxError(hr,'COM',msg,'check whether cybos plus running or not')

    def __del__(self):
        if self.com_cp != None:
            del self.com_cp

"""
cxCybosBaseWithEvent
    private: DO NOT CALL THESE METHODS FROM OUTSIDE
        __init__
        __del__
    public:
        open()
        close()
        on_received
        is_Received
        SetInputValue(type,value)
        Subscribe()
        Unsubscribe()
        Request()
        BlockRequest()
        BlockRequest2(option)
        GetHeaderValue(type)
        GetDataValue(type,index)
        GetDibStatus()
        GetDibMsg1()
        Continue()
        Header()
        Data()

using error code :
    pythoncom.com_error.hr in   __init__,
                                Subscribe(),
                                Unsubscribe(),
                                Request(),
                                BlockRequest(),
                                BlockRequest2(),
                                GetHeaderValue(),
                                GetDataValue(),
                                GetDibStatus(),
                                GetDibMsg1(),
                                Continue(),
                                Header(),
                                Data()

    cxChannel.[1,2], 0xffffffff in open()

    [10] in Subscribe(),
            Unsubscribe(),
            Request(),
            BlockRequest(),
            BlockRequest2(),
            GetHeaderValue(),
            GetDataValue(),
            GetDibStatus(),
            GetDibMsg1(),
            Continue(),
            Header(),
            Data() for com_cp = None

"""

class cxCybosBaseWithEvent :
    com_cp = None
    __b_received = False
    __received_evt_ch = None

    result_ch = None  # it can be stackless channel or Queue.Queue
    report_ch = None  # it can be stackless channel or Queue.Queue

    class cxEvent :
        __ch = None
        def OnReceived(self):
            if self.__ch != None:
                self.__ch.receive('rxed')
        def set_event_channel(self,channel):
            self.__ch = channel
        def reset_event_channel(self):
            if self.__ch != None:
                self.__ch.close()

    def __init__(self,com_cp_str):
        try :
            self.__received_evt_ch = cxChannel()
        except cxError as e :
            raise e
        except :
            raise cxError(0xFFFFFFFF,'general','unknown error','')

        try :
            self.com_cp = DispatchWithEvents(   com_cp_str,\
                                                cxCybosBaseWithEvent.cxEvent )
        except pythoncom.com_error, (hr, msg, exc, arg) :
            raise cxError(hr,'COM',msg,'check whether cybos plus running or not')

    def __del__(self):
        if self.com_cp != None:
            del self.com_cp
        if self.__received_evt_ch != None:
            del self.__received_evt_ch
    
    def open(self, handler):
        if self.__received_evt_ch != None:
            try:
                self.__received_evt_ch.open()
            except cxError as e :
                raise e
            except :
                raise cxError(0xFFFFFFFF,'general','unknown error','')

            self.__received_evt_ch.set_event_handler(handler)
            self.com_cp.set_event_channel(self.__received_evt_ch)
    
    def close(self):
        self.__b_received = False
        if self.com_cp != None :
            self.com_cp.reset_event_channel()
        if self.__received_evt_ch != None :
            self.__received_evt_ch.close()

    def del_result_queue(self) :
        if self.result_ch is not None :
            del self.result_ch
            self.result_ch = None

    def set_result_queue(self, resultQ) :
        self.del_result_queue()
        self.result_ch = resultQ

    def set_result(self, params) :
        if self.result_ch is None :
            print params
            return 0
        if isinstance(self.result_ch, Queue) :
            self.result_ch.put(params)
            return 0
        elif isinstance(self.result_ch, cxChannel) :
            self.result_ch.receive(params)
            return 0
        return 1 

    def del_report_queue(self) :
        if self.report_ch is not None :
            del self.report_ch
            self.report_ch = None

    def set_report_queue(self, reportQ) :
        self.del_report_queue()
        self.report_ch = reportQ

    def report(self, params) :
        if self.report_ch is None :
            print params
            return 0
        if isinstance(self.report_ch, Queue) :
            self.report_ch.put(params)
            return 0
        elif isinstance(self.report_ch, cxChannel) :
            self.report_ch.receive(params)
            return 0
        return 1

    def on_received(self,args):
        self.__b_received = True

    def is_Received(self):
        return self.__b_received

    # Parameter Input Methods...

    def SetInputValue(self,Type,value):
        if self.com_cp != None:
            self.com_cp.SetInputValue(Type,value)

    # Data Requesting Methods...

    def Subscribe(self):
        if self.com_cp != None:
            try:
                self.com_cp.Subscribe()
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"Subscribe\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def Unsubscribe(self):
        self.__b_received = False
        if self.com_cp != None:
            try:
                self.com_cp.Unsubscribe()
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"Unsubscribe\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def Request(self):
        self.__b_received = False
        if self.com_cp != None:
            try:
                return self.com_cp.Request()
            except pythoncom.com_error, (hr, msg, exc, arg) :
                print common.UNI(msg)
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"Request\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def BlockRequest(self):
        if self.com_cp != None:
            try:
                return self.com_cp.BlockRequest()
            except pythoncom.com_error, (hr, msg, exc, arg) :
                #print 'exc', exc
                #print 'exc[2]', exc[2]
                #print 'arg', arg
                raise cxError(hr,'COM',msg,'\"BlockRequest\":%s'%(exc[2]))
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def BlockRequest2(self,option):
        if self.com_cp != None:
            try:
                return self.com_cp.BlockRequest2(option)
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"BlockRequest2\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    # rxed Data Retreiving Methods...

    def GetHeaderValue(self,Type):
        if self.com_cp != None:
            try:
                return self.com_cp.GetHeaderValue(Type)
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"GetHeaderValue\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def GetDataValue(self,Type,index):
        if self.com_cp != None:
            try:
                return self.com_cp.GetDataValue(Type,index)
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"GetDataValue\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    # Status methods...

    def GetDibStatus(self):
        if self.com_cp != None:
            try:
                return self.com_cp.GetDibStatus()
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"GetDibStatus\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def GetDibMsg1(self):
        if self.com_cp != None:
            try:
                return self.com_cp.GetDibMsg1()
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this method \"GetDibMsg1\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')
    
    # Property methods...

    def Continue(self):
        if self.com_cp != None:
            try:
                return self.com_cp.Continue
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this property \"Continue\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def Header(self):
        if self.com_cp != None:
            try:
                return self.com_cp.Header
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and support of this property \"Header\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')

    def Data(self):
        if self.com_cp != None:
            try:
                return self.com_cp.Data
            except pythoncom.com_error, (hr, msg, exc, arg) :
                raise cxError(hr,'COM',msg,'check the connection and suppor tof this property \"Data\"')
        else :
            raise cxError(10,'cxCybosBaseWithEvent','com_cp is None','')


"""
example class
"""

class cxCpStockCur(cxCybosBaseWithEvent) :
    def __init__(self):
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockCur')

    def open(self):
        cxCybosBaseWithEvent.open(self,self.__on_received)

    def __on_received(self,args):
        cxCybosBaseWithEvent.on_received(self,args)
        # TODO : do something from here

        print u'CpStockCur::Received'
        resultList = [
                        [ u'종목코드 : ', self.GetHeaderValue(0) ],
                        [ u'종목명   : ', self.GetHeaderValue(1) ],
                        [ u'시가     : ', unicode(self.GetHeaderValue(4)) ]
                     ]
    
        print resultList

        resultString = u''
        for i in range(0, len(resultList) ) :
            resultString += resultList[i][0] + resultList[i][1] + '\n'
        print resultString
        """
        print u'종목코드',
        print self.GetHeaderValue(0)
        print u'종목명',
        print self.GetHeaderValue(1)
        print u'시가',
        print self.GetHeaderValue(4)
        """

    """
    def Request(self):
        raise cxCybosError('CYBOS','cxCpStockCur is not support Request')

    def BlockRequest(self):
        raise cxCybosError('CYBOS','cxCpStockCur is not support BlockRequest')
    """


class cxCpFutureCode(cxCybosBase):
    def __init__(self):
        cxCybosBase.__init__(self,'cputil.CpFutureCode')
    
    def CodeToName(self,code):
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)
    
    def GetCount(self):
        if self.com_cp != None :
            return self.com_cp.GetCount()

    def GetData(self,Type,index):
        if self.com_cp != None :
            return self.com_cp.GetData(Type,index)

def test_cxCpStockCur():
    print 'test_cxCpStockCur'
    try:
        cpStockCur = cxCpStockCur()
        cpStockCur.open()
        cpStockCur.SetInputValue(0,u'A000660')
        cpStockCur.Subscribe()
    
    
        for i in range(100):
            win32gui.PumpWaitingMessages()
            time.sleep(1)

        dibStatus = cpStockCur.GetDibStatus()

        if dibStatus == 0 :
            print u'정상'
        elif dibStatus == -1 :
            print u'오류'
        elif dibStatus == 1 :
            print u'수신대기'
            print u'\t(Request를 요청하고 아직 Received 이벤트를 받지 않은 상태의 오브젝트로'
            print u'\t 다시 Request/BlockRequest/BlockRequest2를 호출한 경우에 발생)'

        cpStockCur.Unsubscribe()
        cpStockCur.close()

    except cxError as e :
        return

    del cpStockCur


def test_cxCpFutureCode():
    
    cpFutureCode = cxCpFutureCode()
    n = cpFutureCode.GetCount()

    print '개수:%d'%n
    searching_jongmok_code = '101G9'            #ascii
    searching_jongmok_name = 'KOSPI200 1212'    #ascii
    for i in range(n) :
        s1 = cpFutureCode.GetData(0,i)
        s2 = cpFutureCode.GetData(1,i)
        print '종목코드 : ', s1, '종목명 : ', s2
        if s1 == searching_jongmok_code :
            print '찾았다!!'
        if s2 == searching_jongmok_name :
            print '찾았다!!!'
#       print '종목코드:%s, 종목명:%s'% (unicode(s1,'ascii'),unicode(s2,'ascii'))

    print cpFutureCode.CodeToName('10100')

    del cpFutureCode

def test2() :
    cpStockCur = cxCpStockCur()
    cpStockCur.open()
    reportQ = Queue()
    resultQ = Queue()
    cpStockCur.set_report_queue(reportQ)
    cpStockCur.set_result_queue(resultQ)
    print isinstance(reportQ, Queue)
    cpStockCur.report('hello?! cpStockCur')
    print reportQ.get()
    cpStockCur.set_result('result is')
    print resultQ.get()
    cpStockCur.close() 
    del cpStockCur

def test():
    test_cxCpStockCur()
#    test_cxCpFutureCode()
#    test2()

    print 'com reference count :', pythoncom._GetInterfaceCount()


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
