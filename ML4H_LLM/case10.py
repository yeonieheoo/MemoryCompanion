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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Amina Said. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Amina Said Gender: Female Age: 80 Ethnicity: Moroccan Religion: Islam Medical Condition: Alzheimer’s First language: Arabic Family: Three sons Location: Marrakech, Morocco\
        Family Details: Sons - Youssef, 56, carpet trader; Idris, 53, chef; Samir, 49, history teacher.\
        Amina was a spice merchant. She enjoys cooking traditional Moroccan dishes and has a keen sense of smell.\
        What\’s important to you? Family gatherings and preparing meals for special occasions.\
        What\’s happening for you at the moment? Amina sometimes forgets ingredients but recalls the tastes distinctly.\
        What is the impact on you? She feels disheartened when she can\'t remember family recipes.\
        What would you like to happen in the future? She hopes to pass down her culinary secrets to her granddaughters.\
        How might we achieve this? Idris is compiling a family recipe book with Amina\'s guidance.\
        What strengths and support networks do you have to help you? Amina is revered in her community for her culinary skills, and her sons are always by her side.'
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