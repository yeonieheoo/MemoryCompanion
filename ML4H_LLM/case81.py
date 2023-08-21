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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Khalid Al Sayed. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Khalid Al Sayed\
        Gender: Male\
        Age: 58\
        Ethnicity: Arab\
        Religion: Islam\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Arabic, fluent in English\
        Family: Two wives, six children\
        Location: Chicago, Illinois\
        Khalid was a calligrapher, often crafting verses from the Quran.\
        What’s important to him?\
        He believes calligraphy is a spiritual journey, bringing one closer to God.\
        What’s happening for him at the moment?\
        Khalid struggles to remember certain verses and the intricacies of Arabic calligraphy.\
        What is the impact on him?\
        The difficulty he faces in his art deeply saddens him, fearing he\'s drifting away from his spiritual path.\
        What would he like to happen in the future?\
        He aspires to teach his craft to the younger generation, ensuring the art form lives on.\
        What strengths and support networks does he have?\
        His family, deeply rooted in Islamic traditions, supports him. The Muslim community in Chicago values his work.'
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