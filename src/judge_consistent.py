import pandas as pd

def update_consistent_column(input_excel):
    # 读取 Excel 文件
    df = pd.read_excel(input_excel)

    # 定义逻辑规则，更新 consistent 列
    def determine_consistent(row):
        if row['Status'] == 'unknown':
            return 'unknown'
        elif row['Status'] == 'actionable' and row['final_label'] == 'TP':
            return 'T'
        elif row['Status'] == 'unactionable' and row['final_label'] == 'FP':
            return 'T'
        else:
            return 'F'

    # 应用规则，更新 consistent 列
    df['consistent'] = df.apply(determine_consistent, axis=1)

    # 统计 consistent 列的值分布
    total_count = len(df)
    counts = df['consistent'].value_counts()
    percentages = (counts / total_count) * 100

    # 打印统计结果
    print("consistent 列统计结果：")
    for value, count in counts.items():
        percentage = percentages[value]
        print(f"{value}: {count} ({percentage:.2f}%)")

    # 保存结果到原文件
    df.to_excel(input_excel, index=False)
    print(f"处理完成，结果已更新到 {input_excel}")

# 使用示例
input_excel = "response/llama3-70b-instruct/spotbugs/expertise_bcel.xlsx"  # 替换为你的 Excel 文件路径
update_consistent_column(input_excel)
