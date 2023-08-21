import ctypes as c
import numpy as np

def main():
    damageList = []
    for b in range (0,31):
        for a in range(b-1, 0, -1):
            damageList.append([a, b, max(0, instant_damage(b)) - instant_damage(a)])
    for i in range(0,33):
        damageList.append([i, instant_damage(i)])
    damageList = sorted(damageList, key = lambda x: x[-1])

    for i in damageList:
        print(i, floating_weirdness(i[-1]))


def instant_damage(potency):
    return np.int32(3 * 2**((potency % 32) + 1))

def floating_weirdness(damage):
    damage = float(damage)
    bits = float_to_bits(damage)
    exp = (bits >> 23) - 127
    new_mantissa = bits & 12 #bitmask 1100
    new_sign = bool((bits >> 4) & 1)
    if new_sign: weird_complement = ((4 - (new_mantissa >> 2)) & 3) << 2
    else: weird_complement = new_mantissa
    out = (1 - 2 * new_sign) * weird_complement * 2**(exp - 23)
    return out

def float_to_bits(x):
    x = c.c_float(x)
    return c.c_int.from_address(c.addressof(x)).value

main()
