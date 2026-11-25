def sticky_key(text, key):
    """
   Creates a new string from the text given. If a character matches the key, the character is added twice.
   All other characters are added once. Returns the completed string.
    """
    result = ""

    for char in text:                   # Goes through each character and adds it twice if it matches the key
        if char == key:                
            result += 2 * char
        else:                           # If character doesn't match, keep character as it is, only add once
            result += char

    return result


def main():
    print("Inside main() of sticky_key.py")

    # Tests a key that appears several times in the text
    assert sticky_key("banana", "a") == "baanaanaa"

    # Tests consecutive matching characters
    assert sticky_key("apple", "p") == "apppple"

    # Tests when the key does not appear, so the text stays unchanged
    assert sticky_key("kiwi", "v") == "kiwi"

    print("All tests passed")

if __name__ == "__main__":
    main()
