def image_smooth(image):
    """
    Creates a new version of an image without chaning original size.
    
    For each pixel, the fuction finds the neighbouring pixels to all sides of the pixel if they exist
    and returns the average in the form of an integer. 
    
    The new pixels are added to a new row, and the new rows are added to the new image. 
    """
    new_image = []                                                       # New image created so the originial is not changed
    
    for row in range (len (image)):                                      #Loops through each row and each pixel in the image
        new_row = []               
        
        for column in range (len (image [row])): 
            pixel = image [row][column]
            pixel_neighbour = [pixel]
            if row > 0:                                                  # Checking what neighbours exist to each pixel, and add them to the list
                pixel_neighbour.append(image[row-1][column])             # If there is a pixel above, add to the pixel_neighbours
            if row + 1 < len(image):
                pixel_neighbour.append(image[row+1][column])             # If there is a pixel below, add to the pixel_neighbours
            if column > 0:
                pixel_neighbour.append(image[row][column -1])            # If there is a pixel to the left, add to the pixel_neighbours
            if column + 1 < len(image[row]):
                pixel_neighbour.append(image[row][column + 1])           # If there is a pixel to the right, add to the pixel_neighbours

            average = sum(pixel_neighbour) / len(pixel_neighbour)        # Works out the avergae by adding the pixel itself and pixel neighbours together and dividng by the numbers of pixels that exists
            average = int(average)                                       # Converts to an integer each time after average returned, if average is a decimal, it will convert it to an integer
           
            new_row.append(average)                                      # Adds pixel to the new row 
        new_image.append(new_row)                                        # Adds comleted row to the new image 
    return new_image

def main():
    print("Inside main() of image_smooth.py")

    # Tests pixel stays the same after averaging
    assert image_smooth ([[8, 8, 8], [8, 8, 8], [8, 8, 8]]) == ([[8, 8, 8], [8, 8, 8], [8, 8, 8]]) 

    # Tests when a decimal is the average and the function returns an as integer
    assert image_smooth ([[5, 8, 10], [4, 2, 6], [12, 3, 6]]) == ([[5, 6, 8], [5, 4, 6], [6, 5, 5]]) 

    # Tests pixels on the corner when they only have two neighbours 
    assert image_smooth ([[10, 20],[30, 40]]) == ([[20, 23],[26, 30]]) 

    # Test single row with only left and right neighbours, no neighbours up or down
    assert image_smooth ([[12, 24, 42]]) == ([[18, 26, 33]]) 

    # Tests it stays the same if theres only one pixel, no nieghbours to add against
    assert image_smooth ([[58]]) == ([[58]]) 

    print ("All tests passed")
    

if __name__ == "__main__":
    main()
