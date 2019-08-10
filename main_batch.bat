cd /d %~dp0
chcp 932
echo %DATE%%TIME% "バッチ処理を開始します" >> "C:\oss_project\logs\batch_log.txt"
rem C:\ProgramData\Anaconda3\python.exe "C:\oss_project\dbimport.py" %*
C:\Users\masaf\Anaconda3\python.exe "C:\oss_project\dbimport.py" %*

if %ERRORLEVEL% NEQ 0 goto FAILURE

:SUCCESS
echo %DATE%%TIME% "バッチ処理を正常終了します" >> "C:\oss_project\logs\batch_log.txt"
goto END

:FAILURE
echo "バッチ処理を異常終了します" >> "C:\oss_project\logs\batch_log.txt"

:END
exit
