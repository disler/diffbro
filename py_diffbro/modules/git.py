from typing import List
from .cmd import run_shell_command


def get_git_diff(only: List[str], ignore: List[str]):
    command = "git diff -- '**/*.py'"  # need to make this dynamic
    return run_shell_command(command)
