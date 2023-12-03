def read_input(file_path: str) -> list[str]:
    """Read input file line by line."""
    with open(file_path, "r") as input_file:
        lines = input_file.read().splitlines()

    return lines
