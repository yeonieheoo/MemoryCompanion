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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Aisha Patel. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Aisha Patel\
        Gender: Female\
        Age: 59\
        Ethnicity: Indian\
        Religion: Hindu\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Gujarati, fluent in English\
        Family: Husband, three daughters\
        Location: Jersey City, New Jersey\
        Aisha was a renowned Indian classical dancer, often conducting workshops overseas.\
        What’s important to her?\
        She\'s passionate about promoting her cultural heritage and sharing the essence of Indian dance forms with the world.\
        What\’s happening for her at the moment?\
        She sometimes forgets dance sequences or the names of traditional moves.\
        What is the impact on her?\
        She\'s becoming increasingly frustrated, feeling she\'s losing touch with a core part of her identity.\
        What would she like to happen in the future?\
        Aisha aspires to set up a dance academy to ensure her knowledge and passion are passed on.\
        What strengths and support networks does she have?\
        Her daughters, all dancers, practice with her daily. The global dance community reveres her contributions.'
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