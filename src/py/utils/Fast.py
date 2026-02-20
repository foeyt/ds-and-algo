def fast_pow(a: int, b: int) -> int:
    if b < 0:
        return fast_pow(a, -b)

    if b == 0:
        return 1

    result: int = 1
    while b > 0:
        if b % 2 == 1:
            result = result * a
        a = a * a
        b = b // 2
    return result
