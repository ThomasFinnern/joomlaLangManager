#!/usr/bin/python

import os
# import re
import getopt
import sys
import shutil
import io

from datetime import datetime

from TransMatchFileNames import TransMatchFileNames
from TranslateLang import TranslateLang

from jLangConfig import Config

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

class TranslateLangs:
	def __init__(self, srcPath, srcLangId, trgPath, trgLangId):
		self.__srcPath = srcPath
		self.__srcLangId = srcLangId
		self.__trgPath = trgPath
		self.__trgLangId = trgLangId
		
		self.__matches = {}  #
		self.__matchResults = object()
		
		self.matchFileNames ()
		self.doTranslateLangs ()

	def matchFileNames (self, srcPath="", srcLangId="", trgPath="", trgLangId=""):
		
		# New name given
		if (len(srcPath) > 0):
			self.__srcPath = srcPath
		
		# New name given
		if (len(srcLangId) > 0):
			self.__srcLangId = srcLangId
		
		# New name given
		if (len(trgPath) > 0):
			self.__trgPath = trgPath
		
		# New name given
		if (len(trgLangId) > 0):
			self.__trgLangId = trgLangId
		
		if not testDir(self.__srcPath):
			print('***************************************************')
			print('!!! Source folder path not found !!! ? -l ' + self.__srcPath + ' ?')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(2)
		
		if not testDir(self.__trgPath):
			print('***************************************************')
			print('!!! Target folder path not found !!! ? -l ' + self.__trgPath + ' ?')
			print('***************************************************')
			print(HELP_MSG)
			Wait4Key()
			sys.exit(2)
		
		# TransMatchFileNames
		self.__matchResults = TransMatchFileNames (self.__srcPath, self.__srcLangId, self.__trgPath, self.__trgLangId)
		self.__matches =  self.__matchResults.matches









	def doTranslateLangs (self):
		try:
			print('*********************************************************')
			print('doTranslateLangs')
	
			# --------------------------------------------------------------------
			# All given files
			# --------------------------------------------------------------------
			
			outTxt = 'matches: ' + str(len(self.__matches)) + '\n'
			
			hasError = False
			
			for srcFile, trgfile in self.__matches.items():
				outTxt += '  "' + srcFile + '" <=> "' + trgfile + '"' + '\n'
				
				#SourceFile = os.path.join (self.__srcPath, srcFile)
				SourceFile = srcFile
				#TargetFile = os.path.join (self.__trgPath, trgfile)
				TargetFile = trgfile
				
				# --------------------------------------------------------------------
				# translate file
				# --------------------------------------------------------------------

#				hasError = hasError and TranslateLang.TranslateLang (SourceFile, TargetFile)
				
				TranslateLang (SourceFile, TargetFile)
				#TranslateLang.TranslateLang (SourceFile, TargetFile)
			
		# --------------------------------------------------------------------
		#
		# --------------------------------------------------------------------
		except Exception as ex:
			print(ex)
	
		# --------------------------------------------------------------------
		#
		# --------------------------------------------------------------------
	
		finally:
			print('exit TranslateLangs: Error:')
	
		return outTxt
	

	def toString(self):
		outTxt = "--- TranslateLangs: ---------------" + '\n'
	
	
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
	optlist, args = getopt.getopt(sys.argv[1:], 's:t:a:b:12345h')
	
	srcPath = os.path.join ('..', '.regression', 'en-GB')
	#srcPath = os.path.join('..', '.sandbox', 'en-GB')
	srcLangId = 'en-GB'
	trgPath = os.path.join ('..', '.regression', 'de-DE')
	#trgPath = os.path.join('..', '.sandbox', 'de-DE')
	trgLangId = 'de-DE'

	cfgSrcPath = Config.baseSrcPath
	if(len(cfgSrcPath) > 0):
		srcPath = cfgSrcPath
	cfgTrgPath = Config.baseTrgPath
	if(len(cfgTrgPath) > 0):
		trgPath = cfgTrgPath

	for i, j in optlist:
		if i == "-s":
			srcPath = j
		if i == "-t":
			srcLangId = j
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

	Translation = TranslateLangs(srcPath, srcLangId, trgPath, trgLangId)
	
	# does print all
	print(Translation.toString())
	
	Translation.writeLogFile('.\logTransMatch.txt', True)
	
	print_end(start)
