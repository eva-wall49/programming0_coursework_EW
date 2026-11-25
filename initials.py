def initials(*names):
    """
    Returns the initals of one of more names.
    It takes the first letter  of each name, capitalises it and adds a full stop after each inital.
    It returns a string of the initals in the correct order of the names given.

    """
    result = ""

    for name in names:                              # Takes the first letter at position 0 from each name,
                                                    # capatalises it and adds a full stop
        result = result + name[0].upper() + "."

    return result

def main():
    print("Inside main() of initials.py")

    # Test two names returns
    assert initials("Miles", "Davis") == "M.D."

    # Test single name returns
    assert initials("Sade") == "S."
    
    # Test more than two names can be returned
    assert initials("Miles", "Sade", "David") == "M.S.D."

    print ("All tests passed")

if __name__ == "__main__":
    main()

