def lift_distance(floors):
    """
   Calculates the total number of floors travelled by the lift.

   It compares each floor with the next floor and adds the
   distance travelled between them. 
   
   Returns 0 if there are fewer than two stops.
    """

    total = 0
    for i in range(len(floors) - 1):                        # Compares each floor with the next floor in the list
        total += abs(floors[i + 1] - floors[i])             # Used abs so travelling down doesn't give a negative distance
    return total

   
def main():
    print("Inside main() of lift_distance.py")

    # Tests several trips going both up and down
    assert lift_distance([0, 1, 0, 5, 3, 8]) == 14

    # Tests that one stop will return 0 as lift hasn't travelled
    assert lift_distance([8]) == 0

    # Tests that an empty list will return 0 as lift hasn't travelled
    assert lift_distance([]) == 0

    print ("All tests passed")


if __name__ == "__main__":
    main()
