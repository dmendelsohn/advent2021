import argparse
import importlib

import days


def main(day_num: int, part_num: int) -> None:
    selected_solution_module = importlib.import_module(f"days.day{day_num:02d}.solution")
    selected_part_func = getattr(selected_solution_module, f"part_{part_num}")
    solution = selected_part_func()
    print(f"Day {day_num}, Part {part_num}: {solution}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser("TODO")
    parser.add_argument("-d", "--day", dest="day", type=int)
    parser.add_argument("-p", "--part", dest="part", type=int)
    args = parser.parse_args()
    main(args.day, args.part)
