def respond_to_query(message):
    # Convert to lowercase for case-insensitive matching
    message = message.lower()

    if any(greet in message for greet in ["hello", "hi", "hey"]):
        return "Hello there! How can I help you today?"

    elif "your name" in message or "who are you" in message:
        return "My name is ChittiRobot.I'm your friendly chatbot assistant and here to make your life so easy."

    elif "how are you" in message:
        return "I'm doing well, Thanks for asking!How about you?"

    elif "fine" in message or "good" in message:
        return "Glad to hear that! 😊"

    elif "friend" in message :
        return "yes, I always want to be you friend.you're so kind and good"


    elif "bad" in message or "not good" in message:
        return "I'm sorry to hear that. Want to talk about it?"

    elif "what can you do" in message or "features" in message:
        return "I can chat with you, answer basic questions, and cheer you up if you're feeling down!"

    elif "thank you" in message or "thanks" in message:
        return "You're welcome! 😊"

    elif "bye" in message or "goodbye" in message:
        return "Take care! Hope to chat with you again soon."

    elif "food" in message:
        return "my favourite food is information"
    elif "information" in message:
        return "Every information of everywhere"
    elif "happy" in message:
        return "oo I'm also happy and proud of you "
    elif "time" in message:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."

    elif "date" in message:
        from datetime import datetime
        return f"Today’s date is {datetime.now().strftime('%B %d, %Y')}."

    elif "weather" in message:
        return "I can't access real-time weather, but it's always sunny inside a chatbot!"

    elif "help" in message:
        return "Just type something and I'll try to respond. You can ask about time, jokes, or even just chat casually."

    else:
        return "Sorry, I didn't understand your reply. Can you please try asking me in a different way?"
