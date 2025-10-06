print("This app can translate every number to roman numerals")
print("even 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000")
print("but it will take a while...")
print("Let's Mergi(go in Romanian)!")

class RomanNumerals:
    # We are using Operator Overloading here to create the roman number system
    def __init__(self, value):
        self.value = int(input("Enter a number to translate to roman numerals: "))
    def in_to_roman(self, point1):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
            ]
        syms = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
            ]
        roman_num = ''
        i = 0
        while point1 > 0:
            for _ in range(point1 // val[i]):
                roman_num += syms[i]
                point1 -= val[i]
            i += 1
        return roman_num
    def __str__(self):
        return self.in_to_roman(self.value)
num = RomanNumerals(0)
print(num)
# The code above is a simple implementation of converting an integer to Roman numerals using a class and operator overloading.
# The code below is a simple flashcard app that allows users to create and view flashcards.