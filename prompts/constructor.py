from prompts import *
from .basic import *
from .one_shot import *
from .few_shot import *
from .general_info import *
from .expertise import *
from .chain_of_thought import *
from .critique import *
from .self_heuristic import *

def construct_prompt(prompt_template, bug_report):
    prompt_list = []
    if prompt_template == "zero-shot" :
        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':bug_report})
        pass
    elif prompt_template == "one-shot":
        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':one_shot_example1})
        
        prompt_list.append({'role':'user', 'content':bug_report})
        pass
    elif prompt_template == "few-shot":
        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':few_shot_example1})
        prompt_list.append({'role':'user', 'content':few_shot_example2})
        prompt_list.append({'role':'user', 'content':few_shot_example3})
        prompt_list.append({'role':'user', 'content':few_shot_example4})
        prompt_list.append({'role':'user', 'content':bug_report})
        pass
    elif prompt_template == "general-info":
        prompt_list.append({'role':'system', 'content':role})
        prompt_list.append({'role':'system', 'content':reinforce})

        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':task_confirmation})
        #response
        prompt_list.append({'role':'user', 'content':positive_feedback})
        prompt_list.append({'role':'user', 'content':bug_report})
        pass

    elif prompt_template == "expertise":
        prompt_list.append({'role':'system', 'content':role})
        prompt_list.append({'role':'system', 'content':expertise})
        prompt_list.append({'role':'system', 'content':reinforce})

        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':task_confirmation})
        #response
        prompt_list.append({'role':'user', 'content':positive_feedback})
        prompt_list.append({'role':'user', 'content':bug_report})
        pass

    elif prompt_template == "chain-of-thought":
        prompt_list.append({'role':'user', 'content':bug_report})
        prompt_list.append({'role':'user', 'content':chain_question1})
        #response
        prompt_list.append({'role':'user', 'content':chain_question2})
        #response
        prompt_list.append({'role':'user', 'content':chain_question3})
        #response
        prompt_list.append({'role':'user', 'content':chain_question4})
        #response
        prompt_list.append({'role':'user', 'content':chain_question5})
        #response
        prompt_list.append({'role':'user', 'content':chain_instruction})
        #response
        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':bug_report})
        pass
    elif prompt_template == "critique":
        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':bug_report})
        #response
        prompt_list.append({'role':'user', 'content':review_instrction})
        #response
        prompt_list.append({'role':'user', 'content':improve_instruction})
        pass
    elif prompt_template == "self-heuristic":
        prompt_list.append({'role':'user', 'content':heuristic_instruction1})
        prompt_list.append({'role':'user', 'content':task_confirmation})
        #response
        prompt_list.append({'role':'user', 'content':positive_feedback})
        prompt_list.append({'role':'user', 'content':few_shot_example1})
        prompt_list.append({'role':'user', 'content':few_shot_example2})
        prompt_list.append({'role':'user', 'content':few_shot_example3})
        prompt_list.append({'role':'user', 'content':few_shot_example4})
        prompt_list.append(heuristic_instruction2)
        #response
        prompt_list.append({'role':'user', 'content':task_description})
        prompt_list.append({'role':'user', 'content':bug_report})


        pass
    else:
        pass

    return prompt_list
    
