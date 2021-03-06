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
        self.__isDoBackup = False

        self.__baseSrcPath = ""
        self.__baseTrgPath = ""

        self.__comparePaths = {} # compare multiple paths

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

    # --- isDoBackup ---

    @property
    def isDoBackup(self):
        return self.__isDoBackup

    @isDoBackup.setter
    def isDoBackup(self, isDoBackup):
        self.__isDoBackup = isDoBackup

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

    # --- comparePaths ---

    @property
    def comparePaths(self):
        return self.__comparePaths

    @comparePaths.setter
    def comparePaths(self, comparePaths):
        self.__comparePaths = comparePaths

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

            #--- define used segments -------------------------------

            configFile = configparser.ConfigParser()
            configFile.read(iniFileName)

            sourcePath = configFile['selection']['sourcePath']
            task = configFile['selection']['task']

            #--- in selected segments ----------------------------------------------

            self.__isWriteEmptyTranslations = configFile.getboolean(task, 'isWriteEmptyTranslations', fallback=False)
            print('__isWriteEmptyTranslations: ', str(self.__isWriteEmptyTranslations))

            self.__isOverwriteSrcFiles = configFile.getboolean(sourcePath, 'isOverwriteSrcFiles', fallback=False)
            print('__isOverwriteSrcFiles: ', str(self.__isOverwriteSrcFiles))

            self.__isDoBackup = configFile.getboolean(sourcePath, 'isDoBackup', fallback=False)
            print('__isDoBackup: ', str(self.__isDoBackup))


            self.__baseSrcPath = configFile.get (sourcePath, 'sourceFolder')
            print('__baseSrcPath: ', str(self.__baseSrcPath))

            self.__baseTrgPath = configFile.get (sourcePath, 'targetFolder')
            print('__baseTrgPath: ', str(self.__baseTrgPath))

            #--- folder list ---------------------------------

            self.__comparePaths = {}

            if (sourcePath == 'jgerman_wip_all'):

                options = configFile.options(sourcePath)
                for option in options:
                    try:
                        if ('sourcefolder' in option):
                            sourceFolder = configFile.get(sourcePath, option)
                        if ('targetfolder' in option):
                            targetFolder = configFile.get(sourcePath, option)
                            self.__comparePaths[sourceFolder] = targetFolder
                            print('All: sourcePath: ' + sourceFolder + ' targetPath: ' + targetFolder)

                    except:
                        print("exception on %s!" % option)

            else:
                # standard
                self.__comparePaths [self.__baseSrcPath] = self.__baseTrgPath
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
