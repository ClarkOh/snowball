################################################################################
# -*- coding: utf-8 -*-


# author      : Jinwon Oh
# file name   : cxPortfolio.py
# date        : 2013-01-29 16:59:34
# ver         : 
# desc.       : 
# tab size    : set sw=4, ts=4
# python ver. : 2.7.2 Stackless 3.1b3 060516 (default, Dec 21 2011, 17:08:51) [MSC v.1500 32 bit (Intel)]

# ADD CODES FROM HERE

class cxPortFolio :
    DEFAULT  = -6666

    def __init__(self, initTotalAsset) :
        self.initTotalAsset = initTotalAsset
        self.nominalAccount = initTotalAsset
        self.currentTotalAsset = initTotalAsset
        self.maxRiskPrice  = (1.0/100)* initTotalAsset
    
    def __del__(self) :
        pass

    def changeTotalAsset(self, totalAsset) :
        self.initTotalAsset = totalAsset
        self.nominalAccount = totalAsset
        self.currentTotalAsset = totalAsset
        self.maxRiskPrice = (1.0/100)* totalAsset

    def buy(self, amount) :
        if self.currentTotalAsset <= 0 :
            return self.DEFAULT
        self.currentTotalAsset -= amount
        if self.currentTotalAsset <= 0 :
            return self.DEFAULT
        if self.currentTotalAsset <= (9.0/10)* self.nominalAccount :
            self.nominalAccount = self.currentTotalAsset
        self.maxRiskPrice = (1.0/100)*self.nominalAccount
        return 0

    def sell(self, amount) :
        self.currentTotalAsset += amount

        if self.currentTotalAsset >= (11.0/10)* self.nominalAccount :
            self.nominalAccount = self.currentTotalAsset
        self.maxRiskPrice = (1.0/100)*self.nominalAccount
        return 0

    def dump(self) :
        return 'C : %d , N : %d , U : %f'%(self.currentTotalAsset, self.nominalAccount, \
                                            self.maxRiskPrice)


def test() :
    portFolio = cxPortFolio(5000000)

    for i in range(0, 10000) :
        portFolio.buy(200)
        print i , portFolio.dump()
        portFolio.sell(50)
        print i , portFolio.dump()

    del portFolio


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
