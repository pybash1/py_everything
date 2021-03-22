def main():
    import argparse
    import sys
    import os
    import subprocess
    import time
    import textwrap

    ver = 'v1.0.0'
    help_desc='''
setupPyGen {} Help Utility
--------------------------
Welcome to help utility for setupPyGen. setupPyGen is a command-line utility to generate a python package project structure for you. Including setup.py

It has very few command-line arguments, most data is taken input after running, the command "setupPyGen" in the directory where you want to generate you python package project structure.

You are currently using setupPyGen {}, with Python {}.
'''.format(ver, ver, sys.version)

    argparser = argparse.ArgumentParser(prog="setupPyGen", formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent(help_desc))
    argparser.add_argument('-g', '--git', default=False, metavar='', type=bool, required=False, help="Start a git repository in the base directory(True or False).")
    argparser.add_argument('-t', '--tests', default=False, metavar='', type=bool, required=False, help="Add tests/ folder to project directory(True or False).")
    argparser.add_argument('--gitignore', default=False, metavar='', type=bool, required=False, help="Add .gitignore to project directory(True or False).")
    args = argparser.parse_args()

    readmePath = os.path.realpath(os.getcwd()+"\\README.md")
    setupFilePath = os.path.realpath(os.getcwd()+"\\setup.py")
    licensePath = os.path.realpath(os.getcwd()+"\\LICENSE")
    gitignorePath = os.path.realpath(os.getcwd()+"\\.gitignore")
    testsPath = os.path.realpath(os.getcwd()+"\\tests")

    originDir = os.getcwd()

    print("Starting setup.py Generator")
    print("Using Python {}".format(sys.version))
    print("Running SetupPyGen {}".format(ver))
    
    time.sleep(1)
    
    print("Creating setup.py File")
    
    time.sleep(3)
    
    packageName = input("[+]Enter Package Name:")
    
    print("Registering Name to File...")
    
    packageDescription = input("[+]Enter Package Description: ")
    
    print("...")
    
    time.sleep(1)
    
    packageVersion = input("[+]Enter Version: ")
    packageAuthor = input("[+]Enter Author Name: ")
    
    time.sleep(1)
    
    packageEmail = input("[+]Enter Author's Email: ")
    packagesList = input("[+]Enter List of Packages: ")
    
    print("Reading Package List...")
    print("Packages: ")
    
    for package in list(packagesList.split(", ")):
        print(package)
        
    print("Added Packages...")
    
    packages = list(packagesList.split(", "))
    
    if len(packages) <= 0:
        print("setupPyGen: error: cannot generate setup.py with 0 packages! quitting!")
        sys.exit()
    
    for package in packages:
        packagePath = os.getcwd()+"\\"+package
        os.mkdir(packagePath)
        os.chdir(packagePath)
        initPath = os.getcwd()+"\\__init__.py"
        with open(initPath, "w+") as f:
            pass
        os.chdir(originDir)
    
    packageDependencies = input("[+]Enter List of Dependencies: ")
    
    print("Adding Dependencies...")
    print("Installing Dependencies...")
    
    depends = list(packageDependencies.split(", "))
    
    if len(depends) >= 1:
        for depend in depends:
            command = "python -m pip install {}".format(depend)
            run = subprocess.run(command, shell=True, capture_output=True)
    else:
        print("setupPyGen: info: 0 dependencies, huh? great!")
        
    packageLicense = input("[+]Enter License: ")
    packageHomepage = input("[+]Enter Package Homepage: ")
    pythonVersion = input("[+]Minimum Python Version Required: ")
    
    time.sleep(1)
    
    print("Generating setup.py...")
    
    with open(setupFilePath, "w+") as f:
        pass
    
    setupPyData = '''from setuptools import setup

readme_file = open("{}", "r").read()

setup(
    name="{}",
    version="{}",
    description="{}",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    author="{}",
    author_email="{}",
    packages={},
    install_requires={},
    license="{}",
    url="{}",
    python_requires="{}"
)
'''.format(readmePath, packageName, packageVersion, packageDescription, packageAuthor, packageEmail, packages, depends, packageLicense, packageHomepage, pythonVersion)

    with open(setupFilePath, "w+") as f:
        f.write(setupPyData)
        f.close()

    
    print("Generating README...")
    
    readmeData = '''# {}
{}
'''.format(packageName, packageDescription)
    
    with open(readmePath, "w+") as f:
        f.write(readmeData)
    
    print("Generating LICENSE...")
    
    with open(licensePath, "w+") as f:
        pass
    
    print("Checking Dependencies...")
    
    time.sleep(2)
    
    print("Installed All Dependencies successfully...")
    
    if args.git == True:
        print("Initializing git repository...")
        command = "git init"
        run = subprocess.run(command, shell=True, capture_output=True)
    

    if args.gitignore == True:
        print("Generating .gitignore...")
        with open(gitignorePath, 'w+') as f:
            pass


    if args.tests == True:
        print("Generating tests/ folder...")
        os.mkdir(testsPath)
