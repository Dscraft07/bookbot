def get_num_words(book):
    words = book.split()
    return len(words)

def get_num_chars(book):
    book = book.lower()
    res = {}
    chars = list(book)
    for char in chars:
        if char not in res:
            res[char] = 0
        res[char] += 1

    return res


def sort_dict(char_dict):
    res = []
    for k, v in char_dict.items():
        tmp = {}
        tmp["char"] = k
        tmp["num"] = v
        res.append(tmp)

    def sort_on(d):
        return d["num"]

    res.sort(reverse=True, key=sort_on)
    return res