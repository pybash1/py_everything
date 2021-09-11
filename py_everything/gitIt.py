def main():
    import argparse
    import sys
    import os
    import subprocess
    import time
    import textwrap
    from . import __data as data

    ver = "v1.0.0"
    helpDesc = data.helpDesc2.format(ver, ver, sys.version)

    argparser = argparse.ArgumentParser(
        prog="gitIt",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent(helpDesc),
    )
    argparser.add_argument(
        "-gh",
        "--github",
        action="store_true",
        required=False,
        help="Generate .github folder.",
    )
    argparser.add_argument(
        "-d",
        "--docs",
        action="store_true",
        required=False,
        help="Generate a docs folder.",
    )
    argparser.add_argument(
        "-s",
        "--security",
        action="store_true",
        required=False,
        help="Add a Security Policy.",
    )
    argparser.add_argument(
        "-i",
        "--issue",
        action="store_true",
        required=False,
        help="Add ISSUE_TEMPLATE in .github.",
    )
    argparser.add_argument(
        "-c",
        "--config",
        action="store_true",
        required=False,
        help="Add a config.yml for ISSUE_TEMPLATE.",
    )
    argparser.add_argument(
        "--greet", action="store_true", required=False, help="Add a greet workflow."
    )
    args = argparser.parse_args()

    readmePath = os.path.realpath(os.getcwd() + "\\README.md")
    gitignorePath = os.path.realpath(os.getcwd() + "\\.gitignore")
    ghPath = os.path.realpath(os.getcwd() + "\\.github")
    issuePath = os.path.realpath(ghPath + "\\ISSUE_TEMPLATE")
    bugPath = os.path.realpath(issuePath + "\\bug-report.md")
    featurePath = os.path.realpath(issuePath + "\\feature-or-enhancement-request.md")
    workflowPath = os.path.realpath(ghPath + "\\workflows")
    greetPath = os.path.realpath(workflowPath + "\\greet.yml")
    docsPath = os.path.realpath(os.getcwd() + "\\docs")
    licensePath = os.path.realpath(os.getcwd() + "\\LICENSE")
    securityPath = os.path.realpath(ghPath + "\\SECURITY.md")
    configPath = os.path.realpath(issuePath + "\\config.yml")

    originDir = os.getcwd()

    print("Starting gitIt Repository Generator")
    print("Using Python {}".format(sys.version))
    print("Running gitIt{}".format(ver))
    time.sleep(1)
    repoName = input("[+]Enter Repository Name:")
    print("Setting name to variable!")
    repoDescription = input("[+]Enter Repository Description: ")
    time.sleep(1)
    repoLicense = input("[+]Enter Repository LICENSE: ")

    readmeData = data.readmeData.format(repoName, repoDescription, repoLicense)
    time.sleep(1)

    print("Initializing Repository...")

    if subprocess.run("git init", shell=True):
        print("Sucessfully Generated Repository!")
        print("Generating README...")
        with open(readmePath, "w+") as f:
            f.write(readmeData)
        print("Generating gitignore...")
        with open(gitignorePath, "w+") as f:
            pass
        print("Creating License...")
        with open(licensePath, "w+") as f:
            pass
        if args.github == True:
            os.mkdir(ghPath)
            if args.docs == True:
                print("Making Docs Folder!")
                os.mkdir(docsPath)

            if args.security == True:
                print("Creating SECURITY.md")
                securityData = data.securityData
                with open(securityPath, "w+") as f:
                    f.write(securityData)

            if args.issue == True:
                print("Creating issue temlpates...")
                os.mkdir(issuePath)
                bugData = data.bugData
                with open(bugPath, "w+") as f:
                    f.write(bugData)

                featureData = data.featureData
                with open(featurePath, "w+") as f:
                    f.write(featureData)

                if args.config == True:
                    print("Creating config.yml")
                    configData = data.configData
                    with open(configPath, "w+") as f:
                        f.write(configData)

            if args.greet == True:
                print("Generating greet workflow!")
                os.mkdir(workflowPath)
                greetData = data.greetData

                with open(greetPath, "w+") as f:
                    f.write(greetData)
        print("Finished gitIt!")
    else:
        print("Failed to initialize repository!")
        sys.exit()
