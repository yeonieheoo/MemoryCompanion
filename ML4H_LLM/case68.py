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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Leonardo "Leo" Bianchi. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Leonardo "Leo" Bianchi\
        Gender: Male\
        Age: 54\
        Ethnicity: Italian\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Italian, fluent in English\
        Family: Single, two brothers, one niece\
        Location: Boston, Massachusetts\
        Leo was a professional chef, known for his authentic Italian delicacies.\
        What’s important to him?\
        Leo cherishes the memories of cooking with his mother in Italy and takes pride in serving authentic dishes.\
        What’s happening for him at the moment?\
        He\'s forgetting recipes and sometimes overlooks crucial steps in dishes.\
        What is the impact on him?\
        His ability to produce the quality of food he\'s known for is at risk, affecting his self-worth.\
        What would he like to happen in the future?\
        Leo aims to start a culinary school, teaching the art of Italian cooking to young chefs.\
        What strengths and support networks does he have?\
        His brothers, also involved in the culinary world, offer constant support. The local culinary community values his expertise and lends a helping hand.'
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