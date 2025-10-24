# word_finder.py

def load_dictionary(filepath):
    """Load words from a dictionary file, stripping whitespace."""
    with open(filepath, 'r') as f:
        return [line.strip().lower() for line in f if line.strip()]


def find_valid_words(words, letters):
    """
    Find all words that:
      - Are at least 4 letters long
      - Contain only letters from the given 7
      - Contain the first letter of the 7
    """
    required = letters[0]
    valid_letters = set(letters.lower())

    valid_words = []
    for word in words:
        if len(word) >= 4 and required in word and set(word).issubset(valid_letters):
            valid_words.append(word)
    return valid_words


def sort_words(words, special_letters):
    """
    Given a list of words and a word containing 7 special letters,
    returns a new list sorted by value of word descending.
    The value of a word is as follows:
    If the word is length 4: 1 point
    If the word is length N where N > 4: N points
    Additionally, if the word contains all of the special letters, it gets an extra 7 points.
    """
    def word_value(word):
        value = len(word) if len(word) > 4 else 1
        if all(letter in word for letter in special_letters):
            value += 7
        return value

    return sorted(words, key=word_value, reverse=True)


def main():
    dictionary_path = "dictionary.txt"
    letters = input("Enter 7 distinct letters (e.g. 'abcdefg'): ").strip().lower()

    if len(letters) != 7 or len(set(letters)) != 7 or not letters.isalpha():
        print("Error: please enter exactly 7 distinct alphabetic letters.")
        return

    words = load_dictionary(dictionary_path)
    valid_words = find_valid_words(words, letters)
    # valid_words = sort_words(valid_words, special_letters=letters)

    print(f"\nValid words using '{letters}' (must include '{letters[0]}'):\n")
    for word in sort_words(valid_words, special_letters=letters):
        print(word)

    print(f"\nWords that use all letters '{letters}':\n")

    for word in [word for word in valid_words if all(letter in word for letter in letters)]:
        print(word)


if __name__ == "__main__":
    main()
