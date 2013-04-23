################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxLog.py
# date        : 2012-09-28 15:15:09
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import time
import codecs

class cxLog :
    hFile = None
    fileName = u''

    def __init__(self, fileName = unicode(time.strftime('%Y%m%d'))+u'.log' ) :
        self.fileName = fileName
        print self.fileName

    def __del__(self) :
        pass

    def open(self, mode = 'a') :
        self.hFile = codecs.open( self.fileName, mode, 'utf-8' )
        if self.hFile is None : return False
        print 'opened %s'%(self.hFile.name)
        return True

    def close(self) :
        if self.hFile is not None :
            self.hFile.close()
            print 'close %s'%(self.hFile.name)
            del self.hFile
            self.hFile = None

    def write(self, context) :
        writeString = unicode(time.strftime('%Y.%m.%d [%H:%M:%S]')) + \
                      u'\t:\t' + \
                      context + \
                      u'\n'
        if self.hFile == None :
            try :
                self.open()
            except : return False
        elif self.hFile.closed == True :
            try :
                self.open()
            except : return False
        elif self.hFile.closed == False and self.hFile.mode[0] == 'r' :
            self.close()
            try :
                self.open()
            except : return False

        self.hFile.write( writeString )
        return True

    def dump(self) :
        if self.hFile == None :
            try :
                self.open(mode = 'r')
            except : return False
        elif self.hFile.closed == True :
            try :
                self.open(mode = 'r')
            except : return False
        elif self.hFile.closed == False and self.hFile.mode[0] != 'r' :
            self.close()
            try :
                self.open(mode = 'r')
            except : return False

        self.hFile.seek(0,0)

        for line in self.hFile.readlines() :
            print line,

    def readlines(self) :
        if self.hFile == None :
            try :
                self.open(mode = 'r')
            except : return []
        elif self.hFile.closed == True :
            try :
                self.open(mode = 'r')
            except : return []
        elif self.hFile.closed == False and self.hFile.mode[0] != 'r' :
            self.close()
            try :
                self.open(mode = 'r')
            except : return []

        self.hFile.seek(0,0)

        return self.hFile.readlines()

def test() :
    log = cxLog(u'backup\\hi.txt')

    log.write(u'헐헐헐...')
    print 'lines'
    print log.readlines()
    print 'dump'
    log.dump()
    print 'for line'
    for line in log.readlines() :
        print line

    del log


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
