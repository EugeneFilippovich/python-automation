import re

blacklist = ['ipsum', 'quis']


def replace(match):
    word = match.group()
    if word.lower() in blacklist:
        return "[CENSORED]"
    else:
        return word

text = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum."""

text = re.sub(r'\b\w*\b', replace, text, flags=re.I|re.U)
print(text)