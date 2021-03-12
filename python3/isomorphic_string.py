def isIsomorphic(s: str, t: str) -> bool:
    char_dict = {}
    for i, char_s in enumerate(s):
        if char_s not in char_dict:
            char_dict[char_s] = t[i]
        else:
            if char_dict[char_s] != t[i]:
                return False

    if len(set(s)) != len(set(t)):
        return False

    return True


if __name__ == '__main__':
    assert True is isIsomorphic('egg', 'add')
    assert False is isIsomorphic('foo', 'bar')
    assert True is isIsomorphic('paper', 'title')
    assert False is isIsomorphic('badc', 'baba')
