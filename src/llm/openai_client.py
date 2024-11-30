from openai import OpenAI as openai
import time

def get_response(key, url, model, message, top_p=0.1, temperature=0.1, max_retries=15):
    client = openai(
        api_key=key,
        base_url=url
    ) 
    
    retries = 0
    while retries < max_retries:
        print("try for ", retries, " times")
        try:
            response = client.chat.completions.create(
                model=model,  
                messages=message,
                top_p=top_p,
                temperature=temperature,
                max_tokens=4095,
            ) 
            return response
        except openai.error.RateLimitError as e:
            print(f"Rate limit exceeded: {e}. Retrying in 3 seconds...")
            retries += 1
            time.sleep(3)  # wait for 3 seconds before retrying
    raise Exception("Max retries exceeded. Could not get response.")


def call_with_message(key, url, model, messages):
    response = get_response(key, url, model, messages)
    # print("messages----", messages)
    # print("response---",response.choices[0].message)
    return response


def call_with_3messages(key, url, model, messages):
    history_response = []
    # 如果是多轮对话
    # 展开元组为单个列表
    messages = [msg for sublist in messages for msg in sublist]
    # 保存所有轮次的消息
    message_with_historys = []
    print("Processing multiple rounds of messages")

    for message in messages:
        # print("Processing message----", message)
        message_with_historys.append(message)
        # print("complete-----", message_with_historys)
        seccuss = False
        while not seccuss:
            response = get_response(key, url, model, message_with_historys)

            if response is None:
                print("generated_message is None")
            else:
                generated_message = {'role': 'assistant', 'content': response.choices[0].message.content}
                # print("generated_message" , generated_message)
                message_with_historys.append(generated_message)  # 将模型生成的回复加入历史
                history_response.append(generated_message)
                seccuss = True

    return response, history_response

def call_with_2messages(key, url, model, messages):
    history_response = []
    # 如果是多轮对话
    # 展开元组为单个列表
    messages = [msg for sublist in messages for msg in sublist]
    # 保存所有轮次的消息
    message_with_historys = []
    print("Processing multiple rounds of 3messages")
    count = 0

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
            response = get_response(key, url, model, message_with_historys)

            if response is None:
                print("generated_message is None")
            else:
                generated_message = {'role': 'assistant', 'content': response.choices[0].message.content}
                # print("generated_message" , generated_message)
                message_with_historys.append(generated_message)  # 将模型生成的回复加入历史
                history_response.append(generated_message)
                seccuss = True
        count += 1
    # print("/////////////////historyhere////////////////////", history_response) 
    return response, history_response