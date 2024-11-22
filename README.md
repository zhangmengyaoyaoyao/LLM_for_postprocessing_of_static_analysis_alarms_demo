# 数据集处理
## Java
### 格式转换
report/link.py: 在报告中加入rank和priority

report/csv2json_java.py: 转换为json格式

### 转换后的数据
csv格式：report/spotbugs_report

json格式：report/spotbugs_json

例子：

``` json
{
    "category": "MALICIOUS_CODE",
    "vtype": "MS_PKGPROTECT",
    "priority": "2",
    "rank": "18",
    "project": "bcel",
    "warning_line": "@Deprecated\npublic static final String[] SHORT_TYPE_NAMES = { ILLEGAL_TYPE, ILLEGAL_TYPE, ILLEGAL_TYPE, ILLEGAL_TYPE, \"Z\", \"C\", \"F\", \"D\", \"B\", \"S\", \"I\", \"J\", \"V\", ILLEGAL_TYPE, ILLEGAL_TYPE, ILLEGAL_TYPE };",
    "warning_method": "@Deprecated\npublic static final String[] SHORT_TYPE_NAMES = { ILLEGAL_TYPE, ILLEGAL_TYPE, ILLEGAL_TYPE, ILLEGAL_TYPE, \"Z\", \"C\", \"F\", \"D\", \"B\", \"S\", \"I\", \"J\", \"V\", ILLEGAL_TYPE, ILLEGAL_TYPE, ILLEGAL_TYPE };"
}
``` 

## C/C++
### 格式转换
report/csv2json_c.py: 转换为json格式

# 手动处理
例子：
bug_0077_bcel
```
@@ actionable @@ 

This warning is actionable because it points to a specific line of code (`System.exit(-1);`) that is considered a bad practice. The code is explicitly calling `System.exit(-1)` in a default case, which can cause the program to terminate abruptly. This warning suggests that the developer should review and refactor the code to handle the default case more gracefully.
```


# TODO
已解决 1、提示词的example以md形式改写
已解决 2、目前只尝试运行了zero-shot模板
已解决 3、设置每分钟调用10次的限制
已解决 4、提取回答中的结果到excel中
已解决 5、c中tool和projectname需要从json中提取，这样才能区分开zero-shot和general-info
已实验 6、每次都有提供提示词吗——是的，否则没有taskdescription

变量：
llm
工具
提示词技术
项目
bug