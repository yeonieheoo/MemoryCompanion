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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Akihiro Tanaka. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Akihiro Tanaka\
        Gender: Male\
        Age: 56\
        Ethnicity: Japanese\
        Religion: Shinto\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Japanese, speaks English\
        Family: Wife, one son\
        Location: Seattle, Washington\
        Akihiro was a bonsai artist, crafting miniature trees for international exhibitions.\
        What’s important to him?\
        Bonsai, for him, is a reflection of nature\'s beauty and patience.\
        What’s happening for him at the moment?\
        He struggles to remember specific techniques or the growth patterns of certain trees.\
        What is the impact on him?\
        His inability to craft bonsais as he once did deeply disheartens him.\
        What would he like to happen in the future?\
        Akihiro dreams of establishing a bonsai garden and school.\
        What strengths and support networks does he have?\
        His son shares his love for bonsai. Fellow artists and enthusiasts worldwide respect his expertise.'
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