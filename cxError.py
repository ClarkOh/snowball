################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxError.py
# date        : 2012-08-10 14:41:50
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

from common import UNI

class cxError(Exception) :
    code        = None
    category    = None
    desc        = None
    detail_desc = None

    def __init__(self, code, category, desc, detail_desc='') :
        tmpCategory = u''
        tmpDesc     = u''
        tmpMore     = u''

        if category != None :
            tmpCategory = UNI(category)
            if tmpCategory == None : 
                tmpCategory = u''
        if desc != None :
            tmpDesc = UNI(desc)
            if tmpDesc == None : 
                tmpDesc = u''
        if detail_desc != None :
            tmpMore = UNI(detail_desc)
            if tmpMore == None : 
                tmpMore = u''

        self.code = code
        self.category = tmpCategory
        self.desc = tmpDesc
        self.detail_desc = tmpMore

        #print 'cxError.desc', self.desc

    def __del__(self) :
        pass
    
    def dump(self) :
        return u'code : 0x%x, category : \"%s\", desc.: \"%s\", more desc. : \"%s\"' % \
                (self.code, self.category, self.desc, self.detail_desc)

class cxErrorDic :
    error_dic = {}
    def __init__(self):
        self.error_dic[0] = [u'general',u'success',u'']

    def add_cxError(self, err):
        if err.code not in self.error_dic.keys() :
            self.error_dic[err.code] = \
                [err.category, err.desc, err.detail_desc]

    def add(self, code, category, desc, detail_desc=u''):
        tmpCategory = u''
        tmpDesc     = u''
        tmpMore     = u''
        if code not in self.error_dic.keys() :
            if category != None :
                if isinstance(category, str) :
                    tmpCategory = unicode(category,'utf8')
                else :
                    tmpCategory = unicode(category)
            if desc != None :
                if isinstance(desc, str ) :
                    tmpDesc = unicode(desc,'utf8')
                else :
                    tmpDesc = unicode(desc)
            if detail_desc != None :
                if isinstance(detail_desc, str ) :
                    tmpMore = unicode(detail_desc,'utf8')
                else :
                    tmpMore = unicode(detail_desc)
            self.error_dic[code] = [tmpCategory, tmpDesc, tmpMore ]
            return 0
        else : return 1

    def lookup(self, code):
        if code in self.error_dic.keys() :
            return self.error_dic[code]
        else : return None

    def dump(self):
        for code in self.error_dic.keys() :
            print u'code : 0x%x'%code, 
            print u'category : \"%-10s\"'%self.error_dic[code][0],
            print u'desc. : \"%s\"'%self.error_dic[code][1],
            print u'more  : \"%s\"'%self.error_dic[code][2]

            #print u'code : 0x%x, category : \"%-10s\", desc.: \"%s\", more desc. : \"%s\"' % (code, self.error_dic[code][0], self.error_dic[code][1], self.error_dic[code][2] )



def test() :
    error = cxError(1,'COM','예외가 발생했습니다.','find cxChannel')
    error.dump()

    errDic = cxErrorDic()
    msgs = errDic.lookup(0)
    if msgs != None :
        print msgs
    errDic.add_cxError(error)
    msgs = errDic.lookup(error.code)
    if msgs != None :
        print msgs

    errDic.add(2,'FILE','can\'t find file','find!')

    errDic.dump()

    del error


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
