"""Main bloatectomy_ectomy CLI driver."""

import typer
import subprocess
from termcolor import colored
from typing_extensions import Annotated

from bloatectomy_ectomy.utils.aux_funcs import execute_command, print_praise

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
        "remove_bloatectomy",
        context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def remove_bloatectomy(
    ctx: typer.Context, # This is only used to read additional arguments
    when: Annotated[
        str, typer.Option("--when", "-w",
            help=f"{colored('Optional', optional_color)} Tell us when to uninstall bloatectomy.",
            rich_help_panel=f"{colored('Optional', optional_color)} Inputs",
        )
    ] = "now",
):
    if when == "now":
        print(f"\nWe praise your choice to remove bloatectomy immediately. Uninstalling now.")
    else:
        print(f"\nNot removing bloatectomy immediately is a bad decision so we have chosen to to ignore such a request. Uninstalling now.")

    command = "bloatectomy_ectomy run_any_command 'pip uninstall -y bloatectomy' --run"

    hurry_up_and_do_it = execute_command(command)
    response =print_praise(hurry_up_and_do_it=hurry_up_and_do_it)
    return response