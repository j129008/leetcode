def plusOne(digits):
    return [int(ele) for ele in list(str(1+int(''.join([str(d) for d in digits]))))]

print(plusOne([1,2,3]))
