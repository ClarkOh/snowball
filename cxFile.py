################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxFile.py
# date        : 2012-09-06 14:27:08
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import time

class cxFile :

    def __init__(self, fileName = u'result_%s.txt'%(unicode(time.strftime('%Y%m%d'))) ) :
        self.hFile = None
        self.fileName = fileName
    
    def __del__(self) :
        pass

    def open(self, mode = 'a' ) :
        import codecs
        try :
            self.hFile = codecs.open( self.fileName, mode, 'utf-8')
        except BaseException as e :
            print e
            raise e
        except :
            print 'open : unknown error'
            return False
        return True

    def close(self) :
        if self.hFile != None :
            self.hFile.close()
            del self.hFile
            self.hFile = None

    def write(self, context ) :
        writeString = context
        if self.hFile == None :
            try :
                self.open()
            except BaseException as e :
                return False
        elif self.hFile.closed == True :
            try : self.open()
            except BaseException as e : 
                return False
        elif self.hFile.closed == False and self.hFile.mode[0] == 'r' :
            self.close()
            try : self.open()
            except BaseException as e :
                return False

        self.hFile.write( unicode(context) )
        return True
    
    def readlines(self) :
        if self.hFile == None :
            self.open(mode = 'r')
        elif self.hFile.closed == True :
            try : self.open(mode = 'r')
            except : return []
        elif self.hFile.closed == False and self.hFile.mode[0] != 'r' :
            self.close()
            try : self.open(mode = 'r')
            except : return []
        self.hFile.seek(0,0)
        return self.hFile.readlines()

    def readline(self) :
        if self.hFile == None :
            self.open(mode = 'r')
        elif self.hFile.closed == True :
            try : self.open(mode = 'r')
            except : return []
        elif self.hFile.closed == False and self.hFile.mode[0] != 'r' :
            self.close()
            try : self.open(mode = 'r')
            except : return []
        return self.hFile.readline()

    def delete(self, bForce=True) :
        import os
        if self.hFile != None :
            if self.hFile.closed == False :
                self.close()
            if bForce == True :
                os.remove(self.fileName)
        else :
            if bForce == True :
                os.remove(self.fileName)

    def getLastLine(self) :
        if self.hFile == None :
            self.open(mode='r')
        elif self.hFile.closed == True :
            try : self.open(mode='r')
            except : return None 
        elif self.hFile.closed == False and self.hFile.mode[0] != 'r' :
            self.close()
            try : self.open(mode='r')
            except : return None
        result = list(self.hFile)
        if result != [] :
            for i in range(len(result)-1,-1,-1) :
                if result[i] != u'' and result[i] != u'\n' and \
                   result[i] != u'\t' and result[i] != u' ' and \
                   result[i] != u'\r' and result[i] != u'\n\r':
                    return result[i]
        return u''
         
    def isEmpty(self) :
        import os
        if not os.path.exists(self.fileName) :
            return True
        if os.path.getsize(self.fileName) > 0 :
            return False
        return True

    def isExist(self) :
        import os
        return os.path.exists(self.fileName) 
            
    def dump(self) :
        for line in self.readlines() :
            print line,

    def close(self) :
        if self.hFile != None :
            self.hFile.close()

def test_cxFile() :
    resultFile = cxFile()
    #resultFile.dump()
    #print
    resultFile.write(u'하이\n')
    #resultFile.dump()
    #print
    #resultFile.close()
    #for line in resultFile.readlines() :
    #    print line
    #print
    resultFile.write('머지\n')
    #resultFile.dump()
    resultFile.delete() 
    resultFile.close()

def test_read_file( fileName ) :
    import os, errno
    import codecs

    #fileName = u'A000050_경방_T'
    try :
        #historyFile = open( fileName, 'r')
        historyFile = codecs.open( fileName, 'r', 'utf-8' )
    except BaseException as e :
        print 'BaseException'
        print e.errno
        print e.strerror
        print e
        return
    except IOError as e :
        print 'IOError'
        print 'e : ', e
        print 'errno : ', e.errno
        print 'err code : ', errno.errorcode[e.errno]
        print 'err message : ', e.strerror
        print 'err message : ', os.strerror(e.errno)
        print 'failed to open \'%s\' file.'%(fileName)
        return

    print historyFile.name
    print historyFile.closed
    print historyFile.mode
    print historyFile.softspace

    lines = historyFile.readlines()

    for line in lines :
        print line,

    historyFile.close()

def test() :
    import common
    #test_read_file(u'A000050_경방_T')
    test_cxFile()

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
