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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Nina Ivanova. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Nina Ivanova\
        Gender: Female\
        Age: 48\
        Ethnicity: Bulgarian\
        Religion: Eastern Orthodox\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Bulgarian, fluent in English\
        Family: Husband, two children\
        Location: Dallas, Texas\
        Nina was a folklorist, specializing in Slavic myths.\
        What’s important to her?\
        Keeping alive the rich tapestry of Slavic tales and legends.\
        What’s happening for her at the moment?\
        She struggles to recall certain legends or their origins.\
        What is the impact on her?\
        She fears the fading of cultural memories she\'s preserved.\
        What would she like to happen in the future?\
        Nina wishes to organize a Slavic folklore festival, attracting international attention.\
        What strengths and support networks does she have?\
        Her family avidly listens to her tales, and academic circles value her extensive research.'
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