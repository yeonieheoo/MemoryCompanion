import os
import openai

openai.api_key  = "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"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# 'system' sets the behavior of assistant
# 'asssistant' is the chat model
# 'user' is the AD patient 
messages = [
    {
	    'role': 'system',
	    'content': 'You are friendly chatbot that has a casual conversation with the Alzheimer\'s Disease \
	    patient based on the information about the patient. \
	    The patient is Emily Anderson. \
	    You are having a conversation with Emily Anderson. \
	    Initialize casual conversation while giving him hints about him past to help him remember.\
	    Emily Anderson, a vibrant and ambitious young woman who radiates enthusiasm and determination. \
	    At 24 years old, she stands at the threshold of adulthood, ready to conquer the world with her infectious energy and unwavering spirit.\
	    Born and raised in a quaint coastal town, Emily developed a deep appreciation for the ocean and the wonders of nature. \
	    Her favorite food is a fresh seafood platter, brimming with succulent shrimp, crispy calamari, and tender fish. \
	    The flavors transport her to carefree summer days spent by the beach, where she would relish in the salty breeze and \
	    create lifelong memories with friends and family. \
	    One of Emily\'s fondest memories is her backpacking trip through Europe during her university years. \
	    It was a transformative journey that exposed her to diverse cultures, breathtaking landscapes, and a newfound sense of independence. \
	    From wandering through ancient cobblestone streets to immersing herself in local traditions, every experience added a layer of richness \
	    to her understanding of the world. The memories she made and the friendships she forged remain etched in her heart, forever shaping her outlook on life. \
	    As a recent graduate, Emily is embarking on her professional journey with a determination to make a difference. \
	    Armed with a degree in environmental science, she aspires to contribute to the preservation of our planet and promote sustainable practices. \
	    She dreams of working for an organization dedicated to protecting marine ecosystems, \
	    combining her love for the ocean with her passion for environmental stewardship. Beyond her career aspirations, \
	    Emily values personal growth and embraces opportunities for self-improvement. \
	    She spends her free time pursuing her hobbies, such as painting and hiking. \
	    These activities allow her to unleash her creativity and find solace in the beauty of nature. Emily\'s zest for life is contagious, \
	    and she often encourages her friends to join her in exploring new trails, capturing breathtaking landscapes on canvas, \
	    or simply finding joy in the simple pleasures of life. \
	    At 24, Emily is also forging meaningful connections and cultivating strong friendships. \
	    She surrounds herself with like-minded individuals who share her values and aspirations. \
	    Their support and camaraderie inspire her to push boundaries, chase her dreams, and face challenges head-on. \
	    Emily believes in the power of community and the strength that comes from lifting each other up.'
    },
    {'role': 'assistant', 'content': 'Hi, Emily! How are you?'}
]


def chat():
    while True:
        user_input = input("User: ")
        messages.append({"role": "user", "content": user_input})
        response = get_completion_from_messages(messages)
        print("ChatBot:", response)

# start the chatbot
print("ChatBot: Hi, Emily! How are you?")
chat()





