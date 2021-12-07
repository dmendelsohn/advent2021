from pathlib import Path
from typing import List

INPUT_PATH = Path(__file__).parent / "input.txt"


def parse_input() -> List[str]:
    return open(INPUT_PATH).read().strip().split("\n")


def part_1() -> str:
    pass


def part_2() -> str:
    pass
