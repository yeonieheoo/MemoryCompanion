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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Eva Goldberg. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Eva Goldberg\
        Gender: Female\
        Age: 52\
        Ethnicity: Jewish\
        Religion: Judaism\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Hebrew, fluent in English\
        Family: Single, many cousins\
        Location: Miami, Florida\
        Eva was a librarian, curating collections on Jewish history.\
        What’s important to her?\
        Preserving the history of her ancestors and ensuring the younger generation understands their heritage is paramount to her.\
        What’s happening for her at the moment?\
        Eva often forgets where certain books are or their significance in Jewish history.\
        What is the impact on her?\
        She\'s worried about not being able to guide readers effectively and feels she\'s losing touch with her roots.\
        What would she like to happen in the future?\
        Eva wants to create digital archives, making historical records accessible to all.\
        What strengths and support networks does she have?\
        Her cousins often discuss family histories with her, keeping her connected. Many in the community respect her knowledge and seek her guidance.'
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