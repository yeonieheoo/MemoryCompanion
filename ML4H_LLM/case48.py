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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Clara Rosenberg. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Clara Rosenberg Gender: Female Age: 52 Ethnicity: Jewish Religion: Judaism Medical Condition: Alzheimer’s First language: Hebrew Family: Married, two daughters Location: Tel Aviv, Israel\
        Family Details: Husband - Eli, 55, architect; Daughters - Tamar, 29, musician; Leah, 25, marine biologist.\
        Clara was a music teacher who introduced countless students to the beauty of classical music.\
        What’s important to you? For Clara, music is not just sound; it\'s a narrative of emotions and history. She cherishes the moments when a student finds their passion in a piece.\
        What’s happening for you at the moment? Remembering notes, sequences, or even students\' names has become challenging for Clara.\
        What is the impact on you? The melodies that once flowed effortlessly are now a struggle, leading to moments of despair and longing.\
        What would you like to happen in the future? Clara wishes to create a community music ensemble that bridges generations, allowing both young and old to experience the joys of collaborative performance.\
        How might we achieve this? Tamar uses her musical connections to source instruments and recruit members, while Leah connects with environmental groups to host concerts at the beach, combining the magic of music with the wonders of marine life.\
        What strengths and support networks do you have to help you? Former students, in gratitude for Clara\'s teachings, volunteer their time and talents. Eli designs a beautiful stage for outdoor concerts. The local community, familiar with Clara\'s contributions, lends unwavering support.'
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