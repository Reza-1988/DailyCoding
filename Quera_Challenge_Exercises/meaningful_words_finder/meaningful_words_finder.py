def check_words(text: str) -> dict[str, int]:
    raw_words = text.split(" ")
    good_words = []
    final_words = []
    result = {}

    for word in raw_words:
        alphas_l = []
        signs_l = []
        for char in word:
            if char.isalpha():
                alphas_l.append(char)
            else:
                signs_l.append(char)
        if len(alphas_l) > len(signs_l):
            good_words.append(word.capitalize())
    for word in good_words:
        w = []
        for char in word:
            if char.isalpha():
                w.append(char)
        final_words.append("".join(w))
    for word in final_words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result


print(check_words("""hEllO My FriEnDs!!! thIS is A tEsT For your #p#r#o#b#l#e#m a"""))