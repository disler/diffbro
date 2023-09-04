from typing import List
from .cmd import run_shell_command


def get_git_diff(only: List[str], ignore: List[str], branch: str = None):
    """
    Returns the git diff as a string
    If ignore is specified, diffs all files except those with those extensions
    If only is specified, only diffs files with those extensions
    If neither are specified, diffs all files
    """

    command = "git diff"

    if branch:
        print(f"Diffing against branch {branch}")
        command += f" {branch}"

    if only or ignore:
        command += " --"

    if ignore:
        print(f"Diffing ALL files except those with extensions {ignore}")
        files = " ".join(f"':(exclude)**/*{ext}' ':(exclude)*/{ext}" for ext in ignore)
        command += f" {files}"
    elif only:
        print(f"Diffing exclusively files with extensions {only}")
        files = " ".join(f"'**/*{ext}' '*{ext}'" for ext in only)
        command += f" {files}"
    else:
        print(f"Diffing all files (no extensions specified))")

    return run_shell_command(command)
