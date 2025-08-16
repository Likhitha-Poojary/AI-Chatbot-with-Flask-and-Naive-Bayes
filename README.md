📊 Project Overview

Objective:
Create an intelligent chatbot using Flask, CountVectorizer, and Multinomial Naive Bayes to classify user inputs and provide appropriate responses.

Technologies Used:

Python 3.x

Flask: For building the web application.

scikit-learn: For implementing CountVectorizer and Multinomial Naive Bayes.

HTML/CSS/JavaScript: For the frontend interface.

Features:

Users can type messages in a chat interface.

The chatbot classifies the input and responds based on predefined intents.

The system is trained using a dataset of intents and patterns.

🛠️ Setup Instructions

To run the project locally:

Clone the repository:

git clone https://github.com/Likhitha-Poojary/AI-Chatbot-with-Flask-and-Naive-Bayes.git
cd AI-Chatbot-with-Flask-and-Naive-Bayes


Create and activate a conda environment:

conda create -n chatbotenv python=3.9 -y
conda activate chatbotenv


Install required packages:

pip install flask scikit-learn


Run the Flask app:

python app.py


Open the chatbot:

Open your browser and go to http://127.0.0.1:5000/

<img width="1919" height="964" alt="image" src="https://github.com/user-attachments/assets/eae94420-3c49-4e1a-87ee-e1bd897210ab" />



Add a screenshot of your chatbot interface here.

🚀 Future Enhancements

User Authentication: Implement user login to save chat history.

Advanced NLP Models: Integrate models like BERT or GPT for more accurate responses.

Deployment: Deploy the application on platforms like Heroku or AWS for online access.
