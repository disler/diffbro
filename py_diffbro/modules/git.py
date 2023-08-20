from typing import List
from .cmd import run_shell_command


def get_git_diff(only: List[str], ignore: List[str]):
    if only:
        files = ' '.join(f"'**/*{ext}'" for ext in only)
        command = f"git diff -- {files}"
    elif ignore:
        files = ' '.join(f":(exclude)'**/*{ext}'" for ext in ignore)
        command = f"git diff -- . {files}"
    else:
        command = "git diff"
    return run_shell_command(command)
