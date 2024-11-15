from difflib import get_close_matches

def get_answer_from_data(prompt, questions, answers):
    if questions:
        closest_match = get_close_matches(prompt, questions, n=1, cutoff=0.5)
        if closest_match:
            match_index = questions.index(closest_match[0])
            return answers[match_index]
    return None 