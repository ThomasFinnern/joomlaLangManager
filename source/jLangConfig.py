#!/usr/bin/python

import configparser

HELP_MSG = """
Reads config from external file LangManager.ini
The segment selection tells which segment(s) to use for configuration
"""

# ================================================================================
# config
# ================================================================================

class jLangConfig:
    """  """

    def __init__(self, configPathFileName=''):

        self.__configPathFileName  = './LangManager.ini'
        if (len(configPathFileName) > 0):
            self.__configPathFileName = configPathFileName  # CVS modules file name with path

        self.__isWriteEmptyTranslations = False
        self.__isOverwriteSrcFiles = False
        self.__baseSrcPath = ""
        self.__baseTrgPath = ""

        self.__allComparisionPaths = {}

        # ---------------------------------------------
        # assign variables from config file
        # ---------------------------------------------

        self.readConfigFile (self.__configPathFileName)

    # --------------------------------------------------------------------
    #
    # --------------------------------------------------------------------
    # https://wiki.python.org/moin/ConfigParserExamples

    def readConfigFile (self, iniFileName):
        # ToDo: Check if name exists otherwise standard
        # ToDo: try catch ...
        try:
            print('*********************************************************')
            print('readConfigFile')
            print('iniFileName: ' + iniFileName)
            print('---------------------------------------------------------')

            configFile = configparser.ConfigParser(iniFileName)
            configFile.read()

            sourcePath = configFile['selection']['sourcePath']
            task = configFile['selection']['task']

            self.__isWriteEmptyTranslations = configFile.getboolean(task, 'isWriteEmptyTranslations', False)
            print('__isWriteEmptyTranslations: ', str(self.__isWriteEmptyTranslations))

            self.__isOverwriteSrcFiles = configFile.getboolean(sourcePath, 'isOverwriteSrcFiles', False)
            print('__isOverwriteSrcFiles: ', str(self.__isOverwriteSrcFiles))

            self.__baseSrcPath = configFile.get (sourcePath, 'sourceFolder')
            print('__baseSrcPath: ', str(self.__baseSrcPath))

            self.__baseTrgPath = configFile.get (sourcePath, 'targetFolder')
            print('__baseTrgPath: ', str(self.__baseTrgPath))

            #--- folder list ---------------------------------

            self.__allComparisionPaths = {}

            if (sourcePath == 'jgerman_wip_all'):

                options = configFile.options(sourcePath)
                for option in options:
                    try:
                        if ('sourceFolder' in option):
                            sourceFolder = configFile.get(sourcePath, option)
                        if ('targetFolder' in option):
                            targetFolder = configFile.get(sourcePath, option)
                            self.__allComparisionPaths[sourceFolder] = targetFolder
                            print('All: sourcePath: ' + sourceFolder + ' targetPath: ' + targetFolder)

                    except:
                        print("exception on %s!" % option)

            else:
                # standard
                self.__allComparisionPaths [self.__baseSrcPath] = self.__baseTrgPath
                print('All: sourcPath: ' + self.__baseSrcPath + ' targetPath: ' + self.__baseTrgPath)

        except Exception as ex:
            print(ex)

        # --------------------------------------------------------------------
        #
        # --------------------------------------------------------------------

        finally:
            print('exit readConfigFile')

        return

Config = jLangConfig()