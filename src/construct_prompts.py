from prompts import zero_shot, one_shot, few_shot, general_info, expertise, chain_of_thought, critique, self_heuristic

warning = ''

def setWarning(warningNow):
    global warning
    warning = '# warning\n'+warningNow

def setGeneralInfo(toolNow, projectNow):
    general_info.setGeneralInfo(toolNow, projectNow)

# def construct_warning():
#     messages = []

#     user_message =  warning
#     messages.append({'role': 'user', 'content': user_message})
#     #test
#     #print("input_warning:" + user_message)
#     return messages


def construct_zero_shot():
    messages = []

    user_message =  zero_shot.zero_shot_prompt_USER + warning
    messages.append({'role': 'user', 'content': user_message})
    #test
    #print("input_zero_shot:" + user_message)

    return messages


def construct_one_shot():
    messages = []

    user_message =  one_shot.one_shot_prompt_USER1+one_shot.one_shot_example+one_shot.one_shot_prompt_USER2 + warning
    messages.append({'role': 'user', 'content': user_message})
    #test
    #print("input_one_shot:" + user_message)

    return messages


def construct_few_shot():
    messages = []

    user_message =  zero_shot.zero_shot_prompt_USER + few_shot.few_shot_example1 + few_shot.few_shot_example2 + few_shot.few_shot_example3 + few_shot.few_shot_example4 + warning
    messages.append({'role': 'user', 'content': user_message})

    return messages


def construct_general_info():
    messages = []

    messages.append({'role': 'system', 'content': general_info.general_info_system})

    user_message =  zero_shot.zero_shot_prompt_USER + warning
    messages.append({'role': 'user', 'content': user_message})

    return messages


def construct_expertise():
    messages = []

    messages.append({'role': 'system', 'content': general_info.general_info_system})

    user_message =  zero_shot.zero_shot_prompt_USER + expertise.expertise_expertise + warning
    messages.append({'role': 'user', 'content': user_message})

    return messages


def construct_chain():
    messages = []

    user_message =  chain_of_thought.chain_prompt_USER + warning
    messages.append({'role': 'user', 'content': user_message})

    return messages


def construct_critique():
    messages1 = []
    user_message =  zero_shot.zero_shot_prompt_USER + warning
    messages1.append({'role': 'user', 'content': user_message})

    messages2 = []
    user_message =  critique.critique_USER1
    messages2.append({'role': 'user', 'content': user_message})

    messages3 = []
    user_message =  critique.critique_USER2
    messages3.append({'role': 'user', 'content': user_message})
    return messages1, messages2, messages3


def construct_heuristic():
    messages1 = []
    messages1.append({'role': 'system', 'content': general_info.general_info_system})
    user_message =  self_heuristic.heuristic_USER1 + few_shot.few_shot_example1 + few_shot.few_shot_example2 + few_shot.few_shot_example3 + few_shot.few_shot_example4
    messages1.append({'role': 'user', 'content': user_message})

    messages2 = []
    user_message =  self_heuristic.heuristic_USER2 + warning
    messages2.append({'role': 'user', 'content': user_message})

    return messages1, messages2