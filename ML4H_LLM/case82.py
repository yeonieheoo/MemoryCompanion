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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Julia Fernandes. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Julia Fernandes\
        Gender: Female\
        Age: 57\
        Ethnicity: Brazilian\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Portuguese, speaks English\
        Family: Husband (deceased), one daughter\
        Location: Orlando, Florida\
        Julia was a samba dancer, bringing the rhythms of Brazil to the US.\
        What’s important to her?\
        Samba is more than dance; it\'s the heartbeat of her culture and a source of joy.\
        What’s happening for her at the moment?\
        She struggles to remember dance steps and loses rhythm more frequently.\
        What is the impact on her?\
        She\'s disheartened, feeling she\'s losing a part of her soul with every step forgotten.\
        What would she like to happen in the future?\
        Julia wants to open a dance school, ensuring samba remains vibrant in her community.\
        What strengths and support networks does she have?\
        Her daughter, also a dancer, practices with her daily. The Brazilian community in Orlando rallies around her.'
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