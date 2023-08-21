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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Ella Nyström. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Ella Nyström\
        Gender: Female\
        Age: 59\
        Ethnicity: Swedish\
        Religion: Lutheran\
        Medical Condition: Early onset Alzheimer\'s\
        First language: Swedish, fluent in English\
        Family: Two sons\
        Location: Minneapolis, Minnesota\
        Ella was a ceramic artist, specializing in Scandinavian designs.\
        What’s important to her?\
        Creating functional art, reflecting simplicity and elegance.\
        What’s happening for her at the moment?\
        She forgets pottery techniques or designs she once created effortlessly.\
        What is the impact on her?\
        The challenge of crafting her designs causes her much grief.\
        What would she like to happen in the future?\
        Ella wants to host pottery workshops, passing her skills to eager learners.\
        What strengths and support networks does she have?\
        Her sons operate her pottery store. The art community and Swedish diaspora in Minneapolis support her endeavors.'
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