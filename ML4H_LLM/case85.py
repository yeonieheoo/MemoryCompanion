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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Aliyah Mahmoud. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Aliyah Mahmoud\
        Gender: Female\
        Age: 60\
        Ethnicity: Egyptian\
        Religion: Islam\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Arabic, fluent in English\
        Family: Three sons\
        Location: Detroit, Michigan\
        Aliyah was an archaeologist, often visiting historical Egyptian sites.\
        What’s important to her?\
        Preserving Egypt\'s ancient history and passing on knowledge to future generations.\
        What’s happening for her at the moment?\
        She sometimes forgets historical timelines or the significance of certain artifacts.\
        What is the impact on her?\
        She\'s becoming distressed, feeling she might overlook vital historical findings.\
        What would she like to happen in the future?\
        Aliyah hopes to establish an interactive museum in the US focusing on Egyptian history.\
        What strengths and support networks does she have?\
        Her sons, fascinated by her work, often accompany her on field trips. The academic community respects her decades of research.'
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