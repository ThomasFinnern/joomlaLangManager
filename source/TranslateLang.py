#!/usr/bin/python

import os
#import re
import getopt
import sys
import shutil
import io

from datetime import datetime

from jLangFile import *
from jLangItem import *


HELP_MSG = """
Supports translation of joomla lang string to other language
TranslateLang supports the translation of a joomla ini file with
joomla string definitions to a existing file with different language.

The source (normally a en-GB file) contains joomla language definitions

The target (example de_DE file) translation will be supported with
 * Empty translation line for new texts marked with >> New >>
 * Changed translation lines are marked with >> Chg >>

If the target file does not exist the target language definition is used to
create the path and the a file



usage: TranslateLang.py -s <file path name> -t <>file path name> -l <lang definition> [-h]
	-s Source language file
	-f Target language file
	-l Target language definition (actually not neeeded but in the future ...)

	-h shows this message

	-1
	-2
	-3
	-4
	-5


	example:


------------------------------------
ToDo:
  * encoding='utf-8' in all file handlings !!!
  *
  *
  *
  *

"""

#-------------------------------------------------------------------------------
LeaveOut_01 = False
LeaveOut_02 = False
LeaveOut_03 = False
LeaveOut_04 = False
LeaveOut_05 = False

#-------------------------------------------------------------------------------

# ================================================================================
# TranslateLang
# ================================================================================

#toDo: make class with log results

def TranslateLang (SourceFile, TargetFile):
	try:
		print ('*********************************************************')
		print ('TranslateLang')
		print ('SourceFile: ' + SourceFile)
		print ('TargetFile: ' + TargetFile)
		print ('---------------------------------------------------------')

		#---------------------------------------------
		# check input
		#---------------------------------------------

		if SourceFile == '':
			print('***************************************************')
			print('!!! Source file (SourceFile) name is mandatory !!!')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(1)

		if not testFile(SourceFile):
			print('***************************************************')
			print('!!! Source file path not found !!! ? -l ' + SourceFile + ' ?')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(2)

		# --------------------------------------------------------------------

		if TargetFile == '':
			print('***************************************************')
			print('!!! Target file name is mandatory !!!')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(3)

#		if not testFile(StandardFile):
#			print('***************************************************')
#			print('!!! Target file (StandardFile) path not found !!! ? -l ' + Target + ' ?')
#			print('***************************************************')
#			print(HELP_MSG)
#			Wait4Key()
#			sys.exit(4)

		# --------------------------------------------------------------------
		# target file (s)
		# --------------------------------------------------------------------

		# org file name: copy if exist
		# debug helper to kee the original on serveral translation attempts
		orgTargetFile = TargetFile + '.org'
		if (os.path.isfile(orgTargetFile)):
			shutil.copy(orgTargetFile, TargetFile)

		# create file if not exists
		if (not os.path.isfile(TargetFile)):
			f = open(TargetFile, "w")
			f.close()

		# ToDo: Test empty files !!!
		target = jLangFile(TargetFile)

		#empty class
		destination = jLangFile()
		destination.langPathFileName = TargetFile
		
		# keep header
		destination.header = target.header

		# --------------------------------------------------------------------
		# read source file
		# --------------------------------------------------------------------

		source = jLangFile (SourceFile)

		#--------------------------------------------------------------------
		# 
		#--------------------------------------------------------------------

		srcTranslations = source.translations()
		trgTranslations = target.translations()

		#--------------------------------------------------------------------
		# read translations in order of source
		#--------------------------------------------------------------------

		# Plain texts to be translated -> for file
		translationOriginals = []

		idx = 0
		
		# create all translations
		for transId in srcTranslations.keys():

			# translation already done ?
			if (transId in trgTranslations):
				translation = trgTranslations[transId]
			else:
				# empty item
				translation = jLangItem()
			
				# keep naked original texts for 'auto' translation
				translationOriginals.append(srcTranslations[transId].translationText)
				
			destination.set (transId, translation)
			
			idx += 1
		
		# find obsolete / surplus translations
		destination.surplusTranslations = {}

		for transId in trgTranslations.keys():

			# translation not existing source ?
			if (not transId in srcTranslations):
				destination.surplusTranslations [transId] = trgTranslations[transId]

		#--------------------------------------------------------------------
		# results to file
		#--------------------------------------------------------------------

		destination.translationsToFile ()

		orignalTextFile  = TargetFile + '.txt'
		with open(orignalTextFile, mode='wt', encoding='utf-8') as myfile:
			myfile.write('\n'.join(translationOriginals))

		#--------------------------------------------------------------------
		#
		#--------------------------------------------------------------------


	except Exception as ex:
		print(ex)

	# --------------------------------------------------------------------
	#
	# --------------------------------------------------------------------

	finally:
		print ('exit TranslateLang')


	return


##-------------------------------------------------------------------------------

def Wait4Key():
	try:
		input("Press enter to continue")
	except SyntaxError:
		pass


def testFile(file):
	exists = os.path.isfile(file)
	if not exists:
		print ("Error: File does not exist: " + file)
	return exists

def testDir(directory):
	exists = os.path.isdir(directory)
	if not exists:
		print ("Error: Directory does not exist: " + directory)
	return exists

def print_header(start):

	print ('------------------------------------------')
	print ('Command line:', end='')
	for s in sys.argv:
		print (s, end='')

	print ('')
	print ('Start time:   ' + start.ctime())
	print ('------------------------------------------')

def print_end(start):
	now = datetime.today()
	print ('')
	print ('End time:               ' + now.ctime())
	difference = now-start
	print ('Time of run:            ', difference)
	#print ('Time of run in seconds: ', difference.total_seconds())

# ================================================================================
#   main (used from command line)
# ================================================================================

if __name__ == '__main__':
	optlist, args = getopt.getopt(sys.argv[1:], 's:f:y:12345h')

#	SourceFile = ''
#	StandardFile = ''
#	SysFile = ''
	SourceFile = '..\.sandbox\en-GB\com_contact.ini'
	TargetFile = '..\.sandbox\de-DE\com_contact.ini'

	for i, j in optlist:
		if i == "-s":
			SourceFile = j
		if i == "-t":
			TargetFile = j

		if i == "-h":
			print (HELP_MSG)
			sys.exit(0)

		if i == "-1":
			LeaveOut_01 = True
			print ("LeaveOut_01")
		if i == "-2":
			LeaveOut_02 = True
			print ("LeaveOut__02")
		if i == "-3":
			LeaveOut_03 = True
			print ("LeaveOut__03")
		if i == "-4":
			LeaveOut_04 = True
			print ("LeaveOut__04")
		if i == "-5":
			LeaveOut_05 = True
			print ("LeaveOut__05")

	start = datetime.today()

	print_header(start)

	TranslateLang (SourceFile, TargetFile)

	print_end(start)

