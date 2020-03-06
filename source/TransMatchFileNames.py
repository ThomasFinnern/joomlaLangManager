#!/usr/bin/python

import os
# import re
import getopt
import sys
import io
import shutil

from datetime import datetime
from jLangFileList import jLangFileList

HELP_MSG = """

The class contains a list of filenames from two folders given
The user may iterate over matches to externally merge forn one translation to the other 

Therefore a funtion matches i
for each matched Filenames ...



superflous source and target files which have no partner may be queried too

?  

Over the list can be iterated outside

usage: TransMatchFileNames.py -s <path file name> nnn -? xxxx -? yyyy  [-h]
	-s path to source language file path 
	-t path to target language file path 
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
# LangFileList
# ================================================================================

class TransMatchFileNames:
    """ Contains an translation item with references to empty lines and comments """

#    def __init__(self, translation, preLines, folderName):
#        self.__translation =  translation #
#        self.__preLines = preLines  # empty lines and comment before to item line
#        self.__folderName = folderName  # comments behind translation item

    def __init__(self, srcPath, srcLangId, trgPath, trgLangId):
        self.__srcPath = srcPath
        self.__srcLangId = srcLangId
        self.__trgPath = trgPath
        self.__trgLangId = trgLangId

        self.__srcFiles = []  #
        self.__trgFiles = []  #

        self.__matches = []  #

        self.collectFileNames ()
        self.matchFileNames ()

    #--- interface ---
    
    @property
    def langId(self):
        return self.__langId

    @langId.setter
    def langId(self, langId):
        self.__langId = langId

    #--- fileNames ---
    
    @property
    def fileNames(self):
        return self.__fileNames

    @fileNames.setter
    def fileNames(self, fileNames):
        self.__fileNames = fileNames

    #--- folderName ---
    
    @property
    def folderName(self):
        return self.__folderName

    @folderName.setter
    def translation(self, folderName):
        self.__folderName = folderName

    # ================================================================================
    # collect *.ini filed from folder
    # ================================================================================

    def collectFileNames (self, srcPath="", srcLangId="", trgPath="", trgLangId=""):
    
        try:
            print('*********************************************************')
            print('collectFilenames')
            print('srcPath: ' + srcPath)
            print('srcLangId: ' + srcLangId)
            print('trgPath: ' + trgPath)
            print('trgLangId: ' + trgLangId)
            print('---------------------------------------------------------')

            # New name given
            if (len(srcPath) > 0):
                self.srcPath = srcPath

            # New name given
            if (len(srcLangId) > 0):
                self.__srcLangId = srcLangId

            # New name given
            if (len(trgPath) > 0):
                self.__trgPath = trgPath

            # New name given
            if (len(trgLangId) > 0):
                self.__trgLangId = trgLangId

            if not testDir(self.__folderName):
                print('***************************************************')
                print('!!! Folder path not found !!! ? -l ' + self.__folderName + ' ?')
                print('***************************************************')
                print(HELP_MSG)
                Wait4Key()
                sys.exit(2)

            self.__srcFiles = jLangFileList (srcPath, srcLangId)
            self.__trgFiles = jLangFileList (trgPath, trgLangId)

        # toDo: len lists
        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit collectFileNames')

        # toDo: print len lists

        return

    # ================================================================================
    # match file name
    # ================================================================================

    # in ..\en-GB\en-GB.lib_joomla.ini -> ..\de-DE\de-DE.lib_joomla.ini
    # in \en-GB\lib_joomla.ini -> ..\de-DE\lib_joomla.ini
    # in \en-GB\en-GB.lib_joomla.ini -> ..\de-DE\de-DE.lib_joomla.ini
    # in \en-GB\en-GB.lib_joomla.ini -> ..\de-DE\lib_joomla.ini
    # in \en-GB\lib_joomla.ini -> ..\de-DE\de-DE.lib_joomla.ini

    # Search for a compatible file name in found file list
    # Path to files are not given on both sides
    def matchFileNames(self):

        # toDo: print len lists

        try:

            self.__matches = []  #

            for srcFile in self.__srcFiles.fileNames:
                # matching translation file . May have
                # different langIds or missing lang Ids
                matchFile = self.__trgFiles.match (srcFile);

                if (len(matchFile) > 0):
                    srcFilePath = os.path.join (self.__srcPath, srcFile)
                    trgFilePath = os.path.join (self.__trgPath, matchFile)

                    self.__matches [srcFilePath] = trgFilePath #


        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit matchFileName: "' + len(self.__matches) +'"')

        # toDo: print len lists
        return

    # ... lang file name :
    #   a) exact filename exists
    #   b) check if landId.filename exist
    #   c) a/b with input lang name without own lang id

    def hasFile(self, FileName):
        bExist = True
        if (len(self.__translation) < 1):
            bExist = True

        return bExist

    def hasLangFile(self):
        bExist = True
        if (len(self.__translation) < 1):
            bExist = True

        return bExist

    def hasPreLines(self):
        bExist = True
        if (len(self.__preLines) < 1):
            bExist = True

        return bExist

    def hasfolderName(self):
        bExist = True
        if (len(self.__folderName) < 1):
            bExist = True

        return bExist

    def toString(self):

        print ("--- LangfileList: ---------------")

        print ("folderName: " + self.__folderName)
        print ("langId: " + self.__langId)

        for actFile in self.__fileNames:
            print ("File: " + actFile)

        print ("---------------------------------")

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
    optlist, args = getopt.getopt(sys.argv[1:], 's:t:a:b:12345h')

    srcPath = os.path.join ('..', '.regression', 'en-GB')
    srcLangId = 'en-GB'
    trgPath = os.path.join ('..', '.regression', 'de-DE')
    trgLangId = 'de-DE'

    for i, j in optlist:
        if i == "-s":
            srcPath = j
        if i == "-t":
            srcLangId = j
        if i == "-a":
            trgPath = j
        if i == "-b":
            trgLangId = j

        if i == "-i":
            langId = j

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

#f:\Entwickl\rsgallery2\joomlaLangManager\.regression\de-DE\

    # init class
    FileList = TransMatchFileNames(langPath, 'de_DE')

    FileList.toString ()

#    LangFile.mergedToFile("", True)

#   LangFile.Write (bak?)
#    FileList.translationsToFile (langPathFileName + '.new', False, False)
    
    print_end(start)