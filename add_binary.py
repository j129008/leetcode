import ipdb

def addBinary(a, b):
    N = max(len(a), len(b))
    if(len(a) > len(b)):
        b = '0'*(N-len(b)) + b
    else:
        a = '0'*(N-len(a)) + a

    output = ''
    carry = 0
    for i in range(N):
        _a = int(a[N-i-1])
        _b = int(b[N-i-1])
        output = str(_a ^ _b ^ carry) + output
        carry =  (_a & _b) | ((_a ^ _b) & carry)

    if carry == 1:
        output = '1' + output
    return output

res = addBinary('101', '111')
print(res)

