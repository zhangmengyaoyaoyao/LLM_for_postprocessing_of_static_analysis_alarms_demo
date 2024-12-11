few_shot_example_java1 = """\

# example1
# Bug Report
```json
{
    "category": "I18N",
    "vtype": "DM_DEFAULT_ENCODING",
    "priority": "1",
    "rank": "19",
    "project": "mavendp",
    "warning_line": "try ( FileWriter writer = new FileWriter( file, append ) )\n",
    "warning_method": "public static synchronized void write(String string, File file, boolean append, Log log) throws IOException {\nfile.getParentFile().mkdirs();\ntry (FileWriter writer = new FileWriter(file, append)) {\nwriter.write(string);\n}\n}"
}
```

## Your Answer
//your reason
@@ actionable @@
"""



few_shot_example_java2 = """\

# example2
# Bug Report
```json
{
    "category": "MALICIOUS_CODE",
    "vtype": "EI_EXPOSE_REP",
    "priority": "2",
    "rank": "18",
    "project": "net",
    "warning_line": "return this.rootCause;\n",
    "warning_method": "public Throwable getRootCause() {\nreturn this.rootCause;\n}"
}
```

## Your Answer
//your reason
@@ actionable @@
"""

few_shot_example_java3 = """\

# example3
## Bug Report
```json
{
    "category": "DODGY_CODE",
    "vtype": "REC_CATCH_EXCEPTION",
    "priority": "3",
    "rank": "20",
    "project": "configuration",
    "warning_line": "catch (Exception e)\n",
    "warning_method": "public InputSource resolveEntity(String publicId, String systemId) throws SAXException {\nString resolved = resolver.getResolvedEntity(publicId, systemId);\nif (resolved != null) {\nString badFilePrefix = \"file://\";\nString correctFilePrefix = \"file:///\";\nif (resolved.startsWith(badFilePrefix) && !resolved.startsWith(correctFilePrefix)) {\nresolved = correctFilePrefix + resolved.substring(badFilePrefix.length());\n}\ntry {\nInputSource iSource = new InputSource(resolved);\niSource.setPublicId(publicId);\nURL url = new URL(resolved);\nInputStream iStream = url.openStream();\niSource.setByteStream(iStream);\nreturn iSource;\n} catch (Exception e) {\nlog.debug(\"Failed to create InputSource for \" + resolved + \" (\" + e.toString() + \")\");\nreturn null;\n}\n}\nreturn null;\n}"
}
```

## Your Answer
//your reason
@@ unactionable @@
"""


few_shot_example_java4 = """\

# example4
# Bug Report
```json
{
    "category": "BAD_PRACTICE",
    "vtype": "DE_MIGHT_IGNORE",
    "priority": "3",
    "rank": "19",
    "project": "pool",
    "warning_line": "} catch (Exception e) {\n",
    "warning_method": "public void invalidateObject(final K key, final V obj) {\ntry {\npool.invalidateObject(obj);\n} catch (Exception e) {\n}\n}"
}
```

## Your Answer
//your reason
@@ unactionable @@
"""

few_shot_example_c1 = """\

# example1
# Bug Report
```json
{
    "Project": "combine",
    "Tool": "Cppcheck",
    "category": "memleak",
    "file": "src/dstring.c",
    "message": "Memory leak: temp_string",
    "warning_function_name": "dstrtonum",
    "warning_line": "return return_val;",
    "warning_context": "BIGNUMBER\ndstrtonum (string, remainder, base)\n     DStr_string_descriptor *string;\n     DStr_string_descriptor **remainder;\n     int base;\n{\n  BIGNUMBER return_val;\n  char *temp_string;\n  char *temp_remainder;\n\n  if (remainder != NULL)\n    *remainder = string;\n\n  temp_string = malloc (string->length + 1);\n  if (temp_string == NULL)\n    return 0;\n\n  memcpy (temp_string, string->string, string->length);\n  temp_string[string->length] = '\\0';\n\n  return_val = STRTOBIGNUMBER (temp_string, &temp_remainder, base);\n  if (*temp_remainder == '\\0') {\n    /* Either we used the wholde string, or there was an embedded null. */\n    if (temp_remainder - temp_string == string->length) {\n      if (remainder != NULL)\n\t*remainder = NULL;\n      free (temp_string);\n      return return_val;\n      }\n    }\n\n  if (remainder != NULL) {\n    *remainder = dstrnew ();\n    if (*remainder == NULL) {\n      *remainder = string;\n      free (temp_string);\n      return return_val;\n      }\n    (*remainder)->length = string->length - (temp_remainder - temp_string);\n    (*remainder)->string = string->string + (temp_remainder - temp_string);\n    }\n\n  return return_val;\n\n  }\n"
}
```

## Your Answer
//your reason
@@ actionable @@
"""

few_shot_example_c2 = """\

# example2
# Bug Report
```json
{
    "Project": "bash",
    "Tool": "CSA",
    "category": "core.NullDereference",
    "file": "subst.c",
    "message": "Access to field 'word' results in a dereference of a null pointer (loaded from field 'word')",
    "warning_function_name": "quote_list",
    "warning_line": "t = w->word->word;",
    "warning_context": "static WORD_LIST *\nquote_list (list)\n     WORD_LIST *list;\n{\n  register WORD_LIST *w;\n  char *t;\n\n  for (w = list; w; w = w->next)\n    {\n      t = w->word->word;\n      w->word->word = quote_string (t);\n      if (*t == 0)\n\tw->word->flags |= W_HASQUOTEDNULL;\t/* XXX - turn on W_HASQUOTEDNULL here? */\n      w->word->flags |= W_QUOTED;\n      free (t);\n    }\n  return list;\n}\n"
}
```

## Your Answer
//your reason
@@ unactionable @@
"""

few_shot_example_c3 = """\

# example3
# Bug Report
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

few_shot_example_c4 = """\

# example4
# Bug Report
```json
{
    "Project": "gawk",
    "Tool": "Cppcheck",
    "category": "uninitvar",
    "file": "dfa.c",
    "message": "Uninitialized variable: wc",
    "warning_function_name": "dfambcache",
    "warning_line": "d->mbrtowc_cache[uc] = mbrtowc (&wc, &c, 1, &s) <= 1 ? wc : WEOF;",
    "warning_context": "static void\ndfambcache (struct dfa *d)\n{\n  int i;\n  for (i = CHAR_MIN; i <= CHAR_MAX; ++i)\n    {\n      char c = i;\n      unsigned char uc = i;\n      mbstate_t s = { 0 };\n      wchar_t wc;\n      d->mbrtowc_cache[uc] = mbrtowc (&wc, &c, 1, &s) <= 1 ? wc : WEOF;\n    }\n}\n"
}
```

## Your Answer
//your reason
@@ unactionable @@
"""