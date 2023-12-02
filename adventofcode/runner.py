import click


@click.command()
@click.argument("day", default=1)
def run_script(day: int) -> None:
    """Run Advent of Code script for specific day."""
    module = __import__(f"adventofcode.day{day}", fromlist="adventofcode")
    main_func = getattr(module, "main")
    main_func()


if __name__ == "__main__":
    run_script()
