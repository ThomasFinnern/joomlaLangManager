#!/usr/bin/python

import os
# import re
import getopt
import sys
import io
import shutil

from datetime import datetime

HELP_MSG = """

The class collects lines of a joomla language file (read/write ? change ?)

usage: LangFile.py -f <path file name> nnn -? xxxx -? yyyy  [-h]
	-f path to language file 
	-? 


	-h shows this message
	
	-1 
	-2 
	-3 
	-4 
	-5 
	
	
	example:
	
	
------------------------------------
ToDo:
  * sorting,
  * append comment to translation (ID -> line index )
  * 
  * 
  * 

? * sort
? * doubles
? * merge ini  with sys ?	
? Extern: Read *.xml and add    
	
  
"""

# -------------------------------------------------------------------------------
LeaveOut_01 = False
LeaveOut_02 = False
LeaveOut_03 = False
LeaveOut_04 = False
LeaveOut_05 = False


# -------------------------------------------------------------------------------

# ================================================================================
# LangFile
# ================================================================================

class jLangFile:
    """  collects lines of a joomla language file for read/write/update """

    def __init__(self, langPathFileName):
        self.langPathFileName = langPathFileName  # CVS modules file name with path

        self._fileLines = []  # File lines to reconstruct the file in old order
        self._translations = {}  # All translations
        self._langId = 'en-GB'  # lang ID
        self._isSystType = False  # lang file type (normal/sys)
        # self._f = []  # All translations

        # ---------------------------------------------
        # check input
        # ---------------------------------------------

        if not os.path.isfile(langPathFileName):
            print('***************************************************')
            print('!!! Language file not found !!! ? -p/-m ' + langPathFileName + ' ?')
            print('***************************************************')
            print(HELP_MSG)
            sys.exit(1)

        #		self._initLists()  # (later binding)
        self.assignFileContent(self.langPathFileName)

    # ================================================================================
    # extraction of file modules
    # ================================================================================

    #	def _initLists(self):
    #		# read modules file and assign to lists
    #		self.assignFileContent(self.langPathFileName)

    # -------------------------------------------------------------------------------

    def assignFileContent(self, langPathFileName):
        try:
            print('*********************************************************')
            print('LangFile')
            print('langPathFileName: ' + langPathFileName)
            print('---------------------------------------------------------')

            # ---------------------------------------------
            # check input
            # ---------------------------------------------

            if langPathFileName == '':
                print('***************************************************')
                print('!!! Source file (langPathFileName) name is mandatory !!!')
                print('***************************************************')
                print(HELP_MSG)
                Wait4Key()
                sys.exit(1)

            if not testFile(langPathFileName):
                print('***************************************************')
                print('!!! Source file (langPathFileName) not found !!! ? -l ' + langPathFileName + ' ?')
                print('***************************************************')
                print(HELP_MSG)
                Wait4Key()
                sys.exit(2)

            # reset
            self._translations = {}  # All translations
            self._fileLines = []  # File lines to reconstruct the file in old order

            # self._langId = 'en-GB'  # lang ID
            if ('.sys.' in langPathFileName):
                self._isSystType = False  # lang file type (normal/sys)
            else:
                self._isSystType = False  # lang file type (normal/sys)

            # --------------------------------------------------------------------
            # read all lines
            # --------------------------------------------------------------------

            with open(langPathFileName) as f:
                self._fileLines = [line.strip() for line in f]

                print('file lines: ' + str(len(self._fileLines)))
                # All lines

                idx = 0
                for line in self._fileLines:
                    idx += 1

                    # comments
                    if (line.startswith(';')):
                        continue

                    # empty lines
                    if (len(line) < 1):
                        continue

                    # --- translation split -----------------------

                    [pName, pTranslation] = line.split('=', maxsplit=1)
                    transId = pName.strip()
                    translationParanthesis = pTranslation.strip()

                    translation = translationParanthesis [1:-1]

                    # new element
                    if (transId not in self._translations):
                        # todo: own class, save with line as id for telling lines od double entries
                        self._translations[transId] = translation
                    else:
                        # Existing element
                        if (self._translations[transId] == translation):
                            logText = "Existing element found in Line " + str(idx) + ": " + transId + " = " + \
                                      self._translations[transId]
                        else:
                            logText = "Existing mismatching element found in Line " + str(idx) + ":\\r\\n" \
                                      + "1st: " + transId + " = " + self._translations[transId] \
                                      + "2nd: " + transId + " = " + translation
                        print(logText)

            print('file translations: ' + str(len(self._translations)))

            # --- debug exit -----------------------

        #                    if (idx> 20):
        #                       break

        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit assignFileContent')

        return

        # -------------------------------------------------------------------------------

    def translations(self):
        #    	print ('    >>> Enter yyy: ')
        #    	print ('       XXX: "' + XXX + '"')
        #
        #    	ZZZ = ""
        #
        #    	try:
        #
        #
        #    	except Exception as ex:
        #    		print(ex)
        #
        #    	print ('    <<< Exit yyy: ' + ZZZ)
        return self._translations

        # -------------------------------------------------------------------------------
        #

    def get(self, transId):
        print('    >>> Enter get: ')
        print('       transId: "' + transId + '"')

        _translation = ""

        try:
            _translation = self._translations[transId]

        except Exception as ex:
            print(ex)

        print('    <<< Exit yyy: ' + _translation)
        return _translation

    # -------------------------------------------------------------------------------
    #
    def set(self, transId, translation):
        print('    >>> Enter set: ')
        print('       transId: "' + transId + '"')
        print('       translation: "' + translation + '"')

        try:
            self._translations[transId] = translation

        except Exception as ex:
            print(ex)

        print('    <<< Exit set: ')
        return

    # --------------------------------------------------------------------
    # determine build ID
    # --------------------------------------------------------------------

    #		ZZZ = determineZZZ (langPathFileName)
    #		print ('ZZZ: ' + ZZZ)

    # --------------------------------------------------------------------
    # create base folder
    # --------------------------------------------------------------------

    # installPath = os.path.join (RightPath, ZZZ)
    # print ('installPath: ' + installPath)
    # if not os.path.exists(installPath):
    #	os.makedirs(installPath)

    # --------------------------------------------------------------------
    # copy cexecuter folder
    # --------------------------------------------------------------------

    #		copyCexecuterFolder (langPathFileName, installPath)

    # --------------------------------------------------------------------
    # copy Macro folder
    # --------------------------------------------------------------------

    #		copyMacroFolder (langPathFileName, installPath)

    # --------------------------------------------------------------------
    # Create 02 export install folder
    # --------------------------------------------------------------------

    # dstPath = os.path.join(installPath, '02.' + ZZZ + '_export')
    # if not os.path.exists(dstPath):
    #	os.makedirs(dstPath)

    # --------------------------------------------------------------------
    # Create 01 install folder
    # --------------------------------------------------------------------

    # dstPath = os.path.join(installPath, '01.' + ZZZ)
    # if not os.path.exists(dstPath):
    #	os.makedirs(dstPath)

    # --------------------------------------------------------------------
    # copy 7z Files
    # --------------------------------------------------------------------

    #		copy7zFiles (langPathFileName, installPath)

    # --------------------------------------------------------------------
    #
    # --------------------------------------------------------------------

    # --------------------------------------------------------------------
    #
    # --------------------------------------------------------------------

    ##-------------------------------------------------------------------------------
    ## writes file with matching translations
    # Old: safeToFile'
    def mergedToFile(self, newFileName="", isCreateTempFile=True,
                   isDoBackup=True):  # ToDo: enum overwrite/createtempfile/backup ... isOverwrite=False,
        print('    >>> Enter mergedToFile: ')
        #        print('       isOverwrite: "' + str(isOverwrite) + '"')
        print('       isCreateTempFile: "' + str(isCreateTempFile) + '"')
        print('       isDoBackup: "' + str(isDoBackup) + '"')

        isSaved = False

        try:

            dstName = self.langPathFileName

            # New name given
            if (len(newFileName) > 0):
                self.langPathFileName = newFileName

            # remove extension
            dstBaseName = os.path.splitext(self.langPathFileName)[0]
            if (isCreateTempFile):
                dstName = dstBaseName + '.tmp'
            if (isDoBackup):
                bckName = dstBaseName + '.bak'
                shutil.copy2(self.langPathFileName, bckName)

            print('writing to: "' + self.langPathFileName)

            newLines = self.mergedTranlationLines()

            file = open(self.langPathFileName, "w")
            for line in newLines:
                file.write(line + '\r')
            file.close()

            isSaved = True

        except Exception as ex:
            print(ex)

        print('    <<< Exit mergedToFile: ' + str(isSaved))
        return isSaved

    # -------------------------------------------------------------------------------
    #
    # ToDo: mark each translation and later check and add unused translations
    # ToDo: leave out doubles, keep COM_RSGALLERY2_ (last char)
    def mergedTranlationLines(self):
        print('    >>> Enter mergedTranlationLines: ')
        #    	print ('       XXX: "' + XXX + '"')

        mergedLines = []

        try:
            print('file lines: ' + str(len(self._fileLines)))
            print('file translations: ' + str(len(self._translations)))

            idx = 0
            # check each line for existing translation
            for line in self._fileLines:
                idx += 1

                # comments
                if (line.startswith(';')):
                    mergedLines.append(line)
                    continue

                # empty lines
                if (len(line) < 1):
                    mergedLines.append(line)
                    continue

                # print("Line:" + line)

                # --- translation split -----------------------

                [pName, pTranslation] = line.split('=', maxsplit=1)
                transId = pName.strip()
                translationParanthesis = pTranslation.strip()

                oldTtranslation = translationParanthesis [1:-1]

                # translation is deleted
                if (transId not in self._translations):
                    # mergedLines.append(line)
                    continue

                newTranslation = self._translations[transId]
                newLine = transId + ' = "' + newTranslation + '"'

                mergedLines.append(newLine)

        except Exception as ex:
            print(ex)

        #        print('    <<< Exit mergedTranlationLines: ' + str(mergedLines.count()))
        print('    <<< Exit mergedTranlationLines: ' + str(len(mergedLines)))
        return mergedLines

    ##-------------------------------------------------------------------------------
    ## writes file with collected translations

    def translationsToFile(self, newFileName="", isCreateTempFile=True,
                   isDoBackup=True):  # ToDo: enum overwrite/createtempfile/backup ... isOverwrite=False,
        print('    >>> Enter mergedToFile: ')
        #        print('       isOverwrite: "' + str(isOverwrite) + '"')
        print('       isCreateTempFile: "' + str(isCreateTempFile) + '"')
        print('       isDoBackup: "' + str(isDoBackup) + '"')

        isSaved = False

        try:

            dstName = self.langPathFileName

            # New name given
            if (len(newFileName) > 0):
                self.langPathFileName = newFileName

            # remove extension
            dstBaseName = os.path.splitext(self.langPathFileName)[0]
            if (isCreateTempFile):
                dstName = dstBaseName + '.tmp'
            if (isDoBackup):
                bckName = dstBaseName + '.bak'
                shutil.copy2(self.langPathFileName, bckName)

            print('writing to: "' + self.langPathFileName)

            newLines = self.collectedTranlationLines()

            file = open(self.langPathFileName, "w")
            for line in newLines:
                file.write(line + '\r')
            file.close()

            isSaved = True

        except Exception as ex:
            print(ex)

        print('    <<< Exit mergedToFile: ' + str(isSaved))
        return isSaved

    # -------------------------------------------------------------------------------
    #
    # ToDo: mark each translation and later check and add unused translations
    # ToDo: leave out doubles, keep COM_RSGALLERY2_ (last char)
    def collectedTranlationLines(self):
        print('    >>> Enter collectedTranlationLines: ')
        #    	print ('       XXX: "' + XXX + '"')

        collectedLines = []

        try:
            print('file lines: ' + str(len(self._fileLines)))
            print('file translations: ' + str(len(self._translations)))

            idx = 0
            # check each line for existing translation
            for transId, translation in self._translations.items():
                idx += 1

                line = transId  + '="' + translation + '"' # + '"\r'

                collectedLines.append(line)

        except Exception as ex:
            print(ex)

        #        print('    <<< Exit collectedTranlationLines: ' + str(collectedLines.count()))
        print('    <<< Exit collectedTranlationLines: ' + str(len(collectedLines)))
        return collectedLines


##-------------------------------------------------------------------------------
##
# def yyy (XXX):
#	print ('    >>> Enter yyy: ')
#	print ('       XXX: "' + XXX + '"')
#
#	ZZZ = ""
#
#	try:
#
#
#	except Exception as ex:
#		print(ex)
#
#	print ('    <<< Exit yyy: ' + ZZZ)
#	return ZZZ

##-------------------------------------------------------------------------------
##
# def yyy (XXX):
#	print ('    >>> Enter yyy: ')
#	print ('       XXX: "' + XXX + '"')
#
#	ZZZ = ""
#
#	try:
#
#
#	except Exception as ex:
#		print(ex)
#
#	print ('    <<< Exit yyy: ' + ZZZ)
#	return ZZZ

##-------------------------------------------------------------------------------


def dummyFunction():
    print('    >>> Enter dummyFunction: ')


# print ('       XXX: "' + XXX + '"')

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
    optlist, args = getopt.getopt(sys.argv[1:], 'f:12345h')

    langPathFileName = ''
    langPathFileName = '../RSGallery2_J-4/administrator/components/com_rsgallery2/language/en-GB/en-GB.com_rsgallery2.ini'

    for i, j in optlist:
        if i == "-f":
            langPathFileName = j

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

    # init class
    LangFile = jLangFile(langPathFileName)
    LangFile.mergedToFile("", True)
    print_end(start)
