#ifndef FAST
#define FAST


unsigned long long int fastMultiply(unsigned int a, unsigned int b)
{
    if (a == 0 || b == 0)
        return 0;

    unsigned long long int result = 1;
    while (b > 0)
    {
        if (b % 2 == 1)
            result += a;
        a += a;
        b /= 2;
    }
    return result;
}

// 快速幂的本质是利用指数的二进制分解，
// 这段代码并没有显式地写出 “把 b 转成二进制”，而是通过算术运算（整除 2、取余 2）和循环，隐式地完成了二进制分解，并且在分解的同时完成了计算。
unsigned long long int fastPower(unsigned int a, unsigned int b)
{   
    if (b == 0)
        return 1;

    unsigned long long result = 1;
    while (b > 0)
    {
        if (b % 2 == 1)
            result *= a;
        a *= a;
        b /= 2;
    }
    return result;
}

/*
    这个快速乘的思路是：不直接计算完整的 a*b，而是通过数学变形，用浮点近似 + 整数运算抵消溢出，
    最终得到正确的模值，且整个过程只有算术运算，没有循环 / 递归，因此是 O (1) 复杂度。
    核心数学原理：模运算的变形
    我们要计算的是：res = (a × b) mod mod。
    根据模运算的定义，任意整数都可以拆成：a × b = k × mod + r（其中 0 <= r <= mod，r 就是我们要的结果）。
    变形得：r = a×b - k×mod，其中 k = floor(a×b / mod)（向下取整）。
    这个函数的核心就是：先近似算出 k，再通过 a×b - k×mod 得到 r，最后调整符号确保非负。

    步骤 1：近似计算 k = floor (a×b /mod)
        (ld)a / mod * b：先把 a 转成 long double（80 位高精度浮点），除以 mod 后再乘 b，得到 a×b/mod 的近似值；
        再转成 ll（向下取整），得到 k 的近似值 c。
        为什么近似是准确的？因为 long double 的精度足够覆盖 ll 范围的乘法（80 位浮点能精确表示 64 位整数），
        所以 c 就是精确的 floor(a×b/mod)。
    步骤 2：计算 r = a×b - c×mod
        (ull)a * b：把 a/b 转成无符号 64 位（ull），即使相乘溢出，溢出后的结果也是 a×b mod 2^64（无符号溢出的定义），
        但结合 c×mod 的抵消，最终能得到正确的 r；
        (ull)c * mod：同理转成 ull 避免溢出；
        两者的差 res 就是 a×b - c×mod，这个值的范围是 (-mod, mod)（因为 c 是 floor(a×b/mod)）。
    步骤 3：调整符号
        (res + mod) % mod：如果 res 是负数（比如 a×b < c×mod 时），加 mod 再取模，确保结果落在 [0, mod) 区间。
*/
long long int fastModMultiply(long long int a, long long int b, long long int mod)
{
    long long int tmp = (long double) a / mod * b;
    long long int res = (unsigned long long int) a * b - (unsigned long long int) tmp * mod;
    return (res + mod) % mod;
}


long long int fastModPower(long long int a, long long int b, long long int mod)
{
    long long int res = 1;
    while (b > 0)
    {
        if (b & 1)
            res = fastModMultiply(a, b, mod);
        a = fastModMultiply(a, a, mod);
        b >>= 1;
    }
    return res;
}


#endif
