# filter_dictionary.py

def filter_dictionary(input_path="dictionary.txt", output_path="dictionary.txt", min_length=4):
    """
    Reads a dictionary file and writes back only words match certain conditions.
    """
    with open(input_path, 'r') as infile:
        words = [line.strip() for line in infile if filter_word(line.strip())]
    
    print(f"Total words after filtering: {len(words)}")

    with open(output_path, 'w') as outfile:
        for word in words:
            outfile.write(word + '\n')

    print(f"Filtered dictionary written to '{output_path}' with {len(words)} words (≥ {min_length} letters).")


def filter_word(word):
    """
    Returns True if
    The word length is >= 4 and contains at least one vowel,
    Else False.
    """
    return len(word) >= 4 and any(c in 'aeiouy' for c in word.lower())


if __name__ == "__main__":
    filter_dictionary()
