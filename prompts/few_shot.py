few_shot_example1 = """\

# example1
# Bug Report
```json
{
    "bug_type": "ctuArrayIndex",
    "line": 60,
    "column": 14,
    "procedure": "",
    "file": "char_alloca_loop_04.c",
    "qualifier": {
        "Cppcheck": "Array index out of bounds; 'data' buffer size is 10 and it is accessed at offset 10."
    },
    "Trace": [
        {"filename": "drivers/pn532/pn532.c", "line_number": 49, "column_number": 8, "description": ""},
        {"filename": "drivers/pn532/pn532.c", "line_number": 60, "column_number": 14, "description": ""}
    ]
}
````

## Your Answer
// The reason why you make this judgment
@@@ false alarm @@@
"""



few_shot_example2 = """\

# example2
# Bug Report
```json
{
    "bug_type": "Uninitialized Value",
    "line": 158,
    "column": 6,
    "procedure": "apr_pstrcat",
    "file": "strings/apr_strings.c",
    "qualifier": {
        "Infer": "The value read from p was never initialized.",
        "Cppcheck": "Uninitialized variable: saved_lengths"
    },
    "Trace": [
        {"filename": "strings/apr_strings.c", "line_number": 158, "column_number": 6, "description": ""},
        {"filename": "strings/apr_strings.c", "line_number": 139, "column_number": 8, "description": ""},
        {"filename": "strings/apr_strings.c", "line_number": 126, "column_number": 14, "description": ""}
    ]
}
```

## Your Answer
// The reason why you make this judgment
@@@ false alarm @@@
"""

few_shot_example3 = """\

# example3
## Bug Report
```json
{
    "bug_type": "Null Pointer Dereference",
    "line": 24,
    "column": 3,
    "procedure": "",
    "file": "npd.c",
    "qualifier": {
        "Cppcheck": "Possible null pointer dereference: buf"
    },
    "Trace": [
        {"filename": "npd.c", "line_number": 24, "column_number": 3, "description": ""},
        {"filename": "npd.c", "line_number": 21, "column_number": 21, "description": ""},
        {"filename": "npd.c", "line_number": 46, "column_number": 18, "description": ""}
    ]
}
```

## Your Answer
// The reason why you make this judgment
@@@ false alarm @@@
"""


few_shot_example4 = """\

# example4
# Bug Report
```json
{
    "bug_type": "Memory Leak",
    "line": 72,
    "column": 1,
    "procedure": "",
    "file": "/home/koral/Documents/juliet-testv1.3/2017-10-01-juliet-test-suite-for-c-cplusplus-v1-3/C/testcases/CWE122_Heap_Based_Buffer_Overflow/s01/CWE122_Heap_Based_Buffer_Overflow__cpp_CWE193_char_cpy_33.cpp",
    "qualifier": {
        "Cppcheck": "Memory leak: data"
    },
    "Trace_None": [
        {"filename": "/home/koral/Documents/juliet-testv1.3/2017-10-01-juliet-test-suite-for-c-cplusplus-v1-3/C/testcases/CWE122_Heap_Based_Buffer_Overflow/s01/CWE122_Heap_Based_Buffer_Overflow__cpp_CWE193_char_cpy_33.cpp", "line_number": 72, "column_number": 1, "description": ""}
    ]
}
```

## Your Answer
// The reason why you make this judgment
@@@ false alarm @@@
"""