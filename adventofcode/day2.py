from adventofcode.helpers import read_input
from dataclasses import dataclass
import re
from rich import print


@dataclass
class LineInfo:
    game_id: int
    red_count: int
    green_count: int
    blue_count: int

    def is_possible(self) -> bool:
        return self.red_count <= 12 and self.green_count <= 13 and self.blue_count <= 14

    def multiply(self) -> int:
        return self.red_count * self.green_count * self.blue_count


def main():
    lines = read_input(file_path="example_data/day2.txt")
    required_cubes_per_lines = [get_required_cubes_from_line(line) for line in lines]
    possible_line_ids = [
        line_info.game_id
        for line_info in required_cubes_per_lines
        if line_info.is_possible()
    ]
    powered_required_cubes_per_line = [
        line_info.multiply() for line_info in required_cubes_per_lines
    ]
    print(f"Sum of game IDs that are possible: {sum(possible_line_ids)}")
    print(f"Sum of required cubes (powered): {sum(powered_required_cubes_per_line)}")


def get_required_cubes_from_line(line: str) -> LineInfo:
    """Extract information from input line.

    Information:
    - game_id
    - count of required cubes for each color (red, green, blue)
    """
    match = re.search("(?<=Game )[0-9]{1,3}(?=:)", line)
    game_num = int(match.group()) if match else 0
    num_red = max(
        [int(match) for match in re.findall("(?<= )[0-9]{1,2}(?= red)", line)]
    )
    num_green = max(
        [int(match) for match in re.findall("(?<= )[0-9]{1,2}(?= green)", line)]
    )
    num_blue = max(
        [int(match) for match in re.findall("(?<= )[0-9]{1,2}(?= blue)", line)]
    )
    return LineInfo(
        game_id=game_num, red_count=num_red, green_count=num_green, blue_count=num_blue
    )


if __name__ == "__main__":
    main()
