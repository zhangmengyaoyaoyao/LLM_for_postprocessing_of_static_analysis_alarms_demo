import ollama
import time

def get_response(model, messages, max_retries=15):
    retries = 0
    while retries < max_retries:
        print("try for ", retries, " times")
        try:
            response = ollama.chat(
                model=model,  
                messages=messages,
            ) 
            return response
        except Exception as e:
            print(f"Rate limit exceeded: {e}. Retrying in 3 seconds...")
            retries += 1
            time.sleep(3)  # wait for 3 seconds before retrying
    raise Exception("Max retries exceeded. Could not get response.")


def call_with_message(model, messages):
    response = get_response(model, messages)
    # print("messages----", messages)
    # print("response---",response.choices[0].message)
    return response


def call_with_3messages(model, messages):
    history_response = [] # 保存回复
    # 如果是多轮对话
    # 展开元组为单个列表
    messages = [msg for sublist in messages for msg in sublist]
    message_with_historys = [] # 保存历史消息, 用于多轮对话
    print("Processing multiple rounds of messages")

    response = None
    for message in messages:
        # print("Processing message----", message)
        message_with_historys.append(message)
        # print("complete-----", message_with_historys)
        seccuss = False
        while not seccuss:
            response = get_response(model, message_with_historys)
            if response is None:
                print("generated_message is None")
            else:
                generated_message = {'role': 'assistant', 'content': response['message']['content']}
                # print("generated_message" , generated_message)
                message_with_historys.append(generated_message)  # 将模型生成的回复加入历史
                history_response.append(generated_message)
                seccuss = True

    return response, history_response

def call_with_2messages(model, messages):
    history_response = []  # 保存回复
    # 如果是多轮对话
    # 展开元组为单个列表
    messages = [msg for sublist in messages for msg in sublist]
    message_with_historys = [] # 保存历史消息, 用于多轮对话
    print("Processing multiple rounds of 2messages")
    count = 0

    response = None
    for message in messages:
        if count == 0:
            message_with_historys.append(message)
            count += 1
            continue
        message_with_historys.append(message)
        # print("Processing message----", message)
        # print("complete-----", message_with_historys)
        seccuss = False
        while not seccuss:
            response = get_response(model, message_with_historys)

            if response is None:
                print("generated_message is None")
            else:
                generated_message = {'role': 'assistant', 'content': response['message']['content']}
                # print("generated_message" , generated_message)
                message_with_historys.append(generated_message)  # 将模型生成的回复加入历史
                history_response.append(generated_message)
                seccuss = True
        count += 1
    # print("/////////////////historyhere////////////////////", history_response) 
    return response, history_response
