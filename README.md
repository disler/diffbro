# diffbro

*Your AI Peer Review Bro*

### Features

- Different bro modes for more chad engineer like peer reviews
  - chill: will review your code like a chill bro
  - mid: will review your code like a mid level engineer bro
  - chad: will review your code like a chad, staff engineer bro

### TODO

[+] Add diff exclusion of large files like poetry.lock from the diff
    Solution: `git diff -- '*.py' '*.js'`

[] Add cli --only flag to diff only specific file types

[] Add cli --ignore flag to ignore specific file types

[] Add summarybro flag that will create a short summary of the diff for the git commit message