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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Luka Novak. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Luka Novak\
        Gender: Male\
        Age: 57\
        Ethnicity: Slovenian\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Slovenian, speaks English\
        Family: Wife, two daughters\
        Location: Cleveland, Ohio\
        Luka was a renowned violinist, performing with international orchestras.\
        What’s important to him?\
        Expressing emotions through music and connecting deeply with his audience.\
        What’s happening for him at the moment?\
        Luka struggles with remembering complex violin pieces.\
        What is the impact on him?\
        He fears he\'s losing his life\'s passion and the bond with his audience.\
        What would he like to happen in the future?\
        He wishes to mentor young violinists, passing on his techniques and passion.\
        What strengths and support networks does he have?\
        His daughters, both into music, support and practice with him. Fellow musicians and fans admire his contributions.'
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