#!/usr/bin/python

# import os

from datetime import datetime

HELP_MSG = """

The class contains one translated item (line) of a joomla language file
Empty lines and comments in previous lines (ToDo: and comments behind the translation ) 
are also assigned to the item    

------------------------------------
ToDo:
  * Add comments behind the translation. 
     Attention: Beginning of comment may be on wrong place -> '"' within translation and ... 
  * 
"""

# -------------------------------------------------------------------------------

# ================================================================================
# LangFile
# ================================================================================


class jLangItem:
    """ Contains an translation item with references to empty lines and comments """

#    def __init__(self, translation, preLines, commentsBehind):
#        self.__translationText =  translation #
#        self.__preLines = preLines  # empty lines and comment before to item line
#        self.__commentsBehind = commentsBehind  # comments behind translation item

    def __init__(self):
        self.__translationText =  ""    # item translation
        self.__preLines = []        # empty lines and comments before item line
        self.__commentsBehind = ""  # comments behind translation item
#        self.__translationId = ""
#        self.__lineIdx = ""
#        self.__isSame = False #Exat same text as original

# ToDo: LineId for error messages and other ...

    #--- translation ---
    
    @property
    def translationText(self):
        return self.__translationText

    @translationText.setter
    def translationText(self, translation):
        self.__translationText = translation

    #--- preLines ---
    
    @property
    def preLines(self):
        return self.__preLines

    @preLines.setter
    def preLines(self, preLines):
        self.__preLines = preLines

    #--- commentsBehind ---
    
    @property
    def commentsBehind(self):
        return self.__commentsBehind

    @commentsBehind.setter
    def translation(self, commentsBehind):
        self.__commentsBehind = commentsBehind

    def hasTranslation(self):
        bExist = True
        if (len(self.__translationText) < 1):
            bExist = True

        return bExist

    def hasTranslation(self):
        bExist = True
        if (len(self.__translationText) < 1):
            bExist = True

        return bExist

    def hasPreLines(self):
        bExist = True
        if (len(self.__preLines) < 1):
            bExist = True

        return bExist

    def hasCommentsBehind(self):
        bExist = True
        if (len(self.__commentsBehind) < 1):
            bExist = True

        return bExist

