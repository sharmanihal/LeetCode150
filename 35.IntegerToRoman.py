class Solution:
    def intToRoman(self, num_con: int) -> str:
        # Dictionary to map integers to their corresponding Roman numerals
        roman_numerals = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX",
            10: "X", 20: "XX", 30: "XXX", 40: "XL", 50: "L", 60: "LX", 70: "LXX", 80: "LXXX", 90: "XC",
            100: "C", 200: "CC", 300: "CCC", 400: "CD", 500: "D", 600: "DC", 700: "DCC", 800: "DCCC", 900: "CM",
            1000: "M", 2000: "MM", 3000: "MMM"
        }
        
        # Check if the given number is directly available in the dictionary
        if int(num_con) in roman_numerals:
            return roman_numerals[int(num_con)]
        else:
            # Convert the number to an integer
            num = int(num_con)
            res = ""
            # Loop until the number becomes zero
            while num:
                # Find the highest divisor of the number
                divisor = 10 ** (len(str(num)) - 1)
                # Calculate the closest multiple of the divisor
                check = divisor * (num // divisor)
                # Append the corresponding Roman numeral to the result
                res += roman_numerals[check]
                # Update the number by removing the highest digit
                num = num % divisor
            return res
"""
Explanation:
- The `roman_numerals` dictionary maps integers to their Roman numeral equivalents(for just ones, tens and thousands).
- The method first checks if the integer input is directly available in the `roman_numerals` dictionary. If so, it returns the corresponding Roman numeral.
- If the integer is not directly available, it iterates through the digits of the input number, finding the highest divisor (e.g., 1000, 100, 10, or 1), and then appends the corresponding Roman numeral to the result string. It updates the number by removing the highest digit after each iteration until the number becomes zero. Finally, it returns the concate
"""

