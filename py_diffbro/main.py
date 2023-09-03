import argparse
from py_diffbro.modules.constants import PROGRAMMING_FILE_EXTENSIONS
from py_diffbro.modules.llm import prompt
from py_diffbro.modules.git import get_git_diff
from py_diffbro.modules.app_types import BroMode
from py_diffbro.modules.bro import get_diffbro_prompt


# here's a comment to test the git diff
def main():
    parser = argparse.ArgumentParser(
        description="Diffbro: Your AI Peer Review Bro",
        epilog="""
First export your api key, then run an example below.

You can get an API key here: https://platform.openai.com/account/api-keys

Export command
    `export OPENAI_API_KEY=<your openai apikey>`

Examples:
  * I want a chill review on my .py and .js files:
      diffbro --chill --only .py .js
  
  * I'm about to ship production, mission critical UI code, I need a hardcore review on my FE code:
      diffbro --chad --model gpt-4 --only .js .jsx .tsx .vue
  
  * I'm about to a fullstack app and need a comprehensive mid level review on all my code excluding .tsx files:
      diffbro --mid --model gpt-4 --ignore .tsx
  
  * I want legit reviews all the time:
      Create a bash alias: alias dbro='diffbro --chad --model gpt-4'
    """,
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
        default="gpt-3.5-turbo",
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
    args = parser.parse_args()

    model = args.model
    bro_mode: BroMode = BroMode.CHILL
    only = args.only
    ignore = args.ignore

    if args.mid:
        bro_mode = BroMode.MID
    elif args.chad:
        bro_mode = BroMode.CHAD
        if model != 'gpt-4':
            user_input = input("Chad mode is engaged. It is suggested to use 'gpt-4' model. Do you want to switch to 'gpt-4'? (yes/no): ")
            if user_input.lower() == 'yes':
                model = 'gpt-4'

    git_diff = get_git_diff(only, ignore)

    if not git_diff:
        print(f"No git diff for diffbro")
        return

    print(
        f"Building prompt for diffbro in bromode: '{bro_mode}' mode on GPT model '{model}'"
    )

    prompt_text = get_diffbro_prompt(bro_mode, git_diff)

    print(f"Running DIFFBRO")

    response = prompt(prompt_text, model)

    print("DIFFBRO\n\n", response)


if __name__ == "__main__":
    main()
