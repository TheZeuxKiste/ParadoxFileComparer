@echo off
setlocal enabledelayedexpansion

rem set important variables: 



rem check for valid %1 input
if "%~1" == "" ( goto ProcessErrorEmptyArg ) 
rem if [%1] == [] ( goto ProcessErrorEmptyArg ), stripped out quotes via ~, change [] to "" for check of unknown variables

rem arg is input parameter
set arg=%1

rem modsfolder is path to pdx mod folder
set modsfolder=%HOMEDRIVE%%HOMEPATH%\Documents\Paradox Interactive\Crusader Kings III


rem iterate through the current folder and its sub folders, without default delims(delimiters)
rem if nothing found, search other folder for specifed file. same parameters.
for /f "delims=" %%i in ('dir /b/s "..\%arg%" 2^>nul') do ( 

    rem add every found matching the given parameter %1 to variable var
    set var=%%i !var!
)

:::::::::::::::::::::::::::::::::::::::::::::::::::::
rem search secondary directory, your pdx mods folder, CURRENTLY OUT OF ORDER, ICE CREAM MAKER BROKE!!!!
:::::::::::::::::::::::::::::::::::::::::::::::::::::

@REM rem change dir to your local mods folder in Documents --------------------(TODO implement customizable mod location to make compatible with other pdx titles.)
@REM chdir /d "%modsfolder%"
@REM rem quotes protect path, errors could occur if path contains spaces

@REM rem checks for invalid mods folder path, sends you to endoffile and throws errorlevel 2
@REM if %errorlevel% == 1 ( goto ProcessErrorInvalidPath )

@REM rem iterate through the current folder and its sub folders, without default delims(delimiters)
@REM for /f "delims=" %%b in ('dir /b/s "..\%arg%" 2^>nul') do (
    
@REM     set var=%%b !var!
@REM )

rem checks if script found anything, if not, itll abort
if "!var!" == "" ( goto ProcessErrorNothingFound )

rem echo the findings for other programs to catch
echo !var!

:EndOfFile
endlocal
exit /b 0 rem exit with errorlevel 0; everything went well

:ProcessErrorEmptyArg
endlocal
echo FINDVALIDFILES.BAT: what file do you want to find?
echo FINDVALIDFILES.BAT: please enter it as an argument.
exit /b 1 rem exit with errorlevel 1; no arguments passed to this file

:ProcessErrorInvalidPath
endlocal
echo FINDVALIDFILES.BAT: something is wrong with your local game path!
echo FINDVALIDFILES.BAT: please configure your config.json(TODO)
exit /b 2 rem exit with errorlevel 2; invalid path

:ProcessErrorNothingFound
endlocal
echo FINDVALIDFILES.BAT: nothing Found!
exit /b 3 rem exit with errorlevel 3; no Results found