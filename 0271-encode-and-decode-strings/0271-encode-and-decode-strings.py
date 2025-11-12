class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoding = []
        for s in strs:
            encoding.append(str(len(s)) + '#' + s)
        return ''.join(encoding)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # len is int(substring up to #)
        decoded = []
        i = 0
        while i < len(s):
            num = []
            while s[i] != '#':
                num.append(s[i])
                i += 1
            i += 1  # skip '#'
            num = int(''.join(num))
            decoded.append(s[i:i+num])
            i += num
        return decoded

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))