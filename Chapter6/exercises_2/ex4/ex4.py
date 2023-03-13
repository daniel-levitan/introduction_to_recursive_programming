def add_pol(a, b):
    i = 0
    result = []
    if len(b) < len(a):
        a, b = b, a

    while i < len(a):
        result.append(a[i] + b[i])
        i += 1

    while i < len(b):
        result.append(b[i])
        i += 1

    return result


def sub_pol(a, b):
    b_minus = sim_mult(b, [-1])
    return add_pol(a, b_minus)


def sim_mult(a, b):
    result = []
    if len(a) == 1:
        for i in range(len(b)):
            result.append(a[0] * b[i])
        return result

    if len(b) == 1:
        for i in range(len(a)):
            result.append(b[0] * a[i])
        return result


def shift(a, n):
    return [0] * n + a


def mult(a, b):
    if a == [] or b == []:
        return []
    elif len(a) == 1 or len(b) == 1:
        return sim_mult(a, b)
    else:
        n = max(len(a), len(b))
        # n = min(len(a), len(b))
        if n % 2 == 1:
            n -= 1
        # mid = n // 2
        # mid_a = mid
        # mid_b = mid
        mid_a = len(a) // 2
        mid_b = len(b) // 2

        a_low = a[:mid_a]
        a_high = a[mid_a:]

        b_low = b[:mid_b]
        b_high = b[mid_b:]

        ac = mult(a_high, b_high)
        bd = mult(a_low, b_low)

        a_high_plus_a_low = add_pol(a_high, a_low)
        b_high_plus_b_low = add_pol(b_high, b_low)
        t = mult(a_high_plus_a_low, b_high_plus_b_low)
        t = sub_pol(t, ac)
        t = sub_pol(t, bd)



        t = shift(t, n // 2)
        # bd = shift(bd, n)
        ac = shift(ac, n)

        return add_pol(add_pol(ac, t), bd)
        # return bd + t + ac

def main():
    a = [1, 2, 3]
    b = [3, 2, 2]

    print([3, 8, 15, 10, 6], mult(a, b))
    # print(shift(a, 2))
    # pol1 = [3, -5, 0, 1]
    # pol2 = [1, 3, 1, 1]
    # pol3 = [1, 2, 3]

    # print([4, -2, 1, 2], add_pol(pol1, pol2))
    # print([4, -3, 3, 1], add_pol(pol1, pol3))
    # print([2, -8, -1, 0], sub_pol(pol1, pol2))
    # print([2, -7, -3, 1], sub_pol(pol1, pol3))

    # a = [0, 10]
    # b = [6]
    # print(add_pol(a, b))
    # # print(sub_pol(pol1, pol2))
    # # print(sub_pol(pol1, pol3))


if __name__ == '__main__':
    main()
