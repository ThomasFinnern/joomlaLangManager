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
    """ config read from file. First segment in file defines the used segment with configuration items """

    def __init__(self, configPathFileName=''):

        self.__configPathFileName  = './LangManager.ini'
        if (len(configPathFileName) > 0):
            self.__configPathFileName = configPathFileName

        self.__isWriteEmptyTranslations = False
        self.__isOverwriteSrcFiles = False
        self.__baseSrcPath = ""
        self.__baseTrgPath = ""

        self.__allComparisionPaths = {}

        # ---------------------------------------------
        # assign variables from config file
        # ---------------------------------------------

        self.readConfigFile (self.__configPathFileName)

    # --- isWriteEmptyTranslations ---

    @property
    def isWriteEmptyTranslations(self):
        return self.__isWriteEmptyTranslations

    @isWriteEmptyTranslations.setter
    def isWriteEmptyTranslations(self, isWriteEmptyTranslations):
        self.__isWriteEmptyTranslations = isWriteEmptyTranslations

    # --- isOverwriteSrcFiles ---

    @property
    def isOverwriteSrcFiles(self):
        return self.__isOverwriteSrcFiles

    @isOverwriteSrcFiles.setter
    def isOverwriteSrcFiles(self, isOverwriteSrcFiles):
        self.__isOverwriteSrcFiles = isOverwriteSrcFiles

    # --- baseSrcPath ---

    @property
    def baseSrcPath(self):
        return self.__baseSrcPath

    @baseSrcPath.setter
    def baseSrcPath(self, baseSrcPath):
        self.__baseSrcPath = baseSrcPath

    # --- baseTrgPath ---

    @property
    def baseTrgPath(self):
        return self.__baseTrgPath

    @baseTrgPath.setter
    def baseTrgPath(self, baseTrgPath):
        self.__baseTrgPath = baseTrgPath

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

            configFile = configparser.ConfigParser()
            configFile.read(iniFileName)

            sourcePath = configFile['selection']['sourcePath']
            task = configFile['selection']['task']

            self.__isWriteEmptyTranslations = configFile.getboolean(task, 'isWriteEmptyTranslations', fallback=False)
            print('__isWriteEmptyTranslations: ', str(self.__isWriteEmptyTranslations))

            self.__isOverwriteSrcFiles = configFile.getboolean(sourcePath, 'isOverwriteSrcFiles', fallback=False)
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
