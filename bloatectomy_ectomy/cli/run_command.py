"""Generalize CLI driver command intake."""

import typer
from termcolor import colored
from typing_extensions import Annotated

from bloatectomy_ectomy.utils.aux_funcs import execute_command, parse_out_response

typer.rich_utils.STYLE_METAVAR = "bold"
required_color = "light_red"
optional_color = "light_green"

Arg = typer.Argument
Opt = typer.Option
app = typer.Typer(
    name="bloatectomy_ectomy",
    rich_markup_mode="rich",
)

@app.command(
        "run_command",
        context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def run_command(
    ctx: typer.Context, # This is only used to read additional arguments
    command: Annotated[
        str, typer.Argument(...,
            help=f"{colored('Required', required_color)} Command to be executed.",
            rich_help_panel=f"{colored('Required', required_color)} Inputs"
        )
    ],
    run_not_echo: Annotated[
        bool, typer.Option("--no-echo/--echo", "--run/--no-run", "-r/-R", 
            help=f"{colored('Optional', optional_color)} Option to run or echo the entered command.",
            rich_help_panel=f"{colored('Optional', optional_color)} Inputs"
        )
    ] = True,
):
    if run_not_echo:
        uninstall_command = command
    else:
        uninstall_command = f"echo '{command}'"

    uninstall_command_return = execute_command(command=uninstall_command)

    response = parse_out_response(uninstall_command_return=uninstall_command_return)

    return response
