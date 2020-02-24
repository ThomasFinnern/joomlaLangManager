@ECHO OFF
REM Supports translation of joomla lang string to other language

REM google and use: Is there a way to pass parameters “by name” (and not by order) to a batch .bat file?

CLS

SET CmdArgs=
ECHO python TranslateLang.py 

REM Source file
Call :AddNextArg -s "..\.sandbox\en-GB\com_contact.ini"

REM Target file
Call :AddNextArg -t "..\.sandbox\de-DE\com_contact.ini"

REM REM Language ID: Only needed if file does not exist
REM Call :AddNextArg -l "de-DE"

REM 
REM Call :AddNextArg -y ""
 
REM add command line 
REM Call :AddNextArg %*

ECHO.
ECHO ------------------------------------------------------------------------------
ECHO Start cmd:
ECHO.
ECHO python TranslateLang.py %CmdArgs% %* 
     python TranslateLang.py %CmdArgs% %* 

GOTO :EOF

REM ------------------------------------------
REM Adds given argument to the already known command arguments
:AddNextArg 
SET NextArg=%*
SET CmdArgs=%CmdArgs% %NextArg%
ECHO  '%NextArg%'
GOTO :EOF

