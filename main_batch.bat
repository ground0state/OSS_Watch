cd /d %~dp0
chcp 932
echo %DATE%%TIME% "�o�b�`�������J�n���܂�" >> "C:\oss_project\logs\batch_log.txt"
rem C:\ProgramData\Anaconda3\python.exe "C:\oss_project\dbimport.py" %*
C:\Users\masaf\Anaconda3\python.exe "C:\oss_project\dbimport.py" %*

if %ERRORLEVEL% NEQ 0 goto FAILURE

:SUCCESS
echo %DATE%%TIME% "�o�b�`�����𐳏�I�����܂�" >> "C:\oss_project\logs\batch_log.txt"
goto END

:FAILURE
echo "�o�b�`�������ُ�I�����܂�" >> "C:\oss_project\logs\batch_log.txt"

:END
exit
