#! /bin/bash

# Base Start Function
function start
{
    echo "-unittest(Run Tests)"
    echo "-git_status(Check Git Status)"
    echo "-build_docs(Build the Docs Locally)"
    echo "-setup_py_install(Install the package using setup.py)"
    echo "-pip_insall(Install the package using pip)"
    echo "-exit(Exit the program)"

    read -p "Command: " task

    if [ $task == "unittest" ]; then
        unittest
    elif [ $task == "git_status" ]; then
        git_status
    elif [ $ttask == "build_docs" ]; then
        build_docs
    elif [ $task == "setup_py_install" ]; then
        setup_py_install
    elif [ $task == "pip_install" ]; then
        pip_insall
    fi
}

# Function for `unittest` command
function unittest
{
    clear
    cd tests
    python -m unittest test_py_everything.py
    cd ..
    end
}

# Function for `git_status` command
function git_status
{
    echo "-git_short(Short Status)"
    echo "-git_long(Normal Status)"
    read -p "Type: " status_type

    if [ $status_type == "git_short" ]; then
        git_short
    else
        git_long
    fi
}

# Function for `build_docs` command
function build_docs
{
    clear
    cd docs
    make html
    end
}

# Function for `setup_py_install` command
function setup_py_install
{
    clear
    setup.py install
    end
}

# Function for `pip_install` command
function pip_insall
{
    clear
    pip install py_everything
    end
}

# Function for `git_short` command from `git_status` function
function git_short
{
    clear
    git status -s
    end
}

# Function for `git_long` command from `git_status` function
function git_long
{
    clear
    git status
    end
}

# Base End Function
function end
{
    read -n1 -r -p "Press any key to continue..."
    start
}

# Run the `start` function for the first timeafter execution
start
