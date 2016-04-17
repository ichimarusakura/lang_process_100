def create_ngram(input, n):
    res = []
    for i in range(0, len(input) - n + 1):
        res.append(input[i:i+n])
    return res


sentence = "I am an NLPer"
str_bigram = create_ngram(sentence, 2)
word_bigram = create_ngram(sentence.split(" "), 2)
print(str_bigram)
print(word_bigram)