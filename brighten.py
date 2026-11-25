def brighten(image, amount):
    """
    Creates a new image by adding the given amount to every pixel. Pixel values are kept between 0 and 255. 
    Values above 255 become 255 and values below 0 become 0. 
    Returns the new image without changing the original image.
    
    """
    
    new_image = []
    
    for row in image:                           # Goes through each row and each pixel in the image
        new_row = []                    
        
        for pixel in row:
            new_pixel = pixel + amount
            if new_pixel > 255:                 # Keeps pixel values from going above 255
                new_pixel = 255
            if new_pixel < 0:                   # Keeps pixel values from going below 0
               new_pixel = 0
            new_row.append(new_pixel)           # Adds the changed pixel to the new row
        new_image.append(new_row)               # Adds the completed row to the new image
   
    return new_image

def main():
    print("Inside main() of brighten.py")

    # Tests adding 10 and making sure a pixel cannot go above 255
    assert brighten([[250, 180], [100, 20]], 10) == [[255, 190], [110, 30]]
    
    # Tests subtracting 10 and making sure a pixel cannot go below 0
    assert brighten([[5, 50], [100, 200]], -10) == [[0, 40], [90, 190]]

    print ("All tests passed")
    

if __name__ == "__main__":
    main()
