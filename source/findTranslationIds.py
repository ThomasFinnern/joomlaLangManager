#!/usr/bin/python

import os
# import re
import getopt
import sys

from datetime import datetime

from jLangFile import *

HELP_MSG = """
findTranslationIds 
	* Find all references of project translation ids in given project folders
	* (ToDo: Add these findings to existing translation files as empty strings)    
	   New lines will look like //COM_RSGALLERY2_<FOUND_TEXT_ID> =""//
	* (ToDo: Search for not id'd strings like "some Text2 which have no reference)
 

usage: findTranslationIds.py -? nnn -? xxxx -? yyyy  [-h] [list of paths for search, ,,, ]
	-s Source language file  
	-f Standard language file
	-y System language file

	[list of paths for search]    
	-? 

 	-c  Component name prefix  
	
	-h shows this message
	
	-1 
	-2 
	-3 
	-4 
	-5 
	
	
	example:
	
	
------------------------------------
ToDo:
ToDo:
  * 
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
# findTranslationIds
# ================================================================================

def findTranslationIds(SourceFile, StandardFile, SysFile):
    try:
        print('*********************************************************')
        print('findTranslationIds')
        print('SourceFile: ' + SourceFile)
        print('StandardFile: ' + StandardFile)
        print('SysFile: ' + SysFile)
        print('---------------------------------------------------------')

        # ---------------------------------------------
        # check input
        # ---------------------------------------------

        if SourceFile == '':
            print('***************************************************')
            print('!!! Source file (SourceFile) name is mandatory !!!')
            print('***************************************************')
            print(HELP_MSG)
            Wait4Key()
            sys.exit(1)

        if not testFile(SourceFile):
            print('***************************************************')
            print('!!! Source file (LeftPath) path not found !!! ? -l ' + SourceFile + ' ?')
            print('***************************************************')
            print(HELP_MSG)
            Wait4Key()
            sys.exit(2)

        # --------------------------------------------------------------------

        if StandardFile == '':
            print('***************************************************')
            print('!!! Source file (StandardFile) name is mandatory !!!')
            print('***************************************************')
            print(HELP_MSG)
            Wait4Key()
            sys.exit(3)

        if not testFile(StandardFile):
            print('***************************************************')
            print('!!! Source file (StandardFile) path not found !!! ? -l ' + StandardFile + ' ?')
            print('***************************************************')
            print(HELP_MSG)
            #			Wait4Key()
            sys.exit(4)

        # --------------------------------------------------------------------

        if SysFile == '':
            print('***************************************************')
            print('!!! Destination file (RightPath) name is mandatory !!!')
            print('***************************************************')
            print(HELP_MSG)
            Wait4Key()
            sys.exit(5)

        if not testFile(SysFile):
            print('***************************************************')
            print('!!! Destination file (RightPath) path not found !!! ? -r ' + SysFile + ' ?')
            print('***************************************************')
            print(HELP_MSG)
            Wait4Key()
            sys.exit(6)

        # --------------------------------------------------------------------
        # read all files
        # --------------------------------------------------------------------

        master = jLangFile(SourceFile)
        standard = jLangFile(StandardFile)
        system = jLangFile(SysFile)

        # print ('LeftPath: ' + LeftPath)
        # print ('RightPath: ' + RightPath)
        # print ('---------------------------------------------------------')

        # --------------------------------------------------------------------
        # import translations into standard
        # --------------------------------------------------------------------

        translations = standard.translations()

        isChanged = False

        # check all translations
        for transId, translation in translations.items():
            # translation not defined
            if not translation:
                # check source
                srcTranslation = master.get(transId)

                # master translation existing <ß
                if (srcTranslation):
                    standard.set(transId, srcTranslation)

                    isChanged = True

        if (isChanged):
            standard.safeToFile()

        # --------------------------------------------------------------------
        # import translations into sys file
        # --------------------------------------------------------------------

        translations = system.translations()

        isChanged = False

        # check all translations
        for transId, translation in translations.items():
            # translation not defined
            if not translation:
                # check source
                srcTranslation = master.get(transId)

                # master translation existing <ß
                if (srcTranslation):
                    system.set(transId, srcTranslation)

                    isChanged = True

        if (isChanged):
            system.safeToFile()

    except Exception as ex:
        print(ex)

    # --------------------------------------------------------------------
    #
    # --------------------------------------------------------------------

    finally:
        print('exit findTranslationIds')

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

    #	SourceFile = ''
    #	StandardFile = ''
    #	SysFile = ''
    ComponentPrefix = "COM_RSGALLERY2"
    StandardFile = '../RSGallery2_J-4/administrator/components/com_rsgallery2/language/en-GB/en-GB.com_rsgallery2.ini'
    SysFile = '../RSGallery2_J-4/administrator/components/com_rsgallery2/language/en-GB/en-GB.com_rsgallery2.sys.ini'

    for i, j in optlist:
        if i == "-c":
            ComponentPrefix = j
        if i == "-f":
            StandardFile = j
        if i == "-y":
            SysFile = j

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

    # iterate over args and create a path list        

    # dummy test constant
    searchPaths = [
        "f:\Entwickl\rsgallery2\RSGallery2_J-4\administrator\components\com_rsgallery2",
        "f:\Entwickl\rsgallery2\RSGallery2_J-4\administrator\components\com_rsgallery2\language\en-GB\en-GB.com_rsgallery2.ini",
        "f:\Entwickl\rsgallery2\RSGallery2_J-4\components\com_rsgallery2"
    ]

    if (len(args)):
        searchPaths = []

    for searchPath in args:
        searchPaths.append(searchPath)

start = datetime.today()

print_header(start)

findTranslationIds(ComponentPrefix, StandardFile, SysFile)

print_end(start)
