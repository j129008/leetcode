def isHappy(n: int):
    square_sum = n
    history = set()
    while square_sum not in history:
        history.add(square_sum)
        square_sum = sum([int(ele)*int(ele) for ele in list(str(square_sum))])

        if square_sum == 1:
            return True

    return False


print(isHappy(19))
print(isHappy(2))
