# diffbro - AI Powered Peer Reviews

*Your AI Peer Review Bro*

Diffbro is a command line tool that gives you AI powered peer reviews on your codebase. Under the hood diffbro utilizes `git diff` and OpenAI's *GPT-3.5-turbo* and *GPT-4* to review your code and provide feedback on your changes. 

Diffbro is best used before you stage and commit your code to your codebase. Diffbro also supports full branch diff PR feedback as if it were an engineer reviewing your merge request (see `--peer-review` flag). Diffbro is designed to help you catch bugs, improve your code quality, and help you ship with confidence.

![Diffbro Header](https://firebasestorage.googleapis.com/v0/b/solopreneur-d8361.appspot.com/o/Diffbro%2Fdiffbro.jpg?alt=media&token=fefc8d90-10e2-4091-9b03-957af25aee3b)

## Features

- View all commands, options and examples
  - `diffbro --help`

- Run against local changes
  - `diffbro`

- Run diffbro against a branch and create a PR review
  - `diffbro --peer-review main`

- Different bro modes for chill, to chad engineer level peer reviews
  - chill: will review your code like a chill bro (default)
    - `diffbro --chill`
  - mid: will review your code like a mid level engineer bro
    - `diffbro --mid`
  - chad: will review your code like a chad, staff engineer bro
    - `diffbro --chad`

- Choose which files to review
  - Only .py and .js files
    - `diffbro --only .py .js`
  - Everything except .py and .js files
    - `diffbro --ignore .py .js`
  - *Defaults to [".py", ".c", ".cpp", ".java", ".cs", ".php", ".vb", ".html", ".css", ".js", ".ts", ".asp", ".aspx", ".cfm", ".cgi", ".pl", ".cer", ".htm", ".xhtml", ".shtml", ".jsp", ".jsx", ".tsx", ".vue", ".solid", ".toml", ".md", ".go", ".rs", ".swift"]*

- Choose your gpt model
  - `diffbro --model gpt-3.5-turbo`
  - `diffbro --model gpt-4` (default) (recommended for production code)

- Summarize the git diff for a commit message or PR description
  - `diffbro --summarize`

- Override the default prompts with your own custom prompt
  - `diffbro --prompt "Below is a git diff of code. Please review and notify only of critical issues. If there are no critical issues, respond with tons of checkbox emojis"`

- Example command combos
  - '*I want a chill review on my .py and .js files*'
    - `diffbro --chill --only .py .js`
  - '*I'm about to ship production, mission critical UI code, I need a hardcore review on my FE code*'
    - `diffbro --chad --model gpt-4 --only .js .jsx .tsx .vue`
  - '*I'm about to a fullstack app and need a comprehensive mid level review on all my code excluding .tsx files*'
    - `diffbro --mid --model gpt-4 --ignore .tsx`
  - '*I want to run my own prompt against my git diff with a summary for the commit massage*'
    - `diffbro --prompt "Below is a git diff of code. Please review and notify only of critical issues." --summarize`
  - '*I want a quick comparison of my changes against the staging branch with a summary*'
    - `diffbro --peer-review staging --model gpt-3.5-turbo --summarize`
  - '*I want a mid level code review of all of my .ts files*'
    - `diffbro --mid --only .ts`
  - '*I want top tier code reviews all the time*'
    - Throw this line into your `.bashrc` or `.bash_profile`
      - `alias dbro="diffbro --chad --model gpt-4 --summarize"`
    - Then, whenever you want a review, just run
      - `dbro`

## Install & Use

- Install or switch to [Python 3.11 or 3.10 or 3.9 or 3.8](https://www.python.org/downloads/)
  - Check your python version
    - `python --version`

- Install '*stable*' version from [PyPI](https://pypi.org/)
  - `pip install --upgrade diffbro`

- Export your openai api key
  - `export OPENAI_API_KEY=<your-openai-api-key>`

- Make changes to your codebase

- Run diffbro
  - `diffbro`

### Compare local changes

- Before you stage and commit, run diffbro
  - `diffbro`

- Implement the feedback from diffbro

- Commit your code with confidence

### Compare branch changes

- Before you merge, run diffbro
  - `diffbro --peer-review main`

- Implement the feedback from diffbro

- Merge your code with confidence

## Development

#### Install bleeding edge version test version

- Install BLEEDING EDGE version from [TestPyPi](https://test.pypi.org/)
  - `pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple diffbro`

#### Local Dev Commands (excluded from dist)
- run diffbro locally
  - `poetry run diffbro`
- test versions
  - `poetry run python scripts/run_tox.py`
- publish to test pypi
  - `poetry run python scripts/publish_testpypi.py`
- publish to pypi
  - `poetry run python scripts/publish_pypi.py`

## ROADMAP

[✅] POC

[✅] Add GPT model flag

[✅] Add diff exclusion of large files like poetry.lock from the diff

  [✅] Add cli --only flag to diff only specific file types

  [✅] Add cli --ignore flag to ignore specific file types

[✅] Deploy version 0.1.0 to TestPyPi

[✅] Test install version 0.1.0 from TestPyPi

[✅] Deploy version 0.1.2 to pypy

[✅] Add help docs

[✅] Support additional python versions

[✅] Improve openai_api_key check

[✅] Chad should always ask to use gpt-4 (simple yes/no prompt)

[✅] Add custom prompt flag to be run on the diff
  `diffbro --prompt "Below is a git diff of code. Please review and notify only of critical issues."`

[✅] Add summarybro flag that will create a git commit message using the diffbro summary
  `diffbro --summarize` -> "Added new feature to the app, fixed a bug, and refactored some code."

[✅] Add COMPLETE PR review flag which runs diffbro against a branch and creates a PR review
  `diffbro --pr main`

[✅] RELEASE VERSION 1.0.0!!!

[] Parallelize diffbro and commit summary GPT requests

[] Add unit tests

[] What feature would you like to see next? [Submit a feature request](https://github.com/disler/diffbro/issues/new)

[?] Add token limit check to prevent overage charges

[?] Add 'AI Devlogs' section to readme w/links to ai devlogs

[?] Add ~/.diffbro config file support for custom defaults
  - if a cli param was specified in the .diffbro file, use that. Add default values to argparse to detect if a cli param was specified (dirty)