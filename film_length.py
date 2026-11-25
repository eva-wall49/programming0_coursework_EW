def film_length(minutes, units="hours"):
    """
    Converts a number of minutes into hours and minutes or seconds.
    Hours are returned showing the whole hours and leftover minutes.
    If seconds are requested, the minutes are converted into seconds.

    """

    if units == "hours":                            # If hours are requested, work out the whole hours and leftover minutes
      if minutes >= 60:
        hours = minutes // 60                       # Works out how many whole hours are in the minutes
        remainder = minutes -(hours * 60)           # Takes away the minutes used in the whole hours to find what is left
      else: 
        hours = 0
        remainder = minutes
       
      return str(hours) + "h " + str (remainder)+ "m"
    
    else:
      seconds = minutes * 60
      return str(seconds) + "s"
    
    
def main():
    print("Inside main() of film_length.py")

    # Tests minutes that contain whole hours and leftover minutes
    assert film_length (135) == "2h 15m"

    # Tests less than one hour
    assert film_length (55) == "0h 55m"

    # Tests exactly one hour and still shows 0 minutes
    assert film_length(60) == "1h 0m"

    # Tests converting minutes into seconds
    assert film_length (2, "seconds") == "120s"

    print("All tets passed")


if __name__ == "__main__":
    main()
