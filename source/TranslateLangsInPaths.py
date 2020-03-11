#!/usr/bin/python

import os
# import re
import getopt
import sys
import shutil
import io

from datetime import datetime

from TranslateLangs import TranslateLangs

from jLangConfig import Config

HELP_MSG = """
All given paths in config will be used to translate files

Supports translation of joomla lang string to other language
TranslateLangsInPaths supports the translation of a joomla ini file with
joomla string definitions to a existing file with different language.



yyyy

usage: TranslateLangsInPaths.py -s <file path name> -t <>file path name> -l <lang definition> [-h]
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
# TranslateLangsInPaths
# ================================================================================

class TranslateLangsInPaths:
	def __init__(self, comparePaths, srcLangId, trgLangId):
		self.__comparePaths = comparePaths

		self.__srcLangId = srcLangId
		self.__trgLangId = trgLangId
		
		self.doTranslateLangsInPaths ()

	def doTranslateLangsInPaths (self):
		try:
			print('*********************************************************')
			print('doTranslateLangsInPaths')

			# --------------------------------------------------------------------
			# All given paths
			# --------------------------------------------------------------------

			for srcPath, trgPath in self.__comparePaths.items():
				TranslateLangs(srcPath, self.__srcLangId, trgPath, self.__trgLangId)

		# --------------------------------------------------------------------
		#
		# --------------------------------------------------------------------
		except Exception as ex:
			print(ex)
	
		# --------------------------------------------------------------------
		#
		# --------------------------------------------------------------------
	
		finally:
			print('exit TranslateLangsInPaths: Error:')
	
		return
	

	def toString(self):
		outTxt = "--- TranslateLangsInPaths: ---------------" + '\n'
	
	
	def writeLogFile(self, logPathFileName, doAppend=False):
		# mode = doAppend ? "o" : "w"
		if (doAppend):
			mode = "o"
		else:
			mode = "w"
		
		logTxt = self.toString()
		
		#with open(logPathFileName, mode) as logFile:
		#	logFile.write(logTxt)
	
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
	optlist, args = getopt.getopt(sys.argv[1:], 'a:b:12345h')
	
	srcLangId = 'en-GB'
	trgLangId = 'de-DE'

	comparePaths = Config.comparePaths

	for i, j in optlist:
		if i == "-a":
			trgPath = j
		if i == "-b":
			trgLangId = j
		
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

	Translation = TranslateLangsInPaths(comparePaths, srcLangId, trgLangId)
	
	# does print all
	print(Translation.toString())
	
	Translation.writeLogFile('.\logTransMatch.txt', True)
	
	print_end(start)
