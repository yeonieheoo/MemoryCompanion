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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Carlos Morales. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Carlos Morales\
        Gender: Male\
        Age: 52\
        Ethnicity: Puerto Rican\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Spanish, fluent in English\
        Family: Single, two sisters, three nephews\
        Location: San Diego, California\
        Carlos was a naval officer, having served for over 30 years.\
        What’s important to him?\
        He cherishes his time at sea and the bonds formed with fellow officers. Discipline and order are paramount in his life.\
        What’s happening for him at the moment?\
        Carlos sometimes forgets naval codes and has moments of disorientation, even in familiar surroundings.\
        What is the impact on him?\
        He\'s struggling with the thought of being seen as unreliable by his peers, potentially affecting their operations.\
        What would he like to happen in the future?\
        Carlos hopes to mentor young naval cadets and share his experiences through memoirs.\
        What strengths and support networks does he have?\
        His sisters often spend time reminiscing with him. The naval community holds him in high esteem, offering support and counseling.'
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