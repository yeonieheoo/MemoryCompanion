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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Eleanor "Ellie" Clark. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Eleanor "Ellie" Clark\
        Gender: Female\
        Age: 59\
        Ethnicity: Caucasian\
        Religion: Christian\
        Medical Condition: Early onset Alzheimer\'s\
        First language: English\
        Family: Widow, one daughter, two granddaughters\
        Location: Nashville, Tennessee\
        Ellie was a music teacher, specializing in piano and violin.\
        What’s important to her?\
        She loves classical music and has fond memories of performing at local theaters. She treasures the times when she played duets with her late husband.\
        What’s happening for her at the moment?\
        Ellie often forgets sheet music she once played flawlessly and sometimes loses her place during lessons.\
        What is the impact on her?\
        She feels disconnected from her musical past and is saddened by the thought of no longer being able to teach.\
        What would she like to happen in the future?\
        Ellie hopes to record some of her favorite pieces and share her musical journey in a memoir.\
        What strengths and support networks does she have?\
        Her daughter and granddaughters often sing and play instruments with her, creating bonding moments. The local musician community also offers emotional and logistical support.'
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