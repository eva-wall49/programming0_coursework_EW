def name_badge(name, role):
    """
   Joins the name and role into a string. Adds "Hi, I'm" at the start and puts the role inside brackets
   after the name. The function returns greeting as a string.
    """  
    result = "Hi, I'm " + name + " (" + role + ")" 
    return result


def main():
    print("Inside main() of name_badge.py")

    # Tests a single-word name and role
    assert name_badge("Sade", "Singer") == "Hi, I'm Sade (Singer)"

    # Tests that a name containing a space
    assert name_badge("Miles Davis", "Musician") == "Hi, I'm Miles Davis (Musician)"
  
    print ("All tests passed")

if __name__ == "__main__":
    main()
