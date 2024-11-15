import openai
                    
def get_answer_from_openai(prompt, chat_history, max_tokens=70, temperature=0):
    
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=chat_history + [{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=temperature
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        return f"Error: {str(e)}"
