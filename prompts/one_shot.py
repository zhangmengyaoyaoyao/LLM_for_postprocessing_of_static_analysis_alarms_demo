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
@@@ unactionable @@@
"""