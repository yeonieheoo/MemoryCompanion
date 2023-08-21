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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Jabari Nkosi. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Jabari Nkosi\
        Gender: Male\
        Age: 56\
        Ethnicity: Zulu\
        Religion: Ancestral Worship\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Zulu, speaks English\
        Family: Wife, five grandchildren\
        Location: Los Angeles, California\
        Jabari was a musician, playing traditional African instruments at cultural events.\
        What’s important to him?\
        He feels connected to his ancestors when playing music and views it as a form of worship.\
        What’s happening for him at the moment?\
        Jabari sometimes forgets tunes or the significance of certain musical instruments.\
        What is the impact on him?\
        He\'s anxious about losing touch with his cultural roots and the spiritual connection music provides.\
        What would he like to happen in the future?\
        He wishes to teach his grandchildren and other youth the significance of traditional music.\
        What strengths and support networks does he have?\
        His wife sings alongside him, ensuring their performances remain harmonious. The local African community holds him in high regard.'
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