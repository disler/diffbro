# diffbro

*Your AI Peer Review Bro*

### Features

- Different bro modes for chill, to chad engineer level peer reviews
  - chill: will review your code like a chill bro
  - mid: will review your code like a mid level engineer bro
  - chad: will review your code like a chad, staff engineer bro

### TODO

[✅] POC

[] Add GPT model flag

[] Add diff exclusion of large files like poetry.lock from the diff
  Solution: `git diff -- '*.py' '*.js'`
  API: 
    Include specific file types
      diffbro --only '*.py' '*.js'
    Exclude specific file types
      diffbro --ignore '*.py' '*.js'

  [] Add cli --only flag to diff only specific file types

  [] Add cli --ignore flag to ignore specific file types

[] Deploy to TestPyPi

### Icebox

[] Add summarybro flag that will create a git commit message using the diffbro summary