def can_ride(height):
    """
    Returns True if someone meets the minimum height of 120 cm
    to go on the ride.
    
    Returns False if they are below the minimum height requirement.
    """
    if height >= 120:                       # Checks if the height is 120 cm or higher
        return True
    else: 
        return False


def main():
    print("Inside main() of can_ride.py")

# Tests if above minimum   
assert can_ride(123) == True

# Tests if below minimum   
assert can_ride(115) == False

# Tests if exactly 120cm, which should still be allowed 
assert can_ride(120) == True

print("All tests passed")


if __name__ == "__main__":
    main()
