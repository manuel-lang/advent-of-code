def read_input() -> list[str]:
    """Read input file line by line."""
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()

    return lines