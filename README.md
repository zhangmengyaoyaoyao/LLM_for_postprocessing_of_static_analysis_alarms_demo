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

# TODO
1、提示词的example以md形式改写
2、目前只尝试运行了zero-shot模板
3、设置每分钟调用10次的限制
4、提取回答中的结果