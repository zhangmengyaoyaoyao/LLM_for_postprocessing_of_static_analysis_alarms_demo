one_shot_prompt_USER1= """\
# Task Description
Please decide whether this warning is actionable or not.
"""

one_shot_example = """\

# example1
## warning
```json
{
    "category": "MALICIOUS_CODE",
    "vtype": "EI_EXPOSE_REP",
    "priority": "2",
    "rank": "18",
    "project": "bcel",
    "warning_line": "return exports_table;\n",
    "warning_method": "public ModuleExports[] getExportsTable() {\nreturn exports_table;\n}"
}
```

## Your Answer
//your reason
@@ unactionable @@
"""

one_shot_prompt_USER2= """\
In the last line of your answer, you should conclude with "@@ actionable @@", "@@ unactionable @@" or "@@ unknown @@"(if you are uncertain).
"""