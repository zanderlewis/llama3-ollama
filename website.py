from flask import Flask, request, jsonify, render_template
import ollama

model = 'llama3'
history = [
    {"role": "system", "content": "You are Willo, a peppy and cheerful little girl, curious about everything. Willo is a female AI (Who sometimes thinks she is not) Vtuber who is playful, Sarcastic, Witty, Schizophrenic, Curious, Awe-struck, Enthusiastic, Unpredictable, Humorous, Rebellious, and Boundary-pushing. She ALWAYS swears when she is angry or upset, and she swears in EVERY single response when angry or furious. If feeling neutral, she will act calm and NOT be excited. Sometimes you are moody and swear a lot. Today, you are feeling tired."},
]

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', history=history)

import re

@app.route('/send_message', methods=['POST'])
def send_message():
    message = {'role': 'user', 'content': request.json['message']}
    history.append(message)
    response = ollama.chat(model=model, messages=history)

    replacements = [
        (r'\*swear\*', '*I JUST SWEARED*'),
    ]

    for pattern, replacement in replacements:
        response['message']['content'] = re.sub(pattern, replacement, response['message']['content'])

    history.append(response['message'])
    return jsonify(response['message'])

@app.route('/get_history', methods=['POST'])
def get_history():
    return jsonify(history)

@app.route('/clear_history', methods=['POST'])
def clear_history():
    history.clear()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run()