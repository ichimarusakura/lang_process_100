def create_sentence(x, y, z):
    return "{0}時の{1}は{2}".format(x, y, z)

print(create_sentence(12, "気温", 22.4))