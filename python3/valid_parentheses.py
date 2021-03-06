def isValid(s):
    stack = []
    bracket = {')': '(', '}': '{', ']': '['}
    for ch in s:
        if ch in bracket:
            try:
                if bracket[ch] == stack[-1]:
                    stack.pop()
                    continue
            except:
                return False
        stack.append(ch)
    if len(stack) == 0:
        return True
    return False

def isValidFastImp(s):
    bracket = [ '()', '[]', '{}' ]

    for _ in range(len(s)//2):
        for b in bracket:
            s = s.replace(b, '')

    if s == '':
        return True
    return False


print(isValid(']'))
