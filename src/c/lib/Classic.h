#include "Fast.h"
#ifndef CLASSIC
#define CLASSIC

// https://zhuanlan.zhihu.com/p/349360074
// Fermat 素性检验 + 二次探测定理
short isPrimeMillarRabinMethod(long long int val)
{
    if (val < 3 || val % 2 == 0)
        return val == 2;

    long long int u = val - 1;
    long long int t = 0;
    while (u % 2 == 0)
    {
        u /= 2;
        ++t;
    }

    long long int ud[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
    for (int i = 0; i < 7; i++)
    {
        long long int v = fastModPower(ud[i], u, val);
        if (v == 1 || v == val - 1 || v == 0)
            continue;

        for (int j = 1; j <= t; j++)
        {
            v = fastModMultiply(v, v, val);
            if (v == val - 1 && j != t)
            {
                v = 1;
                break;
            }

            if (v == 1)
                return 0;
        }
        if (v != 1)
            return 0;
    }
    return 1;
}


#endif
