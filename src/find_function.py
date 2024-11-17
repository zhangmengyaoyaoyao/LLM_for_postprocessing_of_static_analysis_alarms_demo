# c_file_path 文件路径
# line_number 行号
# function_name 函数名
def find_function(c_file_path, line_number, function_name):
    # 检查文件是否存在
    if not os.path.isfile(c_file_path):
        print(f"错误: 文件 {c_file_path} 不存在。")
        return None, None

    try:
        with open(c_file_path, 'r') as file:
            lines = file.readlines()
    except Exception as e:
        print(f"错误: 无法读取文件 {c_file_path}。异常信息: {e}")
        return None, None

    # 1. 从指定行往上查找第一个顶格的左大括号
    func_start = None
    for i in range(line_number - 1, -1, -1):
        if(lines is None):
            print("No lines")
            break
        if(i <0 or i> len(lines)):
            print("out")
            break
        stripped_line = lines[i]  # 去掉前导空白字符
        if stripped_line.startswith(LEFT_BRACE):  # 只匹配顶格的左大括号
            func_start = i
            print("func_start:" + str(func_start))
            break

    if func_start is None:
        print(f"未找到函数的左大括号，从行号 {line_number} 向上查找失败。")
        return None, None  # 没找到顶格左大括号

    # 2. 从找到的左大括号行开始，向下查找匹配的右大括号
    brace_count = 1  # 已经找到了一个左大括号
    func_end = None
    for i in range(func_start + 1, len(lines)):  # 从左大括号下一行开始
        stripped_line = lines[i]

        # 统计左大括号
        if stripped_line.startswith(LEFT_BRACE):
            brace_count += 1

        # 统计右大括号
        if stripped_line.startswith(RIGHT_BRACE):
            brace_count -= 1

        # 当 brace_count 回到 0 时，表示找到了匹配的右大括号
        if brace_count == 0:
            func_end = i
            break

    if func_end is None:
        print(f"未找到匹配的右大括号，从行号 {func_start + 1} 向下查找失败。")
        return func_start + 1, None  # 没找到匹配的右大括号

    # 3. 从 func_start 行向前查找，找到第一个包含 function_name 的行（不区分大小写）
    new_func_start = None
    function_name_lower = function_name.lower()
    for i in range(func_start - 1, -1, -1):
        if function_name_lower in lines[i].lower():
            new_func_start = i
            break

    if new_func_start is None:
        print(f"未找到包含函数名 '{function_name}' 的行，使用左大括号所在行 {func_start + 1} 作为函数起始行。")
        new_func_start = func_start  # 如果没有找到包含函数名的行，默认起始行为左大括号所在行

    return new_func_start + 1, func_end + 1  # 行号从 1 开始