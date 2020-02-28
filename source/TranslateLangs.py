#!/usr/bin/python

import os
# import re
import getopt
import sys
import shutil
import io

from datetime import datetime

from jLangFile import *

HELP_MSG = """
Supports translation of joomla lang string to other language
TranslateLangs supports the translation of a joomla ini file with
joomla string definitions to a existing file with different language.

The source (normally a en-GB file) contains joomla language definitions

The target (example de_DE file) translation will be supported with
 * Empty translation line for new texts marked with >> New >>
 * Changed translation lines are marked with >> Chg >>

If the target file does not exist the target language definition is used to
create the path and the a file



usage: TranslateLangs.py -s <file path name> -t <>file path name> -l <lang definition> [-h]
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

# -------------------------------------------------------------------------------
LeaveOut_01 = False
LeaveOut_02 = False
LeaveOut_03 = False
LeaveOut_04 = False
LeaveOut_05 = False


# -------------------------------------------------------------------------------

# ================================================================================
# TranslateLangs
# ================================================================================

def TranslateLangs(SourceFolder, TargetFolder, TargetLang):
	try:
		print('*********************************************************')
		print('TranslateLangs')
		print('SourceFolder: ' + SourceFolder)
		print('TargetFolder: ' + TargetFolder)
		print('TargetLang: ' + TargetLang)
		print('---------------------------------------------------------')

		# ---------------------------------------------
		# check input
		# ---------------------------------------------

		if SourceFolder == '':
			print('***************************************************')
			print('!!! Source folder (SourceFolder) name is mandatory !!!')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(1)

		if not testDir(SourceFolder):
			print('***************************************************')
			print('!!! Source folder path not found !!! ? -l ' + SourceFolder + ' ?')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(2)

		# --------------------------------------------------------------------

		if TargetFolder == '':
			print('***************************************************')
			print('!!! Target folder name is mandatory !!!')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(3)

		if not testDir(TargetFolder):
			print('***************************************************')
			print('!!! Target folder (TargetFolder) path not found !!! ? -l ' + TargetFolder + ' ?')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(4)

		# --------------------------------------------------------------------
		# All files in source
		# --------------------------------------------------------------------

		allFiles = [f for f in os.listdir(SourceFolder) if os.path.isfile(os.path.join(SourceFolder, f))]

		for sourceFile in allFiles:
			print('sourceFile: ' + sourceFile)

		return

		# --------------------------------------------------------------------
		# read source file
		# --------------------------------------------------------------------

		source = jLangFile(SourceFolder)

		# --------------------------------------------------------------------
		#
		# --------------------------------------------------------------------

		srcTranslations = source.translations()
		trgTranslations = target.translations()

		# --------------------------------------------------------------------
		# create empty translations
		# --------------------------------------------------------------------

		isChanged = False

		# Texts need to be translated
		translationOriginals = []

		# create all translations
		#       for transId, translation in srcTranslations.items():
		for transId in srcTranslations.keys():

			# translation found ?
			if (transId in trgTranslations):
				translation = trgTranslations[transId]
			else:
				translation = "!!!"
				isChanged = True
				# keep naked original texts for 'auto' translation
				translationOriginals.append(srcTranslations[transId])

			destination.set(transId, translation)

		# ToDo Missing / Merge / empty lines ...

		# --------------------------------------------------------------------
		# results to file
		# --------------------------------------------------------------------

		if (isChanged):
			destination.translationsToFile("", False, False)

			orignalTextFile = TargetFolder + '.txt'
			with open(orignalTextFile, mode='wt', encoding='utf-8') as myfile:
				myfile.write('\n'.join(translationOriginals))

	# --------------------------------------------------------------------
	#
	# --------------------------------------------------------------------


	except Exception as ex:
	    print(ex)

	# --------------------------------------------------------------------
	#
	# --------------------------------------------------------------------

	finally:
	    print('exit TranslateLangs')

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
		print("Error: File does not exist: " + file)
	return exists


def testDir(directory):
	exists = os.path.isdir(directory)
	if not exists:
		print("Error: Directory does not exist: " + directory)
	return exists


def print_header(start):
	print('------------------------------------------')
	print('Command line:', end='')
	for s in sys.argv:
		print(s, end='')

	print('')
	print('Start time:   ' + start.ctime())
	print('------------------------------------------')


def print_end(start):
	now = datetime.today()
	print('')
	print('End time:               ' + now.ctime())
	difference = now - start
	print('Time of run:            ', difference)


# print ('Time of run in seconds: ', difference.total_seconds())

# ================================================================================
#   main (used from command line)
# ================================================================================

if __name__ == '__main__':
	optlist, args = getopt.getopt(sys.argv[1:], 's:f:y:12345h')

	#   SourceFolder = ''
	#   StandardFile = ''
	#   SysFile = ''
	SourceFolder = '..\.sandbox\en-GB'
	TargetFolder = '..\.sandbox\de-DE'
	TargetLang = 'de-DE'

	for i, j in optlist:
		if i == "-s":
			SourceFolder = j
		if i == "-t":
			TargetFolder = j
		if i == "-l":
			TargetLang = j

		if i == "-h":
			print(HELP_MSG)
			sys.exit(0)

		if i == "-1":
			LeaveOut_01 = True
			print("LeaveOut_01")
		if i == "-2":
			LeaveOut_02 = True
			print("LeaveOut__02")
		if i == "-3":
			LeaveOut_03 = True
			print("LeaveOut__03")
		if i == "-4":
			LeaveOut_04 = True
			print("LeaveOut__04")
		if i == "-5":
			LeaveOut_05 = True
			print("LeaveOut__05")

	start = datetime.today()

	print_header(start)

	TranslateLangs(SourceFolder, TargetFolder, TargetLang)

	print_end(start)
