def longestCommonPrefix(strs):
    if len(strs) == 0: return ''
    strs = sorted(strs, key=len)
    LCP = strs[0]
    for word in strs[1:]:
        for i, ch in enumerate(LCP):
            if word[i] != ch:
                LCP = LCP[:i]
                break
    return LCP


d = ["flower", "flow", "flight"]
print(longestCommonPrefix(d))
