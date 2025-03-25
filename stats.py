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