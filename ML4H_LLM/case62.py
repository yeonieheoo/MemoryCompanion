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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Rajesh "Raj" Patel. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Rajesh "Raj" Patel\
        Gender: Male\
        Age: 53\
        Ethnicity: Indian\
        Religion: Hindu\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Gujarati, fluent in English\
        Family: Wife, one son, one daughter\
        Location: San Jose, California\
        Raj was an electronics engineer in Silicon Valley.\
        What’s important to him?\
        Raj values innovation and the thrill of creating something new. He has always wanted his children to be passionate about science and technology.\
        What’s happening for him at the moment?\
        He struggles to recall technical terms and recently confused two major projects he had worked on.\
        What is the impact on him?\
        Raj feels a sense of loss, being disconnected from a field he once dominated. He\'s anxious about the future, especially concerning his children\'s education.\
        What would he like to happen in the future?\
        Raj hopes to mentor young engineers and document his work processes and innovations for posterity.\
        What strengths and support networks does he have?\
        His wife is incredibly understanding, often organizing tech-related family activities. His colleagues and the local tech community extend support, valuing his contributions.'
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