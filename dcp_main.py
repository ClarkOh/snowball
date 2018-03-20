
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
import win32com.client
import ctypes

form_class = uic.loadUiType("dcp_main_window.ui")[0]

# common objects
g_CodeMgr = win32com.client.Dispatch('CpUtil.CpCodeMgr')
g_CpStatus = win32com.client.Dispatch('CpUtil.CpCybos')
g_CpTrade = win32com.client.Dispatch('CpTrade.CpTdUtil')

def dcp_init_plus_check(trade_opt) :
    
    if ctypes.windll.shell32.IsUserAnAdmin():
        print('정상: 관리자 권한으로 실행된 프로세스입니다')
    else:
        print('오류: 일반권한으로 실행됨. 관리자 권한으로 실행해 주세요.')
        return 1

    if(g_CpStatus.IsConnect == 0):
        print('PLUS가 정상적으로 연결되어 있지 않습니다.')
        return 2

    if(trade_opt == 0):
        return 0

    if(g_CpTrade.TradeInit(0) != 0):
        print('주문 초기화 실패')
        return 3

    return 0

# cp6033 : 주식 잔고 조회
class cxCp6033:
    def __init__(self, acc, accFlag):
        self.objReq = win32com.client.Dispatch('CpTrade.CpTd6033')
        self.objReq.SetInputValue(0, acc)
        self.objReq.SetInputValue(1, accFlag[0])
        self.objReq.SetInputValue(2, 50)    # 요청 건수 (최대 50)

    def request(self, result_codes):
        self.objReq.BlockRequest()

        reqStatus = self.objReq.GetDibStatus()
        reqRet = self.objReq.GetDibMsg1()
        print('6033:통신상태', '[', reqStatus, ']', '[', reqRet, ']')
        if reqStatus :
            return 0

        cnt = self.objReq.GetHeaderValue(7)

        if(cnt == 0): return

        print('종목코드 종목명 신용구분 체결잔고수량 체결장부단가 평가금액 평가손익')
        for i in range(cnt):
            code = self.objReq.GetDataValue(12, i)      #종목코드
            name = self.objReq.GetDataValue(0, i)       #종목명
            cashFlag = self.objReq.GetDataValue(1, i)   #신용구분
            date = self.objReq.GetDataValue(2, i)       #대출일
            amount = self.objReq.GetDataValue(7, i)     #체결잔고수량
            buyPrice = self.objReq.GetDataValue(17, i)  #체결장부단가
            evalValue = self.objReq.GetDataValue(9, i)  #평가금액
            evalPerc = self.objReq.GetDataValue(11, i)  #평가손익

            data = [code, name, cashFlag, date, amount, buyPrice, evalValue, evalPerc]
            result_codes.append(data)
            print(data)

    def get(self, result_code_list):
        self.request(result_code_list)

        while self.objReq.Continue:
            self.request(result_code_list)

class cxDcpMainWindow(QDialog, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        if dcp_init_plus_check(1) :
            exit()

        self.account = g_CpTrade.AccountNumber[0]
        self.accFlag = g_CpTrade.GoodsList(self.account, 1)
        #print('계좌번호:', self.account, '상품구분번호:', self.accFlag)
        
        #self.init_UI()

        self.label.setText('계좌번호: %s 상품구분번호: %s'%(self.account, self.accFlag))
        self.btnZango.clicked.connect(self.btnZango_clicked)
        self.btnGetStockAll.clicked.connect(self.btnGetStockAll_clicked)
        self.btnExit.clicked.connect(self.btnExit_clicked)

    def btnZango_clicked(self):
        data_list = []
        cp6033 = cxCp6033(self.account, self.accFlag)
        cp6033.get(data_list)
        del cp6033
        del data_list

    def btnGetStockAll_clicked(self):
        KOSPI_codeList = g_CodeMgr.GetStockListByMarket(1)
        KOSDAQ_codeList = g_CodeMgr.GetStockListByMarket(2)

        print('순서, 종목코드, 구분코드, 종목명, 가격')
        for i, code in enumerate(KOSPI_codeList):
            code2 = g_CodeMgr.GetStockSectionKind(code)
            name = g_CodeMgr.CodeToName(code)
            stdPrice = g_CodeMgr.GetStockStdPrice(code)
            print(i, code, code2, name, stdPrice)

    def btnExit_clicked(self):
        exit()
        return

if __name__ == '__main__' :
    app = QApplication(sys.argv)
    dcp_main_window = cxDcpMainWindow()
    dcp_main_window.show()
    sys.exit(app.exec_())
