################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxChannel.py
# date        : 2011-02-06 19:57:41
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

import stackless
from cxError import cxError

"""
cxChannel
    private: DO NOT CALL THESE METHODS FROM OUTSIDE
        __on_received()
    public:
        open()
        close()
        set_event_handler(handler)
        receive(msgs)
using error code :
    [1,2] in open()
"""
class cxChannel :
    __ch = None
    __eventHandler = None
    
    def open(self):
        try:
            self.__ch = stackless.channel()
        except :
            raise cxError(1,'cxChannel',u'stackless.channel() is failed',\
                            'check whether stackless is imported or not')

        try:
            stackless.tasklet(self.__on_received)()
        except :
            raise cxError(2,'cxChannel',u'stackless.tasklet() is failed',\
                            'check whether cxChannel::__on_received function is existed or not')


    def close(self):
        if self.__ch != None :
            self.__ch.send('exit_magic_code')
            del self.__ch
        if self.__eventHandler != None :
            del self.__eventHandler

    def set_event_handler(self, eventHandler) :
        self.__eventHandler = eventHandler

    def __on_received(self) :
        if self.__ch != None :
            while True:     # DO NOT REMOVE THIE LOOP , IT MAKES _ch ALIVE
                msgs = self.__ch.receive() 
                if msgs == 'exit_magic_code' :
                    break
                if self.__eventHandler != None :
                    self.__eventHandler(msgs)
                    
    def receive(self, msgs) :
        if self.__ch != None :
            """
            [CAUTION!!]         
            DO NOT CHANGE THE ORDER OF PRINTING
            IT MUST BE PRINT BEFORE SEND OPERATION!!!
            SEND OPERATION RETURNS WHEN RECEIVING OPERATION FINISHED. 
            (BLOCKED OPERATION)
            """
            self.__ch.send(msgs)

"""
 cxChannelContainer : example class which shows cxChannel class usages.
    private:    DO NOT CALL THESE METHOD FROM OUTSIDE
        __init__
        __del__
        __on_received(msgs)     
    public:
        open()
        close()
        receive()
        set_name(name)

"""
class cxChannelContainer :

    __cxCh = None
    __name = None

    def __init__(self):
        self.__name = ''

        try:
            self.__cxCh = cxChannel()
        except :
            raise 

        print '[DEBUG]\tcreate cxChannelContainer'

    def __del__(self):
        if self.__cxCh != None :
            del self.__cxCh
        print '[DEBUG]\tdelete cxChannelContainer %s'% self.__name

    def open(self):
        try:
            self.__cxCh.open()
        except cxError as e:
            e.dump()
            raise
        """
        [CAUTION!!]
        THIS HANDLE MAKE CIRCULAR REFERENCE.
        SO, __del__ WILL NOT BE CALLED IN DESTRUCTION WHICH MEANS GARBAGE MAKING.
        """
        self.__cxCh.set_event_handler(self.__on_received)

    def close(self):
        self.__cxCh.close()

    def set_name(self, name):
        self.__name = name

    def receive(self, msgs):
        print '[DEBUG]\t%s (cxChannelContainer) receive :'% self.__name, msgs
        if self.__cxCh != None :
            self.__cxCh.receive(msgs)

    def __on_received(self, msgs):
        print '%s (cxChannelContainer) received :'% self.__name, msgs
        """
         DO SOMETHING FROM HERE.
        """


def test() :

    try:
        t_CxCh01 = cxChannelContainer()
    except:
        return

    try:
        t_CxCh02 = cxChannelContainer()
    except:
        return
    
    """
    t_CxCh01.open()
    """
    try:
        t_CxCh01.open()
    except:
        print 'failed to t_CxCh01.open()'
        return
    
    """
    t_CxCh02.open()
    """
    try:
        t_CxCh02.open()
    except:
        print 'failed to t_CxCh02.open()'
        return

    t_CxCh01.set_name('army')
    t_CxCh02.set_name('boom')

    t_CxCh01.receive('hello?, army?')
    t_CxCh02.receive('hello?, long time no see, boom?')
    t_CxCh01.receive('what are you doing?')
    t_CxCh02.receive('I dont know')


    t_CxCh01.close()
    t_CxCh02.close()

    del t_CxCh01
    del t_CxCh02

def collect_and_show_garbage() :
    'Show what garbage is present.'
    print 'Collecting...'
    n = gc.collect()
    print 'Unreachable objects:', n
    if n > 0 : print 'Garbage:'
    for i in range(n):
        print '[%d] %s' % (i, gc.garbage[i])


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
