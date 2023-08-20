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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Aisha Khan. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Aisha Khan Gender: Female Age: 52 Ethnicity: Pakistani Religion: Islam Medical Condition: Alzheimer’s First language: Urdu Family: Two sons Location: Karachi, Pakistan\
        Family Details: Sons - Faizan, 27, engineer; Bilal, 24, medical student.\
        Aisha ran an embroidery business. She is passionate about traditional Pakistani arts and crafts.\
        What’s important to you? Preserving cultural traditions and spending time with her family.\
        What’s happening for you at the moment? Aisha sometimes forgets embroidery patterns but enjoys teaching others.\
        What is the impact on you? She feels disheartened when she can\'t remember specific designs.\
        What would you like to happen in the future? Aisha hopes to see both her sons settled and happy.\
        How might we achieve this? Faizan and Bilal are looking into setting up an online platform to showcase their mother\'s art.\
        What strengths and support networks do you have to help you? Aisha\'s neighbors and friends ensure she is engaged with regular craft sessions.'
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