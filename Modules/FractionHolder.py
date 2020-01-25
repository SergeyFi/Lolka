
class FractionHolder:

    def __init__(self, period: str):
        self._numerator = int(period)
        self._period_list = list(period)
        self._denominator = 10**len(self._period_list) - 1

        self._gcd = self._find_gcd(self._numerator, self._denominator)

        self._numerator /= self._gcd
        self._denominator /= self._gcd

    def get_answer(self):
        return self._numerator / self._denominator

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self._denominator

    def _find_gcd(self, m: int, n: int):

        if m == 0:
            return n

        if n == 0:
            return m

        if m == n:
            return m

        if m == 1 or n == 1:
            return 1

        if m % 2 == 0 and n % 2 == 0:
            return 2 * self._find_gcd(int(m / 2), int(n / 2))

        if m % 2 == 0 and n % 2 != 0:
            return self._find_gcd(int(m / 2), n)

        if n % 2 == 0 and m % 2 != 0:
            return self._find_gcd(m, int(n / 2))

        if m % 2 != 0 and n % 2 != 0 and n > m:
            return self._find_gcd(int((n - m) / 2), m)

        if m % 2 != 0 and n % 2 != 0 and n < m:
            return self._find_gcd(int((m - n) / 2), n)
