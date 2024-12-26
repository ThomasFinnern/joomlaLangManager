@ECHO OFF
REM <What it does>

CLS

SET CmdArgs=
ECHO python findTranslationIds.py 

REM 
Call :AddNextArg -c "COM_RSGALLERY2"

REM
Call :AddNextArg -f "d:\Entwickl\2022\_gitHub\RSGallery2_J4\administrator\components\com_rsgallery2\language\en-GB\en-GB.com_rsgallery2.ini"
REM
Call :AddNextArg -y "d:\Entwickl\2022\_gitHub\RSGallery2_J4\administrator\components\com_rsgallery2\language\en-GB\en-GB.com_rsgallery2.sys.ini"

REM 
Call :AddNextArg "d:\Entwickl\2022\_gitHub\RSGallery2_J4\administrator\components\com_rsgallery2"
Call :AddNextArg "d:\Entwickl\2022\_gitHub\RSGallery2_J4\administrator\components\com_rsgallery2\language\en-GB\en-GB.com_rsgallery2.ini"
Call :AddNextArg "d:\Entwickl\2022\_gitHub\RSGallery2_J4\components\com_rsgallery2"
 
REM add command line 
REM Call :AddNextArg %*

ECHO.
ECHO ------------------------------------------------------------------------------
ECHO Start cmd:
ECHO.
ECHO python findTranslationIds.py %CmdArgs% %* 
     python findTranslationIds.py %CmdArgs% %* 

GOTO :EOF

REM ------------------------------------------
REM Adds given argument to the already known command arguments
:AddNextArg 
SET NextArg=%*
SET CmdArgs=%CmdArgs% %NextArg%
ECHO  '%NextArg%'
GOTO :EOF

