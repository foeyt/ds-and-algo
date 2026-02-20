def add_hash(key: str) -> int:
    mod = 2147483647
    hash_code = 0
    for ch in key:
        hash_code = (hash_code + ord(ch)) % mod
    return hash_code


def mul_hash(key: str) -> int:
    mod = 2147483647
    hash_code = 0
    for ch in key:
        hash_code =  (1331 * hash_code + ord(ch)) % mod
    return hash_code


def xor_hash(key: str) -> int:
    mod = 2147483647
    hash_code = 0
    for ch in key:
        hash_code = (hash_code ^ ord(ch)) % mod
    return hash_code


def rot_hash(key: str) -> int:
    mod = 2147483647
    hash_code = 0
    for ch in key:
        hash_code = (hash_code << 4) ^ (hash_code >> 28) ^ ord(ch)
    return hash_code
