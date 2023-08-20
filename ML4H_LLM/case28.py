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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Soraya Shah. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Soraya Shah Gender: Female Age: 52 Ethnicity: South Asian Religion: Islam Medical Condition: Alzheimer’s First language: Urdu Family: Widowed, three sons Location: Karachi, Pakistan\
        Family Details: Sons - Asif, 29, software engineer; Bilal, 27, schoolteacher; and Rizwan, 24, medical student.\
        Soraya had been a school principal before retirement, and she\'s passionate about children\'s education.\
        What\’s important to you? Education and nurturing young minds hold a special place in Soraya\'s heart. She believes that a solid foundation can shape the future of any child.\
        What\’s happening for you at the moment? Recently, Soraya has found it challenging to recall events from the past week and has occasionally become disoriented while visiting her old school.\
        What is the impact on you? Soraya has pulled back from active participation in school events, fearful of embarrassing situations or not recognizing familiar faces.\
        What would you like to happen in the future? Soraya hopes to set up a scholarship fund for underprivileged students, continuing her legacy of fostering education.\
        How might we achieve this? Her sons are collaborating with the school\'s alumni network to establish the scholarship in her name, ensuring bright students get the education they deserve.\
        What strengths and support networks do you have to help you? Soraya’s passion for education remains intact, and her three sons are pillars of support. Additionally, her deep-rooted connections with the teaching community assure her of ongoing assistance.'
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