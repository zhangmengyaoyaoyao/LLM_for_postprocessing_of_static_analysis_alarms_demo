def find_function_using_ctags(tags_file, line_number):
    with open(tags_file, 'r') as file:
        tags = file.readlines()
    
    functions = []
    for tag in tags:
        parts = tag.split()
        if len(parts) >= 2 and parts[1].isdigit():
            functions.append((parts[0], int(parts[1])))

    # 按行号排序
    functions.sort(key=lambda x: x[1])

    current_function = None
    for i in range(len(functions)):
        if functions[i][1] > line_number:
            break
        current_function = functions[i]

    if current_function is None:
        return None, None, None

    func_name, start_line = current_function
    end_line = (
        functions[functions.index(current_function) + 1][1] - 1
        if functions.index(current_function) + 1 < len(functions)
        else None
    )

    return func_name, start_line, end_line

# 示例调用
print(find_function_using_ctags('tags.txt', 15))
