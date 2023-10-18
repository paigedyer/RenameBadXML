@echo off

IF "%~1"=="" (
    ECHO Error: Missing input file argument.
    GOTO :EOF
)

FOR %%I IN ("%~1") DO SET InputFileName=%%~nI

SET OutputFile=%InputFileName%.xml

test.exe %1 %OutputFile