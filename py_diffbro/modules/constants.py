PROGRAMMING_FILE_EXTENSIONS = [
    ".py",
    ".c",
    ".cpp",
    ".java",
    ".cs",
    ".php",
    ".vb",
    ".html",
    ".css",
    ".js",
    ".asp",
    ".aspx",
    ".cfm",
    ".cgi",
    ".pl",
    ".cer",
    ".htm",
    ".xhtml",
    ".shtml",
    ".jsp",
    ".jsx",
    ".tsx",
    ".vue",
    ".solid",
    ".toml",
    ".md",
    ".go",
    ".rs",
    ".swift",
]


DETAILED_DIFFBRO_DESCRIPTION = """
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
"""
