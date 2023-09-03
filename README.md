# diffbro

*Your AI Peer Review Bro*

![Diffbro Header](https://firebasestorage.googleapis.com/v0/b/solopreneur-d8361.appspot.com/o/Diffbro%2Fdiffbro.jpg?alt=media&token=fefc8d90-10e2-4091-9b03-957af25aee3b)

## Features

- Different bro modes for chill, to chad engineer level peer reviews
  - chill: will review your code like a chill bro
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
  - *Defaults to [".py", ".c", ".cpp", ".java", ".cs", ".php", ".vb", ".html", ".css", ".js", ".asp", ".aspx", ".cfm", ".cgi", ".pl", ".cer", ".htm", ".xhtml", ".shtml", ".jsp", ".jsx", ".tsx", ".vue", ".solid", ".toml", ".md", ".go", ".rs", ".swift"]*

- Choose your gpt model
  - `diffbro --model gpt-3.5-turbo` (default)
  - `diffbro --model gpt-4` (recommended for production code)

- Example command combos
  - '*I want a chill review on my .py and .js files*'
    - `diffbro --chill --only .py .js`
  - '*I'm about to ship production, mission critical UI code, I need a hardcore review on my FE code*'
    - `diffbro --chad --model gpt-4 --only .js .jsx .tsx .vue`
  - '*I'm about to a fullstack app and need a comprehensive mid level review on all my code excluding .tsx files*'
    - `diffbro --mid --model gpt-4 --ignore .tsx`
  - '*I want legit reviews all the time*'
    - Throw this line into your .bashrc or .bash_profile
      - `alias dbro='diffbro --chad --model gpt-4'`

## Setup

- Install or switch to [Python 3.7.1+](https://www.python.org/downloads/)
  - Check your python version
    - `python --version`

- Install '*stable*' version from [PyPI](https://pypi.org/)
  - `pip install --upgrade diffbro`

- Export your openai api key
  - `export OPENAI_API_KEY=<your-openai-api-key>`

- Make changes to your codebase

- Before you commit, run diffbro
  - `diffbro`

- Implement the feedback from diffbro

- Commit your code with confidence

#### Install bleeding edge version test version

- Install BLEEDING EDGE version from [TestPyPi](https://test.pypi.org/)
  - `pip install --upgrade --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple diffbro`


#### Local Dev (excluded from dist)
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
  Solution: `git diff -- '*.py' '*.js'`
  API: 
    Include specific file types
      diffbro --only '*.py' '*.js'
    Exclude specific file types
      diffbro --ignore '*.py' '*.js'

  [✅] Add cli --only flag to diff only specific file types

  [✅] Add cli --ignore flag to ignore specific file types

[✅] Deploy version 0.1.0 to TestPyPi

[✅] Test install version 0.1.0 from TestPyPi

[✅] Deploy version 0.1.2 to pypy

-- off vid

[✅] Add help docs

[✅] Support additional python versions

[✅] Improve openai_api_key check

[] Add confirm prompts to improve DX 
  - chad should always ask to use gpt-4 (simple yes/no prompt)

[] Add token limit check to prevent overage charges

[] Add 'AI Devlogs' section to readme w/links to ai devlogs

-- on vid

[] Add ~/.diffbro config file support for defaults

[] Add custom prompts with a --custom 'name' which will refer to a custom.* block in ~/.diffbro

[] Add summarybro flag that will create a git commit message using the diffbro summary

[] Deploy to Pypi