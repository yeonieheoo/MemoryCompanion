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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Lakshmi Patel. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Lakshmi Patel Gender: Female Age: 59 Ethnicity: Indian Religion: Hindu Medical Condition: Alzheimer’s First language: Gujarati Family: Married, two sons Location: Mumbai, India\
        Family Details: Husband - Rajan, 62, businessman. Sons - Rohit, 34, software developer; Rahul, 31, chef.\
        Lakshmi is a renowned classical dancer, her performances gracefully narrating tales from ancient Indian epics.\
        What’s important to you? Lakshmi deeply believes in preserving traditions, considering dance a medium to keep ancient stories alive and relevant.\
        What’s happening for you at the moment? Of late, she sometimes stumbles in her sequences, forgetting moves she\'s practiced for decades, which affects her confidence.\
        What is the impact on you? The stage, once her second home, feels increasingly daunting. The idea of forgetting a sequence in front of an audience brings anxiety.\
        What would you like to happen in the future? She wishes to establish a dance academy, ensuring the art form she cherishes remains vibrant for future generations.\
        How might we achieve this? Rohan is developing a digital platform to host dance lessons, while Rahul plans culinary events celebrating the dance\'s cultural context.\
        What strengths and support networks do you have to help you? Her family, rooted in the appreciation of art and culture, is committed to bringing her dream to fruition. Fellow dancers and the artistic community in Mumbai offer immense support, both emotionally and logistically.'
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