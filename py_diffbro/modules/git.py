from typing import List
from .cmd import run_shell_command


def get_git_diff(only: List[str], ignore: List[str]):
    """
    Returns the git diff as a string
    If only is specified, only diffs files with those extensions
    If only is not specified, and ignore is specified, diffs all files except those with those extensions
    If neither are specified, diffs all files
    """
    if only:
        print(f"Diffing exclusively files with extensions {only}")
        files = " ".join(f"'**/*{ext}'" for ext in only)
        command = f"git diff -- {files}"
    elif ignore:
        print(f"Diffing all files except those with extensions {ignore}")
        files = " ".join(f":(exclude)'**/*{ext}'" for ext in ignore)
        command = f"git diff -- . {files}"
    else:
        print(f"Diffing all files (no extensions specified))")
        command = "git diff"
    return run_shell_command(command)
