# Repository Details, Prerequisites, Rules, Etc.

**This document contains different rules, prerequisites, etc. for cloning and editing this Repository.**

> **NOTE:** The Python Packages listed below are must have. Anaconda3, Git Bash, etc. are not neccessary but is preffered to be installed. They may not be required directly, but they help, identify issues and in debugging. Visual Studio Code is recommended to use since it has a lot of potential tools built-in, such as a Debugger, Integrated Terminal, Git and GitHub Integrations, etc. And the extensions are very much optional. But few are required. Such as TODO Highlight is used in the code. Having it would help, but it is not mandatory.

# Git Commit Messages
Commit Messages should follow this pattern from today(19.04.2021)

Pattern - `TYPE <status> <EXTRA> message`

Example - `git commit -m "FIX <done> Issue #1"`

Example 2 - `git commit -m "BUG <doing> <HELP-NEEDED> Issue #2"`

All available Types:
- FIX (Fix something)
- BUG (Fix a bug)
- FEATURE (Working on a new feature or module)
- TEST (Testing something or working with tests)
- ENHANCEMENT (Enhance something)
- EXTRAS (Files that are extra like repository.md)

All available Statuses:
- `<started>` (Started Work)
- `<doing>` (Work in Progress)
- `<done>` (Completed)
- `<finished>` (No Later Edits)

All availble Extras:
- `<HELP-NEEDED>`
- `<REVIEW>`
- `<DO-NOT-TOUCH>`

NOTE: This is applicable only for short commit messages not long ones!

P.S. - Please follow this pattern

# Prerequisites (Required)

## Tools and Technologies:
1. **Python** <= 3.6 (<= 3.8 Preffered) - https://python.org
2. Command Prompt(Windows) or Cygwin(Windows) or Terminal(Unix-Based) or Git Bash(All OS)
3. **Git**(& Git Bash)
4. **GitHub**(Account)
5. Any web browser

Python Packages:
1. **requests**
2. **pytube**
3. **playsound**
4. setuptools
5. wheel
6. pip
7. twine (Just in case)

Extensions (If using VS Code):
1. **Python by Microsoft**

# **Optional** Prerequisites 

Tools and Technologies:
1. Anaconda3
2. GitHub CLI
3. GitHub Desktop

Code Editor(anyone):
1. Visual Studio Code - https://code.visualstudio.com

Extensions in Visual Studio Code:
1. Error Lens by Alexander
2. Git Graph by mhutchie
3. GitLens - Git Supercharged by Eric Amodio
4. Pylance by Microsoft
5. Python Indent by Kevin Rose
6. Python Preview by dongli
7. Python Test Explorer for Visual Studio Code by Little Fox Team
8. TabNine Autocomplete by TabNine
9. GitHub Pull Requests and Issues by GitHub
10. TODO Highlight by Wayou Liu

Font(If using VS Code):
1. Fira Code with Font Ligatures Enabled

Settings for TODO Highlight(if using, not optioanl):
`{

    "todohighlight.keywords": [
        {
            "text": "FIX:",
            "color": "rgb(255, 0, 0)",
            "backgroundColor": "rgba(255, 0, 0, 0.2)",
        },
        {
            "text": "TIP:",
            "color": "rgb(0, 255, 0)",
            "backgroundColor": "rgba(0, 255, 0, 0.2)"
        },
        {
            "text": "TODO:",
            "color": "rgb(255, 0, 0)",
            "backgroundColor": "rgba(0, 0, 225, 0.5)"
        },
        {
            "text": "NOTE:",
            "color": "rgb()",
            "backgroundColor": "rgba()"
        }
    ]
}`
