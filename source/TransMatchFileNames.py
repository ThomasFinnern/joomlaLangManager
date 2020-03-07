#!/usr/bin/python

import os
# import re
import getopt
import sys
import io
import shutil

from datetime import datetime
from jLangFilesList import jLangFilesList

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
        
        self.__matches = {}  #
        self.__missingFiles = []  #
        self.__obsoleteFiles = []  #

        self.collectFileNames ()
        self.matchFileNames ()

        self.check4obsoletfiles()
    
    
    #--- source path ---
    
    @property
    def srcPath(self):
        return self.__srcPath

    @srcPath.setter
    def langId(self, srcPath):
        self.__srcPath = srcPath

    #--- source lang id ---
    
    @property
    def srcLangId(self):
        return self.__srcLangId

    @srcLangId.setter
    def langId(self, srcLangId):
        self.__srcLangId = srcLangId


    #--- target path ---
    
    @property
    def trgPath(self):
        return self.__trgPath

    @trgPath.setter
    def langId(self, trgPath):
        self.__trgPath = trgPath

    # --- target lang id ---

    @property
    def trgLangId(self):
        return self.__trgLangId

    @trgLangId.setter
    def langId(self, trgLangId):
        self.__trgLangId = trgLangId
        
    # --- matching files ---

    @property
    def matches(self):
        return self.__matches

    @matches.setter
    def langId(self, matches):
        self.__matches = matches

    # --- missing files  ---

    @property
    def missingFiles(self):
        return self.__missingFiles

    @missingFiles.setter
    def langId(self, missingFiles):
        self.__missingFiles = missingFiles

    # --- obsolete files ---

    @property
    def obsoleteFiles(self):
        return self.__obsoleteFiles

    @obsoleteFiles.setter
    def langId(self, obsoleteFiles):
        self.__obsoleteFiles = obsoleteFiles

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


            if not testDir(self.srcPath):
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

            self.__srcFiles = jLangFilesList (self.srcPath, self.srcLangId)
            self.__trgFiles = jLangFilesList (self.trgPath, self.trgLangId)

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

            self.__matches = {}  #

            for srcFile in self.__srcFiles.fileNames:
                # matching translation file . May have
                # different langIds or missing lang Ids
                matchFile = self.__trgFiles.matchFileName (srcFile, self.__srcLangId);

                if (len(matchFile) > 0):
                    srcFilePath = os.path.join (self.__srcPath, srcFile)
                    trgFilePath = os.path.join (self.__trgPath, matchFile)

                    self.__matches [srcFilePath] = trgFilePath #
                else:
                    self.__missingFiles.append(srcFile)

        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit matchFileName: "' + str(len(self.__matches)) +'"')

        # toDo: print len lists
        return




    # ... lang file name :
    #   a) exact filename exists
    #   b) check if landId.filename exist
    #   c) a/b with input lang name without own lang id

    def check4obsoletfiles (self):
        
        try:

            self.__obsoleteFiles = []  #

            for trgFile in self.__trgFiles.fileNames:
                # matching translation file . May have
                # different langIds or missing lang Ids
                matchFile = self.__srcFiles.matchFileName (trgFile, self.__trgLangId);

                if (not len(matchFile) > 0):
                    self.__obsoleteFiles.append(trgFile)

        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit matchFileName: "' + str(len(self.__matches)) +'"')

        # toDo: print len lists
        return

    def toStringMatches(self):
    
        outTxt = 'matches: ' + str(len(self.__matches)) + '\n'
    
        for srcFile, trgfile in self.__matches.items():
            outTxt += '  "' + srcFile + '" <=> "' + trgfile + '"' + '\n'
    
        return outTxt

    def toStringMissing(self):
    
        outTxt = 'missing: ' + str(len(self.__missingFiles)) + '\n'
    
        for missingFile in self.__missingFiles:
            outTxt += '  "' + missingFile + '"' + '\n'
    
        return outTxt

    def toStringObsolete(self):
    
        outTxt = 'obsolete: ' + str(len(self.__obsoleteFiles)) + '\n'
    
        for obsoleteFile in self.__obsoleteFiles:
            outTxt += '  "' + obsoleteFile + '"' + '\n'
    
        return outTxt

    def toStringMatches(self):
    
        outTxt = 'matches: ' + str(len(self.__matches)) + '\n'
    
        for srcFile, trgfile in self.__matches.items():
            outTxt += '  "' + srcFile + '" <=> "' + trgfile + '"' + '\n'

        return outTxt

    # toDo use strings ;-)
    def toString(self):

        outTxt = "--- TransMatchFileNames: ---------------" + '\n'

        outTxt += "srcPath: " + self.__srcPath + '\n'
        outTxt += "srcLangId: " + self.__srcLangId + '\n'
        outTxt += "trgPath: " + self.__trgPath + '\n'
        outTxt += "trgLangId: " + self.__trgLangId + '\n'

        outTxt += '\n'
        outTxt += self.toStringMatches()
        
        outTxt += '\n'
        outTxt += self.toStringMissing()
        
        outTxt += '\n'
        outTxt += self.toStringObsolete()

        outTxt += "---------------------------------------"
        
        return  outTxt

    def writeLogFile (self, logPathFileName, doAppend=False):
    
        # mode = doAppend ? "o" : "w"
        if (doAppend):
            mode =  "o"
        else:
            mode = "w"
        
        logTxt = self.toString()
        
        with open(logPathFileName, mode) as logFile:
            logFile.write(logTxt)
    
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

    #srcPath = os.path.join ('..', '.regression', 'en-GB')
    srcPath = os.path.join ('..', '.sandbox', 'en-GB')
    srcLangId = 'en-GB'
    #trgPath = os.path.join ('..', '.regression', 'de-DE')
    trgPath = os.path.join ('..', '.sandbox', 'de-DE')
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
    FileList = TransMatchFileNames(srcPath, srcLangId, trgPath, trgLangId)

    # does print all
    print (FileList.toString())

    FileList.writeLogFile ('.\logTransMatch.txt', True)
    
    print_end(start)