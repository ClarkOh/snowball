################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxCybosPlus.py
# date        : 2012-08-10 13:13:47
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

from cxCybosBase import cxCybosBase, cxCybosBaseWithEvent
from win32com.client import Dispatch, DispatchWithEvents, constants
from cxChannel import cxChannel
import pythoncom
import time
import win32gui


class cxCpCybos :

    #com_cp = None
    #__b_rx_disconnect = False
    #__disconnect_evt_ch = None

    class cxEvent :

        #__ch = None

        def __init__(self) :
            self.__ch = None

        def OnDisconnect(self) :
            if self.__ch != None :
                self.__ch.receive('disconnected')

        def set_event_channel(self, channel) :
            self.__ch = channel

        def reset_event_channel(self) :
            if self.__ch != None :
                self.__ch.close()

    def __init__(self) :
        self.com_cp = None
        self.__b_rx_disconnect = False
        self.__disconnect_evt_ch = cxChannel()
        self.com_cp = DispatchWithEvents('CpUtil.CpCybos',cxCpCybos.cxEvent)

    def __del__(self) :
        if self.com_cp != None :
            del self.com_cp
        if self.__disconnect_evt_ch != None :
            del self.__disconnect_evt_ch

    def open(self) :
        if self.__disconnect_evt_ch != None :
            self.__disconnect_evt_ch.open()
            self.__disconnect_evt_ch.set_event_handler(self.__on_disconnected)
            self.com_cp.set_event_channel(self.__disconnect_evt_ch)

    def close(self) :
        self.__b_rx_disconnect = False
        if self.com_cp != None :
            self.com_cp.reset_event_channel()
        if self.__disconnect_evt_ch != None :
            self.__disconnect_evt_ch.close()

    def __on_disconnected(self, *args) :
        self.__b_rx_disconnect = True
        print 'received disconnect event'

    def isRxDisconnect(self) :
        if self.com_cp != None :
            return self.__b_rx_disconnect
        return False

    def IsConnect(self) :
        if self.com_cp != None :
            return self.com_cp.IsConnect

    def ServerType(self) :
        if self.com_cp != None :
            return self.com_cp.ServerType

    def LimitRequestRemainTime(self) :
        if self.com_cp != None :
            return self.com_cp.LimitRequestRemainTime

    def GetLimitRemainCount(self, limitType) :
        if self.com_cp != None :
            return self.com_cp.GetLimitRemainCount(limitType)


class cxCpStockCode(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpStockCode')

    def CodeToName(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)

    def NameToCode(self, name) :
        if self.com_cp != None :
            return self.com_cp.NameToCode(name)

    def CodeToFullCode(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToFullCode(code)

    def FullCodeToName(self, fullcode) :
        if self.com_cp != None :
            return self.com_cp.FullCodeToName(fullcode)

    def CodeToIndex(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToIndex(code)

    def GetCount(self) :
        if self.com_cp != None :
            return self.com_cp.GetCount()

    def GetData(self, type, index) :
        if self.com_cp != None :
            return self.com_cp.GetData(type, index)

    def GetPriceUnit(self, code, basePrice, directionUp) :
        if self.com_cp != None :
            return self.com_cp.GetPriceUnit(code, basePrice, directionUp)


class cxCpFutureCode(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpFutureCode')

    def CodeToName(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)

    def GetCount(self) :
        if self.com_cp != None :
            return self.com_cp.GetCount()

    def GetData(self, type, index) :
        if self.com_cp != None :
            return self.com_cp.GetData(type, index)


class cxCpOptionCode(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpOptionCode')

    def CodeToName(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)

    def GetCount(self) :
        if self.com_cp != None :
            return self.com_cp.GetCount()

    def GetData(self, type, index) :
        if self.com_cp != None :
            return self.com_cp.GetData(type, index)


class cxCpSOptionCode(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpSOptionCode')

    def CodeToName(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)

    def GetCount(self) :
        if self.com_cp != None :
            return self.com_cp.GetCount()

    def GetData(self, type, index) :
        if self.com_cp != None :
            return self.com_cp.GetData(type, index)


class cxCpKFutureCode(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpKFutureCode')

    def CodeToName(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)

    def GetCount(self) :
        if self.com_cp != None :
            return self.com_cp.GetCount()

    def GetData(self, type, index) :
        if self.com_cp != None :
            return self.com_cp.GetData(type, index)


class cxCpElwCode(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpElwCode')

    def CodeToName(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)

    def GetCount(self) :
        if self.com_cp != None :
            return self.com_cp.GetCount()

    def GetData(self, type, index) :
        if self.com_cp != None :
            return self.com_cp.GetData(type, index)

    def GetStockElwBaseCode(self, ElwCode) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwBaseCode(ElwCode)

    def GetStockElwBaseName(self, ElwCode) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwBaseName(ElwCode)

    def GetStockElwBasketCodeList(self, ElwCode) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwBasketCodeList(ElwCode)

    def GetStockElwBasketCompList(self, ElwCode) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwBasketCompList(ElwCode)

    def GetStockElwLpCodeList(self, ElwCode) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwLpCodeList(ElwCode)

    def GetNameByStockElwLpCode(self, LpCode) :
        if self.com_cp != None :
            return self.com_cp.GetNameByStockElwLpCode(LpCode)

    def GetStockElwBaseList(self) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwBaseList()

    def GetStockElwIssuerList(self) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwIssuerList()

    def GetStockElwCodeListByBaseCode(self, baseCode) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwCodeListByBaseCode(baseCode)

    def GetStockElwCodeListByRightType(self, rightType) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwCodeListByRightType(rightType)


class cxCpCodeMgr(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpCodeMgr')

    def CodeToName(self, code) :
        if self.com_cp != None :
            return self.com_cp.CodeToName(code)

    def GetStockMarginRate(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockMarginRate(code)

    def GetStockMemeMin(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockMemeMin(code)

    def GetStockIndustryCode(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockIndustryCode(code)

    def GetStockMarketKind(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockMarketKind(code)

    def GetStockControlKind(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockControlKind(code)

    def GetStockSupervisionKind(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockSupervisionKind(code)

    def GetStockStatusKind(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockStatusKind(code)

    def GetStockCapital(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockCapital(code)

    def GetStockFiscalMonth(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockFiscalMonth(code)

    def GetStockGroupCode(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockGroupCode(code)

    def GetStockKospi200Kind(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockKospi200Kind(code)

    def GetStockSectionKind(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockSectionKind(code)

    def GetStockLacKind(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockLacKind(code)

    def GetStockListedDate(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockListedDate(code)

    def GetStockMaxPrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockMaxPrice(code)

    def GetStockMinPrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockMinPrice(code)

    def GetStockParPrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockParPrice(code)

    def GetStockStdPrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockStdPrice(code)

    def GetStockYdOpenPrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockYdOpenPrice(code)

    def GetStockYdHighPrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockYdHighPrice(code)

    def GetStockYdLowPrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockYdLowPrice(code)

    def GetStockYdClosePrice(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockYdClosePrice(code)

    def IsStockCreditEnable(self, code) :
        if self.com_cp != None :
            return self.com_cp.IsStockCreditEnable(code)

    def GetStockParPriceChageType(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockParPriceChageType(code)

    def GetStockElwBasketCodeList(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwBasketCodeList(code)

    def GetStockElwBasketCompList(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockElwBasketCompList(code)

    def GetStockListByMarket(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetStockListByMarket(code)

    def GetGroupCodeList(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetGroupCodeList(code)

    def GetGroupName(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetGroupName(code)

    def GetIndustryList(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetIndustryList(code)

    def GetIndustryName(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetIndustryName(code)

    def GetMemberList(self, code) :
        if self.com_cp != None :
            return self.com_cp.GetMemberList(code)

    def GetKosdaqIndustry1List(self) :
        if self.com_cp != None :
            return self.com_cp.GetKosdaqIndustry1List()

    def GetKosdaqIndustry2List(self) :
        if self.com_cp != None :
            return self.com_cp.GetKosdaqIndustry2List()

    def GetMarketStartTime(self) :
        if self.com_cp != None :
            return self.com_cp.GetMarketStartTime()

    def GetMarketEndTime(self) :
        if self.com_cp != None :
            return self.com_cp.GetMarketEndTime()


class cxCpUsCode(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpUsCode')

    def GetUsCodeList(self, usType) :
        if self.com_cp != None :
            return self.com_cp.GetUsCodeList(usType)

    def GetNameByUsCode(self, usCode) :
        if self.com_cp != None :
            return self.com_cp.GetNameByUsCode(usCode)


class cxCpCalcOptGreeks(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpUtil.CpCalcOptGreeks')

    def Calculate(self) :
        if self.com_cp != None :
            self.com_cp.Calculate()

    def CallPutType(self, value) :
        if self.com_cp != None :
            self.com_cp.CallPutType = value

    def Price(self, value) :
        if self.com_cp != None :
            self.com_cp.Price = value

    def UnderPrice(self, value) :
        if self.com_cp != None :
            self.com_cp.UnderPrice = value

    def ExerPrice(self, value) :
        if self.com_cp != None :
            self.com_cp.ExerPrice = value

    def VolatilityType(self, value) :
        if self.com_cp != None :
            self.com_cp.VolatilityType = value

    def Volatility(self, value) :
        if self.com_cp != None :
            self.com_cp.Volatility = value

    def ExpirDays(self, value) :
        if self.com_cp != None :
            self.com_cp.ExpirDays = value

    def RFInterRate(self, value) :
        if self.com_cp != None :
            self.com_cp.RFInterRate = value

    def DividRate(self, value) :
        if self.com_cp != None :
            self.com_cp.DividRate = value

    def TV(self) :
        if self.com_cp != None :
            return self.com_cp.TV

    def Delta(self) :
        if self.com_cp != None :
            return self.com_cp.Delta

    def Gamma(self) :
        if self.com_cp != None :
            return self.com_cp.Gamma

    def Theta(self) :
        if self.com_cp != None :
            return self.com_cp.Theta

    def Vega(self) :
        if self.com_cp != None :
            return self.com_cp.Vega

    def Rho(self) :
        if self.com_cp != None :
            return self.com_cp.Rho

    def IV(self) :
        if self.com_cp != None :
            return self.com_cp.IV


class cxCpStockMst(cxCybosBaseWithEvent) :
    
    headerIndexDic = {
         0 : [u'string',   u'종목코드'                             ] ,
         1 : [u'string',   u'종목명'                               ] ,
         2 : [u'string',   u'대신업종코드'                         ] ,
         3 : [u'string',   u'그룹코드'                             ] ,
         4 : [u'string',   u'시간'                                 ] ,
         5 : [u'string',   u'소속구분'                             ] ,
         6 : [u'string',   u'대형,중형,소형'                       ] ,
         8 : [u'long',     u'상한가'                               ] ,
         9 : [u'long',     u'하한가'                               ] ,
        10 : [u'long',     u'전일종가'                             ] ,
        11 : [u'long',     u'현재가'                               ] ,
        12 : [u'long',     u'전일대비'                             ] ,
        13 : [u'long',     u'시가'                                 ] ,
        14 : [u'long',     u'고가'                                 ] ,
        15 : [u'long',     u'저가'                                 ] ,
        16 : [u'long',     u'매도호가'                             ] ,
        17 : [u'long',     u'매수호가'                             ] ,
        18 : [u'long',     u'누적거래량'                           ] ,
        19 : [u'long',     u'누적거래대금'                         ] ,
        20 : [u'long',     u'EPS'                                  ] ,
        21 : [u'long',     u'신고가'                               ] ,
        22 : [u'long',     u'신고가일'                             ] ,
        23 : [u'long',     u'신저가'                               ] ,
        24 : [u'long',     u'신저가일'                             ] ,
        25 : [u'short',    u'신용시장'                             ] ,
        26 : [u'short',    u'결산월'                               ] ,
        27 : [u'long',     u'기준가'                               ] ,
        28 : [u'float',    u'PER'                                  ] ,
        31 : [u'decimal',  u'상장수식수'                           ] ,
        32 : [u'long',     u'상장자본금'                           ] ,
        33 : [u'long',     u'외국인DATA일자'                     ] ,
        34 : [u'long',     u'외국인TIME일자'                     ] ,
        35 : [u'decimal',  u'외국인상장주식수'                   ] ,
        36 : [u'decimal',  u'외국인주문주식수'                   ] ,
        37 : [u'long',     u'외국인한도수량'                     ] ,
        38 : [u'float',    u'외국인한도비율'                     ] ,
        39 : [u'decimal',  u'외국인주문가능수량'                  ] ,
        40 : [u'float',    u'외국인주문가능비율'                  ] ,
        42 : [u'string',   u'증권전산업종코드'                  ] ,
        43 : [u'short',    u'매매수량단위'                       ] ,
        44 : [u'char',     u'정상/이상급등/관리/거래정지코드'    ] ,
        45 : [u'char',     u'소속구분코드'                       ] ,
        46 : [u'long',     u'전일거래량'                          ] ,
        47 : [u'long',     u'52주최고가'                          ] ,
        48 : [u'long',     u'52주최고일'                          ] ,
        49 : [u'long',     u'52주최저가'                          ] ,
        50 : [u'long',     u'52주최저일'                          ] ,
        52 : [u'string',   u'벤처기업구분'                        ] ,
        53 : [u'string',   u'KOSPI200채용여부'                   ] ,
        54 : [u'short',    u'액면가'                               ] ,
        55 : [u'long',     u'예상체결가'                          ] ,
        56 : [u'long',     u'예상체결가전일대비'                ] ,
        57 : [u'long',     u'예상체결수량'                       ] ,
        58 : [u'char',     u'예상체결가구분flag'                ] ,
        59 : [u'char',     u'장구분flag'                         ] ,
        60 : [u'char',     u'자사주신청여부'                      ] ,
        61 : [u'long',     u'자사주신청수량'                     ] ,
        62 : [u'long',     u'거래원외국계매도총합'                ] ,
        63 : [u'long',     u'거래원외국계매수총합'                ] ,
        64 : [u'long',     u'신용잔고비율'                         ] ,
        65 : [u'char',     u'CB여부'                              ] ,
        66 : [u'char',     u'관리구분'                             ] ,
        67 : [u'char',     u'투자경고구분'                         ] ,
        68 : [u'char',     u'거래정지구분'                         ] ,
        69 : [u'char',     u'불성실공시구분'                      ] ,
        70 : [u'long',     u'BPS'                                  ] 
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockMst')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
            [
                self.GetDibStatus(),
                self.GetDibMsg1(),
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,
                self.get_header_value_list(),
                []
            ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockMst.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpStockMstM(cxCybosBaseWithEvent) :

    headerIndexDic = {}

    dataIndexDic = {
         0 : [u'string', u'종목 코드' ] ,
         1 : [u'string', u'종목명' ] ,
         2 : [u'long', u'대비' ] ,
         3 : [u'short', u'대비 구분 코드' ] ,
         4 : [u'long', u'현재가' ] ,
         5 : [u'long', u'매도호가' ] ,
         6 : [u'long', u'매수호가' ] ,
         7 : [u'unsigned long', u'거래량' ] ,
         8 : [u'char', u'장 구분 플래그' ] ,
         9 : [u'long', u'예상 체결가' ] ,
        10 : [u'long', u'예상 체결가 전일 대비' ] ,
        11 : [u'unsigned long', u'예상 체결 수량' ] 
    }
    
    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockMstM')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_data_value_list(self, countIndex) :
        dataValueList = []
        tmpList = []
        count = self.GetHeaderValue(countIndex)
        for i in range(0, count ) :
            tmpDic = {}
            for key in self.dataIndexDic.keys() :
                tmpDic[key] = self.dataIndexDic[key] + [ self.GetDataValue( key, i ) ]
            dataValueList.append(tmpDic)
        return dataValueList

    def getResult(self) :
        resultList = [
                self.GetDibStatus(),
                self.GetDibMsg1(),
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,
                [],
                self.get_data_value_list(0)
        ]
        return resultList

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockMstM.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpStockMst2(cxCybosBaseWithEvent) :

    headerIndexDic = {}

    dataIndexDic = { 
         0 : [u'string', u'종목 코드' ] ,
         1 : [u'string', u'종목명' ] ,
         2 : [u'long', u'시간(HHMM)' ] ,
         3 : [u'long', u'현재가' ] ,
         4 : [u'long', u'전일대비' ] ,
         5 : [u'char', u'상태구분' ] ,
         6 : [u'long', u'시가' ] ,
         7 : [u'long', u'고가' ] ,
         8 : [u'long', u'저가' ] ,
         9 : [u'long', u'매도호가' ] ,
        10 : [u'long', u'매수호가' ] ,
        11 : [u'unsigned long', u'거래량 [주의] 단위 1주' ] ,
        12 : [u'long', u'거래대금 [주의] 단위 천원' ] ,
        13 : [u'long', u'총매도잔량' ] ,
        14 : [u'long', u'총매수잔량' ] ,
        15 : [u'long', u'매도잔량' ] ,
        16 : [u'long', u'매수잔량' ] ,
        17 : [u'unsigned long', u'상장주식수' ] ,
        18 : [u'long', u'외국인보유비율(%)' ] ,
        19 : [u'long', u'전일종가' ] ,
        20 : [u'unsigned long', u'전일거래량' ] ,
        21 : [u'long', u'체결강도' ] ,
        22 : [u'unsigned long', u'순간체결량' ] ,
        23 : [u'char', u'체결가비교 Flag' ] ,
        24 : [u'char', u'호가비교 Flag' ] ,
        25 : [u'char', u'동시호가구분' ] ,
        26 : [u'long', u'예상체결가' ] ,
        27 : [u'long', u'예상체결가 전일대비' ] ,
        28 : [u'long', u'예상체결가 상태구분' ] ,
        29 : [u'unsigned long', u'예상체결가 거래량' ] 
    } 


    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockMst2')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_data_value_list(self, countIndex) :
        dataValueList = []
        tmpList = []
        count = self.GetHeaderValue(countIndex)
        for i in range(0, count ) :
            tmpDic = {}
            for key in self.dataIndexDic.keys() :
                tmpDic[key] = self.dataIndexDic[key] + [ self.GetDataValue( key, i ) ]
            dataValueList.append(tmpDic)
        return dataValueList

    def getResult(self) :
        resultList = [
                self.GetDibStatus(),
                self.GetDibMsg1(),
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,
                [],
                self.get_data_value_list(0)
        ]
        return resultList

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockMst2.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpStockCur(cxCybosBaseWithEvent) :

    headerIndexDic = {
             0 : [u'string', u'종목 코드' ] ,
             1 : [u'string', u'종목명' ] ,
             2 : [u'long', u'전일대비' ] ,
             3 : [u'long', u'시간' ] ,
             4 : [u'long', u'시가' ] ,
             5 : [u'long', u'고가' ] ,
             6 : [u'long', u'저가' ] ,
             7 : [u'long', u'매도호가' ] ,
             8 : [u'long', u'매수호가' ] ,
             9 : [u'long', u'누적거래량' ] ,
            10 : [u'long', u'누적거래대금' ] ,
            13 : [u'long', u'현재가' ] ,
            14 : [u'char', u'체결 상태' ] ,
            15 : [u'long', u'누적 매도체결수량 (체결가 방식)' ] ,
            16 : [u'long', u'누적매수체결수량 (체결가 방식)' ] ,
            17 : [u'long', u'순간체결수량' ] ,
            18 : [u'long', u'시간 (초)' ] ,
            19 : [u'char', u'예상 체결가 구분 플래그' ] ,
            20 : [u'char', u'장 구분 플래그' ] ,
            21 : [u'long', u'장전시간외 거래량' ] ,
            22 : [u'char', u'대비부호' ] ,
            23 : [u'long', u'LP보유수량' ] ,
            24 : [u'long', u'LP보유수량 대비' ] ,
            25 : [u'float', u'LP보유율' ] ,
            26 : [u'char', u'체결 상태 (호가방식)' ] ,
            27 : [u'long', u'누적 매도체결수량 (호가 방식)' ] ,
            28 : [u'long', u'누적 매수체결수량 (호가 방식)' ] ,
    }
    
    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockCur')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
                [
                        self.GetDibStatus(),
                        self.GetDibMsg1(),
                        self.Continue(),
                        unicode(time.strftime('%Y%m%d%H%M%S')),
                        self.__class__.__name__,
                        self.get_header_value_list(),
                        []
                ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
#        print 'cxCpStockCur.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpStockFrnOrd(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockFrnOrd')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockFrnOrd.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpStockMember1(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockMember1')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockMember1.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpStockMember(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockMember')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockMember.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpStockJpBid2(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockJpBid2')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockJpBid2.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpStockJpBid(cxCybosBaseWithEvent) :

    headerIndexDic = {
         0 : [u'string', u'종목코드' ] ,
         1 : [u'long', u'시간' ] ,
         2 : [u'long', u'거래량' ] ,
         3 : [u'long', u'1차 매도호가' ] ,
         4 : [u'long', u'1차 매수호가' ] ,
         5 : [u'long', u'1차 매도잔량' ] ,
         6 : [u'long', u'1차 매수잔량' ] ,
         7 : [u'long', u'2차 매도호가' ] ,
         8 : [u'long', u'2차 매수호가' ] ,
         9 : [u'long', u'2차 매도잔량' ] ,
        10 : [u'long', u'2차 매수잔량' ] ,
        11 : [u'long', u'3차 매도호가' ] ,
        12 : [u'long', u'3차 매수호가' ] ,
        13 : [u'long', u'3차 매도잔량' ] ,
        14 : [u'long', u'3차 매수잔량' ] ,
        15 : [u'long', u'4차 매도호가' ] ,
        16 : [u'long', u'4차 매수호가' ] ,
        17 : [u'long', u'4차 매도잔량' ] ,
        18 : [u'long', u'4차 매수잔량' ] ,
        19 : [u'long', u'5차 매도호가' ] ,
        20 : [u'long', u'5차 매수호가' ] ,
        21 : [u'long', u'5차 매도잔량' ] ,
        22 : [u'long', u'5차 매수잔량' ] ,
        23 : [u'long', u'총매도잔량' ] ,
        24 : [u'long', u'총매수잔량' ] ,
        25 : [u'long', u'시간외 총매도잔량' ] ,
        26 : [u'long', u'시간외 총매수잔량' ] ,
        27 : [u'long', u'6차 매도호가' ] ,
        28 : [u'long', u'6차 매수호가' ] ,
        29 : [u'long', u'6차 매도잔량' ] ,
        30 : [u'long', u'6차 매수잔량' ] ,
        31 : [u'long', u'7차 매도호가' ] ,
        32 : [u'long', u'7차 매수호가' ] ,
        33 : [u'long', u'7차 매도잔량' ] ,
        34 : [u'long', u'7차 매수잔량' ] ,
        35 : [u'long', u'8차 매도호가' ] ,
        36 : [u'long', u'8차 매수호가' ] ,
        37 : [u'long', u'8차 매도잔량' ] ,
        38 : [u'long', u'8차 매수잔량' ] ,
        39 : [u'long', u'9차 매도호가' ] ,
        40 : [u'long', u'9차 매수호가' ] ,
        41 : [u'long', u'9차 매도잔량' ] ,
        42 : [u'long', u'9차 매수잔량' ] ,
        43 : [u'long', u'10차 매도호가' ] ,
        44 : [u'long', u'10차 매수호가' ] ,
        45 : [u'long', u'10차 매도잔량' ] ,
        46 : [u'long', u'10차 매도잔량' ] ,
        47 : [u'long', u'1차 LP매도잔량' ] ,
        48 : [u'long', u'1차 LP매수잔량' ] ,
        49 : [u'long', u'2차 LP매도잔량' ] ,
        50 : [u'long', u'2차 LP매수잔량' ] ,
        51 : [u'long', u'3차 LP매도잔량' ] ,
        52 : [u'long', u'3차 LP매수잔량' ] ,
        53 : [u'long', u'4차 LP매도잔량' ] ,
        54 : [u'long', u'4차 LP매수잔량' ] ,
        55 : [u'long', u'5차 LP매도잔량' ] ,
        56 : [u'long', u'5차 LP매수잔량' ] ,
        57 : [u'long', u'6차 LP매도잔량' ] ,
        58 : [u'long', u'6차 LP매수잔량' ] ,
        59 : [u'long', u'7차 LP매도잔량' ] ,
        60 : [u'long', u'7차 LP매수잔량' ] ,
        61 : [u'long', u'8차 LP매도잔량' ] ,
        62 : [u'long', u'8차 LP매수잔량' ] ,
        63 : [u'long', u'9차 LP매도잔량' ] ,
        64 : [u'long', u'9차 LP매수잔량' ] ,
        65 : [u'long', u'10차 LP매도잔량' ] ,
        66 : [u'long', u'10차 LP매수잔량' ] ,
        67 : [u'long', u'LP매도잔량 10차 합' ] ,
        68 : [u'long', u'LP매수잔량10차 합' ] ,
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockJpBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
                [
                        self.GetDibStatus(),
                        self.GetDibMsg1(),
                        self.Continue(),
                        unicode(time.strftime('%Y%m%d%H%M%S')),
                        self.__class__.__name__,
                        self.get_header_value_list(),
                        []
                ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
#        print 'cxCpStockJpBid.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpStockBid(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockBid.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpStockWeek(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockWeek')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockWeek.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpStockStu(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockStu')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpStockStu.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCbGraph1(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CbGraph1')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCbGraph1.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockIndexIR(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockIndexIR')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockIndexIR.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockIndexIChart(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockIndexIChart')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockIndexIChart.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockIndexIS(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockIndexIS')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockIndexIS.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockAdR(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockAdR')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockAdR.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockAdS(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockAdS')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockAdS.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockAdKR(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockAdKR')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockAdKR.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockAdKS(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockAdKS')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockAdKS.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockCbChk(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockCbChk')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockCbChk.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockOutMst(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockOutMst')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockOutMst.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockOutCur(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.StockOutCur')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockOutCur.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureMst(cxCybosBaseWithEvent) :

    headerIndexDic = {
        0 : [u'string', u'선물코드'],
        1 : [u'short', u'종목SN'],
        2 : [u'string', u'한글종목명'],
        3 : [u'string', u'영문종목명'],
        4 : [u'string', u'축약종목명'],
        5 : [u'string', u'종목명'],
        6 : [u'long', u'상장일'],
        7 : [u'long', u'상장일수'],
        8 : [u'short', u'잔존일수'],
        9 : [u'long', u'최종거래일(마지막거래일)'],
        10 : [u'char', u'최종거래일여부'],
        11 : [u'float', u'배당액지수미래가치'],
        12 : [u'char', u'기준가격구분'],
        13 : [u'float', u'기준가격'],
        14 : [u'float', u'이론가격(결제가)'],
        15 : [u'float', u'이론가격(기준가)'],
        16 : [u'float', u'CD금리'],
        17 : [u'float', u'상한가'],
        18 : [u'float', u'하한가'],
        19 : [u'char', u'전일정산가격구분'],
        20 : [u'float', u'전일정산가격'],
        21 : [u'char', u'전일종가구분'],
        22 : [u'float', u'전일종가'],
        23 : [u'long', u'전일체결수량'],
        24 : [u'long', u'전일체결대금'],
        25 : [u'long', u'전일미결제약정수량'],
        26 : [u'long', u'상장중최고가일자'],
        27 : [u'float', u'상장중최고가'],
        28 : [u'long', u'상장중최저가일자'],
        29 : [u'float', u'상장중최저가'],
        31 : [u'long', u'입회일자'],
        32 : [u'char', u'시장가허용구분'],
        35 : [u'float', u'최종결제지수'],
        36 : [u'char', u'최종결제지수구분'],
        37 : [u'float', u'매도 1 우선호가'],
        38 : [u'float', u'매도 2 우선호가'],
        39 : [u'float', u'매도 3 우선호가'],
        40 : [u'float', u'매도 4 우선호가'],
        41 : [u'float', u'매도 5 우선호가'],
        42 : [u'long', u'매도 1 우선호가수량'],
        43 : [u'long', u'매도 2 우선호가수량'],
        44 : [u'long', u'매도 3 우선호가수량'],
        45 : [u'long', u'매도 4 우선호가수량'],
        46 : [u'long', u'매도 5 우선호가수량'],
        47 : [u'long', u'매도총호가수량'],
        48 : [u'short', u'매도 1 우선호가건수'],
        49 : [u'short', u'매도 2 우선호가건수'],
        50 : [u'short', u'매도 3 우선호가건수'],
        51 : [u'short', u'매도 4 우선호가건수'],
        52 : [u'short', u'매도 5 우선호가건수'],
        53 : [u'long', u'매도 총 호가건수'],
        54 : [u'float', u'매수 1 우선호가'],
        55 : [u'float', u'매수 2 우선호가'],
        56 : [u'float', u'매수 3 우선호가'],
        57 : [u'float', u'매수 4 우선호가'],
        58 : [u'float', u'매수 5 우선호가'],
        59 : [u'long', u'매수 1 우선호가수량'],
        60 : [u'long', u'매수 2 우선호가수량'],
        61 : [u'long', u'매수 3 우선호가수량'],
        62 : [u'long', u'매수 4 우선호가수량'],
        63 : [u'long', u'매수 5 우선호가수량'],
        64 : [u'long', u'매수총호가수량'],
        65 : [u'short', u'매수 1 우선호가건수'],
        66 : [u'short', u'매수 2 우선호가건수'],
        67 : [u'short', u'매수 3 우선호가건수'],
        68 : [u'short', u'매수 4 우선호가건수'],
        69 : [u'short', u'매수 5 우선호가건수'],
        70 : [u'long', u'매수 총 호가건수'],
        71 : [u'float', u'현재가'],
        72 : [u'float', u'시가'],
        73 : [u'float', u'고가'],
        74 : [u'float', u'저가'],
        75 : [u'long', u'누적체결수량'],
        76 : [u'long', u'누적거래대금(백만원단위)'],
        77 : [u'long', u'전일대비'],
        78 : [u'long', u'순간체결수량'],
        79 : [u'float', u'금일정산가격'],
        80 : [u'long', u'미결제약정수량'],
        82 : [u'long', u'체결시각'],
        83 : [u'long', u'처리시각'],
        86 : [u'char', u'금일정산가격구분'],
        87 : [u'string', u'미결제약정구분'],
        88 : [u'float', u'이론선물지수'],
        89 : [u'float', u'KOSPI 200 지수'],
        90 : [u'float', u'basis'],
        91 : [u'float', u'kospi 200 전일대비'],
        100 : [u'char', u'조건부 지정가 허용구분'],
        101 : [u'char', u'최유리 지정가 허용구분'],
        102 : [u'long', u'C.B 적용 상한가'],
        103 : [u'long', u'C.B 적용 하한가'],
        104 : [u'long', u'전일 최종매매체결 시각'],
        107 : [u'long', u'전일미결제약정'],
        108 : [u'long', u'근월물 의제약정가격'],
        109 : [u'long', u'원월물 의제약정가격'],
        110 : [u'string', u'스프레드 근월물 표준코드'],
        111 : [u'string', u'스프레드 원월물 표준코드'],
        112 : [u'string', u'기초자산코드'],
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureMst')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
                [
                        self.GetDibStatus(),
                        self.GetDibMsg1(),
                        self.Continue(),
                        unicode(time.strftime('%Y%m%d%H%M%S')),
                        self.__class__.__name__,
                        self.get_header_value_list(),
                        []
                ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureMst.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureWide(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureWide')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureWide.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureCurr(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureCurr')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureCurr.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureCurOnly(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureCurOnly')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureCurOnly.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureMo1(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureMo1')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureMo1.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureK200(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureK200')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureK200.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureBid1(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureBid1')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureBid1.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureWeek1(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureWeek1')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureWeek1.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutOptRest(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutOptRest')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutOptRest.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureFtu(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureFtu')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureFtu.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureGr1(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureGr1')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureGr1.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureIndexH(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureIndexH')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureIndexH.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureIndexI(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureIndexI')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureIndexI.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureOptionStat(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureOptionStat')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureOptionStat.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutureOptionStatPb(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.FutureOptionStatPb')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutureOptionStatPb.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionMst(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionMst')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionMst.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionCur(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionCur')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionCur.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionMo(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionMo')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionMo.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionBid(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionBid.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionWeek(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionWeek')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionWeek.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionFtu(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionFtu')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionFtu.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionGr1(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionGr1')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionGr1.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionGen(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionGen')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionGen.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionGreek(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionGreek')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionGreek.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionCallPut(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionCallPut')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionCallPut.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionAtm(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionAtm')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionAtm.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionInfo(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionInfo')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionInfo.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionTv(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.OptionTv')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionTv.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxSOptionMst(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.SOptionMst')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxSOptionMst.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxSOptionCur(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.SOptionCur')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxSOptionCur.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxSOptionBid(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.SOptionBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxSOptionBid.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxSOptionWeek(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.SOptionWeek')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxSOptionWeek.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxSOptionCallPut(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.SOptionCallPut')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxSOptionCallPut.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpConclusion(cxCybosBaseWithEvent) :
    
    headerIndexDic = {
         1 : [u'string',   u'계좌명'               ] ,
         2 : [u'string',   u'종목명'               ] ,
         3 : [u'long',     u'체결수량'             ] ,
         4 : [u'long',     u'체결가격'             ] ,
         5 : [u'long',     u'주문번호'             ] ,
         6 : [u'long',     u'원주문번호'           ] ,
         7 : [u'string',   u'계좌번호'             ] ,
         8 : [u'string',   u'상품관리구분코드'     ] ,
         9 : [u'string',   u'종목코드'             ] ,
        12 : [u'string',   u'매매구분코드'         ] ,
        14 : [u'string',   u'체결구분코드'         ] ,
        15 : [u'string',   u'신용대출구분코드'     ] ,
        16 : [u'string',   u'정정취소구분코드'     ] ,
        17 : [u'string',   u'현금신용대용구분코드' ] ,
        18 : [u'string',   u'주문호가구분코드'     ] ,
        19 : [u'string',   u'주문조건구분코드'     ] ,
        20 : [u'long',     u'대출일'               ] ,
        21 : [u'long',     u'장부가'               ] ,
        22 : [u'long',     u'매도가능수량'         ] ,
        23 : [u'long',     u'체결기준잔고수량'     ] 
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpConclusion')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
                [
                        self.GetDibStatus(),
                        self.GetDibMsg1(),
                        self.Continue(),
                        unicode(time.strftime('%Y%m%d%H%M%S')),
                        self.__class__.__name__,
                        self.get_header_value_list(),
                        []
                ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpConclusion.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())



class cxCpFConclusion(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpFConclusion')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpFConclusion.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxExpectIndexR(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.ExpectIndexR')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxExpectIndexR.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxExpectIndexS(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.ExpectIndexS')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxExpectIndexS.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7223(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr7223')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7223.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7225(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr7225')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7225.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7818(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr7818')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7818.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7818C(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr7818C')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7818C.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7819(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr7819')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7819.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7819C(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr7819C')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7819C.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8081(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8081')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8081.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8082(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8082')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8082.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8083(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8083')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8083.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8091(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8091')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8091.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8091S(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8091S')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8091S.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8092S(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8092S')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8092S.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8111(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8111')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8111.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8111S(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8111S')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8111S.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8111KS(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8111KS')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8111KS.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxPgaTime8112(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.PgaTime8112')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxPgaTime8112.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8116(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8116')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8116.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8300(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8300')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8300.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpFore8311(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpFore8311')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpFore8311.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpFore8312(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpFore8312')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpFore8312.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8561(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8561')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8561.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8561T(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8561T')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8561T.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8562(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8562')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8562.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8563(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'Dscbo1.CpSvr8563')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8563.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockAdj(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockAdj')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockAdj.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockUniMst(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockUniMst')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockUniMst.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockUniCur(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockUniCur')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockUniCur.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockUniWeek(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockUniWeek')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockUniWeek.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockUniJpBid(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockUniJpBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockUniJpBid.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockUniBid(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockUniBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockUniBid.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockChart(cxCybosBaseWithEvent) :

    headerIndexDic = {
        0 : [u'string', u'종목코드' ] ,
        1 : [u'short', u'필드개수' ] ,
        2 : [u'string array', u'필드명의 배열' ],
        3 : [u'long', u'수신개수' ],
        4 : [u'ushort', u'마지막봉틱수' ] ,
        5 : [u'ulong', u'최근거래일 (YYYYMMDD)' ],
        6 : [u'ulong or float', u'전일종가' ] ,
        7 : [u'ulong or float', u'현재가' ],
        8 : [u'char', u'대비부호' ] ,
        9 : [u'long or float', u'대비' ],
        10 : [u'ulong or ulonglong', u'거래량' ],
        11 : [u'ulong or float', u'매도호가' ],
        12 : [u'ulong or float', u'매수호가'],
        13 : [u'ulong or float', u'시가'],
        14 : [u'ulong or float', u'고가'],
        15 : [u'ulong or float', u'저가'],
        16 : [u'ulonglong', u'거래대금'],
        17 : [u'char', u'종목상태'],
        18 : [u'ulonglong', u'상장주식수'],
        19 : [u'ulong', u'자본금 (백만원)'],
        20 : [u'ulong or ulonglong', u'전일거래량'],
        21 : [u'ulong', u'최근갱신시간 (hhmm)'],
        22 : [u'ulong or float', u'상한가'],
        23 : [u'ulong or float', u'하한가']
    }

    dataIndexDic = {
        0: [u'ulong', u'날짜'],
        1: [u'long', u'시간 (hhmm)'],
        2: [u'long or float', u'시가'],
        3: [u'long or float', u'고가'],
        4: [u'long or float', u'저가'],
        5: [u'long or float', u'종가'],
        6: [u'long or float', u'전일대비'],
        8: [u'ulong or ulonglong', u'거래량 (만원 단위)' ],
        9: [u'ulonglong', u'거래대금'],
        10: [u'ulong or ulonglong', u'누적체결매도수량'],
        11: [u'ulong or ulonglong', u'누적체결매수수량'],
        12: [u'ulonglong', u'상장주식수'],
        13: [u'ulonglong', u'시가총액'],
        14: [u'ulong', u'외국인주문한도수량'],
        15: [u'ulong', u'외국인주문가능수량'],
        16: [u'ulong', u'외국인현보유수량'],
        17: [u'float', u'외국인현보유비율'],
        18: [u'ulong', u'수정주가일자 (YYYYMMDD)'],
        19: [u'float', u'수정주가비율'],
        20: [u'long', u'기관순매수'],
        21: [u'long', u'기관누적순매수'],
        22: [u'long', u'등락주선'],
        23: [u'float', u'등락비율'],
        24: [u'ulonglong', u'예탁금'],
        25: [u'float', u'주식회전율'],
        26: [u'float', u'거래성립률'],
        37: [u'char', u'대비부호']
    }

    fieldNameDic = {
        u'날짜' : 0,
        u'시간' : 1,
        u'시가' : 2,
        u'고가' : 3,
        u'저가' : 4,
        u'종가' : 5,
        u'전일대비' : 6,
        u'거래량' : 8,
        u'거래대금' : 9,
        u'누적체결매도수량' : 10,
        u'누적체결매수수량' : 11,
        u'상장주식수' : 12,
        u'시가총액' : 13,
        u'외국인주문한도수량' : 14,
        u'외국인주문가능수량' : 15,
        u'외국인현보유수량' : 16,
        u'외국인현보유비율' : 17,
        u'수정주가일자' : 18,
        u'수정주가비율' : 19,
        u'기관순매수량' : 20,
        u'기관누적순매수량' : 21,
        u'등락주선' : 22,
        u'등락비율' : 23,
        u'예탁금' :  24,
        u'주식회전율' : 25,
        u'거래성립률' : 26,
        u'대비부호' : 37,
    }

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockChart')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def get_data_value_list(self, countIndex) :
        dataValueList = []
        tmpList = []
        count = self.GetHeaderValue(countIndex)
        #print 'count', count
        fieldNum = self.GetHeaderValue(1)
        #print 'fieldNum', fieldNum
        fieldNameList = self.GetHeaderValue(2)
        #print 'fieldNameList', fieldNameList, len(fieldNameList)
        for i in range(0, count ) :
            tmpDic = {}
            for Type in range( 0, fieldNum ) :
                key = self.fieldNameDic[fieldNameList[Type]]
                #print Type,
                #print self.GetDataValue(Type,i)
                tmpDic[key] = self.dataIndexDic[key] + [ self.GetDataValue(Type, i ) ]
            dataValueList.append(tmpDic)
        """
        for i in range(0, count ) :
            tmpDic = {}
            for fieldName in fieldNameList : 
                print fieldName,
                key = self.fieldNameDic[fieldName]
                print key,
                print self.GetDataValue(key,i)
                #tmpDic[key] = self.dataIndexDic[key] + [ self.GetDataValue( key, i ) ]
            dataValueList.append(tmpDic)
        """
        return dataValueList

    def getResult(self) :
        result = \
            [       
                self.GetDibStatus(),                # status
                self.GetDibMsg1(),                  # order result
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,            
                self.get_header_value_list(),
                self.get_data_value_list(3)
            ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockChart.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpMarketWatch(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpMarketWatch')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpMarketWatch.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpMarketWatchS(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpMarketWatchS')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpMarketWatchS.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxFutOptChart(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.FutOptChart')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxFutOptChart.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxOptionCurOnly(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.OptionCurOnly')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxOptionCurOnly.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpFutOptTheoVal(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpFutOptTheoVal')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpFutOptTheoVal.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxElw(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.Elw')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxElw.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxElwAll(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.ElwAll')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxElwAll.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxElwJpBid2(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.ElwJpBid2')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxElwJpBid2.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxElwJpBid(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.ElwJpBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxElwJpBid.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxElwInvest(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.ElwInvest')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxElwInvest.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxElwUnderCur(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.ElwUnderCur')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxElwUnderCur.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7726(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7726')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7726.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7748(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7748')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7748.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCmeMst(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CmeMst')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCmeMst.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCmeBid(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CmeBid')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCmeBid.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCmeDaily(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CmeDaily')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCmeDaily.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCmeCurr(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CmeCurr')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCmeCurr.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCmeBidOnly(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CmeBidOnly')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCmeBidOnly.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCmeCurOnly(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CmeCurOnly')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCmeCurOnly.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCmeMo(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CmeMo')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCmeMo.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxK200Expect(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.K200Expect')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxK200Expect.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxMarketEye(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.MarketEye')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxMarketEye.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxWorldCur(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.WorldCur')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxWorldCur.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr3744(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr3744')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr3744.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7037(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7037')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7037.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7043(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7043')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7043.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7043(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7043')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7043.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7063(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7063')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7063.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7066(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7066')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7066.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7068(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7068')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7068.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7212(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7212')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7212.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7215A(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7215A')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7215A.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7215B(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7215B')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7215B.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7216(cxCybosBaseWithEvent) :

    headerIndexDic = {
         0 : [u'string', u'종목코드' ] ,
         1 : [u'short', u'카운트' ] ,
         2 : [u'long', u'조회일자' ] ,
    }

    dataIndexDic = {
         0 : [u'long', u'일자' ] ,
         1 : [u'long', u'종가' ] ,
         2 : [u'char', u'전일대비 flag' ] ,
         3 : [u'long', u'전일대비' ] ,
         4 : [u'float', u'전일대비율' ] ,
         5 : [u'long', u'거래량' ] ,
         6 : [u'long', u'기관매매' ] ,
         7 : [u'long', u'기관매매 누적' ] ,
         8 : [u'long', u'외국인 순매매' ] ,
         9 : [u'float', u'외국인 지분율' ] ,
    }

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7216')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def get_data_value_list(self, countIndex) :
        dataValueList = []
        tmpList = []
        count = self.GetHeaderValue(countIndex)
        for i in range(0, count ) :
            tmpDic = {}
            for key in self.dataIndexDic.keys() :
                tmpDic[key] = self.dataIndexDic[key] + [ self.GetDataValue( key, i ) ]
            dataValueList.append(tmpDic)
        return dataValueList

    def getResult(self) :
        result = \
            [       
                self.GetDibStatus(),                # status
                self.GetDibMsg1(),                  # order result
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,            
                self.get_header_value_list(),
                self.get_data_value_list(1)
            ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7216.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpSvrNew7221(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7221')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7221.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7221S(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7221S')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7221S.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7222(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7222')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7222.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvrNew7224(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvrNew7224')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvrNew7224.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7254(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7254')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7254.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8114(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr8114')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8114.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr8548(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr8548')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr8548.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr9842(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr9842')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr9842.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr9842S(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr9842S')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr9842S.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpSvr7326(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.CpSvr7326')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpSvr7326.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxStockOpenSb(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpSysDib.StockOpenSb')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxStockOpenSb.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTdUtil(cxCybosBase) :

    def __init__(self) :
        cxCybosBase.__init__(self,'CpTrade.CpTdUtil')

    def AccountNumber(self) :
        if self.com_cp != None :
            return self.com_cp.AccountNumber

    def GoodsList(self, AccountNumber, nFilter) :
        if self.com_cp != None :
            return self.com_cp.GoodsList(AccountNumber, nFilter)

    def TradeInit(self) :
        if self.com_cp != None :
            return self.com_cp.TradeInit(0)


class cxCpTd0311(cxCybosBaseWithEvent) :

    headerIndexDic = {
         0 : [ u'string',  u'주문종류코드'     ] ,
         1 : [ u'string',  u'계좌번호'         ] ,
         2 : [ u'string',  u'상품관리구분코드' ] ,
         3 : [ u'string',  u'종목코드'         ] ,
         4 : [ u'long',    u'주문수량'         ] ,
         5 : [ u'long',    u'주문단가'         ] ,
         8 : [ u'long',    u'주문번호'         ] ,
         9 : [ u'string',  u'계좌명'           ] ,
        10 : [ u'string',  u'종목명'           ] ,
        12 : [ u'string',  u'주문조건구분코드' ] ,
        13 : [ u'string',  u'주문호가구분코드' ] 
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0311')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
            [       
                self.GetDibStatus(),                # status
                self.GetDibMsg1(),                  # order result
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,            # means 'cxCpTd0311',
                self.get_header_value_list(),
                []
            ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0311.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())
        


class cxCpTd0312(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0312')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0312.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0313(cxCybosBaseWithEvent) :

    headerIndexDic = {
         1 : [ u'long',    u'원주문번호'       ] ,
         2 : [ u'string',  u'계좌번호'         ] ,
         3 : [ u'string',  u'상품관리구분코드' ] ,
         4 : [ u'string',  u'종목코드'         ] ,
         5 : [ u'string',  u'주문수량'         ] ,
         6 : [ u'long',    u'주문단가'         ] ,
         7 : [ u'long',    u'주문번호'         ] ,
         8 : [ u'string',  u'계좌명'           ] ,
         9 : [ u'string',  u'종목명'           ] ,
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0313')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
            [       
                self.GetDibStatus(),                # status
                self.GetDibMsg1(),                  # order result
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,            # means 'cxCpTd0313'
                self.get_header_value_list(),
                []
            ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0313.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpTd0314(cxCybosBaseWithEvent) :

    headerIndexDic = {
         1 : [ u'long',    u'원주문번호'       ] ,
         2 : [ u'string',  u'계좌번호'         ] ,
         3 : [ u'string',  u'상품관리구분코드' ] ,
         4 : [ u'string',  u'종목코드'         ] ,
         5 : [ u'string',  u'취소수량'         ] ,
         6 : [ u'long',    u'주문번호'         ] ,
         7 : [ u'string',  u'계좌명'           ] ,
         8 : [ u'string',  u'종목명'           ] ,
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0314')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        result = \
            [       
                self.GetDibStatus(),                # status
                self.GetDibMsg1(),                  # order result
                self.Continue(),
                unicode(time.strftime('%Y%m%d%H%M%S')),
                self.__class__.__name__,            # means 'cxCpTd0314'
                self.get_header_value_list(),
                []
            ]
        return result

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0314.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())



class cxCpTd0315(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0315')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0315.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0316(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0316')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0316.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0317(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0317')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0317.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0303(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0303')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0303.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0306(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0306')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0306.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0354(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0354')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0354.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0732(cxCybosBaseWithEvent) :

    headerIndexDic = {
         0 : [u'string',   u'계좌번호'                 ] ,
         1 : [u'string',   u'상품관리구분코드'         ] ,
         2 : [u'string',   u'계좌명'                   ] ,
         3 : [u'longlong', u'예수금'                   ] ,
         4 : [u'long',     u'미수금'                   ] ,
         5 : [u'long',     u'전일장내현금 매도'        ] ,
         6 : [u'long',     u'전일장내현금 매수'        ] ,
         7 : [u'long',     u'전일신용융자 매도'        ] ,
         8 : [u'long',     u'전일신용융자 매수'        ] ,
         9 : [u'long',     u'전일신용대주 매도'        ] ,
        10 : [u'long',     u'전일신용대주 매수'        ] ,
        11 : [u'long',     u'전일현금수수료'           ] ,
        12 : [u'long',     u'전일현금제세금'           ] ,
        13 : [u'long',     u'전일현금정산금'           ] ,
        14 : [u'long',     u'전일장외단주 매도'        ] ,
        15 : [u'long',     u'전일장외단주 매수'        ] ,
        16 : [u'long',     u'전일장외수수료'           ] ,
        17 : [u'long',     u'전일장외제세금'           ] ,
        18 : [u'long',     u'전일장외정산금'           ] ,
        19 : [u'long',     u'전일합계매도금'           ] ,
        20 : [u'long',     u'전일합계매수금'           ] ,
        21 : [u'long',     u'전일합계수수료'           ] ,
        22 : [u'long',     u'전일합계제세금'           ] ,
        23 : [u'long',     u'전일합계정산금'           ] ,
        24 : [u'long',     u'전일장내현금 신규융자'    ] ,
        25 : [u'long',     u'전일신용융자 융자상환'    ] ,
        26 : [u'long',     u'전일장내현금 신규대주'    ] ,
        27 : [u'long',     u'전일신용융자 대주상환'    ] ,
        28 : [u'long',     u'전일장내현금 신용상환'    ] ,
        29 : [u'long',     u'전일상환융자이자'         ] ,
        30 : [u'long',     u'전일상황이용료'           ] ,
        31 : [u'long',     u'전일현금거래세'           ] ,
        32 : [u'long',     u'전일대주소득세'           ] ,
        33 : [u'long',     u'전일대주주민세'           ] ,
        34 : [u'long',     u'금일장내현금 매도'        ] ,
        35 : [u'long',     u'금일장내현금 매수'        ] ,
        36 : [u'long',     u'금일신용융자 매도'        ] ,
        37 : [u'long',     u'금일신용융자 매수'        ] ,
        38 : [u'long',     u'금일신용대주 매도'        ] ,
        39 : [u'long',     u'금일신용대주 매수'        ] ,
        40 : [u'long',     u'금일현금수수료'           ] ,
        41 : [u'long',     u'금일현금제세금'           ] ,
        42 : [u'long',     u'금일현금정산금'           ] ,
        43 : [u'long',     u'금일장외단주 매도'        ] ,
        44 : [u'long',     u'금일장외단주 매수'        ] ,
        45 : [u'long',     u'금일장외수수료'           ] ,
        46 : [u'long',     u'금일장외제세금'           ] ,
        47 : [u'long',     u'금일장외정산금'           ] ,
        48 : [u'long',     u'금일합계매도금'           ] ,
        49 : [u'long',     u'금일합계매수금'           ] ,
        50 : [u'long',     u'금일합계수수료'           ] ,
        51 : [u'long',     u'금일합계제세금'           ] ,
        52 : [u'long',     u'금일합계정산금'           ] ,
        53 : [u'long',     u'금일장내현금 신규융자'    ] ,
        54 : [u'long',     u'금일신용융자 융자상환'    ] ,
        55 : [u'long',     u'금일장내현금 신규대주'    ] ,
        56 : [u'long',     u'금일신용융자 대주상환'    ] ,
        57 : [u'long',     u'금일장내현금 신용상환'    ] ,
        58 : [u'long',     u'금일상환융자이자'         ] ,
        59 : [u'long',     u'금일상황이용료'           ] ,
        60 : [u'long',     u'금일현금거래세'           ] ,
        61 : [u'long',     u'금일대주소득세'           ] ,
        62 : [u'long',     u'금일대주주민세'           ] ,
        63 : [u'long',     u'익일영업일'               ] ,
        64 : [u'longlong', u'익영업일예수금'           ] ,
        65 : [u'long',     u'결제일'                   ] ,
        66 : [u'longlong', u'결제일예수금'             ] 
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0732')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        resultList = [
            self.GetDibStatus(),
            self.GetDibMsg1(),
            self.Continue(),
            unicode(time.strftime('%Y%m%d%H%M%S')),
            self.__class__.__name__,
            self.get_header_value_list(),
            []
        ]
        return resultList

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0732.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpTd3811(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd3811')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd3811.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTdNew5331A(cxCybosBaseWithEvent) :

    headerIndexDic = {
         0 : [u'string',   u'종목코드'                 ] ,
         1 : [u'string',   u'종목명'                   ] ,
         2 : [u'char',     u'증거금율구분코드'         ] ,
         3 : [u'longlong', u'증거금20%주문가능금액'    ] ,
         4 : [u'longlong', u'증거금30%주문가능금액'    ] ,
         5 : [u'longlong', u'증거금40%주문가능금액'    ] ,
         6 : [u'longlong', u'증거금50%주문가능금액'    ] ,
         7 : [u'longlong', u'증거금60%주문가능금액'    ] ,
         8 : [u'longlong', u'증거금70%주문가능금액'    ] ,
         9 : [u'longlong', u'증거금100%주문가능금액'   ] ,
        10 : [u'longlong', u'현금주문가능금액'         ] ,
        11 : [u'long',     u'증거금20%주문가능수량'    ] ,
        12 : [u'long',     u'증거금30%주문가능수량'    ] ,
        13 : [u'long',     u'증거금40%주문가능수량'    ] ,
        14 : [u'long',     u'증거금50%주문가능수량'    ] ,
        15 : [u'long',     u'증거금60%주문가능수량'    ] ,
        16 : [u'long',     u'증거금70%주문가능수량'    ] ,
        17 : [u'long',     u'증거금100%주문가능수량'   ] ,
        18 : [u'long',     u'현금주문가능수량'         ] ,
        19 : [u'longlong', u'증거금20%융자주문가능금액'] ,
        20 : [u'longlong', u'증거금30%융자주문가능금액'] ,
        21 : [u'longlong', u'증거금40%융자주문가능금액'] ,
        22 : [u'longlong', u'증거금50%융자주문가능금액'] ,
        23 : [u'longlong', u'증거금60%융자주문가능금액'] ,
        24 : [u'longlong', u'증거금70%융자주문가능금액'] ,
        25 : [u'longlong', u'융자주문가능금액'         ] ,
        26 : [u'long',     u'증거금20%융자주문가능수량'] ,
        27 : [u'long',     u'증거금30%융자주문가능수량'] ,
        28 : [u'long',     u'증거금40%융자주문가능수량'] ,
        29 : [u'long',     u'증거금50%융자주문가능수량'] ,
        30 : [u'long',     u'증거금60%융자주문가능수량'] ,
        31 : [u'long',     u'증거금70%융자주문가능수량'] ,
        32 : [u'long',     u'융자주문가능수량'         ] ,
        33 : [u'long',     u'대주가능수량'             ] ,
        34 : [u'long',     u'매도가능수량'             ] ,
        35 : [u'longlong', u'매입80%가능금액'          ] ,
        36 : [u'long',     u'매입80%가능수량'          ] ,
        37 : [u'longlong', u'매입100%가능금액'         ] ,
        38 : [u'long',     u'매입100%가능수량'         ] ,
        39 : [u'longlong', u'매입110%가능금액'         ] ,
        40 : [u'long',     u'매입110%가능수량'         ] ,
        41 : [u'longlong', u'매입120%가능금액'         ] ,
        42 : [u'long',     u'매입120%가능수량'         ] ,
        43 : [u'longlong', u'매입140%가능금액'         ] ,
        44 : [u'long',     u'매입140%가능수량'         ] ,
        45 : [u'longlong', u'예수금'                   ] ,
        46 : [u'longlong', u'대용금'                   ] ,
        47 : [u'longlong', u'가능예수금'               ] ,
        48 : [u'longlong', u'가능대용금'               ] ,
        49 : [u'longlong', u'신용상환차익금액'         ] ,
        50 : [u'longlong', u'신용담보현금금액'         ] ,
        51 : [u'longlong', u'미결제환원금'             ] ,
        52 : [u'longlong', u'결제환원금'               ] ,
        53 : [u'longlong', u'대주가능금액'             ] ,
        54 : [u'char',     u'주식적용증거금구분코드'   ] ,
                # '1' : 현행증거금
                # '2' : 증거금100%
                # '3' : 대용40%
                # '4' : 증거금 20%
                # '5' : 증거금 30%
                # '6' : 강제증거금 100%
        55 : [u'string',   u'주식정용증거금구분내용'   ] 
    }

    dataIndexDic = {}

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTdNew5331A')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def getResult(self) :
        resultList = [
            self.GetDibStatus(),
            self.GetDibMsg1(),
            self.Continue(),
            unicode(time.strftime('%Y%m%d%H%M%S')),
            self.__class__.__name__,
            self.get_header_value_list(),
            []
        ]
        return resultList

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTdNew5331A.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpTdNew5331B(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTdNew5331B')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTdNew5331B.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd5339(cxCybosBaseWithEvent) :

    headerIndexDic = {
        0 : [u'string',   u'계좌번호'         ] ,
        1 : [u'string',   u'상품관리구분코드' ] ,
        4 : [u'string',   u'계좌명'           ] ,
        5 : [u'long',     u'수신개수'         ] 
    }

    dataIndexDic = { 
         0 : [u'string',   u'상품관리구분코드'     ] ,
         1 : [u'long',     u'주문번호'             ] ,
         2 : [u'long',     u'원주문번호'           ] ,
         3 : [u'string',   u'종목코드'             ] ,
         4 : [u'string',   u'종목명'               ] ,
         5 : [u'string',   u'주문구분내용'         ] ,
         6 : [u'long',     u'주문수량'             ] ,
         7 : [u'long',     u'주문단가'             ] ,
         8 : [u'long',     u'체결수량'             ] ,
         9 : [u'string',   u'신용구분'             ] ,
        10 : [u'string',   u'계좌번호'             ] ,
        11 : [u'long',     u'정정취소가능수량'     ] ,
        13 : [u'string',   u'매매구분코드'         ] ,
        17 : [u'string',   u'대출일'               ] ,
        18 : [u'string',   u'주문입력매체코드'     ] ,
        19 : [u'string',   u'주문호가구분코드내용' ] ,
        21 : [u'string',   u'주문호가구분코드'     ] ,
        22 : [u'string',   u'주문구분코드'         ] ,
        23 : [u'string',   u'주문구분내용'         ] ,
        24 : [u'string',   u'현금신용대용구분코드' ] ,
        25 : [u'string',   u'주문종가구분코드'     ] ,
        26 : [u'string',   u'주문입력매체코드내용' ] ,
        27 : [u'long',     u'정정주문수량'         ] ,
        28 : [u'long',     u'취소주문수량'         ] 
    }

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd5339')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def get_data_value_list(self, countIndex) :
        dataValueList = []
        tmpList = []
        count = self.GetHeaderValue(countIndex)
        for i in range(0, count ) :
            tmpDic = {}
            for key in self.dataIndexDic.keys() :
                tmpDic[key] = self.dataIndexDic[key] + [ self.GetDataValue( key, i ) ]
            dataValueList.append(tmpDic)
        return dataValueList

    def getResult(self) :
        resultList = [
            self.GetDibStatus(),
            self.GetDibMsg1(),
            self.Continue(),
            unicode(time.strftime('%Y%m%d%H%M%S')),
            self.__class__.__name__,
            self.get_header_value_list(),
            self.get_data_value_list(5)
        ]
        return resultList

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd5339.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpTd5341(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd5341')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd5341.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd5342(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd5342')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd5342.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6033(cxCybosBaseWithEvent) :

    headerIndexDic = {
         0 : [u'string',   u'계좌명'           ] ,
         1 : [u'long',     u'결제 잔고수량'    ] ,
         2 : [u'long',     u'체결 잔고 수량'   ] ,
         3 : [u'longlong', u'평가금액(단위:원)'] ,
         4 : [u'longlong', u'평가손익(단위:원)'] ,
         6 : [u'longlong', u'대출금액(단위:원)'] ,
         7 : [u'long',     u'수신개수'         ] ,
         8 : [u'double',   u'수익율'           ] ,
         9 : [u'longlong', u'D+2 예상 예수금'  ] ,
        10 : [u'longlong', u'대주평가금액'     ] ,
        11 : [u'longlong', u'잔고평가금액'     ] ,
        12 : [u'longlong', u'대주금액'         ] ,
    }

    dataIndexDic = {
         0 : [u'string',   u'종목명'                               ] ,
         1 : [u'char',     u'신용구분'                             ] ,
         2 : [u'string',   u'대출일'                               ] ,
         3 : [u'long',     u'결제 잔고수량'                        ] ,
         4 : [u'long',     u'결제 장부단가'                        ] ,
         5 : [u'long',     u'전일체결수량'                         ] ,
         6 : [u'long',     u'금일체결수량'                         ] ,
         7 : [u'long',     u'체결잔고수량'                         ] ,
         9 : [u'longlong', u'평가금액(단위:원) - 천원 미만은 내림' ] ,
        10 : [u'longlong', u'평가손익(단위:원) - 천원 미만은 내림' ] ,
        11 : [u'double',   u'수익률'                               ] ,
        12 : [u'string',   u'종목코드'                             ] ,
        13 : [u'char',     u'주문구분'                             ] ,
        15 : [u'long',     u'매도가능수량'                         ] ,
        16 : [u'string',   u'만기일'                               ] ,
        17 : [u'double',   u'체결장부단가'                         ] ,
        18 : [u'longlong', u'손익단가'                             ] 
    } 

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6033')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def get_header_value_list(self) :
        valueList = []
        if self.headerIndexDic == None or \
            len(self.headerIndexDic) == 0 : return []

        dic = self.headerIndexDic
        tmpDic = {}
        for key in dic.keys() :
            tmpDic[key] = dic[key] + [ self.GetHeaderValue(key) ]
        valueList.append(tmpDic)
        return valueList

    def get_data_value_list(self, countIndex) :
        dataValueList = []
        tmpList = []
        count = self.GetHeaderValue(countIndex)
        for i in range(0, count ) :
            tmpDic = {}
            for key in self.dataIndexDic.keys() :
                tmpDic[key] = self.dataIndexDic[key] + [ self.GetDataValue( key, i ) ]
            dataValueList.append(tmpDic)
        return dataValueList

    def getResult(self) :
        resultList = [
            self.GetDibStatus(),
            self.GetDibMsg1(),
            self.Continue(),
            unicode(time.strftime('%Y%m%d%H%M%S')),
            self.__class__.__name__,
            self.get_header_value_list(),
            self.get_data_value_list(7)
        ]
        return resultList

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6033.__on_received'
        # TODO : DO SOMETHING FROM HERE
        if self.result_ch is not None :
            self.set_result(self.getResult())


class cxCpTd0322(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0322')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0322.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0323(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0323')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0323.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0326(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0326')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0326.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0355(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0355')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0355.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0356(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0356')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0356.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0359(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0359')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0359.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0386(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0386')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0386.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0387(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0387')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0387.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0388(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0388')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0388.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0389(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0389')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0389.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTdNew9061(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTdNew9061')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTdNew9061.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTdNew9064(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTdNew9064')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTdNew9064.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd9065(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd9065')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd9065.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6831(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6831')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6831.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6832(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6832')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6832.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6833(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6833')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6833.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6841(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6841')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6841.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6842(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6842')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6842.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6843(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6843')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6843.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0721F(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0721F')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0721F.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd0723(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd0723')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd0723.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd5371(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd5371')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd5371.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd5372(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd5372')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd5372.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6197(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6197')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6197.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd6722(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd6722')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd6722.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd9081(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd9081')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd9081.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd9082(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd9082')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd9082.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd9083(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd9083')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd9083.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd9084(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd9084')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd9084.__on_received'
        # TODO : DO SOMETHING FROM HERE


class cxCpTd9085(cxCybosBaseWithEvent) :

    def __init__(self) :
        cxCybosBaseWithEvent.__init__(self,'CpTrade.CpTd9085')

    def open(self) :
        cxCybosBaseWithEvent.open(self, self.__on_received)

    def __on_received(self, args) :
        cxCybosBaseWithEvent.on_received(self, args)
        print 'cxCpTd9085.__on_received'
        # TODO : DO SOMETHING FROM HERE

def test() :
    import sys
    getCybosPlusClassDic(sys.stdout)

def getCybosPlusClassDic( errLog = None ) :
    import sys
    import inspect
    from cxError import UNI 

    classList = [ ( className, classObj ) \
                  for className, classObj \
                  in inspect.getmembers(sys.modules[__name__], inspect.isclass) \
                  if (className != 'cxCybosBase') and \
                     (className != 'cxCybosBaseWithEvent') and \
                     (className != 'cxChannel') ]

    classDic = {}

    for className, classObj in classList :
        try : classDic[className] = classObj()
        except TypeError as e :
            if errLog != None : 
                print 'e.message', e.message
                errLog.write(u'%s : %s'%(className, UNI(e.message)))
                continue
        except : 
            continue

    return classDic
    
#global variable of cybos plus class dictionary.
#DO NOT getCybosPlusClassDic function again. use & reference this variable.
gCybosPlusClassDic = getCybosPlusClassDic()

def test3() :
    cpTd0311 = cxCpTd0311()
    print name 
    del cpTd0311

def test2() :
    cpTd6033 = cxCpTd6033()
    
    cpTd6033.SetInputValue(0,10)
    cpTd6033.BlockRequest()
    print cpTd6033.Header.Count


    del cpTd6033
    """
    cpStockCode = cxCpStockCode()
    jongmok_name = cpStockCode.CodeToName('A000660')
    print '종목명:', jongmok_name
#   print '종목명:%s'%jongmok_name
#   print unicode(jongmok_name)         #OK
#   print unicode('하이닉스')           #Failed
#   if unicode(jongmok_name,'ascii') == u'SK하이닉스' :
#    if jongmok_name == 'SK하이닉스' :
#       print '찾았다'
#   if unicode(jongmok_name) == unicode('하이닉스'):
#       print '찾았다'
    del cpStockCode
#   pass
    """


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
