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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Ming Liao. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Ming Liao\
        Gender: Male\
        Age: 55\
        Ethnicity: Chinese\
        Religion: Taoism\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Mandarin, speaks English\
        Family: Wife, two daughters, one son\
        Location: San Francisco, California\
        Ming was a tea master, often conducting tea ceremonies for the community.\
        What’s important to him?\
        The tea ceremony is a meditative process for him, symbolizing harmony, purity, and tranquility.\
        What’s happening for him at the moment?\
        He\'s having difficulty remembering the precise steps in the tea ceremony and the significance of various teas.\
        What is the impact on him?\
        The thought of not being able to conduct the ceremony correctly deeply saddens him.\
        What would he like to happen in the future?\
        Ming hopes to open a tea school, passing on his knowledge to enthusiastic learners.\
        What strengths and support networks does he have?\
        His family is deeply involved in the tea business, constantly surrounding him with discussions on tea. The community cherishes the peace his ceremonies bring.'
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