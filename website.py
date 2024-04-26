from flask import Flask, request, jsonify, render_template
import ollama

model = 'llama3'
history = []

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', history=history)

@app.route('/send_message', methods=['POST'])
def send_message():
    message = {'role': 'user', 'content': request.json['message']}
    history.append(message)
    response = ollama.chat(model=model, messages=history)
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
    app.run(debug=True)