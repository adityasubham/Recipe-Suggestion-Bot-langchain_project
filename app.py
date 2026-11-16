
import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Load API key from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API key not found. Please add it in the .env file.")
    exit()


# Connect Gemini AI model
try:
    model = ChatGoogleGenerativeAI(
        model="gemini-3.8-flash",
        google_api_key=api_key,
        temperature=0.7
    )

except Exception as error:
    print("Error connecting to Gemini:", error)
    exit()


# Create prompt template
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a friendly Recipe Suggestion Bot. "
        "Suggest simple recipes based on the ingredients "
        "provided by the user. Use easy English and simple "
        "cooking instructions. Mention the recipe name, "
        "preparation time, ingredients and cooking steps. "
        "Respect vegetarian preferences and food allergies. "
        "If no ingredients are provided, ask the user to "
        "enter the available ingredients."
    ),
    ("human", "{user_input}")
])


# Create LangChain chain
recipe_chain = prompt | model | StrOutputParser()


# Main function
def main():

    print("=" * 50)
    print("          RECIPE SUGGESTION BOT")
    print("=" * 50)

    print("Enter the ingredients available at your home.")
    print("I will suggest a recipe for you.")
    print("Type 'exit' to close the chatbot.\n")

    while True:

        user_input = input("You: ").strip()

        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Thank you for using Recipe Suggestion Bot!")
            break

        if not user_input:
            print("Bot: Please enter some ingredients.\n")
            continue

        try:
            response = recipe_chain.invoke({
                "user_input": user_input
            })

            print("\nSuggested Recipe:\n")
            print(response)
            print()

        except Exception as error:

            error_message = str(error).upper()

            if "429" in error_message or "RESOURCE_EXHAUSTED" in error_message:
                print("\nBot: Your Gemini API request limit has been reached.")
                print("Please try again after your quota resets.\n")

            elif "503" in error_message or "UNAVAILABLE" in error_message:
                print("\nBot: Gemini server is currently busy.")
                print("Please try again after some time.\n")

            elif "401" in error_message or "403" in error_message:
                print("\nBot: API authentication failed.")
                print("Please check your Gemini API key.\n")

            else:
                print("\nBot: Sorry, I could not suggest a recipe.")
                print("Please check your internet connection and settings.")
                print("Error:", error)
                print()


# Run the program
if __name__ == "__main__":
    main()
