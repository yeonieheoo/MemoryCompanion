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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Ana Sofia Ramos. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Ana Sofia Ramos Gender: Female Age: 55 Ethnicity: Portuguese Religion: Catholic Medical Condition: Alzheimer’s First language: Portuguese Family: Husband and a son Location: Porto, Portugal\
        Family Details: Husband - Manuel, 56, wine merchant. Son - Pedro, 25, studying architecture in Lisbon.\
        Ana was a school principal. She adores fado music and seaside walks.\
        What’s important to you? Educating children, family traditions, and listening to fado.\
        What’s happening for you at the moment? Ana sometimes confuses her students\' names but finds solace in her daily routines.\
        What is the impact on you? She is distressed when she can\'t remember recent school events.\
        What would you like to happen in the future? Ana hopes to attend Pedro\'s graduation and celebrate with family.\
        How might we achieve this? Manuel and Pedro are organizing a trip to Lisbon for the graduation.\
        What strengths and support networks do you have to help you? Ana is respected in her school community, and her husband and son are her pillars of support.'
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