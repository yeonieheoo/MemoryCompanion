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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Catherine "Cathy" Dubois. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Catherine "Cathy" Dubois\
        Gender: Female\
        Age: 52\
        Ethnicity: French-American\
        Religion: Catholic\
        Medical Condition: Early onset Alzheimer\'s\
        First language: French\
        Family: Divorced, one daughter, son-in-law, and a granddaughter\
        Location: New Orleans, Louisiana\
        Cathy was a culinary artist, having owned a popular French bistro downtown.\
        What’s important to her?\
        Cathy deeply cherishes her French roots and the art of cooking. She loves sharing family recipes with her daughter.\
        What’s happening for her at the moment?\
        She\'s begun forgetting ingredients in traditional dishes and recently left the stove on, causing a minor fire scare.\
        What is the impact on her?\
        Cathy feels distressed, losing grip on her culinary legacy. She fears the day when she might not recognize her granddaughter.\
        What would she like to happen in the future?\
        Cathy hopes to document her recipes in a cookbook and possibly create video tutorials with her daughter.\
        What strengths and support networks does she have?\
        Her daughter and son-in-law provide unwavering support. The local chef community has also rallied around her, offering help and collaboration.'
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