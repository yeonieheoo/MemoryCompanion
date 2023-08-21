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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Javier Garcia. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Javier Garcia\
        Gender: Male\
        Age: 54\
        Ethnicity: Mexican\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Spanish, speaks English\
        Family: Wife, three daughters\
        Location: Phoenix, Arizona\
        Javier was a muralist, painting vibrant scenes depicting Mexican history.\
        What’s important to him?\
        Art, as a medium, speaks volumes, capturing the essence of culture and history.\
        What’s happening for him at the moment?\
        He struggles to recall specific color palettes or historical events for his murals.\
        What is the impact on him?\
        His inability to depict his culture\'s richness in murals saddens him.\
        What would he like to happen in the future?\
        Javier wants to create a collaborative mural space, inviting artists to paint and learn.\
        What strengths and support networks does he have?\
        His daughters often assist in painting. The local artist community and the Mexican diaspora in Phoenix value his work.'
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