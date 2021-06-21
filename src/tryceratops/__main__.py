import logging.config

import click

import tryceratops
from tryceratops.analyzers import Runner
from tryceratops.main import parse_python_files_from_dir
from tryceratops.settings import ERROR_LOG_FILENAME, LOGGING_CONFIG

runner = Runner()


def print_finished_status():
    print("Done processing! 🦖✨")
    print(f"Processed {runner.analyzed_files} files")
    print(f"Found {len(runner.violations)} violations")

    if runner.had_issues:
        print(
            f"Had {len(runner.runtime_errors)} unexpected issues "
            f"stored in {ERROR_LOG_FILENAME}"
        )


@click.command()
@click.argument("dir")
@click.version_option(tryceratops.__version__)
def entrypoint(dir: str):
    parsed_files = list(parse_python_files_from_dir(dir))
    violations = list(runner.analyze(parsed_files))

    for violation in violations:
        print(str(violation))

    print_finished_status()


def main():
    logging.config.dictConfig(LOGGING_CONFIG)
    entrypoint()


if __name__ == "__main__":
    main()
