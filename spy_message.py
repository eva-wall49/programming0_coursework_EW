def spy_message(note, secret):
    """
    Checks if all the letters in secret can be found in the note in the correct order.
    The letters don't have to be next to each other.
    Returns True if all the secret letters are found, otherwise its False.

    """
    secret_position = 0                                           # Starts at position 0, which is the first letter of the secret

    for char in note:                                               
        if char == secret[secret_position]:                       # If the character matches the secret letter being looked for,  
            secret_position += 1                                  # move to the next position in the secret
        if secret_position == len(secret):                        # If every letter in the secret has been found, return True
            return True
    return False

def main():
    print("Inside main() of spy_message.py")

    # Tests when all secret letters can be found in the correct order
    assert spy_message ("swim in the sea", "sit") == True

    # Tests when there are not enough matching letters in the note
    assert spy_message ("Eva", "vva") == False

    # Tests when the letters exist but are not in the correct order
    assert spy_message("abcdef", "dac") == False

    print ("All tests passed")


if __name__ == "__main__":
    main()
