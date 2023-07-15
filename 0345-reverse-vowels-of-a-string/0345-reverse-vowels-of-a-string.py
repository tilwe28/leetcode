class Solution:
    def reverseVowels(self, s: str) -> str:
        def isVowel(c: str) -> bool:
            c = c.lower()
            if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
                return True
            else:
                return False
        
        consonants = [c for c in s if not isVowel(c)]
        consonants.reverse()
        vowels = [c for c in s if isVowel(c)]
        
        result = ""
        
        for c in s:
            if isVowel(c):
                result += vowels.pop()
            else:
                result += consonants.pop()
        return result