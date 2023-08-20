import argparse
from py_diffbro.modules.llm import prompt
from py_diffbro.modules.git import get_git_diff
from py_diffbro.modules.app_types import BroMode
from py_diffbro.modules.bro import get_diffbro_prompt


# here's a comment to test the git diff
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--chill", action="store_true")
    parser.add_argument("-m", "--mid", action="store_true")
    parser.add_argument("-d", "--chad", action="store_true")
    parser.add_argument("-o", "--model", type=str, default="gpt-4")
    args = parser.parse_args()

    bro_mode: BroMode = BroMode.CHILL

    if args.mid:
        bro_mode = BroMode.MID
    elif args.chad:
        bro_mode = BroMode.CHAD

    git_diff = get_git_diff()

    if not git_diff:
        print(f"No git diff for diffbro")
        return

    prompt_text = get_diffbro_prompt(bro_mode, git_diff)

    response = prompt(prompt_text)

    print("DIFFBRO\n\n", response)


if __name__ == "__main__":
    main()
