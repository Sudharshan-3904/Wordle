def check_guess(guess, target_word):
    """Check the guess against the target word and return feedback"""
    feedback = []
    for i, (g_char, t_char) in enumerate(zip(guess, target_word)):
        if g_char == t_char:
            feedback.append({'letter': g_char, 'status': 'correct'})
        elif g_char in target_word:
            feedback.append({'letter': g_char, 'status': 'present'})
        else:
            feedback.append({'letter': g_char, 'status': 'absent'})
    
    return {
        'feedback': feedback,
        'is_correct': guess == target_word
    }