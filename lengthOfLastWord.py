class LengthOfLastWord:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        arreglo = s.split(" ")
       
        
        return len(arreglo[-1])