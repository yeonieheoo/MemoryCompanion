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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Nadia Ahmed. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Nadia Ahmed\
        Gender: Female\
        Age: 53\
        Ethnicity: Egyptian\
        Religion: Muslim\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Arabic, fluent in English\
        Family: Husband, three daughters\
        Location: Chicago, Illinois\
        Nadia was a history professor, specializing in ancient Egyptian history.\
        What’s important to her?\
        She treasures her Egyptian heritage and has a passion for sharing knowledge about ancient civilizations.\
        What’s happening for her at the moment?\
        She struggles with chronology, sometimes confusing timelines during her lectures.\
        What is the impact on her?\
        Her confidence in her expertise is wavering, and she feels the weight of possibly misleading her students.\
        What would she like to happen in the future?\
        Nadia hopes to write a comprehensive book on Egyptian history, combining visuals and text.\
        What strengths and support networks does she have?\
        Her husband often aids in her research, and her daughters actively engage her in historical discussions. The academic community provides a platform for collaborations and support.'
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