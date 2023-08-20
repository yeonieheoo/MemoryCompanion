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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Aiden Murphy. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Aiden Murphy Gender: Male Age: 54 Ethnicity: White Irish Religion: Catholic Medical Condition: Alzheimer’s First language: English Family: Single, two brothers Location: Dublin, Ireland\
        Family Details: Brothers - Sean, 57, carpenter; and Liam, 50, bartender.\
        Aiden is an amateur astronomer, spending nights observing stars and tracking celestial patterns.\
        What\’s important to you? The universe, with its vastness and mysteries, has always captivated Aiden. He finds solace and connection in stargazing.\
        What\’s happening for you at the moment? Aiden occasionally forgets to set up his telescope properly or loses track of the constellations he\'s observing.\
        What is the impact on you? Aiden has missed out on several celestial events, leading to a feeling of loss and detachment from his beloved hobby.\
        What would you like to happen in the future? He dreams of setting up an astronomy club for youngsters, sparking interest in the wonders of the universe.\
        How might we achieve this? Sean and Liam are working on renting a space for the club, while Aiden is preparing beginner-level content for new members.\
        What strengths and support networks do you have to help you? Aiden\'s vast knowledge about the cosmos is still profound. Both Sean and Liam, along with the local astronomy community, provide the emotional and practical support he needs.'
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