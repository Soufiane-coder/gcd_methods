from performance import performance


@performance
def gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    if a == 0 or b == 0:
        return max(a, b)

    for num in range(min(a, b), 0, -1):
        if a % num == 0 and b % num == 0:
            return num

