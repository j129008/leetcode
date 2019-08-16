
def addBinary(a, b):
    N = max(len(a), len(b))
    if(len(a) > len(b)):
        b = '0'*(N-len(b)) + b
    else:
        a = '0'*(N-len(a)) + a

    output = ''
    carry = 0
    for i in range(N):
        adder = int(a[N-i-1]) + int(b[N-i-1]) + carry

        if adder == 2:
            carry = 1
            adder = 0
            output = '0' + output
        elif adder == 1:
            output = '1' + output
            carry = 0
        elif adder == 3:
            output = '1' + output
            carry = 1
        else:
            output = '0' + output
            carry = 0
    if carry == 1:
        output = '1' + output
    return output


res = addBinary('101', '111')
print(res)

