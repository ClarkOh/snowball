# -*- coding: utf-8 -*-
# author : Jinwon Oh
#
# 

import os
import sys
from time import localtime, strftime
#import subprocess

def makePyTemplate( fileName ) :

	if fileName == '':
		print 'file name is empty'

		return

	if fileName[-3:] != '.py' :
		fileName += '.py'

	try:
		hFile = open(fileName,'r')
	except IOError: #fileName is not exist
		pass
	else : #fileName is exist already, ask overwrite or not
		overwrite = raw_input('%s is already exist. Would you overwrite it? (y/N) : '%fileName)

		if overwrite == '' :	# default 'N'
			overwrite == 'n'

		if overwrite == 'y' :
			hFile.close()
			pass
		else :
			print 'Bye~~'
			hFile.close()
			return

	try:
		hFile = open(fileName,'w')
	except IOError as (errno, errmsg):
		print '[%s] I/O error (%d) : %s' % (fileName,errno,errmsg)
		return
	except :
		print 'Unexpected error : ', sys.exc_info()[0]
		raise

	hFile.write('#'*80)
	hFile.write('\n')
	hFile.write('# -*- coding: utf-8 -*-\n\n\n')
	hFile.write('# author      : Jinwon Oh\n')
	hFile.write('# file name   : %s\n' % fileName)
	hFile.write('# date        : %s\n' % strftime("%Y-%m-%d %H:%M:%S", localtime() ) )
	hFile.write('# ver         : \n')
	hFile.write('# desc.       : \n')
	hFile.write('# tab size    : set sw=4, ts=4\n')
	hFile.write('# python ver. : %s\n' % (sys.version) )
	hFile.write('\n')
	hFile.write('# ADD CODES FROM HERE\n\n')

	hFile.write('class cHello :\n')
	hFile.write('\tdef __init__(self) :\n')
	hFile.write('\t\tprint "hello"\n')
	hFile.write('\tdef __del__(self) :\n')
	hFile.write('\t\tpass\n')
	hFile.write('\n\n')

	hFile.write('def test() :\n')
	hFile.write('\thello = cHello()\n')
	hFile.write('\tdel hello\n\n\n')

	hFile.write('def collect_and_show_garbage() :\n')
	hFile.write('\t"Show what garbage is present."\n')
	hFile.write('\tprint "Collecting..."\n')
	hFile.write('\tn = gc.collect()\n')
	hFile.write('\tprint "Unreachable objects:", n\n')
	hFile.write('\tif n > 0 : print "Garbage:"\n')
	hFile.write('\tfor i in range(n):\n')
	hFile.write('\t\tprint "[%d] %s" % (i, gc.garbage[i])\n\n')

	hFile.write('if __name__ == "__main__" :\n')
	hFile.write('\timport gc\n\n')
	hFile.write('\tgc.set_debug(gc.DEBUG_LEAK)\n\n')
	hFile.write('\tprint "before"\n')
	hFile.write('\tcollect_and_show_garbage()\n')
	hFile.write('\tprint "testing..."\n')
	hFile.write('\tprint "-"*79\n\n')
	hFile.write('\ttest()\n\n')
	hFile.write('\tprint "-"*79\n')
	hFile.write('\tprint "after"\n')
	hFile.write('\tcollect_and_show_garbage()\n\n')
	hFile.write('\traw_input("Hit any key to close this window...")\n')

	hFile.close()
	print "OK, %s is ready!" % fileName

#	subprocess.call("gvim %s &"%fileName,shell=False)
#	os.system("gvim %s&"%fileName)
#	os.execvp('gvim', ['gvim',fileName])

	return


if __name__ == '__main__' :

	fileName = raw_input('Please, input the file name : ')

	makePyTemplate(fileName)

	raw_input("Hit any key to close this window...")

