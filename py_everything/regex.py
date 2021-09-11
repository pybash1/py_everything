import re

# Regex to match any web URL(irrespective of protocol/URI, subdomain, url path, query parameters)
url = r"((\S*)?:\/\/(.)?)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.?[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)"
# Precompiled URL regex
urlC = re.compile(url)

# Regex to match any local filepath(irrespective of OS)
filepath = r"^(.*/)([^/]*)$"
# Precompiled Filepath regex
filepathC = re.compile(filepath)

# Regex to match any number(irrespective of length)
number = r"\d+"
# Precompiled number regex
numberC = re.compile(number)

# Regex to match anything
anything = r"(?s).*"
# Precompiled anything regex
anythinC = re.compile(anything)

# Regex to match any string(data within quotes(double or single))
string = r'["\'](.*?)["\']'
# Precompiled string regex
stringC = re.compile(string)

# Regex to match any email address
email = r"^\w+([-+.\']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"
# Precompiled email regex
emailC = re.compile(email)

# Regex to match any alphanumeric text
alphanumeric = r"^[a-zA-Z0-9]*$"
# Precompiled alphanumeric regex
alphanumericC = re.compile(alphanumeric)

# Regex to match complex passwords(password validator)
password = r'(?=(.*[0-9]))(?=.*[\!@#$%^&*()\\[\]{}\-_+=~`|:;"\'<>,./?])(?=.*[a-z])(?=(.*[A-Z]))(?=(.*)).{8,}'
# Precompiled password regex
passwordC = re.compile(password)

# Regex to match any IPv4 Address
ip6 = r"[0-9a-fA-F]{1,4}::[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}:[0-9a-fA-F]{1,4}"
# Precompiled iIPv6 regex
ip6C = re.compile(ip6)

# Regex to match any date in format(ddMMYY) with separators of -, ., or /
date = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"
# Precompiled date regex
dateC = re.compile(date)

# Regex to match any time in format(HH:MM) with optional 0 in HH 12-Hour
time12 = r"^(0?[1-9]|1[0-2]):[0-5][0-9]$"
# Precompiled time12 regex
time12C = re.compile(time12)

# Regex to match any time in format(HH:MM) with optional 0 in HH 24-Hour
time24 = r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"
# Precompiled time24 regex
time24C = re.compile(time24)

# Regex to match any HTML tag with attributes
html = r"<\/?[\w\s]*>|<.+[\W]>"
# Precompiled HTML regex
htmlC = re.compile(html)

# Regex to match any hex code color
hexCode = r"^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
# Precompiled hex code regex
hexCodeC = re.compile(hexCode)

# Regex to match any empty string
emptyString = r"^\s*$"
# Precompiled empty string regex
emptyStringC = re.compile(emptyString)
