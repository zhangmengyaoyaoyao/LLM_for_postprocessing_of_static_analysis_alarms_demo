tool = 'SpotBugs'
project = 'bcel'

def setGeneralInfo(toolNow, projectNow):
    global tool, project  # 声明使用全局变量
    tool = toolNow
    project = projectNow

general_info_system = f"""\ 
You are an expert programmer, possessing advanced skills in analyzing program code using static analysis tools. You will use your expertise to analyze warnings that are generated by {tool} on {project}. 
"""