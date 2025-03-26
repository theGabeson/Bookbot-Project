def word_counter(text):
    word_number = len(text.split())
    return word_number

def character_counter(text):
    lowercase_text = text.lower()
    character_dict = {}
    for c in lowercase_text:
        if c in character_dict:
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    return character_dict

def sort_on(dict):
    return dict["count"]

def character_sorter(char_dict):
    chars_list = []
    for char, count in char_dict.items():
        chars_list.append({"char": char, "count": count})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list