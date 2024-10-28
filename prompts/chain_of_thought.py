chain_question1 = """\
Is the error type common in false positives? \
"""

chain_question2 = """\
Do the file paths point to the core or key modules of the project?\
Does the file path point to generated code, test code, or third-party library code? \
"""

chain_question3 = """\
What is the purpose and functions of this function? \
Is it often called or potentially exposed to the outside world? \
"""

chain_question4 = """\
Does the error trace information show a clear call chain?\
Is the source of the problem obvious in the error traceback, or is it a problem that may only occur under certain edge cases? \
"""

chain_question5 = """\
Does the description clearly indicate the potential impact of this error, or does it mention specific conditions or environmental factors that can cause this error?
"""

chain_instruction = """\
Let's integrate the above information, and complete the following task.
"""