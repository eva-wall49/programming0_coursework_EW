def clear_full_rows(grid):
    """
    Full rows are rows with all 1s. 
    This function removes all full rows from the grid and replaces them 
    with new rows with the same amount of 0s and places them at the top of newly returned grid.
    
    """
    remaining_rows = []
    full_rows = 0

    for row in grid:                        # Goes through each row 
        is_full = True

        for value in row:                   # Checking full rows for a zero, stating when a row is not full by 'false'
            if value == 0:
             is_full = False
        
        if is_full:                 
                                            # If row is full, count it as a full row, otherwise add the originalrow to the neww grid
           full_rows += 1   
        else: 
            remaining_rows.append(row)

    for i in range(full_rows):              # Relace each full row with sam number of 0s to values in row, then insert row of zeros at the top of grid
            row_zeros = [0] *len(row)
            remaining_rows.insert (0, row_zeros)

    return remaining_rows
        

def main():
    print("Inside main() of clear_full_rows.py")

    # Test grid with more than one full row
    assert clear_full_rows (([[1,1,1], [0,1,0],[1,1,1]])) == [[0,0,0], [0,0,0], [0,1,0]]
   
    # Test grid with only one full row 
    assert clear_full_rows ([[1,0,0], [0,0,1], [1,1,1]]) == [[0,0,0], [1,0,0], [0,0,1]]
   
    # Test grid with no full rows
    assert clear_full_rows ([[0,0,1], [0,1,0], [1,0,1]]) == [[0,0,1], [0,1,0], [1,0,1]]

    # test grid with row more than three numbers 
    assert clear_full_rows ([[1,0,0,1], [0,0,0,0], [1,1,1,1]]) == [[0,0,0,0], [1,0,0,1], [0,0,0,0]]

    print ("All tests passed")

if __name__ == "__main__":
    main()
