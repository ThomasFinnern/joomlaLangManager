@ECHO OFF
REM Lang File supports a joomla language file (read/write ? change ?)

CLS

SET CmdArgs=
ECHO python jLangFile.py 

REM 
Call :AddNextArg -f "..\RSGallery2_J-4\administrator\components\com_rsgallery2\language\en-GB\en-GB.com_rsgallery2.ini"
                     
REM 
REM Call :AddNextArg -n "modules"
 
REM add command line 
REM Call :AddNextArg %*

ECHO.
ECHO ------------------------------------------------------------------------------
ECHO Start cmd:
ECHO.
ECHO python jLangFile.py %CmdArgs% %* 
     python jLangFile.py %CmdArgs% %* 

GOTO :EOF

REM ------------------------------------------
REM Adds given argument to the already known command arguments
:AddNextArg 
SET NextArg=%*
SET CmdArgs=%CmdArgs% %NextArg%
ECHO  '%NextArg%'
GOTO :EOF

