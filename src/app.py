from flask import Flask, render_template, jsonify, request
from word_service import get_random_word
from game_logic import check_guess

app = Flask(__name__)

# Store the current word in memory (in production, use proper session management)
current_word = None

@app.route('/')
def home():
    global current_word
    current_word = get_random_word()
    return render_template('game.html')

@app.route('/check_guess', methods=['POST'])
def process_guess():
    guess = request.json.get('guess', '').lower()
    if not guess or len(guess) != 5:
        return jsonify({'error': 'Invalid guess'}), 400
    
    result = check_guess(guess, current_word)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)