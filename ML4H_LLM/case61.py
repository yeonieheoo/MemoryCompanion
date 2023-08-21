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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Anastasia "Ana" Popova. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Anastasia "Ana" Popova\
        Gender: Female\
        Age: 51\
        Ethnicity: Russian\
        Religion: Eastern Orthodox\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Russian, fluent in English\
        Family: Single, one sister, two nephews\
        Location: New York City, New York\
        Ana was a ballet instructor at a prestigious academy in NYC.\
        What’s important to her?\
        Ana takes pride in her Russian heritage and the discipline ballet has instilled in her. She loves seeing her students succeed on stage.\
        What’s happening for her at the moment?\
        She\'s finding it hard to demonstrate complex ballet moves, and occasionally, she loses balance while teaching.\
        What is the impact on her?\
        Ana feels a diminishing connection to ballet, her lifelong passion. Her confidence in teaching is waning.\
        What would she like to happen in the future?\
        Ana hopes to document her teaching methods in a series and mentor a successor to continue her legacy.\
        What strengths and support networks does she have?\
        Her sister and nephews are a constant source of comfort. Her students and colleagues from the ballet community rally around her, offering support and understanding.'
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