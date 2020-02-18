#!/usr/bin/python

import os
# import re
import getopt
import sys
import io
import shutil

from datetime import datetime

HELP_MSG = """
The class contains translation ids of a joomla component/module/plugin
It is normally initialised b an other script.
It may read/write to/fromm file though

usage: TranslationIds.py -f <path file name> nnn -? xxxx -? yyyy  [-h]
	-f path to translation IDs file (normally not used) 
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
# TranslationIds
# ================================================================================

class TranslationIds:
    """  """

    def __init__(self):
        self.translationRefPathFileName = ""  # resulting file not needed

        self._TranslationReferences = {}  # All translation IDs with list of occurrences in file


    # ================================================================================
    #
    # ================================================================================

    # -------------------------------------------------------------------------------

    def addItem(self, TranslationId, FileName, LineNumber):
        try:
            print('*********************************************************')
            print('TranslationIds')
            print('TranslationId: ' + TranslationId)
            print('FileName: ' + FileName)
            print('LineNumber: ' + str(LineNumber))
            print('---------------------------------------------------------')

            # ---------------------------------------------
            # check input
            # ---------------------------------------------

            if TranslationId == '':
                print('***************************************************')
                print('!!! TranslationId is mandatory !!!')
                print('***************************************************')
                print(HELP_MSG)
                Wait4Key()
                sys.exit(1)

            # ToDO: Check starts with prefix -> add prefix code
            if not TranslationId.startswith('COM_RSGALLERY2'):
                print('***************************************************')
                print('!!! TranslationId must match prefix !!!')
                print('***************************************************')
                #print(HELP_MSG)
                #Wait4Key()
                #sys.exit(1)

            if LineNumber == '':
                print('***************************************************')
                print('!!! LineNumber is mandatory !!!')
                print('***************************************************')
                #print(HELP_MSG)
                #Wait4Key()
                #sys.exit(1)
                return

            # --------------------------------------------------------------------
            # create object
            # --------------------------------------------------------------------

            origin = {}

            origin ['FileName'] = FileName
            origin ['LineNumber'] = LineNumber

            # --------------------------------------------------------------------
            # TranslationId, [origins]
            # --------------------------------------------------------------------

            # new: create reference
            if (not TranslationId in self._TranslationReferences):
                self._TranslationReferences [TranslationId] = []

            # append origin to reference
            self._TranslationReferences[TranslationId].append (origin)


        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit addItem')

        return

    # -------------------------------------------------------------------------------

    def translationRefs(self):
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
        return self._TranslationReferences

    def translationIds(self):
        print ('    >>> Enter translationIds: ')

        _translationIds = []

        try:
            #
            for translationId, _translationRef in self._TranslationReferences:
                _translationIds.append(translationId)

        except Exception as ex:
            print(ex)

        print ('    <<< Exit translationIds: ' + str(len(_translationIds)))

        return _translationIds

    # -------------------------------------------------------------------------------
    #
    def get(self, translationId):
        print('    >>> Enter get: ')
        print('       translationId: "' + translationId + '"')

        _translationId = ""

        try:
            _translationId = self._translations[translationId]

        except Exception as ex:
            print(ex)

        print('    <<< Exit get: ' + translationId)
        return translationId

    # -------------------------------------------------------------------------------
    #
    def origins (self, translationId):
        print('    >>> Enter get: ')
        print('       translationId: "' + translationId + '"')

        _origins = []

        try:
            _origins = self._translations[translationId]

        except Exception as ex:
            print(ex)

        print('    <<< Exit origins: ' + translationId + ': ' + str(len(_origins)))
        return _origins


    ##-------------------------------------------------------------------------------
    ## writes file with matching translations

    def safeToFile(self, newFileName=""):
        print('    >>> Enter safeToFile: ')
        isSaved = False

        try:

            dstName = self.translationRefPathFileName

            # New name given
            if (len(newFileName) > 0):
                dstName = newFileName
                self.translationRefPathFileName = newFileName

            print('writing to: "' + dstName)

            file = open(dstName, "w")

            #
            #for translationId, _translationRef in self._TranslationReferences:
            for translationId in self._TranslationReferences.keys():

                _origins = self._TranslationReferences[translationId]

                _origin = _origins[0]

                _origin_0 = _origin['FileName']
                _origin_1 = _origin['LineNumber']

                line = translationId.ljust(20) + " " + _origin['FileName'] + " " + str(_origin['LineNumber'])
                file.write(line + '\r')

                if (len(_origins) > 1):
                    for _origin in _origins:
                        line = " ".ljust(20) + " " + _origin['FileName'] + " " + str(_origin['LineNumber'])
                        file.write(line + '\r')

                file.write('\r')
            file.close()

            isSaved = True

        except Exception as ex:
            print(ex)

        print('    <<< Exit safeToFile: ' + str(isSaved))
        return isSaved



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
    TranslationIds = TranslationIds(langPathFileName)
    TranslationIds.safeToFile("", True)
    print_end(start)
