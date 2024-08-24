
"""Main bloatectomy_ectomy CLI script."""

import sys
import typer
from wasabi import msg
from bloatectomy_ectomy.cli.run_command import run_command
from bloatectomy_ectomy.cli.main_purpose import remove_bloatectomy

def main():
    """Main typer CLI function."""

    commands = {
        "remove_bloatectomy": remove_bloatectomy,
        "run_any_command": run_command,
    }
    if len(sys.argv) == 1:
        msg.info("Available commands", ", ".join(commands), exits=1)
    command = sys.argv.pop(1)
    sys.argv[0] = f"bloatectomy_ectomy {command}"
    if command in commands:
        typer.run(commands[command])
    else:
        available = "Available: {}".format(", ".join(commands))
        msg.fail("Unknown Command: {}".format(command), available, exits=1)
