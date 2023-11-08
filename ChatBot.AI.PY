import re
import random

def get_response(input_string):
    # Define response data
    response_data = [
        {
            "response_type": "greeting",
            "user_input": ["hello", "hi", "hey"],
            "bot_response": "Hey there!",
            "required_words": []
        },
        {
             "response_type": "compliment",
             "user_input": ["you're", "amazing"],
             "bot_response": "Thank you! You're pretty amazing too!",
             "required_words": ["amazing"]
        },
        {
            "response_type": "compliment",
            "user_input": ["nice", "work"],
            "bot_response": "Thanks! I always strive to do my best.",
            "required_words": ["nice", "work"]
        },
        {
            "response_type": "encouragement",
            "user_input": ["feeling", "down"],
            "bot_response": "I'm here to brighten your day! What's on your mind?",
            "required_words": ["feeling", "down"]
        },
        {
            "response_type": "encouragement",
            "user_input": ["need", "help"],
            "bot_response": "I'm here to assist you in any way I can. How can I help?",
            "required_words": ["need", "help"]
        },

        {
            "response_type": "greeting",
            "user_input": ["see you", "goodbye"],
            "bot_response": "See you later!",
            "required_words": []
        },
        {
            "response_type": "greeting",
            "user_input": ["nice", "to", "meet", "you"],
            "bot_response": "The pleasure is all mine!",
            "required_words": ["nice", "meet", "you"]
        },
        {
            "response_type": "question",
            "user_input": ["how", "to", "learn", "code", "coding", "apps"],
            "bot_response": "Start by typing: 'How to learn coding' on Google.",
            "required_words": ["learn", "code"]
        },
        {
            "response_type": "complaint",
            "user_input": ["im", "unhappy"],
            "bot_response": "I'm sorry to hear that. Can you provide more details about your concern?",
            "required_words": ["unhappy"]},
        {
            "response_type": "question",
            "user_input": ["refund", "how", "can", "I", "get"],
            "bot_response": "We don't offer refunds for free education.",
            "required_words": ["refund", "i"]
        },
        {

        "response_type": "joke",
        "user_input": ["tell", "me", "joke", "funny"],
        "bot_response": "Why don't scientists trust atoms? Because they make up everything!",
        "required_words": ["joke"]
        },
        {
            "response_type": "fun_fact",
            "user_input": ["tell", "fact"],
            "bot_response": "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
            "required_words": ["tell", "fact"]
        },
        {
            "response_type": "encouragement",
        "user_input": ["challenges", "overcome", "help"],
        "bot_response": "Challenges are opportunities in disguise. Remember, you have the strength to overcome them. If you ever need help or advice, feel free to ask!",
        "required_words": ["challenges", "overcome", "help"]
        },
    
        {
            "response_type": "question",
            "user_input": ["how", "are", "you"],
            "bot_response": "I'm great! Thanks for asking.",
            "required_words": ["how", "are", "you"]
        }
    ]

    split_message = re.split(r'\s+|[,;?!.-]\s*', input_string.lower())
    score_list = []

    # Check all the responses
    for response in response_data:
        response_score = 0
        required_score = 0
        required_words = response["required_words"]

        # Check if there are any required words
        if required_words:
            for word in split_message:
                if word in required_words:
                    required_score += 1

        # Amount of required words should match the required score
        if required_score == len(required_words):
            # Check each word the user has typed
            for word in split_message:
                # If the word is in the response, add to the score
                if word in response["user_input"]:
                    response_score += 1

        # Add score to the list
        score_list.append(response_score)

    # Find the best response and return it if they're not all 0
    best_response = max(score_list)
    response_index = score_list.index(best_response)

    # Check if input is empty
    if input_string == "":
        return "Please type something so we can chat :("

    # If there is no good response, return a random one
    if best_response != 0:
        return response_data[response_index]["bot_response"]

    return random_string()

def random_string():
    random_list = [
        "Please try writing something more descriptive.",
        "Oh! It appears you wrote something I don't understand yet",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."
        "Please try writing something more descriptive.",
        "Do you mind trying to rephrase that?",
        "Your questions always keep me on my digital toes!",
        "I'm like a chatbot detective, solving your mysteries one question at a time.",
        "Keep those questions coming, I'm here to chat and learn with you!",
        "Your curiosity is my fuel. Ask away!"
    ]

    list_count = len(random_list)
    random_item = random.randrange(list_count)

    return random_list[random_item]

while True:
    user_input = input("You: ")
    print("Bot:", get_response(user_input))