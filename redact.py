def redact(sentence, banned):
    """
    Starts with a sentence and a list of banned words and 
    replaces any banned words with the same number of asterisks 
    per letter in the banned word, then returns the sentence.
    """
    words = sentence.split()                        # Splits the sentence into separate words and creates a new list for the result
    new_words =[]

    for word in words:
        if word in banned: 
            new_words.append ("*" * len(word))      # Replaces a banned word with the same amount of asterisks per letter in that word.
        else: new_words.append(word)                # If not a banned word, keep the word
    return " ".join(new_words)                      # Join new appended words together with spaces to form a new sentence


def main():
    print("Inside main() of redact.py")

    # Tests replacing more than one banned word
    assert redact ("Green eggs and ham", ["eggs", "ham"]) == "Green **** and ***"
    
    # Tests replacing one banned word
    assert redact ("The Twits", ["Twits"]) == "The *****"
    
    # Tests when none of the banned words appear, so the sentence stays the same
    assert redact ("George and the Giant Peach", ["Apple", "Banana"]) == "George and the Giant Peach"

    print ("All tests passed")
if __name__ == "__main__":
    main()
