def get_formatted_name (last, occupation, *middle):

    initials = []

    for m in middle:
        initials.extend(m[0])

    middle_str = ".".join(initials)

    full_name = f"{middle_str.title()}. {last.title()}, {occupation.lower()}"

    return full_name