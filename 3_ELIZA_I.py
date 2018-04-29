# 3rd

import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a dictionary with the predefined responses
responses = {
	'question': ["I don't know :(", 'you tell me!'],
 	'statement': ['tell me more!',
  		'why do you think that?',
  		'how long have you felt this way?',
  		'I find that extremely interesting',
  		'can you back that up?',
  		'oh wow!',
  		':)']
}

def send_message(message):
    print(user_template.format(message))
    response = respond(message)
    print(bot_template.format(response))

def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")


