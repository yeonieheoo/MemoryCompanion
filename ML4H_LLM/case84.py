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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Isabella Rossi. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Isabella Rossi\
        Gender: Female\
        Age: 55\
        Ethnicity: Italian\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Italian, fluent in English\
        Family: Husband, two sons\
        Location: New York City, New York\
        Isabella was an opera singer, having performed on stages worldwide.\
        What’s important to her?\
        The opera is her world, embodying drama, passion, and the depth of human emotion.\
        What’s happening for her at the moment?\
        She sometimes forgets lyrics or the emotional nuance of certain performances.\
        What is the impact on her?\
        The thought of not performing at her best deeply troubles her, fearing the loss of her audience\'s admiration.\
        What would she like to happen in the future?\
        Isabella dreams of teaching at prestigious music academies, sharing her experience and techniques.\
        What strengths and support networks does she have?\
        Her husband, a pianist, practices daily with her. The global opera community reveres her talent.'
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