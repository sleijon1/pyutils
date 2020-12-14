from functools import reduce


def crt(mod: list, remainders: list):
    """ Chinese remainder theorem. Given
    a set of pairwise coprime divisors and
    their remainders returns the unique remainder
    of the divison by all of them

    Keyword args:
    mod -- the set of divisors
    remainders -- the set of remainders
    """
    products = []
    for i, _ in enumerate(mod):
        products.append(1)
        for j, divisor_2 in enumerate(mod):
            if i != j:
                products[i] *= divisor_2
        remainder = products[i] % mod[i]
        if remainder != remainders[i]:
            k = 1
            temp = remainder
            while True:
                temp = remainder
                if (temp*k) % mod[i] == remainders[i]:
                    products[i] *= k
                    break
                k += 1
    valid = sum(products)
    divisible = reduce((lambda x, y: x*y), mod)
    # Reduce our valid number to the smallest possible
    while True:
        temp = valid
        temp -= divisible
        if temp < 0:
            break
        valid = temp
    return valid
