from data_utils import load_data


def rainfall_summary(rows):
    """
    Uses the valid rainfall rows to calculate a rainfall summary.
    Rows with missing rainfall or the wrong number of values are skipped.
    Estimated rainfall has the * removed before being used.

    Returns the number of months used, mean rainfall, and the year and month with the highest rainfall.

    """
    months_used = 0
    total_rainfall = 0
    wettest_rainfall = 0
    wettest_year = 0
    wettest_month = 0

    for row in rows:
        if len(row) != 7:                                               # Skip rows that do not have exactly 7 values
          continue
        
        if row[5] == "---":                                             # Skip row if rainfall is missing, wwhich is defined by "---"
            continue

        rainfall = row[5]

        if rainfall.endswith("*"):                                      # Discovering if rainfalls value ends with '*', if it does, remove it. 
            rainfall = rainfall.strip("*")                              
        rainfall = float(rainfall)                                      # Make all rainfall values a float, not just values that end with '*' 
                                                                        # (Therefore, outside of the if statement)
        months_used +=1
        total_rainfall += rainfall

        if rainfall > wettest_rainfall:                                 # If this rainfall is the highest found so far, remember its rainfall, year and month
            wettest_rainfall = rainfall
            wettest_year = int(row[0])
            wettest_month = int (row[1])

    mean_rainfall = total_rainfall / months_used                        # Calculate the mean rainfall and round it to 1 decimal place
    mean_rainfall = round (mean_rainfall, 1)

    return [months_used, mean_rainfall, wettest_year, wettest_month]

       
    
def main():
    print("Inside main() of rainfall_summary.py")

    rows = load_data("paisleydata.txt")
    # one line of the file as a list of strings.

    # Print the head and tail of the data
    for row in rows[:5]:
        print(row)
    print(".\n.\n.")
    for row in rows[-5:]:
        print(row)


    # Test valid rainfall rows and calculating the mean
    assert rainfall_summary ([["2020", "1", "5", "2", "1", "20.0", "50"], ["2020", "2", "6", "3", "0", "40.0", "60"]]) == [2, 30.0, 2020, 2]
   
    # Tests when a missing rainfall value is skipped and moves on to the next row 
    assert rainfall_summary ([["2019", "11", "5", "2", "1", "20.0", "50"],["2020", "2", "6", "3", "0", "---", "60"],["2021", "7", "7", "4", "0", "40.0", "70"]]) == [2, 30.0, 2021, 7]

    # Tests when estimated rainfall (*) is still used and if not has it removed the '*'. As well as testing the mean rainfall has returned as a float
    assert rainfall_summary ([["2018", "4", "5", "2", "1", "20.0*", "50"],["2023", "9", "6", "3", "0", "40.0", "60"]]) == [2, 30.0, 2023, 9]

    # Tests that if two months have the same highest rainfall, the first one is kept
    assert rainfall_summary ([["2019", "6", "5", "2", "1", "50.0", "50"],["2023", "9", "6", "3", "0", "50.0", "60"]]) == [2, 50.0, 2019, 6]

    # Tests that '---' in another column does not cause valid rainfall to be skipped
    assert rainfall_summary ([["2020", "4", "---", "2", "1", "30.0", "50"],["2021", "8", "6", "3", "0", "50.0", "60"]]) == [2, 40.0, 2021, 8]

    # Tests that a row without exactly 7 values is skipped
    assert rainfall_summary([["Site", "closed"],["2022", "5", "6", "3", "0", "40.0", "60"]]) == [1, 40.0, 2022, 5]
    
    print ("All tests passed")


if __name__ == "__main__":
    main()
