################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : commonTemplate.py
# date        : 2012-10-11 17:57:20
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

import locale
import codecs

sys.stdout = codecs.getwriter(locale.getpreferredencoding())(sys.stdout)
sys.stderr = codecs.getwriter(locale.getpreferredencoding())(sys.stderr)

"""
[unicode|None]  UNI                             ( text )
void            findCodecName                   ( text )
dateTimeString  getToday                        ( void )
resultString    getHeaderResultStringPortrait   ( headerList, titleOption )
resultString    getHeaderResultStringLandscape  ( headerList, titleOption )
resultString    getDataResultStringPortrait     ( dataList, titleOption )
resultString    getDataResultStringLandscape    ( dataList, titleOption )
resultString    getResultStringPortrait         ( resultList, 
                                                  statusOption, 
                                                  headerValue,
                                                  dataValue,
                                                  titleOption )
resultString    getResultStringLandscape        ( resultList,
                                                  statusOption,
                                                  headerValue,
                                                  dataValue,
                                                  titleOption )
void            dumpResult                      ( resultList )
titleString     getTitleString                  ( titleDic )
valueString     getValueString                  ( resultList )
[0|-1|-2]       templateSetInputValue           ( obj, paramList, errLog )
resultList      templateBlockRequest            ( obj, paramList, resultFile, errLog )
[True|False]    templateRequest                 ( obj, paramList, errLog )
"""
"""
[unicode or None] UNI( contents )
    convert the contents which is written by codec 'cp949' or 'euc-kr' to 'unicode'
    if errors, will return None
"""
def UNI( text ) :
    if text is None : return None
    if isinstance(text, str) :
        result = u''
        
        #import win32console
        #print 'stdout.encoding',sys.stdout.encoding
        #print 'stderr.encoding',sys.stderr.encoding
        #print 'Console.encoding', win32console.GetConsoleCP()
        #print 'ConsoleOutput.encoding', win32console.GetConsoleOutputCP()
        
        #try : result = unicode(text, sys.stderr.encoding).encode('utf8')
        #try : result = unicode(text, sys.stderr.encoding).encode('utf8')
        #try : result = unicode(text, 'euc-kr').encode('utf8')
        #try : result = unicode(text, 'mbcs').encode('cp949')
        #try : result = unicode(text, 'cp949').encode('utf8')

        try : result = text.decode('utf-8')
        except BaseException as e :
            try : result = text.decode(sys.stdout.encoding)
            except BaseException as e :
                return None
        except :
            print 'UNKNOWN ERROR OCCURED', sys.exc_info()[0], sys.exc_info()[1]
            return None

        #print 'UNI.result', unicode(result)

        """
        try :
            result = unicode(text, 'cp949').encode('utf8')
        except UnicodeError as e :       #UnicodeEncodeError
            print e
            try : result = unicode(text, 'euc-kr').encode('utf8')
            except UnicodeError as e :   #UnicodeEncodeError
                print e
                try : result = unicode(text, 'mbcs').encode('utf8')
                except UnicodeError :
                    return None
        """
        return unicode(result)
    else : return unicode(text)

class cxReturnValue :
    def __init__(self, argValue=None, argResult=u'ok', argFunc=u'') :
        if argFunc == u'' :
            import inspect
            self.func_name = UNI(inspect.stack()[1][3])
        else :
            self.func_name = argFunc
        self.value = argValue
        self.result = argResult
    def dump(self) :
        #TODO : if self.value is list, add dump code for list.
        return '['+self.func_name+u' '+self.value+' '+self.result+']'
    def getList(self) :
        return [ self.func_name, self.value, self.result ]

def __function_name__() :
    #sys._getframe().f_code.co_name
    import inspect
    return UNI(inspect.stack()[1][3])

def dumpDict( argDict, tabCount=0 ) :
    if argDict == None or len(argDict) == 0 :
        return u''
    string = u'  '*tabCount + u'{' + u'\n'
    for key in argDict.keys() :
        if isinstance(argDict[key],list) == True :
            string += dumpList(argDict[key], tabCount+1)
        elif isinstance(argDict[key],dict) == True :
            string += dumpDict(argDict[key], tabCount+1)
        else :
            string += u'  '*(tabCount+1) + UNI(argDict[key]) + u'\n'
    string += '  '*tabCount + u'}' + u'\n'
    return string
def dumpList( argList, tabCount=0 ) :
    if argList == None or len(argList) == 0 :
        return u''
    string = u'  '*tabCount + u'[' + u'\n'
    for item in argList :
        if isinstance(item, list) == True :
            string += dumpList( item, tabCount+1 )
        elif isinstance(item, dict) == True :
            string += dumpDict( item, tabCount+1 )
        elif item is None :
            string += u'  '*(tabCount+1) + u'None' + u'\n'
        else :
            string += u'  '*(tabCount+1) + UNI(item) + u'\n'
    string += u'  '*tabCount + u']' + u'\n'
    return string
def findCodecName( text, 
                   displayEncodingCodecName = sys.stdout.encoding,
                   encodingErrorFlag = 0 ) :
    from sets import Set
    from encodings.aliases import aliases
    
    print text

    encodingCodecSet = Set()
    for encodingName in aliases.items() :
        encodingCodecSet.add(encodingName[1].replace('_','-'))

    """ 
    # [DUMP ENCODING CODEC]
    for encodingCodec in encodingCodecSet :
        if encodingCodec == 'cp949' : print 'FOUND'
        print encodingCodec,
    """
    
    if len(encodingCodecSet.intersection([displayEncodingCodecName])) == 0 :
        print 'invalid displayEncodingCodecName : %s'%(displayEncodingCodecName)
        return
    

    for encodingCodec in encodingCodecSet :

        try :
            encodedStr = text.decode(encodingCodec).encode(displayEncodingCodecName)
        
#        except UnicodeEncodeError as e :
#            if encodingErrorFlag == 1 :
#                print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":',e
#            continue
#        except UnicodeDecodeError as e :
#            if encodingErrorFlag == 1 :
#                print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":',e
#            continue
#        except ValueError as e :
#            if encodingErrorFlag == 1 :
#                print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":',e
#            continue
#        except TypeError as e :
#            if encodingErrorFlag == 1 :
#                print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":',e
#            continue
#        except IOError as e :
#            if encodingErrorFlag == 1 :
#                print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":',e
#            continue
#        except LookupError as e :
#            if encodingErrorFlag == 1 :
#                print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":',e
#            continue
        except BaseException as e :
            if encodingErrorFlag == 1 :
                print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":', e
            continue

        print '"',encodingCodec,'"','->','"',sys.stdout.encoding,'":', encodedStr
def getToday() :
    import time
    dateTimeStr = unicode(time.strftime('%Y%m%d'))
    return dateTimeStr

def getOneDayPlus(dateInt) :
    import datetime
    dateYear = dateInt/10000
    dateInt -= dateYear*10000
    dateMonth = dateInt/100
    dateDay = dateInt - (dateMonth*100)
    add_a_day = datetime.date(dateYear,dateMonth,dateDay) + datetime.timedelta(days=1)
    return int(add_a_day.strftime('%Y%m%d'))
    
def getHeaderResultStringPortrait( headerList , titleOption = 0 ) :

    resultString = u''
    if headerList == None : return resultString
    if len(headerList) == 0 : return resultString
    if isinstance(headerList, list) :
        for headerDic in headerList :
            for key in headerDic.keys() :
                if titleOption != 0 :
                    if type(headerDic[key][2]) == tuple :
                        resultString += u'\t%s : (\n'%(headerDic[key][1])
                        for value in headerDic[key][2] :
                            resultString += u'\t\t%s\n'%(value)
                        resultString += u'\t)\n'
                    else :
                        resultString += u'\t%s : %s\n'%(headerDic[key][1], headerDic[key][2])
                else :
                    if type(headerDic[key][2]) == tuple :
                        resultString += u'(\t'
                        for value in headerDic[key][2] :
                            resultString += u'%s\t'%(value)
                        resultString += u')\t'
                    else :
                        resultString += u'%s\t'%(headerDic[key][2])
            if titleOption == 0 :
                resultString += u'\n'

    return resultString
def getHeaderResultStringLandscape( headerList, titleOption = 0 ) :
    resultString = u''
    if headerList == None : return resultString
    if len(headerList) == 0 : return resultString
    if isinstance(headerList, list) :
        headerDic = headerList[0] 
        if titleOption != 0 :       # title
            for key in headerDic.keys() :
                resultString += u'%s\t'%(headerDic[key][1])
            resultString += u'\n'

        for key in headerDic.keys() :
            value = headerDic[key][2]
            if type(value) == tuple :
                #resultString += u'%s\t'%(value[0])
                for tupleValue in value :
                    resultString += u'%s,'%(tupleValue)
                resultString += u'\t'
            else :
                resultString += u'%s\t'%(headerDic[key][2])
        resultString += u'\n'

    return resultString
def getDataResultStringPortrait( dataList , titleOption = 0 ) :

    resultString = u''
    if dataList == None : return resultString
    if len(dataList) == 0 : return resultString 
    if isinstance(dataList, list) :
        for dataDic in dataList :
            for key in dataDic.keys() :
                if titleOption != 0 :
                    if type(dataDic[key][2]) == tuple :
                        resultString += u'\t%s : (\n'%(dataDic[key][1])
                        for value in dataDic[key][2] :
                            resultString += u'\t\t%s\n'%(value)
                        resultString += u'\t)\n'
                    else :
                        resultString += u'\t%s : %s\n'%(dataDic[key][1], dataDic[key][2])
                else :
                    if type(dataDic[key][2]) == tuple :
                        resultString += u'(\t'
                        for value in dataDic[key][2] :
                            resultString += u'%s\t'%(value)
                        resultString += u')\t'
                    else :
                        resultString += u'%s\t'%(dataDic[key][2])
            if titleOption == 0 :
                resultString += u'\n'

    return resultString
def getDataResultStringLandscape( dataList, titleOption = 0 ) :
    resultString = u''
    if dataList == None : return resultString
    if len(dataList) == 0 : return resultString
    if isinstance(dataList, list) :
        if titleOption != 0 :
            dataDic = dataList[0]
            for key in dataDic.keys() :
                resultString += u'%s\t'%(dataDic[key][1])
            resultString += u'\n'

        for dataDic in dataList :
            for key in dataDic.keys() :
                resultString += u'%s\t'%(dataDic[key][2])
            resultString += u'\n'

    return resultString
def getResultStringLandscape( resultList, 
                              statusOption = 0, 
                              headerValue = 0, 
                              dataValue = 0,
                              titleOption = 0 ) :
    resultString = u''
    if statusOption != 0 :
        if titleOption != 0 :
            resultString += u'GetDibStatus\tGetDibMsg1\tContinue\tTime\tClass Name\n'
        resultString += u'%s\t%s\t%s\t%s\t%s\n'%( resultList[0],resultList[1],
                                                  resultList[2],resultList[3],resultList[4])

    if headerValue != 0 :
        resultString += getHeaderResultStringLandscape( resultList[5], titleOption )

    if dataValue != 0 :
        resultString += getDataResultStringLandscape( resultList[6], titleOption )

    return resultString
def getResultDibStatus(result) :
    return result[0]
def getResultDibMsg1(result) :
    return result[1]
def getResultContinue(result) :
    return result[2]
def getResultTime(result) :
    return result[3]
def getResultClassName(result) :
    return result[4]
def getResultHeaderList(result) :
    return result[5]
def getResultDataList(result) :
    return result[6]
def getResultStringPortrait( resultList,
                             statusOption = 0,
                             headerValue = 0,
                             dataValue = 0,
                             titleOption = 0 ) :
    resultString = u''
    if statusOption != 0 :
        if titleOption != 0 :
            resultString += u'GetDibStatus : %s\n'%(resultList[0])
            resultString += u'GetDibMsg1 : %s\n'%(resultList[1])
            resultString += u'Continue : %s\n'%(resultList[2])
            resultString += u'Time : %s\n'%(resultList[3])
            resultString += u'Class Name : %s\n'%(resultList[4])

    if headerValue != 0 :
        resultString += getHeaderResultStringPortrait( resultList[5], titleOption )
    if dataValue != 0 :
        resultString += getDataResultStringPortrait( resultList[6], titleOption )

    return resultString
def dumpResult( resultList ) :

    for dataDic in resultList :
        print u'    {'
        for key in dataDic.keys() :
            print u'        %s = {'%(key)
            for item in dataDic[key] :
                if type(item) == tuple :
                    print u'            ('
                    for value in item :
                        print u'                %s'%(value)
                    print u'            )'
                else :
                    print u'            %s'%(item)
            print u'        }'
        print u'    }'
def getTitleString( dic ) :
    title = u''
    for key in dic :
        title += dic[key][1] + u'\t'
    title += u'\n'
    return title
def getValueString( resultList ) :
    string = u''
    if resultList == None : return string
    for dic in resultList :
        for key in dic.keys() :
            string += u'%s\t'%(dic[key][2])
        string += u'\n'
    string += u'\n'
    return string
def templateSetInputValue( obj, paramList, errLog = sys.stderr ) :
    from cxError import cxError

    eCodeDic = { 'OK' : 0, 'cxError' : -1, 'UnknownError' : -2 }

    for param in paramList :
        try :
            if len(param) >= 3 :
                obj.SetInputValue( param[0], param[1:] )
            else :
                obj.SetInputValue( param[0], param[1] )
        except cxError as e :
            if errLog != None :
                errLog.write(u'%s.SetInputValue : %s : %s\n'%(obj.__class__.__name__, 
                                                            e.desc,
                                                            e.detail_desc))
            return eCodeDic['cxError']
        except :
            if errLog != None :
                errLog.write(u'%s.SetInputValue : %s %s\n'%(  obj.__class__.__name__, 
                                                            sys.exc_info()[0],
                                                            sys.exc_info()[1] ) )
            return eCodeDic['UnknownError']

    return eCodeDic['OK']

def templateBlockRequest(   obj,
                            paramList,
                            resultFile = None,
                            errLog = sys.stderr ) :
    from cxError import cxError

    if templateSetInputValue( obj, paramList, errLog ) != 0 :   # cxError or UnknownError
        errLog.write(u'templateSetInputValue.cxError occured\n')
        return None

    bContinue = 1
    resultList = []

    while bContinue == 1 :
        #ret = obj.BlockRequest()
        
        try :
            ret = obj.BlockRequest()
        except cxError as e :
            #print e.dump()
            if errLog != None :
                errLog.write(u'%s.BlockRequest : %s : %s\n'%\
                             (obj.__class__.__name__, 
                              e.desc,
                              e.detail_desc))
            return resultList
        

        if ret == 1 : # 1 : 통신 요청 실패
            if errLog != None :
                errLog.write(u'%s.BlockRequest : %s\n'%\
                             (obj.__class__.__name__,
                              u'통신 요청 실패'))
            return resultList
        elif ret == 3 : # 3 : 그외의 내부 오류
            if errLog != None :
                errLog.write(u'%s.BlockRequest : %s\n'%\
                             (obj.__class__.__name__,
                              u'그외의 내부 오류'))
            return resultList

        result = obj.getResult()
        resultList.append(result)

        #print getResultStringPortrait(result, 1, 1, 1, 1)
        #print result[6]

        if resultFile != None :
            resultFile.write(getValueString(result[6]))

        nDibStatus = result[0]
        if ( nDibStatus == -1 ) or ( nDibStatus == 1 ) : # 1 -> waiting, -1 -> error
            if errLog != None :
                errLog.write(result[1])
                return resultList

        bContinue = result[2]
    # end of 'while bContinue == 1'

    return resultList
def templateRequest( obj, paramList, errLog = sys.stderr ) :

    if templateSetInputValue( obj, paramList, errLog ) != 0 :
        return False
    
    try :
        obj.Request()
    except cxError as e :
        if errLog != None :
            errLog.write(u'%s.Request : %s : %s\n'%( obj.__class__.__name__. 
                                                    e.desc,
                                                    e.detail_desc ))
        return False

    return True

def testBlockRequest( clsName, paramList, 
                      statusOption, headerValue, dataValue, landscape,
                      resultFile = sys.stdout, errLog = sys.stderr ) :

    #from cxCybosPlus import getCybosPlusClassDic
    from cxCybosPlus import gCybosPlusClassDic

    #cpClsDic = getCybosPlusClassDic()
    cpClsDic = gCybosPlusClassDic[clsName]

    resultList = templateBlockRequest( cpClsDic, paramList )

    bFirst = 1

    if resultList == None :
        del cpClsDic
        return

    for results in resultList :
        if landscape != 0 :
            resultFile.write( getResultStringLandscape( results,
                                                        statusOption,
                                                        headerValue,
                                                        dataValue,
                                                        titleOption = bFirst ) )
        else :
            resultFile.write( getResultStringPortrait( results,
                                                       statusOption,
                                                       headerValue,
                                                       dataValue,
                                                       titleOption = bFirst ) )
        bFirst = 0

    del cpClsDic
def checkFileExist( pathFileName ) :

    try :
        hFile = open(pathFileName,'r')
    except BaseException as e :
        #print e
        return False

    hFile.close()
    return True

def getFieldDataList( dataLineList ) :
    return [ data for data in filter(lambda x : x != u'\n', dataLineList.split(u' ')) ]

def sortListTuple( argList, basisIndex ) :
    return [ b for a,b in sorted( (tup[basisIndex], tup) for tup in argList ) ]

def test_cxStockMst() :
    from cxCybosPlus import gCybosPlusClassDic
    #from cxLog import cxLog

    #log = cxLog()
    #resultFile = cxFile()

    className = 'cxCpStockMst'
    cpClsDic = gCybosPlusClassDic[className]

    paramList = [
        [ 0, 'A000660' ],
    ]

    resultList = templateBlockRequest( cpClsDic[className], paramList )

    bFirst = 1

    for results in resultList :
        print getResultStringLandscape( results,
                                        statusOption = 1,
                                        headerValue = 1,
                                        dataValue = 1,
                                        titleOption = bFirst )
        bFirst = 0

    del cpClsDic
def test_cxStockChart() :

    from cxCybosPlus import gCybosPlusClassDic        
    from cxLog import cxLog
    from cxFile import cxFile
   
    log = cxLog()
    resultFile = cxFile()

    className = 'cxStockChart'
    cpClsDic = gCybosPlusClassDic[className]

    fieldList = [ 0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, \
                  14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, \
                  25, 26, 37 ]

    paramList = [ 
        [ 0, u'A000660' ], # 하이닉스
        [ 1, ord('1') ],
        [ 2, 20121010 ],
        [ 3, 19920901 ],
        [ 4, len(fieldList) ],
        [ 5 ] + fieldList,
        [ 6, ord('D') ],
        [ 10, ord('3') ]
    ]
   
    resultList = templateBlockRequest( cpClsDic[className], paramList, errLog = log )

    bFirst = 1
    for results in resultList :
        resultFile.write( getResultStringLandscape( results, 
                                                    statusOption = 0, 
                                                    headerValue = 0, #len(results[5]), 
                                                    dataValue = 1, #len(results[6]),
                                                    titleOption = bFirst ) )
        bFirst = 0
        
        #resultFile.write( getHeaderResultString(results[5], 1 ) )
        #resultFile.write( '\n' )
        #resultFile.write( getDataResultString(results[6], 1 ) )
        

    log.close()
    resultFile.close()

    del cpClsDic
def test_findCodecName() :
    testStr = '안녕하세요'
    #uniStr = unicode(testStr)
    #uniStr = unicode(unicode(testStr,'utf-8').encode('utf-8'))
    #print uniStr, type(uniStr)
    findCodecName(testStr, encodingErrorFlag = 0 )
    print testStr
    print unicode(testStr.decode('utf-8'))
def test_cpBlockRequest() :
    from cxFile import cxFile
    resultFile = cxFile()
    paramList = [
        [ 0, 'A000660'],
    ]
    testBlockRequest( 'cxCpStockMst', paramList, 1, 1, 1, 0, resultFile, sys.stderr )
    resultFile.close()

def test() :
    #test_cxStockChart()
    #test_cxStockMst()
    #test_cpBlockRequest()
    #test_findCodecName()
    #print '안녕하세요'
    #print UNI('안녕하세요')
    print __function_name__()

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

    print '\n',"-"*79
    print "after"
    collect_and_show_garbage()

    #raw_input("Hit any key to close this window...")
