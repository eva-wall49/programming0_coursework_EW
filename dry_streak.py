def dry_streak(rainfall):
    """
    Rainfall is a list measuring daily rain occurences. A value of 0 shows a dry day. 
    The function returns the longest streak of dry days in the list. 

    """
    current_streak = 0                                      # Keep track of the current dry streak and the longest streak found
    longest_streak = 0
    
    for day in rainfall:                                    # Goes through each daily rainfall value
        if day == 0:                                        # If the rainfall is 0, add another day to the current dry streak
            current_streak += 1
            if current_streak > longest_streak:             # If the current streak becomes longer than the streak before, make it new longest streak
                longest_streak = current_streak
        else:
            current_streak = 0                              # If it rains, the current dry streak ends and starts again from 0
    return longest_streak

def main():
    print("Inside main() of dry_streak.py")

# Tests multiple dry streaks and returns the longest one
assert dry_streak([0, 0, 1, 0, 0, 0, 0, 1, 0]) == 4

# Tests when there are no dry days
assert dry_streak([1, 1, 1, 1]) == 0

# Tests a shorter streak
assert dry_streak([0, 0, 1, 0]) == 2

print("All tests passed")
       

if __name__ == "__main__":
    main()
