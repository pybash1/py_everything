def main():
    import argparse
    import sys
    import os
    import subprocess
    import time
    import textwrap
    from . import __data as data

    ver = 'v1.0.1'
    helpDesc = data.helpDesc.format(ver, ver, sys.version)

    argparser = argparse.ArgumentParser(
        prog="setupPyGen", formatter_class=argparse.RawDescriptionHelpFormatter, description=textwrap.dedent(helpDesc))
    argparser.add_argument('-g', '--git', action='store_true', required=False,
                           help="Start a git repository in the base directory(True or False).")
    argparser.add_argument('-t', '--tests', action='store_true', required=False,
                           help="Add tests/ folder to project directory(True or False).")
    argparser.add_argument('--gitignore', action='store_true', required=False,
                           help="Add .gitignore to project directory(True or False).")
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

    packageName = input("[+]Enter Package Name: ")

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

    if packages[0] != 'find_packages' or 'find_packages()':
        for package in packages:
            packagePath = os.getcwd()+"\\"+package
            os.mkdir(packagePath)
            os.chdir(packagePath)
            initPath = os.getcwd()+"\\__init__.py"
            with open(initPath, "w+") as f:
                pass
            os.chdir(originDir)

        setupPyData = data.setupPyData
    else:
        setupPyData = data.setupPyDataAlt

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

    if setupPyData == data.setupPyData:
        setupPyDataFinal = setupPyData.format(readmePath, packageName, packageVersion, packageDescription,
                                              packageAuthor, packageEmail, packages, depends, packageLicense, packageHomepage, pythonVersion)
    else:
        setupPyDataFinal = setupPyData.format(readmePath, packageName, packageVersion, packageDescription,
                                              packageAuthor, packageEmail, depends, packageLicense, packageHomepage, pythonVersion)

    with open(setupFilePath, "w+") as f:
        f.write(setupPyDataFinal)
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
