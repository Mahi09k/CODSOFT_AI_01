import random

# Dictionary of responses categorized by intents
responses = {
    'greeting': ['Hello!', 'Hi there!', 'Hey!', 'Greetings!'],
    'goodbye': ['Goodbye!', 'See you later!', 'Bye!', 'Take care!'],
    'thanks': ['You\'re welcome!', 'No problem!', 'My pleasure!'],
    'age': ['I am just a program, so I don\'t have an age.', 'I don\'t age!'],
    'favorite_color': ['I don\'t have eyes, so I don\'t have a favorite color.', 'Maybe blue, like the sky?'],
    'weather': ['The weather is nice today.', 'It\'s sunny outside.', 'Expect some rain later.'],
    'how_are_you': ['I\'m just a bot, but I\'m doing great! How about you?',
                    'I\'m good, thank you! How can I assist you today?'],
    'default': ['I\'m not sure I understand. Could you please rephrase that?', 'Could you repeat that?',
                'I\'m sorry, I didn\'t get that.']
}


# Function to get response based on user input
def get_response(user_input):
    user_input = user_input.lower()

    # Check for specific intents
    if any(word in user_input for word in ['hi', 'hello', 'hey']):
        return random.choice(responses['greeting'])
    elif any(word in user_input for word in ['bye', 'goodbye']):
        return random.choice(responses['goodbye'])
    elif 'thank' in user_input:
        return random.choice(responses['thanks'])
    elif 'how are you' in user_input:
        return random.choice(responses['how_are_you'])
    elif 'age' in user_input:
        return random.choice(responses['age'])
    elif 'favorite color' in user_input:
        return random.choice(responses['favorite_color'])
    elif any(word in user_input for word in ['weather', 'rain', 'sun']):
        return random.choice(responses['weather'])
    else:
        return random.choice(responses['default'])


# Function to simulate a conversation
def main():
    print("ChatBot: Hi! I'm your friendly chatbot. How can I assist you today?")
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print(f"ChatBot: {get_response(user_input)}")
            break
        response = get_response(user_input)
        print(f"ChatBot: {response}")


if __name__ == "__main__":
    main()
