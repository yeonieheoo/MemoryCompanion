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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Gabriela Rojas. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Gabriela Rojas Gender: Female Age: 54 Ethnicity: Chilean Religion: Catholic Medical Condition: Alzheimer’s First language: Spanish Family: Partner Location: Santiago, Chile\
        Family Details: Partner - Lucia, 56, archaeologist.\
        Gabriela is a renowned chef who specialized in traditional Chilean cuisine. She loves dancing and the sea.\
        What’s important to you? Her recipes, the sea breeze, and the local dance festivals.\
        What’s happening for you at the moment? She sometimes confuses ingredients but still relishes cooking.\
        What is the impact on you? Distress when she can\'t remember specific family recipes.\
        What would you like to happen in the future? To visit Valparaiso and enjoy the sea with Lucia.\
        How might we achieve this? Lucia is organizing a surprise trip for Gabriela\'s upcoming birthday.\
        What strengths and support networks do you have to help you? Gabriela has the support of her culinary community and Lucia\'s unwavering love.'
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