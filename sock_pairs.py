def sock_pairs(socks):
    """
    Returns the number of matching pairs of socks in the list. A pair matches when both socks are the same colour.
    Returns 0 if there are no matching pairs or the list is empty.

    """
    pairs = 0

    for pair in socks:
      if pair[0] == pair[1]:        # Compares the two socks at positions 0 and 1 and adds 1 if they match
       pairs += 1
    return pairs                    # Returns number of pairs if they match


def main():
    print("Inside main() of sock_pairs.py")

    # Tests wehn all pairs match
    assert sock_pairs ([["red", "red"], ["purple", "purple"]]) == 2
    
    # Tests when no pairs match
    assert sock_pairs ([["red", "blue"], ["white,", "red"]]) == 0
    
    # tests an empty list returns 0 as there are no pairs
    assert sock_pairs ([]) == 0

    print ("All tests passed")


if __name__ == "__main__":
    main()
