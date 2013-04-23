################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxTurtleTrading.py
# date        : 2012-11-06 17:19:02
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import common
from cxStockDayData import cxStockDayData
from cxFile         import cxFile
from math           import fabs
from cxLists        import cxList

def calculate_N( dataList, N_condition ):

    n_List = []
    dataListLen = len(dataList)
    for dataIndex in range(0,dataListLen) :
        maxPrice, minPrice, closingPrice = dataList[dataIndex]
        if dataIndex >= 1 :
            prevMaxPrice, prevMinPrice, prevClosingPrice = dataList[dataIndex-1]
            n = max( [ fabs( maxPrice - minPrice ),
                       fabs( maxPrice - prevClosingPrice ),
                       fabs( prevClosingPrice - minPrice ) ] )
            n_List.append(n)

        if dataIndex >= N_condition :
            N = float(sum(n_List)/float(N_condition))

    return N


def remove_not_trading_stocks(dataList) :
    
    stockNum = len(dataList)

    deleteIndexList = []

    for stockData in dataList :
        date, maxPrice, minPrice, closingPrice, tradingVolumn, tradingCost = \
                stockData[1][-1]
        if tradingVolumn == 0 : # 10 이하인거 빼버릴까? 쩝...
            print 'remove %s'%(stockData[0])
            dataList.remove(stockData)


def test_remove_not_trading_stocks() :
    stockDayData = cxStockDayData()
    dataList = stockDayData.loadLogDataFromFile()
    remove_not_trading_stocks(dataList)
    del stockDayData.data[0:-1]
    stockDayData.data = dataList
    stockDayData.saveLogDataToFile(fileName = u'cxStockDayDataRemovedNotTradingStock.dat')
    del dataList
    del stockDayData

def save_data_of_turtle_trading_per_stock() :

    S1_entryCondition = 20
    S1_exitCondition = 10
    S2_entryCondition = 55
    S2_exitCondition = 20
    N_condition = 20

    stockDayData = cxStockDayData()

    print 'start : load stockDayData'
    rawDataList = stockDayData.loadLogDataFromFile(fileName = \
                                    u'cxStockDayDataRemovedNotTradingStock.dat')
    print 'end : load stockDayData'

    if rawDataList == None :
        print 'loading stockDayData : failed'
        return None

    #remove_not_trading_stocks(rawDataList)

    turtleDataPerStockFile = cxFile(u'turtleDataPerStockFile.txt')
    
    stockNum = len(rawDataList)

    #stockNum = 1

    for stockIndex in range(0,stockNum) :
        turtleDataPerStockFile.write(u'%s\n'%rawDataList[stockIndex][0])
        
        dayDataList = rawDataList[stockIndex][1]
        dayDataLen = len(dayDataList)

        for dayIndex in range(0, dayDataLen) :
            ( currentDate, currentMaxPrice, currentMinPrice, 
              currentClosingPrice, currentTradingVolumn, currentTradingCost ) = \
              dayDataList[dayIndex]

            S1_entryPrice = 0
            S1_exitPrice = 0
            S2_entryPrice = 0
            S2_exitPrice = 0
            n = 0               # 오늘의 변동성
            N = 0.0

            if dayIndex >= 1 :
                ( prevDate, prevMaxPrice, prevMinPrice, prevClosingPrice,
                    prevTradingVolumn, prevTradingCost ) = dayDataList[dayIndex-1]

                n = max( [ fabs( currentMaxPrice - currentMinPrice ),
                           fabs( currentMaxPrice - prevClosingPrice ),
                           fabs( prevClosingPrice - currentMinPrice ) ] )

            if dayIndex >= S1_entryCondition :
                S1_entryPrice = \
                    max( [ maxPrice 
                            for date, maxPrice, minPrice, closingPrice,
                                tradingVolumn, tradingCost 
                            in  dayDataList[(dayIndex-S1_entryCondition):dayIndex] ] )

            if dayIndex >= S1_exitCondition :
                S1_exitPrice = \
                    min( [ minPrice 
                            for date, maxPrice, minPrice, closingPrice,
                                tradingVolumn, tradingCost
                            in  dayDataList[(dayIndex-S1_exitCondition):dayIndex] ] )

            if dayIndex >= S2_entryCondition :
                S2_entryPrice = \
                    max( [ maxPrice
                            for date, maxPrice, minPrice, closingPrice,
                                tradingVolumn, tradingCost
                            in  dayDataList[(dayIndex-S2_entryCondition):dayIndex] ] )
            
            if dayIndex >= S2_exitCondition :
                S2_exitPrice = \
                    min( [ minPrice
                            for date, maxPrice, minPrice, closingPrice,
                                tradingVolumn, tradingCost
                            in  dayDataList[(dayIndex-S2_exitCondition):dayIndex] ] )

            if dayIndex >= ( N_condition + 1 ) :

                N = calculate_N( [ [ maxPrice, minPrice, closingPrice ]
                                   for date, maxPrice, minPrice, closingPrice,
                                       tradingVolumn, tradingCost
                                   #in  dayDataList[(dayIndex-N_condition-1):dayIndex] ] , 
                                   in  dayDataList[(dayIndex-N_condition):dayIndex+1] ] , 
                                 N_condition )

            turtleDataPerStockFile.write(u'\t%d %d %d %d %d %d %d %d %d %f\n' \
                    % ( currentDate, currentMaxPrice, currentMinPrice, currentClosingPrice,
                        S1_entryPrice, S1_exitPrice, S2_entryPrice, S2_exitPrice, n, N ) )
   
    del rawDataList
    turtleDataPerStockFile.close()



def test_turtle_trading_per_stock(fileName = u'turtleDataPerStockFile.txt') :
   
    initTotalAsset = 5000000
    totalAsset = initTotalAsset

    stockCode = u''
    bFirst = True

    wishList = cxList()
    purchasedList = cxList()
    goodsList = cxList()
    transactionList = cxList()

    resultFile = cxFile()

    for line in open(fileName) :
        strDataList = line.split()
        if len(strDataList) == 1 :
            if stockCode != strDataList[0] :
                if bFirst == True :
                    stockCode = strDataList[0]
                    bFirst = False
                else :
                    # calculating result of turtle trading for stockCode
                    # clean or reset the data for turtle trading
                    if purchasedList.has(stockCode) :
                        sellingList = purchasedList.getListOf(stockCode)
                        totalPurchasedNum = 0
                        totalPurchasedPrice = 0
                        for code, num, price, n_entryPrice, n_exitPrice in sellingList :
                            totalPurchasedNum += num
                        totalPurchasedPrice = totalPurchasedNum * closingPrice
                        totalAsset += totalPurchasedPrice
                        purchasedList.delete(stockCode,1)
                        resultFile.write( u'\t%s %s %s %d %d\n'% \
                                          ('now','total',stockCode,totalPurchasedPrice,totalAsset))
                    wishList.delete(stockCode)
                    goodsList.delete(stockCode)
                    stockCode = strDataList[0]
                    totalAsset = initTotalAsset

        else :  
            #print 'purchasedList len', purchasedList.len() 
            #for item in purchasedList.dataList :
            #    resultFile.write(u'%s %d %d %f %f\n'%(item[0],item[1],item[2],item[3],item[4]))
            # process turtle trading
            ( date, maxPrice, minPrice, closingPrice, S1_entryPrice, S1_exitPrice,
              S2_entryPrice, S2_exitPrice, n, N ) = strDataList
            maxPrice = int(maxPrice)
            minPrice = int(minPrice)
            closingPrice = int(closingPrice)
            S1_entryPrice = int(S1_entryPrice)
            S1_exitPrice = int(S1_exitPrice)
            S2_entryPrice = int(S2_entryPrice)
            S2_exitPrice = int(S2_exitPrice)
            n = int(n)
            N = float(N)

            #print stockCode,
            #print date,maxPrice,minPrice,closingPrice,
            #print S1_entryPrice,S1_exitPrice,S2_entryPrice,S2_exitPrice,n,N
            
            if wishList.has(stockCode) :
                entryPrice = wishList.getListOf(stockCode)[0][-2]
                condition = wishList.getListOf(stockCode)[0][-1]
                # calculate max trading cost
                maxTradingCost = 100000 #int(totalAsset * 0.02)
                # calculate unit for max risk cost
                unit = int(maxTradingCost * 0.02)
                # calculate stock num to buy.
                if N == 0 :
                    wishList.delete(stockCode,1)
                    continue
                stockNum = int(unit/N)
                # calculate transaction cost.
                #purchasedPrice = maxPrice
                purchasedPrice = closingPrice
                transactionCost = stockNum * purchasedPrice
                if transactionCost > maxTradingCost :
                    stockNum = int(maxTradingCost/purchasedPrice)
                    transactionCost = stockNum * purchasedPrice
                # add transaction info. to transaction list
                transactionList.add( [ 'buy', stockCode, stockNum, purchasedPrice,
                                        purchasedPrice + N,
                                        purchasedPrice - 2*N ] )
                purchasedList.add( [ stockCode, stockNum, purchasedPrice,
                                     purchasedPrice + N,
                                     purchasedPrice - 2*N ] )

                #wishList.pop(stockCode)
                wishList.delete(stockCode,1)
                totalAsset -= transactionCost

                resultFile.write( u'\t%s %s %s %d %s %dx%d=%d, %d, %d, %d\n'% \
                                    (date,'buy ', condition, entryPrice, stockCode,stockNum,purchasedPrice,
                                     transactionCost,unit,maxTradingCost,totalAsset) )
            # end of if wishList.has(stockCode)

            if goodsList.has(stockCode) :
                exitPrice = goodsList.getListOf(stockCode)[0][-2]
                condition = goodsList.getListOf(stockCode)[0][-1]
                # get stock list from purhcased list
                stockList = purchasedList.getListOf( stockCode )
                # get total stock num from stock list
                totalPurchasedNum = 0
                totalPurchasedPrice = 0
                for code, num, price, n_entryPrice, n_exitPrice in stockList :
                    totalPurchasedNum += num
                    totalPurchasedPrice += num * price
                # calculated total earning price by selling
                #sellPrice = minPrice
                sellPrice = closingPrice
                earningPrice = sellPrice * totalPurchasedNum
                # add transaction info. to transaction list
                transactionList.add( [ 'sell', stockCode, totalPurchasedNum, sellPrice ] )
                                          
                # delete stock in purchased list
                purchasedList.delete(stockCode,1)
                goodsList.delete(stockCode,1)
                totalAsset += earningPrice
                resultFile.write( u'\t%s %s %s %d %s %dx%d=%d, %d, %d\n'% \
                                    (date,'sell',condition,exitPrice,
                                     stockCode,totalPurchasedNum,sellPrice,
                                     earningPrice,earningPrice-totalPurchasedPrice,
                                     totalAsset) )
            # end of if goodsList.has(stockCode)

            if closingPrice > S1_entryPrice :
                wishList.add( [ stockCode, closingPrice, S1_entryPrice, 'S1_entry' ] )
            # end of if closingPrice > S1_entryPrice
            if closingPrice > S2_entryPrice :
                wishList.add( [ stockCode, closingPrice, S2_entryPrice, 'S2_entry' ] )
            # end of if closingPrice > S2_entryPrice


            if purchasedList.has( stockCode ) :
                stockDataList = purchasedList.getListOf( stockCode )
                #print purchasedList.has(stockCode)
                #print stockDataList[0]
                ( purchasedStockCode, purchasedStockNum, purchasedStockPrice,   \
                  purchasedN_entryPrice, purchasedN_exitPrice ) = stockDataList[-1]
                if closingPrice > purchasedN_entryPrice :
                    wishList.add( [ stockCode, closingPrice, purchasedN_entryPrice, 'N_entry' ] )
                if closingPrice < S1_exitPrice :
                    goodsList.add( [ stockCode, closingPrice, S1_exitPrice, 'S1_exit' ] )
                if closingPrice < S2_exitPrice :
                    goodsList.add( [ stockCode, closingPrice, S2_exitPrice, 'S2_exit' ] )
                if closingPrice < purchasedN_exitPrice  :
                    goodsList.add( [ stockCode, closingPrice, purchasedN_exitPrice, 'N_exit' ] )
            # end of if purchasedList.has(stockCode)

    # end of for statement

    resultFile.close()


def test_calculate_N() :
    testList = [ [ 2, 1, 1 ],
                 [ 4, 2, 3 ],
                 [ 7, 3, 5 ] ]

    print calculate_N(testList,2)

def test() :
#    test_calculate_N()
#    test_remove_not_trading_stocks()
#    save_data_of_turtle_trading_per_stock()
    test_turtle_trading_per_stock()

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
