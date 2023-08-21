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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Naomi Ng. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Naomi Ng\
        Gender: Female\
        Age: 47\
        Ethnicity: Chinese\
        Religion: Buddhist\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Cantonese, fluent in English\
        Family: Husband, two sons\
        Location: San Francisco, California\
        Naomi was a master of traditional Chinese calligraphy.\
        What’s important to her?\
        Keeping the intricate art of calligraphy alive, representing Chinese culture\'s soul.\
        What’s happening for her at the moment?\
        She struggles to remember certain brush strokes and techniques.\
        What is the impact on her?\
        Her self-worth diminishes as her skills fade.\
        What would she like to happen in the future?\
        Naomi hopes to curate a traveling exhibition showcasing the evolution of Chinese calligraphy.\
        What strengths and support networks does she have?\
        Her family cherishes her artwork. Chinese cultural societies and art aficionados applaud her mastery.
'
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