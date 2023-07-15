class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        charList = list(s)
        i = 0
        j = len(charList) - 1
        while (i < j):
            if (charList[i] not in vowels):
                i += 1
                continue
            if (charList[j] not in vowels):
                j -= 1
                continue
            charList[i], charList[j] = charList[j], charList[i]
            i += 1
            j -= 1
        return ''.join(charList)
