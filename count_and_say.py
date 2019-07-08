def spliter(x):
    x = str(x)
    return_string = []
    head = 0
    i = 0
    for i in range(len(x)-1):
        if x[i] != x[i+1]:
            return_string.append(x[head:i+1])
            head = i+1
    return_string.append(x[head:])
    return return_string

def talker(x):
    talk = ''
    for ele in spliter(x):
        talk += str(len(ele))+ele[0]
    return talk

history = dict()
def countAndSay(n):
    start = 1
    for i in range(1, n):
        if i in history:
            start = history[i]
        else:
            start = talker(start)
            history[i] = start
    return str(start)


print(countAndSay(5))

