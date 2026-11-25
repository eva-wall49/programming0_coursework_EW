def space_shuttle(n, engine_present=True):
    """
    Creates a countdown from n for the space shuttle. 

    If the engine is present, the countdown stops at 1 and ends with Liftoff. 
    If the engine isn't present, then the countdown includes 0 and ends 
    with a different message. 

    Negative numbers will return the Ground Control message.
    """
    
    if n < 0:                                                               # If n is negative theres no countdown
        return "Ground Control, we have a problem"

    if n == 0 and engine_present == True:                                   # If n is 0 and the engine is present there is nothing to count down
        return "Liftoff!"

    result = ""                                                             # Using an empty string to build the countdown

    if engine_present == True:                                              # Countdown to 1 when the engine is present
            for number in range(n, 0, -1):
                result += str(number) + "..."
    
            result += "Liftoff!"

    else:                                                                   # Without the engine, include 0 in the countdown
            
        for number in range(n, -1, -1):
            result += str(number) + "..."

        result += "That's another fine mess you've gotten me into, Stan"

    return result
        
       

def main():
    print("Inside main() of space_shuttle.py")

    # Testing a normal countdown with the engine, this checks the backwards couontdown and the noraml ending
    assert space_shuttle(4) == "4...3...2...1...Liftoff!"         
    
    #Testing no engine. Checks that the zero is included and correct ending is used
    assert space_shuttle (3, False) == "3...2...1...0...That's another fine mess you've gotten me into, Stan"

    #Test starting at 0 returns correctly
    assert space_shuttle(0) == "Liftoff!"

    #Tests when there is a negative value so it doesn't attempt a countdown
    assert space_shuttle(-2) == "Ground Control, we have a problem"

    print ("All tests passed")

if __name__ == "__main__":
    main()
