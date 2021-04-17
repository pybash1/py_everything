# setupPyGen #

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
'''

setupPyDataAlt = '''from setuptools import setup, find_packages

readme_file = open("{}", "r").read()

setup(
    name="{}",
    version="{}",
    description="{}",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    author="{}",
    author_email="{}",
    packages=find_packages(),
    install_requires={},
    license="{}",
    url="{}",
    python_requires="{}"
)
'''

helpDesc='''
setupPyGen {} Help Utility
------------------------------
Welcome to help utility for setupPyGen. setupPyGen is a command-line utility to generate a python package project structure for you. Including setup.py

It has very few command-line arguments, most data is taken input after running, the command "setupPyGen" in the directory where you want to generate you python package project structure.

You are currently using setupPyGen {}, with Python {}.
'''

# GitIt #

helpDesc2='''
gitIt {} Help Utility
-------------------------
Welcome to help utility for gitIt. gitIt is a command-line utility to generate a git repository for you.
It generates a GitHub Ready repository.

You are currently using gitIt {}, with Python {}.
'''

readmeData = '''# {}

{}

License - {}
'''

securityData = '''# Security Policy

## Supported Versions

v1.0.0 is currently supported by security updates.

| Version | Supported          |
| ------- | ------------------ |
| 1.0.0   | :white_check_mark: |

## Reporting a Vulnerability

Found a vulnerability? Create an issue and report it [here](https://example.com).

'''

bugData = '''---
name: Bug Report
about: Create a report to help us improve
title: "[BUG]"
labels: bug
assignees: ''
---

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Import something
2. Write some code
3. Run some code
4. Error occurs

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots**
If possible or applicable, please add screenshots to help explain your problem.

**Device:**
  - OS: [e.g. Windows, Linux]
  - Device: [e.g. Phone, PC]

**Additional context**
Add any other context about the problem here.
'''

featureData = '''---
name: Feature or Enhancement Request
about: Suggest an idea for this project.
title: "[FEATURE_OR_ENHANCEMENT]"
labels: enhancement
assignees: ''
---

**Is your request related to a problem? If Yes, please describe.**
A clear and concise description of what the problem is. If any issue is open with your context, please mention it.

**Describe the solution you'd like, if applicable.**
A clear and concise description of what you want to happen.

**Not regarding a issue or problem? If Yes, describe here.**
Want a new function or class added in, describe it here.

**Additional context**
Add any other context or screenshots about the feature request here.
'''

configData = '''blank_issues_enabled: true

contact_links:
  - name: Question
    url: https://example.com/
    about: Have a question? Find your answer here!

  - name: Documentation
    url: https://example.com/
    about: Can't figure out something? Check out our Documentation!
'''

greetData = '''name: Greet

on: [pull_request, issues]

jobs:
  greeting:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/first-interaction@v1
      with:
        repo-token: ${{ secrets.GITHUB_TOKEN }}
        issue-message: "Thanks for opening the issue. Hope, it get's fixed soon."
        pr-message: 'Thanks for contributing to $GITHUB_REPOSITORY.'
'''

# conversion.py

unitTypes = {
    "k": 1000,
    "h": 100,
    "da": 10,
    "b": 1,
    "d": 0.1,
    "c": 0.01,
    "m": 0.001
}
