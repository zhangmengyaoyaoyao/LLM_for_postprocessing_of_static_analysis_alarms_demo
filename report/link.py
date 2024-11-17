import pandas as pd

projects_name = ['bcel', 'codec', 'collections', 'configuration', 'dbcp', 'digester', 'fileupload', 'mavendp', 'net', 'pool']


for name in projects_name:
    # Load the Excel files
    project_df = pd.read_excel(f"report/spotbugs2/{name}.xlsx")
    raw_df = pd.read_csv(f"report/spotbugs1/{name}.csv")

    # 初始化新列
    project_df.insert(3, 'priority', None)  # 插入新列priority到第3列
    project_df.insert(4, 'rank', None)      # 插入新列rank到第4列


    for idx, row in project_df.iterrows():
        no_value = row['no']
        # 检查表二中是否有对应行
        if no_value < len(raw_df):  # 避免越界
            # 提取priority和rank值
            priority_value = raw_df.at[no_value - 1, 'priority']
            rank_value = raw_df.at[no_value - 1, 'rank']
            
            # 插入到表一的第3和第4列
            project_df.at[idx, 'priority'] = priority_value
            project_df.at[idx, 'rank'] = rank_value

    project_df.to_csv(f"report/spotbugs_linked/{name}_linked.csv", index=False)
