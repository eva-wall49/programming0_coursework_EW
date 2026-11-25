def tide_turns(heights):
    """
    Count how many times the tide changes direction. Heights are checked in order to see if 
    the tide is going up or down. 
    It returns the number of times the tide changes direction.
    """
    changes = 0 
    previous_direction = ""   

    for i in range (len(heights)-1):                    # Compares each height with the next height in the list
        if heights[i + 1] > heights[i]:                 # Works out if the tide is going up or down by comparing if the next height > the one its on
                                         
            current_direction = "up"
        else:  
            current_direction = "down"
       
        if previous_direction != "" and current_direction != previous_direction:
           changes += 1                                 # Adds a change if the direction is different from previous one
        
        previous_direction = current_direction          # Remembers the direction so it can do the next comparison in list
    return changes




def main():
    print("Inside main() of tide_turns.py")

    # testing so see that changes in the list matches to 3
    assert tide_turns ([6,7,5,3,4,1]) == 3 

    # testing to see if fewer than 3 readings returns 0
    assert tide_turns ([6,7,]) == 0    

    # Tests when the tide keeps going in the same direction
    assert tide_turns([2, 4, 6, 8]) == 0    

    print ("All tests passed")

if __name__ == "__main__":
    main()
