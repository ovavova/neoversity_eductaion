def get_fullname(first_name: str, last_name: str, middle_name = "") -> str:
    if middle_name:
        name = f'{first_name} {middle_name} {last_name}'
    else:
        name = f'{first_name} {last_name}'
    return name
