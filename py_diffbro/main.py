import argparse
from modules.llm import prompt
from modules.git import get_git_diff

# here's a comment to test the git diff
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--chill', action='store_true')
    parser.add_argument('-m', '--mid', action='store_true')
    parser.add_argument('-d', '--chad', action='store_true')
    args = parser.parse_args()

    git_diff = get_git_diff()

    print("git_diff", git_diff)
    print("chill", args.chill)
    print("mid", args.mid)
    print("chad", args.chad)

if __name__ == "__main__":
    main()
    main()
