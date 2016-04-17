import random

def shuffle_sentence(input):
    res_words = []

    for word in input.split(" "):
        if len(word) > 4:
            shuffle_str = list(word[1:len(word) - 1])
            random.shuffle(shuffle_str)
            res_words.append(word[0:1] + "".join(shuffle_str) + word[len(word) - 1:len(word)])
        else:
            res_words.append(word)
    return " ".join(res_words)

shuffled_sentence = shuffle_sentence("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind .")
print(shuffled_sentence)