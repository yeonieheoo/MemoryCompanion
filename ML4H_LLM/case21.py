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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Aditi Varma. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Aditi Varma Gender: Female Age: 59 Ethnicity: Indian Religion: Hindu Medical Condition: Alzheimer’s First language: Hindi Family: Widowed, two sons Location: Jaipur, India\
        Family Details: Sons - Arjun, 33, businessman; Rohan, 29, software engineer.\
        Aditi is a skilled Kathak dancer. The rhythm of the ghungroos and the grace of the dance form have been an integral part of her life.\
        What’s important to you? Dance has always been Aditi\'s expression of joy, sorrow, and spirituality. The traditional tales she narrates through dance have been passed down through generations.\
        What’s happening for you at the moment? Aditi sometimes forgets the intricate steps or loses rhythm during her practice sessions. At times, she finds it hard to recognize some of her older students.\
        What is the impact on you? Aditi feels a deep sense of loss when she struggles with her dance. She\'s apprehensive about performing on stage, fearing she might falter and disappoint her audience.\
        What would you like to happen in the future? She wishes to pass on her legacy by training her granddaughter in Kathak. Aditi also dreams of seeing a grand recital of all her students.\
        How might we achieve this? Rohan is documenting her dance lessons for future generations. Arjun is coordinating with her older students for a grand recital to honor her contributions.\
        What strengths and support networks do you have to help you? Aditi\'s undying passion for dance drives her. Her students, past and present, have formed a network of support, sharing stories and experiences to keep her spirits high.'
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