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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Masaru "Masa" Tanaka. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Masaru "Masa" Tanaka\
        Gender: Male\
        Age: 58\
        Ethnicity: Japanese\
        Religion: Shinto\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Japanese, speaks English\
        Family: Wife, one son\
        Location: Seattle, Washington\
        Masa was a fisherman, having fished the Pacific for over 40 years.\
        What’s important to him?\
        The sea is a major part of his life, and he treasures the traditions passed down through generations.\
        What’s happening for him at the moment?\
        He sometimes loses direction at sea and has difficulty recalling fishing techniques.\
        What is the impact on him?\
        His ability to provide for his family and maintain the fishing traditions is at risk.\
        What would he like to happen in the future?\
        Masa wishes to pass on his fishing knowledge to the younger generation and ensure the continuation of his family\'s legacy.\
        What strengths and support networks does he have?\
        His wife often joins him on fishing trips, providing companionship and support. The local fishing community respects his expertise and often seeks his advice.'
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