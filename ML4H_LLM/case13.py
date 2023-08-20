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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Rahul Menon. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Rahul Menon Gender: Male Age: 70 Ethnicity: Indian Religion: Hindu Medical Condition: Alzheimer’s First language: Malayalam Family: Wife, son, and two daughters Location: Kerala, India\
        Family Details: Wife - Lakshmi, 68, homemaker. Son - Arun, 45, software engineer in Bangalore. Daughters - Anjali, 43, dance teacher; Deepa, 40, botanist.\
        Rahul was a boatman in the backwaters of Kerala. He enjoys fishing and local festivals.\
        What’s important to you? His memories of navigating the waters and the camaraderie of fellow boatmen.\
        What’s happening for you at the moment? Forgets specific routes but recalls festivals vividly.\
        What is the impact on you? He becomes restless if kept away from the water for long.\
        What would you like to happen in the future? Wishes to partake in the annual boat race one more time.\
        How might we achieve this? Arun and Anjali are planning to organize a small boat race in his honor.\
        What strengths and support networks do you have to help you? Rahul is beloved in his community, and his family is deeply supportive.'
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