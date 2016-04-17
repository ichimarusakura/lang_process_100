def create_ngram(input, n):
    res = []
    for i in range(0, len(input) - n + 1):
        res.append(input[i:i+n])
    return res


bigram1 = set(create_ngram("paraparaparadise", 2))
bigram2 = set(create_ngram("paragraph", 2))

print(bigram1 ^ bigram2)
print(bigram1 & bigram2)
print(bigram1 - bigram2)

if "se" in bigram1:
    print("bigram of 'paraparaparadise' has 'se'.")
else:
    print("bigram of 'paraparaparadise' has not 'se'.")


if "se" in bigram2:
    print("bigram of 'paragraph' has 'se'.")
else:
    print("bigram of 'paragraph' has not 'se'.")
