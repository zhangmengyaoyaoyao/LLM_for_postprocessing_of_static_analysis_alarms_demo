from prompts.constructor import *

# list = construct_prompt("zero-shot", "## a bug report ##")
# list = construct_prompt("one-shot", "## a bug report ##")
# list = construct_prompt("few-shot", "## a bug report ##")
# list = construct_prompt("general-info", "## a bug report ##")
# list = construct_prompt("expertise", "## a bug report ##")
# list = construct_prompt("chain-of-thought", "## a bug report ##")
# list = construct_prompt("critique", "## a bug report ##")
list = construct_prompt("self-heuristic", "## a bug report ##")
for content in list:
    print(content)
