zero_shot_prompt = """\
# Task Description
I will be responsible for identifying whether error reports are false positives. \
The error reports generated by static analysis tools will be provided to me, including reports from SPOTBUGS for Java projects and reports from CPPCHECK, INFER, and CSA for C/C++ projects.\
I will verify the bug's existence and classify them as either real bug or false alarm.\
In the last line of my answer, I should conclude with either '@@@ real bug @@@', '@@@ false alarm @@@', or '@@@ unknown @@@'.\n
At the end of my response, I should conclude with either '@@@ Real Error @@@' or '@@@ False Positive @@@'.
"""