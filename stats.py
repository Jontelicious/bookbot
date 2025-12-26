def get_num_words(words):

    count_words = words.split()

    num_words = len(count_words)

    return num_words


def get_chars_dict(count):

    chars = {}

    for current in count:
        lowered_char = current.lower()

        if lowered_char in chars:
            chars[lowered_char] = chars[lowered_char] + 1

        else:
            chars[lowered_char] = 1

    return chars

def sort_on(item):

    return item["num"]


def chars_dict_to_sorted_list(item):
    char_list = []

    for char, count in item.items():
        char_list.append({
            "char": char,
            "num": count
        })

    char_list.sort(reverse=True, key=sort_on)

    return char_list


