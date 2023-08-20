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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Elijah Moore. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Elijah Moore Gender: Male Age: 58 Ethnicity: African American Religion: Baptist Medical Condition: Alzheimer’s First language: English Family: Wife and two daughters Location: Atlanta, USA\
        Family Details: Wife - Keisha, 57, pharmacist. Daughters - Jasmine, 32, lawyer; Maya, 28, photographer.\
        Elijah was a jazz musician. He loves playing the saxophone and attending jazz festivals.\
        What’s important to you? His music, weekend family BBQs, and mentoring young musicians.\
        What’s happening for you at the moment? He occasionally forgets tunes but can still feel the rhythm.\
        What is the impact on you? Frustration when he can\'t play complex pieces as before.\
        What would you like to happen in the future? To play one last show at a renowned jazz club.\
        How might we achieve this? His daughters are planning a special concert in his honor.\
        What strengths and support networks do you have to help you? Elijah has a tight-knit community of musicians and unwavering support from his family.'
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