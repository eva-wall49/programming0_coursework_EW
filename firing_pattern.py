def firing_pattern(motif, seconds):
    """
   Repeats the motif for the number of seconds given. A 1 means the neuron fires and a 0 means it doesn't.
   The function counts how many 1s appear in the repeated pattern and returns the number of spikes. 
   Returns 0 if seconds is 0.
    
    """
    
    new_pattern = ""                                # Start with an empty pattern and position 0 in the motif
    i = 0
    
    if seconds == 0:
            return 0
    
    while len(new_pattern) != seconds:              # Keep adding characters from the motif until the seconds needed are reached
        if i >= len(motif):                         # Start again from position 0 when the end of the motif is reached
            i = 0
            new_pattern += motif[i]
        else: 
            new_pattern += motif[i] 
            i += 1
    print(new_pattern)
    count = new_pattern.count("1")                  # Count the 1s in the finished pattern to get the number of spikes

    return count
    

def main():
    print("Inside main() of firing_pattern.py")
   
    # Tests that the motif repeats correctly over several seconds
    assert firing_pattern("110", 7) == 5    

    # Tests zero seconds, where no spikes can happen
    assert firing_pattern("110", 0) == 0

    # Tests a motif that contains no spikes
    assert firing_pattern("000", 5) == 0

    print ("All tests passed")

if __name__ == "__main__":
    main()
