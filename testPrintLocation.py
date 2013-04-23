################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : testPrintLocation.py
# date        : 2012-12-04 15:40:23
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.1 Stackless 3.1b3 060516 (release27-maint, Jan  1 2011, 13:04:37) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE


def test() :
    from time import sleep 
    import sys 

    for x in range(100): 
        print '\rDownloading: %s (%d%%)' % ("|"*(x/2), x), 
        sys.stdout.flush() 
        sleep(0.1)  


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
