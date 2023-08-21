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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Priyanka Patel. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Priyanka Patel\
        Gender: Female\
        Age: 55\
        Ethnicity: Gujarati (Indian)\
        Religion: Hinduism\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Gujarati, fluent in English\
        Family: Husband, one daughter, one son\
        Location: San Jose, California\
        Priyanka was a classical Indian dancer, skilled in Kathak.\
        What’s important to her?\
        Expressing stories through dance, and the spiritual connection it offers.\
        What’s happening for her at the moment?\
        She occasionally forgets intricate dance steps or loses rhythm.\
        What is the impact on her?\
        The thought of not being able to dance distresses her deeply.\
        What would she like to happen in the future?\
        Priyanka wishes to establish a dance academy, promoting Kathak to the younger generation.\
        What strengths and support networks does she have?\
        Her daughter is also a dancer and practices with her. The Indian community in San Jose holds her in high esteem.'
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