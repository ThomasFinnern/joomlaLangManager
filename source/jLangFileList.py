#!/usr/bin/python

# import os

from datetime import datetime

HELP_MSG = """

The class contains a list of filenames in given folder.

It enables to check if a filename exist even if it 
has a language ID like de-De in front or missing

Over the list can be iterated outside

------------------------------------
ToDo:
  *      
  * 
"""

# -------------------------------------------------------------------------------

# ================================================================================
# LangFile
# ================================================================================


class jLangFileList:
    """ Contains an translation item with references to empty lines and comments """

#    def __init__(self, translation, preLines, folderName):
#        self.__translation =  translation #
#        self.__preLines = preLines  # empty lines and comment before to item line
#        self.__folderName = folderName  # comments behind translation item

    def __init__(self):
        self.__langId =  ""    # de-DE 
        self.__fileNames = []  # empty lines and comments before item line
        self.__folderName = ""  # 

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

