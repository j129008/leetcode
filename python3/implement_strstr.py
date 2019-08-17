def strStr(haystack, needle):
    if needle == "": return 0
    if needle in haystack:
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    j -= 1
                    break
            if j == len(needle)-1:
                return i
    return -1

print(strStr("mississippi", "issip"))
