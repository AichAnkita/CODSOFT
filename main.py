
from chatbot_logic import respond_to_query

def start_chat():
    print("Chatbot: Hello! Type something to start a new conversation (type 'exit'/'adieu'/'peace out' to leave).")

    while True:
        user_message = input("Ankita: ").strip().lower()

        if user_message in ["exit", "adieu","peace out"]:
            print("Chatbot: Thanks for chatting with me.Bye,Bye! Take care dear")
            break

        bot_reply = respond_to_query(user_message)
        print(f"Chatbot: {bot_reply}")

if __name__ == "__main__":
    start_chat()
