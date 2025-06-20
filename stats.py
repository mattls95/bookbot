def get_number_of_words(text):
    words = text.split()
    return len(words)

def number_of_characters(text):
    dictionary = {}
    for char in text:
        if char.lower() in dictionary:
            dictionary[char.lower()] += 1
        else:
            dictionary[char.lower()] = 1
        
    return dictionary

def sort_on(items):
    return items[1]

def sort_dictionary(dictionary):
    list_of_dict = list(dictionary.items())
    return sorted(list_of_dict, reverse=True, key=sort_on)


