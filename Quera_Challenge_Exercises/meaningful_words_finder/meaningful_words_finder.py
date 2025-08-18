def check_words(text: str) -> dict[str, int]:
    raw_words = text.split()
    good_words = []
    result = {}

    for word in raw_words:
        alphas_l = [char for char in word if char.isalpha()]
        signs_l = [char for char in word if not char.isalpha() ]
        if len(alphas_l) > len(signs_l):
            good_words.append("".join(alphas_l).capitalize())
    for word in sorted(good_words):
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result
