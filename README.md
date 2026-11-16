Recipe Suggestion Bot Using LangChain

1. Introduction

The Recipe Suggestion Bot is a simple AI-based chatbot developed using Python and LangChain. It helps users find recipes using the ingredients available at home.

The user enters the names of available ingredients, and the chatbot suggests a suitable recipe with its preparation time, required ingredients and cooking steps.

2. Objective

To develop a simple chatbot using LangChain.

To suggest recipes based on available ingredients.

To understand how to connect an AI model with Python.

To learn how prompt templates are used in LangChain.

3. Technologies Used

Programming Language: Python

Framework: LangChain

AI Model: Google Gemini

Library: Python Dotenv

Editor: Visual Studio Code

4. Project Files

Recipe Suggestion Bot/
│
├── app.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md

app.py – Contains the main chatbot program.

.env – Stores the Gemini API key.

.gitignore – Prevents private files from being uploaded.

requirements.txt – Contains the required Python libraries.

README.md – Contains information about the project.

5. Installation and Setup

Step 1: Create a virtual environment

python -m venv .venv

Step 2: Activate the virtual environment

For Mac:

source .venv/bin/activate

Step 3: Install the required libraries

pip install -r requirements.txt

Step 4: Add the Gemini API key

Create a .env file and add your API key:

GEMINI_API_KEY=your_actual_api_key

Do not share your API key publicly.

6. How to Run the Project

Open the terminal in the project folder and execute:

python app.py

Enter the ingredients available at home. The chatbot will generate a suitable recipe.

Example input:

I have potato, onion, tomato and garlic.

7. Working of the Project

The user enters the available ingredients.

The Python program receives the input.

LangChain sends the input to the prompt template.

The Gemini AI model processes the ingredients.

The chatbot generates a suitable recipe.

The recipe is displayed to the user.

8. Features

Suggests recipes based on available ingredients.

Provides simple cooking instructions.

Displays preparation time and ingredient details.

Uses Google Gemini for generating responses.

Handles empty input and basic errors.

Allows users to exit the chatbot by typing exit.

9. Conclusion

Through this project, I learned how to create a simple AI chatbot using Python and LangChain. I also understood how to connect the Gemini model, use prompt templates and accept user input. This project helped me understand the basic working of an AI-based application.

10. Future Scope

Add a graphical user interface.

Provide different recipe categories.

Add more language options.

Include nutritional information.

Suggest recipes based on dietary preferences.