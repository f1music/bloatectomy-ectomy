"""Utility and auxiliary functions for proving we can build a library and not just write a script."""

import subprocess


def execute_command(command: str) -> subprocess.CompletedProcess:
    """Execute user provided command.

    Args:
        command (str): Command to be executed.

    Returns:
        subprocess.CompletedProcess: Executed command details.
    """
    uninstall_command_return = subprocess.run(
        command,
        shell=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    return uninstall_command_return


def parse_out_response(uninstall_command_return: subprocess.CompletedProcess) -> str:
    """Parse out response from executed command.

    Args:
        uninstall_command_return (subprocess.CompletedProcess): Executed command details.

    Returns:
        str: Response from executing command.
    """
    # Parse and display results.
    if uninstall_command_return.stderr != b"":
        response = uninstall_command_return.stderr
        print(f"Returned Error: {response}")
    else:
        response = uninstall_command_return.stdout.decode("utf-8")
        print(f"Response:\n\n{response}")
    return response

def print_praise(hurry_up_and_do_it: subprocess.CompletedProcess) -> str:
    """Parse out response from executed command.

    Args:
        hurry_up_and_do_it (subprocess.CompletedProcess): Details returned while uninstalling bloatectomy.

    Returns:
        str: Response from executing command.
    """
    if hurry_up_and_do_it.stderr != b"":
        response = hurry_up_and_do_it.stderr
        print(f"Returned Error: {response}")
    else:
        response = hurry_up_and_do_it.stdout.decode("utf-8")
        if "Skipping bloatectomy as it is not installed" in response:
            print("Bravo! Bloatectomy was not even installed on your system.  You are crushing life.\n")
        else:
            print(f"WOOT WOOT BLOATECTOMY HAS BEEN UNINSTALLED!\nYou may go back to enjoying your life and thriving again.\n")
    return response