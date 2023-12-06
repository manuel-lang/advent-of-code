from adventofcode.helpers import read_input
import re


def main() -> None:
    lines = read_input(file_path="example_data/day4.txt")
    num_copies = [0] * len(lines)
    score_without_copies = 0
    overall_num_cards_with_copies = 0
    for line in lines:
        copies_for_card = num_copies.pop(0)
        num_matches, card_score = get_line_worth(line)
        score_without_copies += card_score
        num_cards_with_copies = 1 + copies_for_card
        overall_num_cards_with_copies += num_cards_with_copies
        for i in range(num_matches):
            num_copies[i] += num_cards_with_copies

    print(f"Sum of scratchcard points: {score_without_copies}")
    print(f"Sum of scratchcards with copies: {overall_num_cards_with_copies}")


def get_numbers_from_part(value: str) -> set[int]:
    """Extract all numbers from a string containing numbers."""
    str_numbers = re.findall(r"\d+", value)
    return {int(nr) for nr in str_numbers}


def get_line_worth(line: str) -> tuple[int, int]:
    """Count worth of a line based on matches."""
    numbers_part = line.split(": ")[1]
    winning_numbers = get_numbers_from_part(numbers_part.split("|")[0])
    given_numbers = get_numbers_from_part(numbers_part.split("|")[1])
    num_matches = len(given_numbers & winning_numbers)
    if num_matches == 0:
        return 0, 0
    return num_matches, 2 ** (num_matches - 1)


if __name__ == "__main__":
    main()
