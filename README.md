# 1 项目说明
## 1.1 目录结构
文件夹       | 说明
----------- | -----
prompts  | 存放提示词
report  | 原始数据。spotbugs_linked是完整的警告（包含手工标记结果），spotbugs/是最终的json格式Java项目警告；c_json/是json格式C/C++项目警告。
response  | LLMs返回的回答，子文件夹名称代表“LLM/prompt_technique/project_name”
src  | 核心代码
src/llm  | 从不同平台调用不同LLMs
test  | 临时测试，暂时没有用处

## 1.2 核心代码
文件       | 说明
----------- | -----
src/construct_prompts.py  | 根据采用的提示词技术合成提示词
src/find_function.py  | 目前采用的学长写的提取C函数的代码
src/toexcel_and_comp  | 将LLM的回答存储到excel中,并判断LLM的结论与手工标记结果的一致性
src/response2excel.py  | 将LLM的回答存储到excel中
src/judge_consistent.py  | 判断LLM的结论与手工标记结果的一致性
report/csv2json_java.py  | 将Java项目警告转换为json格式
report/csv2json_c.py  | 将C/C++项目警告转为json格式

# 2 如何上手（调用LLM分类警告）
## 2.1 获取API-KEY
### 2.1.1 Llama3.1-70B-Instruct
阿里云百炼：https://bailian.console.aliyun.com/#/model-market

NVIDIA(推荐-速度快，免费token多):https://build.nvidia.com/meta/llama-3_1-70b-instruct

OpenRouter: https://openrouter.ai/meta-llama/llama-3.1-70b-instruct:free

### 2.1.2 GLM
BigModel: https://bigmodel.cn/pricing

## 2.2 运行
在src/llm/chat_···.py中，用你相应平台的api-key填充在
```
# your api key
key = ""
```
运行命令
```
python3 -m src.llm.chat_···.py
```

## 2.3 数据后处理
在src/toexcel_and_comp.py中，修改你要处理的项目名称（projects）、使用的LLM（model）、警告来源静态分析工具（tool）

然后运行
```
python3 -m src.toexcel_and_comp
```

# 3 实验方法

## 3.1 数据集处理
### 3.1.1 Java
#### 预处理-格式转换
report/link.py: 在报告中加入rank和priority

report/csv2json_java.py: 转换为json格式

转换后的数据

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

### 3.1.2 C/C++
#### 提取函数上下文
因为原警告所在函数提取结果存在错误，我们重新提取警告所在函数作为警告上下文。同时，为了控制token数量，我们规定若函数长度超过100行，以警告上下100行代码作为警告上下文。

具体方法见：
https://github.com/zhangmengyaoyaoyao/Extract-Function-Snippet-From-C-Projects

#### 预处理-格式转换
report/csv2json_c.py: 转换为json格式

### 后处理
提取结果

部分例子手动处理

## 3.2 实验变量：
llm
工具
提示词技术
项目
bug


# 4 实验进度
**Java项目**

模型    | 项目1  | 项目2 | 项目3 | 项目4 
-------- | ----- | ----- | ----- | -----  
模型/项目 | bcel  |  collections  |  dbcp  |  mavendp
Llama3.1-70B-Instruct | √ | √ | √ | √ 
GLM-4-flash | √ | √ | √ | √ 
gpt-3.5-turbo-0125 | √ | √ | √ | √

**C项目**

所有（10个项目）

Llama3.1-70B-Instruct

GLM-4-flash

gpt-3.5-turbo-0125


# TODO
已解决 1、提示词的example以md形式改写

已解决 2、目前只尝试运行了zero-shot模板

已解决 3、设置每分钟调用10次的限制

已解决 4、提取回答中的结果到excel中

已解决 5、c中tool和projectname需要从json中提取，这样才能区分开zero-shot和general-info

已实验 6、每次都有提供提示词吗——是的，否则没有taskdescription

7、比较结果时去除训练集

