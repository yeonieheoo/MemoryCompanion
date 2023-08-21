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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Mira Patel. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Mira Patel\
        Gender: Female\
        Age: 58\
        Ethnicity: Indian\
        Religion: Hindu\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Gujarati, fluent in English\
        Family: Husband, two sons, and a daughter-in-law\
        Location: New Jersey\
        Mira was a mathematics teacher. She enjoys cooking traditional Indian meals and has a vast collection of sarees. Festivals, especially Diwali, are a big affair in her home. She\'s deeply rooted in her culture and traditions.\
        What\’s important to her?\
        Mira values her culture and is passionate about passing her traditions to the next generation. Her recipes, collected over decades, mean a lot to her. She\'s also concerned about forgetting important religious practices.\
        What\’s happening for her at the moment?\
        She\'s been misplacing items more frequently and forgetting steps in her recipes. This Diwali, she couldn\'t recall a ritual she\'s been performing for years.\
        What is the impact on her?\
        Mira is distressed when she forgets cultural and religious practices, fearing she won\'t be able to pass them on. She\'s also been avoiding social gatherings, fearing judgment.\
        What would she like to happen in the future?\
        Mira hopes to document her recipes and rituals, possibly with the help of her family. She\'s also looking into joining a local support group for people with early onset Alzheimer\'s.\
        What strengths and support networks does she have?\
        Her family is closely-knit and supportive. The local Indian community also provides cultural support. Her neighbor, Lisa, has been a great help, assisting Mira with daily tasks.'
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