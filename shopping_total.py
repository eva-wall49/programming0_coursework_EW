def shopping_total(prices):
    """
    Adds together all the prices in the shopping list.
    If the total is below £20, a £3.50 delivery charge is added.
    A total of £20 or more has no delivery charge. Returns 0 if the shopping list is empty.
    """
    total = 0                                      # If the shopping list is empty, return 0 as there is nothing to deliver
    if prices == []:
        return total
    else:
     for price in prices:                          # Goes through each price and adds it to the total
        total += price
    if total < 20:                                 # Adds the delivery charge if the total is below £20
            total += 3.50
    return total


def main():
    print("Inside main() of shopping_total.py")

    # Tests a total below £20 where the delivery charge is added
    assert shopping_total([8.90, 4.50]) == 16.90
    
    # Tests a total above £20 where no delivery charge is added
    assert shopping_total([6.50, 18.70]) == 25.20
    
    # Tests exactly £20, which shouldn't have a delivery charge
    assert shopping_total([9.60, 10.40]) == 20.00
    
    # Tests an empty basket, which should return 0
    assert shopping_total([]) == 0.00

    print ("All tests passed")


if __name__ == "__main__":
    main()
