def tax(incom):
    brackets = [0, 100000, 250000, 1000000]
    tax_rates = [0, 0.05, 0.10, 0.20]
    res = 0

    if(not isinstance(incom, (int, float))):
        return None

    for i in range(len(brackets) - 1, 0, -1):
        if(incom > brackets[i]):
            remain = incom - brackets[i]
            incom -= remain
            res += remain * tax_rates[i]
    return res
