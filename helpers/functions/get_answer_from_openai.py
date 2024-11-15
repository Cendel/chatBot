import openai
                    
def get_answer_from_openai(prompt,system_message, max_tokens=70, temperature=0):
    
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
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
        return "I'm sorry, but I couldn't process your request right now. Please try again later. 🙁"




