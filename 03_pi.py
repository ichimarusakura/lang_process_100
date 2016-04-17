import re

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = re.split("\W+", str)
words = list(filter(lambda w: len(w) > 0, words))

for word in words:
    print(len(word))