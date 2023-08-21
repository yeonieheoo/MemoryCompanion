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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Liliana Morales. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Liliana Morales\
        Gender: Female\
        Age: 51\
        Ethnicity: Colombian\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Spanish, speaks English\
        Family: Two sons\
        Location: Miami, Florida\
        Liliana was a dance instructor, teaching Salsa and Cumbia.\
        What’s important to her?\
        The rhythm of life, expressed through dance.\
        What’s happening for her at the moment?\
        Liliana occasionally loses her step sequence.\
        What is the impact on her?\
        She\'s saddened, fearing she may lose her dance spirit.\
        What would she like to happen in the future?\
        She aims to participate in an international dance festival, showcasing Colombian dance forms.\
        What strengths and support networks does she have?\
        Her sons also dance, often joining her. The Latino community in Miami cherishes her energy and passion.'
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