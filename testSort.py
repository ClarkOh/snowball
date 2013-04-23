################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : testSort.py
# date        : 2013-04-23 00:24:12
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.2 Stackless 3.1b3 060516 (default, Dec 21 2011, 17:08:51) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

def testSort(argList) :
    return [ b for a,b in sorted( (tup[0], tup) for tup in argList ) ]

def test() :
    testList = [ [ 19980103, 5465,  3.4 ],
                 [ 19961224, 12000, 1.2 ],
                 [ 20130615, 503,   10.2] ]
    #sortedList = testSort(testList)
    from common import sortListTuple
    sortedList = sortListTuple( testList, 0 )
    print sortedList

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
