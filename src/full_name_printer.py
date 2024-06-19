def get_formatted_name (last, occupation, middle):

    initials = []

    for m in middle:
        initials.extend(m[0])

    middle_str = ".".join(initials)

    full_name = f"{middle_str.title()}. {last.title()}, {occupation.lower()}"

    return full_name

if __name__ == "__main__":
    
    print ()
    last = input ("\tKindly enter your family name: ")
    middle = input ("\tPlease provide your given name, and if you have any, list your middle names separated by spaces: ").split (" ")
    occupation = input ("\tWhat is your current occupation or profession? ")

    print ()
    print (f"\tIntroducing {get_formatted_name(last, occupation, middle)}")
    print ()