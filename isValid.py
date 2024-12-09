class IsValid:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        
        abiertos = []
        
        parejas = {'(': ')', '[': ']', '{': '}'}
        for letra in s:
            if letra in parejas:
                abiertos.append(letra)
            elif not abiertos or parejas[abiertos.pop()] != letra:
                return False
        return len(abiertos) == 0
        