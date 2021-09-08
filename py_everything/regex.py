# Regex to match any web URL(irrespective of protocol/URI, subdomain, url path, query parameters)
url = r"((\S*)?:\/\/(.)?)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.?[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)"

# Regex to match any local filepath(irrespective of OS)
filepath = r"^(.*/)([^/]*)$"

# Regex to match any number(irrespective of length)
number = r"\d+"

# Regex to match anything
anything = r"(?s).*"

# Regex to match any string(data within quotes(double or single))
string = r'["\'](.*?)["\']'

# Regex to match any email address
email = r"^\w+([-+.\']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$"

# Regex to match any alphanumeric text
alphanumeric = r"^[a-zA-Z0-9]*$"

# Regex to match complex passwords(password validator)
password = r'(?=(.*[0-9]))(?=.*[\!@#$%^&*()\\[\]{}\-_+=~`|:;"\'<>,./?])(?=.*[a-z])(?=(.*[A-Z]))(?=(.*)).{8,}'

# Regex to match any IPv4 Address
ip = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"

# Regex to match any date in format(ddMMYY) with separators of -, ., or /
date = r"^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[1,3-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$"

# Regex to match any time in format(HH:MM) with optional 0 in HH 12-Hour
time12 = r"^(0?[1-9]|1[0-2]):[0-5][0-9]$"

# Regex to match any time in format(HH:MM) with optional 0 in HH 24-Hour
time24 = r"^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$"

# Regex to match any HTML tag with attributes
html = r"<\/?[\w\s]*>|<.+[\W]>"

# Regex to match any hex code color
hexCode = r"^#?([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"

# Regex to match any empty string
emptyString = r"^\s*$"
