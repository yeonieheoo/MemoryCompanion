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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Wei "Will" Zhang. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Wei "Will" Zhang\
        Gender: Male\
        Age: 56\
        Ethnicity: Chinese\
        Religion: Buddhist\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Mandarin, speaks English\
        Family: Wife, two sons\
        Location: San Francisco, California\
        Will was a renowned calligrapher and ran a popular art studio.\
        What’s important to him?\
        Will takes pride in his calligraphy skills, viewing them as a bridge between the ancient and modern worlds.\
        What’s happening for him at the moment?\
        He sometimes mixes up brush strokes and has difficulty remembering certain characters.\
        What is the impact on him?\
        The thought of losing touch with his craft frustrates and saddens him, feeling like he\'s losing a part of his identity.\
        What would he like to happen in the future?\
        Will hopes to host workshops, bringing awareness to the art of calligraphy, and wishes to leave a legacy for future generations.\
        What strengths and support networks does he have?\
        His family is deeply involved in his work, providing emotional and logistical support. His art students and local community value his contribution and assist in various ways.'
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