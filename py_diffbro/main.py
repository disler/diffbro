from modules.llm import prompt
from modules.git import get_git_diff


def main():
    git_diff = get_git_diff()

    print("git_diff", git_diff)


if __name__ == "__main__":
    main()
