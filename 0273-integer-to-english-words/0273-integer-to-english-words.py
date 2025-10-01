class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones_map = {
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
        }
        tens_map = {
            2: "Twenty",
            3: "Thirty",
            4: "Forty",
            5: "Fifty",
            6: "Sixty",
            7: "Seventy",
            8: "Eighty",
            9: "Ninety",
        }
        teens_map = {
            0: "Ten",
            1: "Eleven",
            2: "Twelve",
            3: "Thirteen",
            4: "Fourteen",
            5: "Fifteen",
            6: "Sixteen",
            7: "Seventeen",
            8: "Eighteen",
            9: "Nineteen"
        }

        res = []
        preceding_digit = 0
        curr_place = 0
        num_digits = 0
        while num:
            curr_place += 1
            digit = num % 10
            num //= 10

            if num_digits == 3:
                res.append("Thousand")
            elif num_digits == 6:
                if res[-1] == "Thousand":
                    res.pop()
                res.append("Million")
            elif num_digits == 9:
                if res[-1] == "Million":
                    res.pop()
                res.append("Billion")

            if curr_place == 3 and digit > 0:
                res.append("Hundred")

            if curr_place % 2 == 1 and digit > 0:
                res.append(ones_map[digit])
            elif digit == 1:
                if preceding_digit > 0:
                    res.pop()
                res.append(teens_map[preceding_digit])
            elif digit > 0:
                res.append(tens_map[digit])

            preceding_digit = digit
            curr_place %= 3
            num_digits += 1

        return " ".join(res[::-1])

"""
keep track of current digit's place
for each digit, determine the word given the place

ones digit is just number
1: One
2: Two
3: Three
4: Four
5: Five
6: Six
7: Seven
8: Eight
9: Nine
0: Zero       * Unless there are  preceding digits

tens digit:
1: Ten, Eleven, Twelve, [Prefix]teen    * Depends on following digit
2: Twenty
3: Thirty
4: Forty
5: Fifty
6: Sixty
7: Seventy
8: Eighty
9: Ninety
0: ""       * Nothing

hundreds digit:
[0-9]:      * Same as ones digit
Hundred     * Only if not 0

more preceding digits repeats pattern:
Thousand    * Only if any of the 3 digits is not 0
Million     * Only if any of the 3 digits is not 0
"""