import openai
                
def get_answer_from_openai(prompt,system_message, ai_model, max_tokens=70, temperature=0):
    
    try:
        response = openai.ChatCompletion.create(
            model=ai_model,
            messages = [
                system_message,
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=temperature
        )
        answer = response['choices'][0]['message']['content'].strip()
        return answer
    except Exception as e:
        print(e)
        return "I'm sorry, but I couldn't process your request right now. Please try again later. 🙁"