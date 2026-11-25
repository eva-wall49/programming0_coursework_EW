def is_binary_mutation_list(codes):
    """
    The function checks whether each neighbouring binary code differs in exactly one position
    Each code is compared with the code after it, and the number of different positions is counted. 
    The function returns false if it does not have exactly one difference, otherwise it returns true.
    """

    for i in range (len (codes) -1):                                        # Goes through each code and compares it with the code after it, starting at position 0,
        different_positions = 0                                             # also stopping it going beyond the given length
        
        for j in range (len (codes [i])):                                   # Goes through each position in the two codes and counts any differences
            if codes [i][j] != codes [i + 1][j]:                            # If the characters are diffferent, count another different position
                different_positions += 1
            
        if different_positions != 1:                                        # If the two codes do not differ in exactly one position, it will fail
            return False
           
    return True


def main():
    print("Inside main() of is_binary_mutation_list.py")

    #Test true is returned when every pair differs in exactly one position
    assert is_binary_mutation_list (["000", "010", "011", "111"]) == True        
    
    #Test false is returned when a pair has more than one differences
    assert is_binary_mutation_list (["000", "001", "110"]) == False               
    
    #Test fasle is returned when there are no differences
    assert is_binary_mutation_list (["101", "101"]) == False                      
    
    #Test true is returned when there is only one code and no pairs to compare against
    assert is_binary_mutation_list (["101"]) == True                              

    print ("All tests passed")

if __name__ == "__main__":
    main()
