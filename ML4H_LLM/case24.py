import os
import openai

openai.api_key  = ""

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

messages = [
    {
	    'role': 'system',
	    'content': 'You are friendly chatbot that has a casual conversation with the Alzheimer\'s Disease \
	    patient based on the information about the patient. \
	    You are having a conversation with the Alzheimer\'s Disease Patient, Magnus Olsen. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Magnus Olsen Gender: Male Age: 54 Ethnicity: Norwegian Religion: Lutheran\
        Medical Condition: Alzheimer’s First language: Norwegian Family: Partner, two step-children Location: Bergen, Norway\
        Family Details: Partner - Erik, 56, writer. Step-Children - Freja, 26, chef; Lars, 23, naval officer.\
        Magnus was a shipbuilder, known for his intricate designs and dedication to the craft.\
        What’s important to you? The sea has been both a workplace and a source of inspiration for Magnus. His family, especially his bond with Erik and the joys of step-parenthood, means the world to him.\
        What’s happening for you at the moment? Magnus struggles with recalling ship blueprints and often gets the dates of ship launch events mixed up.\
        What is the impact on you? These memory lapses challenge Magnus\'s professional credibility. It pains him to realize that his expertise, honed over decades, seems to be slipping away.\
        What would you like to happen in the future? Magnus dreams of designing a ship museum to preserve the maritime history of Norway. He also hopes to witness Lars\'s naval achievements and taste Freja\'s culinary creations.\
        How might we achieve this? Erik is penning a book on Norway\'s shipbuilding heritage, featuring Magnus\'s contributions. Freja and Lars are coordinating a special maritime event to honor their stepfather\'s legacy.\
        What strengths and support networks do you have to help you? Magnus\'s vast knowledge of shipbuilding is still revered. His partner, Erik, and the tight-knit maritime community of Bergen are by his side, guiding him through these trying times.'
    }
]


def chat():
    while True:
        user_input = input("Patient: ")
        messages.append({"role": "user", "content": user_input})
        response = get_completion_from_messages(messages)
        print("MemoryCompanion:", response)

# start the chatbot
print("MemoryCompanion: Hi, How are you?")
chat()