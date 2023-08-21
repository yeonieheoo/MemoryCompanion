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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Mikhail Ivanov. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Mikhail Ivanov\
        Gender: Male\
        Age: 58\
        Ethnicity: Russian\
        Religion: Eastern Orthodox\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Russian, fluent in English\
        Family: Wife, two sons\
        Location: Boston, Massachusetts\
        Mikhail was a chess grandmaster, competing internationally.\
        What’s important to him?\
        The strategic depth and intellectual challenge of chess.\
        What’s happening for him at the moment?\
        Mikhail often forgets certain strategic plays or overlooks opponent moves.\
        What is the impact on him?\
        He\'s distressed, fearing he won\'t be able to compete at elite levels.\
        What would he like to happen in the future?\
        Mikhail hopes to coach aspiring chess players and pass on his strategic insights.\
        What strengths and support networks does he have?\
        His sons, both avid chess players, regularly play with him. The global chess community recognizes his achievements.'
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