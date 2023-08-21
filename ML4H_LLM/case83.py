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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Seo-jun Park. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Seo-jun Park\
        Gender: Male\
        Age: 54\
        Ethnicity: Korean\
        Religion: Buddhism\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Korean, speaks English\
        Family: Single, two nieces\
        Location: Dallas, Texas\
        Seo-jun was a Taekwondo master, holding a black belt 5th dan.\
        What’s important to him?\
        Martial arts is his life, emphasizing discipline, respect, and self-control.\
        What’s happening for him at the moment?\
        He\'s starting to forget certain techniques and the philosophy behind them.\
        What is the impact on him?\
        He feels he\'s losing his life\'s purpose and the respect of his students.\
        What would he like to happen in the future?\
        Seo-jun wants to write a book on the philosophy of Taekwondo, hoping to inspire others.\
        What strengths and support networks does he have?\
        His nieces, both martial artists, train with him. The martial arts community respects his decades of dedication.'
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