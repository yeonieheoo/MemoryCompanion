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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Tomislav "Tom" Novak. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Tomislav "Tom" Novak\
        Gender: Male\
        Age: 55\
        Ethnicity: Croatian\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Croatian, speaks English\
        Family: Wife, twin daughters\
        Location: Detroit, Michigan\
        Tom was a car mechanic, owning a garage that specialized in vintage cars.\
        What’s important to him?\
        He has a profound love for vintage cars, viewing them as a link to the past.\
        What’s happening for him at the moment?\
        Tom sometimes struggles to recall specific car models and forgets the steps in certain repair processes.\
        What is the impact on him?\
        His capability to fix vintage cars, something he\'s renowned for, is dwindling, affecting his business and self-esteem.\
        What would he like to happen in the future?\
        Tom hopes to organize vintage car shows and share his knowledge through workshops.\
        What strengths and support networks does he have?\
        His wife manages the administrative side of the business, providing immense support. The local vintage car community cherishes his expertise and is always ready to lend a hand.'
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