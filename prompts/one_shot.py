one_shot_prompt_USER1= """\
# Task Description
Please decide whether this warning is actionable or not.
"""

one_shot_example_java = """\

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

one_shot_example_c = """\
# example1
## warning
```json
{
    "Project": "binutils",
    "Tool": "Infer",
    "category": "BUFFER_OVERRUN_L3",
    "file": "binutils/bfdtest2.c",
    "message": "Offset added: [16, +oo] (⇐ [0, +oo] + [16, +oo]) Size: [0, +oo] by call to `bfd_check_format_matches`.",
    "warning_function_name": "check_format_any",
    "warning_line": "if (bfd_check_format_matches (abfd, format, &targets))",
    "warning_context": "static bfd_boolean\ncheck_format_any (struct bfd *abfd, bfd_format format)\n{\n  char** targets = NULL;\n\n  if (bfd_check_format_matches (abfd, format, &targets))\n    return TRUE;\n\n  if (targets)\n    {\n      bfd_find_target (targets[0], abfd);\n\n      return bfd_check_format (abfd, format);\n    }\n\n  return FALSE;\n}\n"
}
```

## Your Answer
//your reason
@@ unactionable @@
"""

one_shot_prompt_USER2= """\
In the last line of your answer, you should conclude with "@@ actionable @@", "@@ unactionable @@" or "@@ unknown @@"(if you are uncertain).
"""