@ECHO OFF
REM Compiles all *.py file in directory

python -V

	REM echo.
	echo --- %1
	python -m py_compile %1
	
)

ECHO Done
PAUSE


