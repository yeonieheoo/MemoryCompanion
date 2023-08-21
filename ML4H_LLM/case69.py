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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Klara Schmidt. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Klara Schmidt\
        Gender: Female\
        Age: 60\
        Ethnicity: German\
        Religion: Lutheran\
        Medical Condition: Early onset Alzheimer\'s\
        First language: German, speaks English\
        Family: Wife, one son\
        Location: Portland, Oregon\
        Klara was a botanist, frequently contributing to journals on plant conservation.\
        What’s important to her?\
        She\'s deeply connected to nature and believes in conserving rare plant species.\
        What\’s happening for her at the moment?\
        She\'s finding it difficult to identify certain plants and sometimes forgets their scientific names.\
        What is the impact on her?\
        Klara is worried about her fading connection with the plant world and the impact on her research work.\
        What would she like to happen in the future?\
        She wishes to establish a conservatory garden, providing a sanctuary for endangered plants.\
        What strengths and support networks does she have?\
        Her wife, an environmentalist, is a pillar of strength. The scientific community provides her with the latest research tools and collaborative opportunities.'
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