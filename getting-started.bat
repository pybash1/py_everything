@echo off

title Getting Started with py_everything

:: Base start block
:start
echo -unittest(Run Tests)
echo -git_status(Check Git Status)
echo -build_docs(Build the Docs Locally)
echo -setup_py_install(Install the package using setup.py)
echo -pip_insall(Install the package using pip)
echo -exit(Exit the program)
set /p TASK=Command: 
goto %TASK%

:: Block for `unittest` command
:unittest
cls
cd tests
python -m unittest test_py_everything.py
cd ..
goto end

:: Block for `git_status` command
:git_status
echo -git_short(Short Status)
echo -git_long(Normal Status)
set /p GIT=Short or Normal?
goto %GIT%

:: Block for `build_docs` command
:build_docs
cls
cd docs
make html
goto end

:: Block for `setup_py_install` command
:setup_py_install
cls
setup.py install
goto end

:: Block for `pip_intall` command
:pip_insall
cls
pip install py_everything
goto end

:: Block for `git_short` command from `git _status` block
:git_short
cls
git status -s
goto end

:: Block for `git_long` command from `git _status` block
:git_long
cls
git status
goto end

:: Base exit block
:exit
exit

:: Base end block
:end
pause
cls
goto start
