def coin_bias(tosses):
    """
    Checks if the difference between heads and tails is outside the expected range.
    Counts the heads and tails, works out the drift and compares it with the square root of the number of tosses.
    Returns True if the drift is outside the range, otherwise False.

    """

    n = len (tosses)                        # Counts the tosses and works out the drift
    heads = tosses.count("H")
    tails = tosses.count("T") 
    drift = heads - tails
    limit = n ** 0.5                        # Works out the square root of the number of tosses

    if drift > limit or drift <-limit:      # Checks if the drift is outside the positive or negative limit
      return True 
    else:
      return False


def main():
    print("Inside main() of coin_bias.py")

    # Tests an empty string, which should return False
    assert coin_bias ("") == False

    # Tests when the drift is outside the expected range
    assert coin_bias ("HTHHTHH") == True
    
    # Tests when the drift is exactly equal to the limit
    assert coin_bias ("HHHT") == False

    print ("All tests passed")

if __name__ == "__main__":
    main()
