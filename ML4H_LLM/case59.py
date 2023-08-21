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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Aria Ito. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Aria Ito\
        Gender: Female\
        Age: 56\
        Ethnicity: Japanese\
        Religion: Shinto\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Japanese, speaks English\
        Family: Husband, one son\
        Location: Seattle, Washington\
        Aria is a master of Ikebana (Japanese flower arrangement) and has taught classes at a local community center for years.\
        What’s important to her?\
        Aria deeply values the philosophy behind Ikebana and believes in harmonizing with nature. She has a close bond with her son, who has always shown interest in her art.\
        What’s happening for her at the moment?\
        She\'s been having difficulty remembering certain floral arrangements, and recently, she lost track of an entire class session.\
        What is the impact on her?\
        Aria feels a sense of loss, fearing that she might forget the intricate details of Ikebana. She\'s also worried about losing touch with her students.\
        What would she like to happen in the future?\
        Aria hopes to capture her teachings on video, preserving her techniques. She also wishes to impart as much knowledge as possible to her son.\
        What strengths and support networks does she have?\
        Her husband helps manage her classes, and her son has shown keen interest in learning and preserving her legacy. The community center and her students offer support and understanding.'
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