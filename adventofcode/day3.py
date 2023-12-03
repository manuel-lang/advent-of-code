from rich import print
from adventofcode.helpers import read_input
from dataclasses import dataclass
import re
from typing import Generator


@dataclass(frozen=True)
class NumberRepresentation:
    value: int
    row: int
    column_start: int
    column_end: int

    def is_surrounded_by_symbol(self, symbol_map: list[list[bool]]) -> bool:
        """Check if number is surrounded by a symbol."""
        for check_row in range(self.row - 1, self.row + 2):
            for check_column in range(self.column_start - 1, self.column_end + 1):
                if (
                    is_in_boundaries(check_row, check_column, symbol_map)
                    and symbol_map[check_row][check_column]
                ):
                    return True

        return False


def main() -> None:
    lines = read_input(file_path="example_data/day3.txt")
    symbol_map = list(get_symbol_map(lines))
    number_reprs = list(get_numbers_with_indices(lines))

    # Quiz 1
    count = sum(
        [n.value for n in number_reprs if n.is_surrounded_by_symbol(symbol_map)]
    )
    print(f"Sum of numbers with adjacent symbols: {count}")

    # Quiz 2
    gears = get_gear_map(lines)
    gear_count = get_adjacent_numbers_of_gears_sum(gears, number_reprs)
    print(f"Sum of adjacent number of gears: {gear_count}")


def get_adjacent_numbers_of_gears_sum(
    gear_map: Generator[list[bool], None, None],
    number_represenations: list[NumberRepresentation],
) -> int:
    """Summarize all numbers where one gear (*) is surrounded by exactly two numbers."""
    gear_counts = []
    for row_index, row in enumerate(gear_map):
        for column_index, value in enumerate(row):
            if value:
                adjacent_numbers = set()
                for number_repr in number_represenations:
                    if number_repr.row in range(
                        row_index - 1, row_index + 2
                    ) and column_index in range(
                        number_repr.column_start - 1, number_repr.column_end + 1
                    ):
                        adjacent_numbers.add(number_repr)

                if len(adjacent_numbers) == 2:
                    prod = (
                        list(adjacent_numbers)[0].value
                        * list(adjacent_numbers)[1].value
                    )
                    gear_counts.append(prod)

    return sum(gear_counts)


def is_in_boundaries(row_index: int, column_index, map: list[list]) -> bool:
    """Check if a row index and a column index are within a map."""
    return (
        row_index >= 0
        and column_index >= 0
        and row_index < len(map)
        and column_index < len(map[0])
    )


def get_symbol_map(lines: list[str]) -> Generator[list[bool], None, None]:
    """Check for each position in a map if neither a number nor a dot is present."""
    non_symbol_filter = r"(\d|\.)"
    for line in lines:
        matches = list(re.finditer(non_symbol_filter, line))
        result = [True for _ in line]
        for m in matches:
            result[m.start()] = False
        yield result


def get_gear_map(lines: list[str]) -> Generator[list[bool], None, None]:
    """Get gear (*) positions in lines."""
    for line in lines:
        matches = re.finditer(r"\*", line)
        result = [False for _ in line]
        for m in matches:
            result[m.start()] = True
        yield result


def get_numbers_with_indices(
    lines: list[str]
) -> Generator[NumberRepresentation, None, None]:
    """Extract all numbers from lines."""
    for i, line in enumerate(lines):
        matches = re.finditer(r"\d+", line)
        for match in matches:
            yield NumberRepresentation(
                value=int(match.group()),
                row=i,
                column_start=match.start(),
                column_end=match.end(),
            )


if __name__ == "__main__":
    main()
