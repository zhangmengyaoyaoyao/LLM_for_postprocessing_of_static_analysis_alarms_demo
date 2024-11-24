few_shot_example1 = """\

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



few_shot_example2 = """\

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

few_shot_example3 = """\

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


few_shot_example4 = """\

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