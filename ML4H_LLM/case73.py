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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Grace Okafor. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Grace Okafor\
        Gender: Female\
        Age: 56\
        Ethnicity: Nigerian\
        Religion: Protestant\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Igbo, fluent in English\
        Family: Husband, two sons, one daughter\
        Location: Houston, Texas\
        Grace was a pediatric nurse, known for her compassionate approach.\
        What’s important to her?\
        She values her ability to connect with children and provide comfort during their hospital stays.\
        What’s happening for her at the moment?\
        Grace sometimes forgets medical procedures and has moments of confusion regarding patient histories.\
        What is the impact on her?\
        She\'s deeply concerned about the welfare of her young patients and her capacity to provide them with the best care.\
        What would she like to happen in the future?\
        Grace aims to volunteer for children\'s charities and wishes to document her nursing experiences in a book.\
        What strengths and support networks does she have?\
        Her family provides emotional stability, often discussing her day-to-day experiences. The nursing community rallies around her, offering support and guidance.'
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