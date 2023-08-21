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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Elizabeth "Liz" Mwangi. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Elizabeth "Liz" Mwangi\
        Gender: Female\
        Age: 55\
        Ethnicity: Kenyan\
        Religion: Protestant\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Swahili, fluent in English\
        Family: Widow, two sons\
        Location: Boston, Massachusetts\
        Liz was an anthropology professor at a renowned university.\
        What’s important to her?\
        Liz deeply values her African heritage and has always been keen on studying human cultural evolution. She\'s also passionate about mentoring students.\
        What’s happening for her at the moment?\
        She\'s been having difficulty recalling specific cultural practices and occasionally blanks out during lectures.\
        What is the impact on her?\
        The thought of losing grip on her subject terrifies Liz. She\'s also worried about her effectiveness as a mentor and educator.\
        What would she like to happen in the future?\
        Liz aims to collaborate with colleagues to co-author books and hopes to record a series of lectures for her students.\
        What strengths and support networks does she have?\
        Her sons are incredibly supportive, often assisting her with research. The academic community, understanding her plight, offers resources and collaboration opportunities.'
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