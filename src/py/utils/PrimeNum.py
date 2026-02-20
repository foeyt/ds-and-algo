def fast_mod_mul(a: int, b: int, mod: int) -> int:
    return (a * b) % mod


def fast_mod_pow(a: int, b: int, mod: int) -> int:
    result: int = 1
    while b != 0:
        if (b & 1 != 0):
            result = fast_mod_mul(result, a, mod)
        a = fast_mod_mul(a, a, mod)
        b >>= 1
    return result


def millar_rabin(val: int) -> bool:
    if val < 3 and val % 2 == 0:
        return val == 2
    
    u: int = val - 1
    t: int = 0
    while u % 2 == 0:
        u //= 2
        t += 1

    ulist: list = [2,325,9375,28178,450775,9780504,1795265022]
    for i in ulist:
        v: int = fast_mod_pow(i, u, val)
        if v == 1 or v == 0 or v == val - 1:
            continue
        for j in range(t + 1):
            v = fast_mod_mul(v, v, val)
            if v == val - 1 and j != t:
                v = 1
                break
            if v != 1:
                return False
    return True
