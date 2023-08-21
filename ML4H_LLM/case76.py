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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Diego Gonzalez. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Diego Gonzalez\
        Gender: Male\
        Age: 54\
        Ethnicity: Mexican\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Spanish, speaks English\
        Family: Single, two brothers\
        Location: San Antonio, Texas\
        Diego was a chef, known for his traditional Mexican cuisine.\
        What’s important to him?\
        He takes pride in using recipes passed down through generations, always emphasizing the importance of family meals.\
        What’s happening for him at the moment?\
        Diego sometimes forgets ingredient combinations or cooking techniques.\
        What is the impact on him?\
        He\'s worried about disappointing his restaurant patrons and losing his culinary touch.\
        What would he like to happen in the future?\
        He aims to publish a cookbook and train aspiring chefs in his culinary art.\
        What strengths and support networks does he have?\
        His brothers, who co-run the restaurant, are always by his side, offering assistance. Many in the local community admire his culinary skills.'
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