import re
from enum import Enum

class NumberEnum(Enum):
    zero = 0
    one = 1
    two = 2
    three = 3
    four = 4
    five = 5
    six = 6
    seven = 7
    eight = 8
    nine = 9

def main() -> None:
    lines = read_input()
    calibration_values: list[int] = []
    calibration_values_with_text: list[int] = []
    for line in lines:
        calibration_value = extract_calibration_value_from_digits(line, include_text_representation=False)
        calibration_value_with_text = extract_calibration_value_from_digits(line, include_text_representation=True)

        if calibration_value:
            calibration_values.append(calibration_value)

        if calibration_value_with_text:
            calibration_values_with_text.append(calibration_value_with_text)

    print(f"Solution for part 1: {sum(calibration_values)}")
    print(f"Solution for part 2: {sum(calibration_values_with_text)}")
        
def read_input() -> list[str]:
    """Read input file line by line."""
    with open("input.txt", "r") as input_file:
        lines = input_file.readlines()
    
    return lines

def get_value_from_tuple(str_value: str) -> int:
    """Extract value from regex match."""
    if str_value in NumberEnum._member_map_:
        return NumberEnum._member_map_[str_value].value

    return int(str_value)

def extract_calibration_value_from_digits(value: str, include_text_representation: bool = False) -> int | None:
    """Extract first and last int value from line (part 1)."""
    if not include_text_representation:
        re_filter = "[0-9]"
    else:
        re_filter = "|".join([f"{val}" for val in NumberEnum._member_names_] + ["[0-9]"])

    detected_numbers = re.findall(re_filter, value)
    if not detected_numbers:
        return None
    
    first_number = get_value_from_tuple(detected_numbers[0])
    last_number = get_value_from_tuple(detected_numbers[-1])
    number = first_number * 10 + last_number
    return number


if __name__ == "__main__":
    main()
    