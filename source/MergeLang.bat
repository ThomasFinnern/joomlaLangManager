@ECHO OFF
REM <What it does>

CLS

SET CmdArgs=
ECHO python MergeLang.py 

REM 
Call :AddNextArg -c "COM_RSGALLERY2"
REM 
Call :AddNextArg -s "f:\Entwickl\rsgallery2\RSGallery2_J-4\administrator\components\com_rsgallery2\language\en-GB\Sorted_J3.x.ini"

REM 
Call :AddNextArg -f "f:\Entwickl\rsgallery2\RSGallery2_J-4\administrator\components\com_rsgallery2\language\en-GB\en-GB.com_rsgallery2.ini"

REM 
Call :AddNextArg -y "f:\Entwickl\rsgallery2\RSGallery2_J-4\administrator\components\com_rsgallery2\language\en-GB\en-GB.com_rsgallery2.sys.ini"
 
REM add command line 
REM Call :AddNextArg %*

ECHO.
ECHO ------------------------------------------------------------------------------
ECHO Start cmd:
ECHO.
ECHO python MergeLang.py %CmdArgs% %* 
     python MergeLang.py %CmdArgs% %* 

GOTO :EOF

REM ------------------------------------------
REM Adds given argument to the already known command arguments
:AddNextArg 
SET NextArg=%*
SET CmdArgs=%CmdArgs% %NextArg%
ECHO  '%NextArg%'
GOTO :EOF

