from decimal import Decimal


def zad3():
    return [Decimal(20 + x * 5) / 10 for x in range(8)]


print(zad3())
