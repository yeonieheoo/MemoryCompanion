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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Robert "Rob" McIntyre. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Robert "Rob" McIntyre\
        Gender: Male\
        Age: 57\
        Ethnicity: Caucasian\
        Religion: Atheist\
        Medical Condition: Early onset Alzheimer\'s\
        First language: English\
        Family: Single, no children, two younger siblings\
        Location: Portland, Oregon\
        Rob worked in software development. He\'s a board game enthusiast and has an impressive collection from various parts of the world.\
        What’s important to him?\
        Rob takes immense pride in his analytical skills and treasures memories of games won against strong opponents. He also values the freedom of living independently.\
        What’s happening for him at the moment?\
        Rob has been struggling to follow complex board game rules, which were previously second nature to him.\
        What is the impact on him?\
        These memory lapses make him feel vulnerable, especially the idea of depending on others or moving to assisted living.\
        What would he like to happen in the future?\
        He hopes to stay independent for as long as possible and wishes to digitize his game collection, making them more accessible.\
        What strengths and support networks does he have?\
        His siblings visit him regularly, and his close-knit gaming community offers emotional support and camaraderie.'
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