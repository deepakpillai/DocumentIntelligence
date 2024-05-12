import openai

def process_prompt(message_history, temperature=0.1):
    openai.api_type = ""
    openai.api_base = ""
    openai.api_version = ""
    openai.api_key = ""
    
    response = openai.ChatCompletion.create(
        engine="",
        messages = message_history,
        temperature=temperature,
        max_tokens=800,
        top_p=0.2,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    text = response['choices'][0]['message']["content"]
    return text