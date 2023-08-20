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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Naomi Thompson. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Naomi Thompson Gender: Female Age: 90 Ethnicity: British Religion: Protestant Medical Condition: Alzheimer’s First language: English Family: Two daughters Location: Brighton, UK\
        Family Details: Daughters - Fiona, 65, retired nurse; Elaine, 62, bookshop owner.\
        Naomi was a primary school teacher. She has a fondness for classic English literature.\
        What’s important to you? Recalling the joy of teaching and reading stories to her students.\
        What’s happening for you at the moment? She occasionally confuses characters from different novels.\
        What is the impact on you? Naomi becomes disoriented when she misplaces her favorite books.\
        What would you like to happen in the future? Hopes to narrate her favorite tales to her great-grandchildren.\
        How might we achieve this? Elaine is recording Naomi\'s readings for posterity.\
        What strengths and support networks do you have to help you? Naomi\'s neighbors and daughters ensure she\'s engaged with regular reading sessions.'
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