#!/usr/bin/python

import os
import io
import re
import getopt
import sys

from datetime import datetime

from jLangFile import *
from TranslationIds import TranslationIds

HELP_MSG = """
findTranslationIdsInPath 
	* Find all references of project translation ids in given project folders
	* (ToDo: Add these findings to existing translation files as empty strings)    
	   New lines will look like //COM_RSGALLERY2_<FOUND_TEXT_ID> =""//
	* (ToDo: Search for not id'd strings like "some Text2 which have no reference)
 

usage: findTranslationIdsInPath.py -? nnn -? xxxx -? yyyy  [-h] [list of paths for search, ,,, ]
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
  * Second/multiple use may be counted / displayed
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
# findTranslationIdsInPath
# ================================================================================

def findAllTranslationIds(componentPrefix, searchPaths, StandardFile, SysFile):
    try:
        print('*********************************************************')
        print('findAllTranslationIds')
        print('componentPrefix: ' + componentPrefix)

        print('searchPaths count: ' + str(len(searchPaths)))
        for idx, searchPath in enumerate(searchPaths):
            print('searchPath [' + str(idx) + ']: "' + searchPath + '"')

        print('StandardFile: ' + StandardFile)
        print('SysFile: ' + SysFile)
        print('---------------------------------------------------------')

        # ---------------------------------------------
        # check input
        # ---------------------------------------------

        if componentPrefix == '':
            print('***************************************************')
            print('!!! Component Prefix name is mandatory !!!')
            print('***************************************************')
            print(HELP_MSG)
            Wait4Key()
            sys.exit(1)

        if len(searchPaths) < 1:
            print('***************************************************')
            print('!!! Search paths not given !!!')
            print('***************************************************')
            print(HELP_MSG)
            Wait4Key()
            sys.exit(1)

        errFound = False
        for idx, searchPath in enumerate(searchPaths):

            if not testDir(searchPath):
                print('***************************************************')
                print('!!! Directory path does not exist for searchPath [' + str(idx) + ']: "' + searchPath + '"')
                print('***************************************************')
                errFound = True

        # Any directory not found
        if (errFound):
            sys.exit(1)

        # --------------------------------------------------------------------
        # lang files
        # --------------------------------------------------------------------

        #        master = jLangFile(SourceFile)
        #        standard = jLangFile(StandardFile)
        #        system = jLangFile(SysFile)

        # print ('LeftPath: ' + LeftPath)
        # print ('RightPath: ' + RightPath)
        # print ('---------------------------------------------------------')

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        translationIds = TranslationIds ()

        # check all translations
        for searchPath in searchPaths:
            findTranslationIdsInPath(searchPath, componentPrefix, translationIds)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        # save list
        translationIds.safeToFile(".\\foundTranslations.txt")


    except Exception as ex:
        print(ex)

    # --------------------------------------------------------------------
    #
    # --------------------------------------------------------------------

    finally:
        print('exit findAllTranslationIds')

    return


def findTranslationIdsInPath(searchPath, componentPrefix, translationIds):
    print('    >>> Enter findTranslationIdsInPath: ')
    print('       searchPath: "' + searchPath + '"')
    print('       translationIds: "' + str(len(translationIds.translationRefs())) + '"')

    try:
        # All files in folder
        for fileName in find_files(searchPath):
            findTranslationIdsInFile (fileName, componentPrefix, translationIds)

#        #Debug small number of translations
#        if(len(translationIds.translationRefs()) > 5):
#            return

        # All folders in folder
        for folderName in find_folders(searchPath):
            findTranslationIdsInPath(os.path.join(searchPath, folderName), componentPrefix, translationIds)

    except Exception as ex:
        print(ex)

    print('    <<< Exit findTranslationIdsInPath: ' + str(len(translationIds.translationRefs())))
    return

#-----------
def findTranslationIdsInFile(filePathName, componentPrefix, translationIds):
    print('    >>> Enter findTranslationIdsInFile: ')
    print('       filePathName: "' + filePathName + '"')
    print('       translationIds: "' + str(len(translationIds.translationRefs())) + '"')

    try:
        searchRegex = "\\b" + componentPrefix + "\\w+"

        # All lines
        lineIdx = 0
        with open(filePathName) as fin:
            for line in fin:
                lineIdx = lineIdx + 1

                # found start of translation prefix
                if (componentPrefix in line):

                    #findings = re.findall("\b\w+", line)

                    findings = re.findall(searchRegex, line)

                    for translationId in findings:
                        print(
                            "translationId: " + translationId
                            + " " + "line: " + str(lineIdx)
                            + " " + "file: " + filePathName
                            )

                        translationIds.addItem (translationId, filePathName, lineIdx)

    except Exception as ex:
        print(ex)

    print('    <<< Exit findTranslationIdsInFile: ' + str(len(translationIds.translationRefs())))
    return


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


#-------------------------------------------------------------------------------
# Small library
#-------------------------------------------------------------------------------

def find_files(nextDir):
    for item in os.listdir(nextDir):
        pathFileName = os.path.join (nextDir, item)
        if os.path.isfile(pathFileName):
            # yield file name
            yield pathFileName
        else:
            continue


def find_folders(nextDir):
    for item in os.listdir(nextDir):
        pathName = os.path.join (nextDir, item)
        if os.path.isfile(pathName):
            continue
        else:
            # yield folder name
            yield pathName


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
    componentPrefix = "COM_RSGALLERY2"
    StandardFile = '../RSGallery2_J-4/administrator/components/com_rsgallery2/language/en-GB/en-GB.com_rsgallery2.ini'
    SysFile = '../RSGallery2_J-4/administrator/components/com_rsgallery2/language/en-GB/en-GB.com_rsgallery2.sys.ini'

    for i, j in optlist:
        if i == "-c":
            componentPrefix = j
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
        "f:\\Entwickl\\rsgallery2\\RSGallery2_J-4\\administrator\\components\\com_rsgallery2",
        "f:\\Entwickl\\rsgallery2\\RSGallery2_J-4\\components\\com_rsgallery2",
        "f:\\Entwickl\\rsgallery2\\RSGallery2_J-4\\media\\com_rsgallery2",
    ]

    if (len(args)):
        searchPaths = []

    for searchPath in args:
        searchPaths.append(searchPath)

    start = datetime.today()

    print_header(start)

    findAllTranslationIds(componentPrefix, searchPaths, StandardFile, SysFile)

    print_end(start)
