import re

# regex [A-z] contains "`", holy shit...

def isPalindrome(s):
    s = re.sub(r'[^A-Za-z0-9\w]', '', s).lower()
    rev_s = s[::-1]

    if s == rev_s:
        return True

    return False

if isPalindrome("`l;`` 1o1 ??;l`"):
    print('True')
else:
    print('False')
