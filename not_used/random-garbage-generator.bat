@echo off
setlocal EnableDelayedExpansion

goto Main

:Main
set const_rs_chars=0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
set "RandomStringOutput="
set "RandomStringReturn="
set /a RandomStringLength=0

set /a RandomStringLength=32
set "RandomStringReturn=PushRandomStringFile"
set /a var_push_garbage_length=0
set /a var_push_garbage_length_target=16
set "var_random_garbage_file_path=%cd%\random-garbage"
if exist %var_random_garbage_file_path% del %var_random_garbage_file_path%
goto RandomString

:PushRandomStringFile
echo %RandomStringOutput%
echo %RandomStringOutput% >> %var_random_garbage_file_path%
set /a var_push_garbage_length=%var_push_garbage_length%+1
if %var_push_garbage_length%==%var_push_garbage_length_target% goto gitPush
goto RandomString

:gitPush
git add --all
git commit -m "asd"
git push
goto Exit

: : RandomString function

:RandomString
set var_rs_buffer=0
for /l %%b IN (0, 1, %RandomStringLength%) do (
  set /a rand=!RANDOM! * 61 / 32768
  for /f %%i in ('echo %%const_rs_chars:~!rand!^,1%%') do set var_rs_buffer=!var_rs_buffer!%%i
)
set RandomStringOutput=%var_rs_buffer%
goto %RandomStringReturn%

: : RandomString function

:Exit