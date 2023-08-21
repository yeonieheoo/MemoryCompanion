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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Isla MacGregor. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Isla MacGregor\
        Gender: Female\
        Age: 53\
        Ethnicity: Scottish\
        Religion: Protestant\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Scots Gaelic, fluent in English\
        Family: Two daughters\
        Location: Denver, Colorado\
        Isla was a folklorist, preserving Scottish tales and traditions.\
        What’s important to her?\
        Keeping the essence of Scottish folklore alive for future generations.\
        What’s happening for her at the moment?\
        She often forgets parts of tales or the morals behind them.\
        What is the impact on her?\
        Isla feels she\'s losing touch with a core part of her heritage.\
        What would she like to happen in the future?\
        She wants to create an interactive platform to share Scottish folklore globally.\
        What strengths and support networks does she have?\
        Her daughters love listening to her tales. The Scottish diaspora in Denver values her contributions.'
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