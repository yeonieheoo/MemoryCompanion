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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Mateo Bianchi. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Mateo Bianchi\
        Gender: Male\
        Age: 45\
        Ethnicity: Italian\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Italian, fluent in English\
        Family: Wife, one daughter\
        Location: New York, New York\
        Mateo was a chef, running a popular Italian trattoria.\
        What’s important to him?\
        Celebrating family and tradition through food.\
        What’s happening for him at the moment?\
        He occasionally forgets recipes passed down for generations.\
        What is the impact on him?\
        His confidence in the kitchen wanes.\
        What would he like to happen in the future?\
        Mateo dreams of authoring a cookbook, mixing classic recipes with new culinary innovations.\
        What strengths and support networks does he have?\
        His wife manages the restaurant, and food critics admire his culinary prowess.'
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