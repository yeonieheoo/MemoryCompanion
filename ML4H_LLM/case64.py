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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Alejandro "Alex" Gomez. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Alejandro "Alex" Gomez\
        Gender: Male\
        Age: 58\
        Ethnicity: Cuban\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Spanish, fluent in English\
        Family: Wife, one daughter, two grandsons\
        Location: Miami, Florida\
        Alex owned a popular salsa club in Miami and was an acclaimed salsa dancer.\
        What’s important to him?\
        Alex loves the Cuban culture and the joy of dancing. He dreams of seeing his grandsons take over his club one day.\
        What’s happening for him at the moment?\
        He\'s finding it hard to follow salsa beats and occasionally loses rhythm while dancing.\
        What is the impact on him?\
        Alex is heartbroken over the thought of losing touch with salsa. His self-worth is deeply tied to his dancing prowess.\
        What would he like to happen in the future?\
        Alex hopes to choreograph unique salsa routines and organize dance workshops. He wishes to leave a dancing legacy for his grandsons.\
        What strengths and support networks does he have?\
        His family stands firmly by his side, and his club patrons offer love and support. The dance community in Miami values his contribution and rallies to help.'
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