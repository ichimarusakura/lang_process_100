import re

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
symbols = list(filter(lambda word: len(word) > 0, re.split("\W", str)))

is_single_word = lambda n: n in [1, 5, 6, 7, 8, 9, 15, 16, 19]
for i in range(0, len(symbols)):
    symbol = symbols[i]
    if is_single_word(i+1):
        print(symbol[0:1])
    else:
        print(symbol[0:2])