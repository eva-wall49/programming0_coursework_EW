def valid_dice(roll):
    """
    Checks if a number could be rolled on a normal six-sided dice. 
    Returns True if the roll is between 1 and 6, including 1 and 6.
    Returns False if the roll is outside this range.

    """
    if roll >=1 and roll <=6:          # Checks that the roll is within both limits of a six-sided dice
        return True
    else:
        return False


def main():
    print("Inside main() of valid_dice.py")
    
    # Tests the highest valid roll
    assert valid_dice(6) == True

    # Tests a roll below the valid range
    assert valid_dice(0) == False

    # Tests a roll above the valid range
    assert valid_dice(8) == False

    # Tests the lowest valid rollS
    assert valid_dice(1) == True
    
    print("All tests passed")

if __name__ == "__main__":
    main()
