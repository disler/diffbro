import argparse
from py_diffbro.modules.constants import (
    DETAILED_DIFFBRO_DESCRIPTION,
    PROGRAMMING_FILE_EXTENSIONS,
)
from py_diffbro.modules.llm import prompt
from py_diffbro.modules.git import get_git_diff
from py_diffbro.modules.app_types import BroMode
from py_diffbro.modules.bro import SUMMARY_BRO_PROMPT, get_diffbro_prompt


def main():
    parser = argparse.ArgumentParser(
        description="Diffbro: Your AI Peer Review Bro",
        epilog=DETAILED_DIFFBRO_DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-c",
        "--chill",
        action="store_true",
        help="Get a chill, jr-level engineer, relaxed diffbro PR review",
    )
    parser.add_argument(
        "-m",
        "--mid",
        action="store_true",
        help="Get a mid-level engineer, diffbro PR review",
    )
    parser.add_argument(
        "-d",
        "--chad",
        action="store_true",
        help="Get a chad, sr-level engineer, intense diffbro PR review",
    )
    parser.add_argument(
        "-o",
        "--model",
        type=str,
        default="gpt-4",
        help="GPT model use 'gpt-3.5-turbo' or 'gpt-4'",
    )
    parser.add_argument(
        "--only",
        nargs="*",
        default=PROGRAMMING_FILE_EXTENSIONS,
        help="Only include files with these extensions",
    )
    parser.add_argument(
        "--ignore", nargs="*", default=[], help="Ignore files with these extensions"
    )
    parser.add_argument(
        "-p", "--prompt", type=str, default="", help="Specify a custom prompt"
    )
    parser.add_argument(
        "-s", "--summarize", action="store_true", help="Summarize the git diff"
    )
    parser.add_argument(
        "-r",
        "--peer-review",
        type=str,
        default="",
        help="Specify the branch to compare the git diff against",
    )
    args = parser.parse_args()

    model = args.model
    bro_mode: BroMode = BroMode.CHILL
    only = args.only
    ignore = args.ignore
    custom_prompt = args.prompt
    summarize = args.summarize
    peer_review = args.peer_review

    if args.mid:
        bro_mode = BroMode.MID
    elif args.chad:
        bro_mode = BroMode.CHAD
        if model != "gpt-4":
            user_input = input(
                "Chad mode is engaged. It is suggested to use 'gpt-4' model for optimal results. Do you want to switch to 'gpt-4'? (y/n): "
            )
            if user_input.lower() in ["yes", "y"]:
                model = "gpt-4"

    git_diff = get_git_diff(only, ignore, peer_review)

    if not git_diff:
        print(f"No git diff for diffbro")
        return

    print(
        f"Building prompt for diffbro in bromode: '{bro_mode}' mode on GPT model '{model}'"
        f"{f' with custom prompt: {custom_prompt}' if custom_prompt else ''}"
        f"{f' Will generate diff summary.' if summarize else ''}"
    )

    if not custom_prompt:
        prompt_text = get_diffbro_prompt(bro_mode, git_diff)
    else:
        prompt_text = f"{custom_prompt}\n\n{git_diff}"

    print(f"Running DIFFBRO")

    diffbro_response = prompt(prompt_text, model)

    print("\n\nDIFFBRO\n\n", diffbro_response)

    if summarize:
        print(f"\n\nSummarizing git diff for diffbro on GPT model '{model}'")

        summary_prompt_text = f"{SUMMARY_BRO_PROMPT}\n\n{git_diff}"

        summary_diffbro_response = prompt(summary_prompt_text, model)

        print("\n\nDIFFBRO SUMMARY\n\n", summary_diffbro_response)


if __name__ == "__main__":
    main()
