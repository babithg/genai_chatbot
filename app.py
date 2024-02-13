import ollama
from flask import Flask, request, jsonify, render_template

def chat_model(user_input):
    print("Fetching response from Ollama...")
    response = ollama.chat(model='starcoder:1b', messages=[
    {
        'role': 'user',
        'content': user_input,
    },
    ])
    return response['message']['content']

# App Initiate 
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.get_json()
        input_text = data.get('text', '')

        output = chat_model(input_text)
        print("Sending back the respose to user as json...")
        return jsonify({'response': output})

if __name__ == '__main__':
    app.run(debug=True)
