class RomanToInt:
    def romanToInt(self, s: str) -> int:
        numeros = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        entero = 0
        for i in range(len(s) - 1):
            if numeros[s[i]] < numeros[s[i + 1]]:
                entero -= numeros[s[i]]
            else:
                entero += numeros[s[i]]
        return entero + numeros[s[-1]]
