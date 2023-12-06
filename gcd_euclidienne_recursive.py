from performance import performance


@performance
def result(a, b):  # To calculate the time total time of operation
    def gcd(a, b):
        assert a >= b and b >= 0 and a + b > 0
        return gcd(b, a % b) if b > 0 else a
    return gcd(a, b)

