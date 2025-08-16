import json
import random
from flask import Flask, request, jsonify, render_template_string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load intents dataset
with open("intents.json") as f:
    intents = json.load(f)

# Prepare training data
X, y = [], []
for intent in intents['intents']:
    for pattern in intent['patterns']:
        X.append(pattern)
        y.append(intent['tag'])

# Train model
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)
model = MultinomialNB()
model.fit(X_vec, y)

# Function to get chatbot response
def get_response(user_input):
    input_vec = vectorizer.transform([user_input])
    pred = model.predict(input_vec)[0]
    for intent in intents['intents']:
        if intent['tag'] == pred:
            return random.choice(intent['responses'])
    return "Sorry, I didn’t understand that."

# Flask app
app = Flask(__name__)

# Home route with chat interface
@app.route("/", methods=["GET"])
def home():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Chatbot</title>
        <style>
            body { font-family: Arial, sans-serif; margin: 50px; }
            #chatbox { width: 500px; height: 400px; border: 1px solid #ccc; padding: 10px; overflow-y: scroll; }
            #userInput { width: 400px; padding: 10px; }
            button { padding: 10px; }
            .user { color: blue; }
            .bot { color: green; }
        </style>
    </head>
    <body>
        <h2>Chatbot</h2>
        <div id="chatbox"></div>
        <input type="text" id="userInput" placeholder="Type a message..." />
        <button onclick="sendMessage()">Send</button>

        <script>
            function sendMessage() {
                let input = document.getElementById('userInput').value;
                if(input.trim() === "") return;
                
                let chatbox = document.getElementById('chatbox');
                chatbox.innerHTML += '<div class="user"><b>You:</b> ' + input + '</div>';

                fetch('/chat', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ message: input })
                })
                .then(response => response.json())
                .then(data => {
                    chatbox.innerHTML += '<div class="bot"><b>Bot:</b> ' + data.response + '</div>';
                    chatbox.scrollTop = chatbox.scrollHeight;
                });

                document.getElementById('userInput').value = '';
            }

            document.getElementById("userInput").addEventListener("keypress", function(e) {
                if(e.key === "Enter") sendMessage();
            });
        </script>
    </body>
    </html>
    """
    return render_template_string(html_content)

# Chat API route
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    response = get_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
