#!/usr/bin/python

import os
# import re
import getopt
import sys
import io
import shutil

from datetime import datetime

HELP_MSG = """

The class contains a list of filenames in given folder.

It enables to check if a filename exist even if it 
has a language ID like de-De in front or missing

Over the list can be iterated outside

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

class jLangFileList:
    """ Contains an translation item with references to empty lines and comments """

#    def __init__(self, translation, preLines, folderName):
#        self.__translation =  translation #
#        self.__preLines = preLines  # empty lines and comment before to item line
#        self.__folderName = folderName  # comments behind translation item

    def __init__(self, folderName, langId):
        self.__folderName = folderName  #
        self.__langId = langId    # de-DE

        self.__fileNames = []  # List of files without path to file

        self.collectFileNames ()
        
    #--- translation ---
    
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

    def collectFileNames (self, newFolderName=""):
    
        try:
            print('*********************************************************')
            print('collectFilenames')
            print('newFolderName: ' + newFolderName)
            print('---------------------------------------------------------')

            # New name given
            if (len(newFolderName) > 0):
                self.__folderName = newFolderName

            if not testDir(self.__folderName):
                print('***************************************************')
                print('!!! Folder path not found !!! ? -l ' + self.__folderName + ' ?')
                print('***************************************************')
                print(HELP_MSG)
                Wait4Key()
                sys.exit(2)


            # --------------------------------------------------------------------
            # All files in source
            # --------------------------------------------------------------------

            actFolderName = self.__folderName
            allFiles = [f for f in os.listdir(actFolderName) if os.path.isfile(os.path.join(actFolderName, f))]
    
            for actFile in allFiles:
                # ends with .ini
                if (actFile.endswith('.ini')):
                    self.__fileNames.append(os.path.join(actFolderName, actFile))
                    print('sourceFile: ' + actFile)


        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit assignFileContent')

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
    def matchFileName(self, sourceFileName="", srcLangId = ""):

        try:
            scrStartId = srcLangId + '.'
            trgStartId = self.__langId + '.'

            #--- prepare comparison name --------------------------
            
            hasLangId = False

            shortCompareName = sourceFileName
            if (sourceFileName.startswith(scrStartId)):
                shortCompareName = shortCompareName.replace (scrStartId, '')
                
            #--- compare short -----------------------------------
            
            matched = ''
            
            #
            if (shortCompareName in self.__fileNames):
                matched = shortCompareName
            else:
                longCompareName = trgStartId + shortCompareName
                if (shortCompareName in self.__fileNames):
                    matched = shortCompareName

        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit matchFileName: "' + matched +'"')

        return matched

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
    optlist, args = getopt.getopt(sys.argv[1:], 'p:12345h')

    langPath = os.path.join ('..', '.regression', 'de-DE')
    langId = 'de-DE'

    for i, j in optlist:
        if i == "-p":
            langPath = j

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
    FileList = jLangFileList(langPath, 'de_DE')

    FileList.toString ()

#    LangFile.mergedToFile("", True)

#   LangFile.Write (bak?)
#    FileList.translationsToFile (langPathFileName + '.new', False, False)
    
    print_end(start)