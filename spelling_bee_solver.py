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


def main():
    dictionary_path = "dictionary.txt"
    letters = input("Enter 7 distinct letters (e.g. 'abcdefg'): ").strip().lower()

    if len(letters) != 7 or len(set(letters)) != 7 or not letters.isalpha():
        print("Error: please enter exactly 7 distinct alphabetic letters.")
        return

    words = load_dictionary(dictionary_path)
    valid_words = find_valid_words(words, letters)

    print(f"\nValid words using '{letters}' (must include '{letters[0]}'):\n")
    for word in sorted(valid_words, key=lambda w: (-len(w), w)):
        print(word)


if __name__ == "__main__":
    main()
