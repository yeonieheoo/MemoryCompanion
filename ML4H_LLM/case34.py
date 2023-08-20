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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Imani Naser. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Imani Naser Gender: Female Age: 56 Ethnicity: Arab Religion: Muslim Medical Condition: Alzheimer’s First language: Arabic Family: Married, four children Location: Alexandria, Egypt\
        Family Details: Husband - Sayid, 60, librarian. Children - Amira, 33, physician; Hani, 30, marine biologist; Layla, 27, poet; and Kareem, 24, footballer.\
        Imani was a chef, specializing in traditional Egyptian cuisine, running a small but famous eatery in Alexandria.\
        What’s important to you? For Imani, food is a bridge to memories, relationships, and heritage. Every dish she makes is steeped in history and love.\
        What’s happening for you at the moment? She often finds herself forgetting recipes she’s known her whole life, sometimes even mistaking one ingredient for another.\
        What is the impact on you? The kitchen was her realm, her sanctuary. The forgetfulness disrupts her connection to her ancestors, traditions, and even to her own identity.\
        What would you like to happen in the future? Imani desires to create a cookbook, a blend of recipes, stories, and photographs, capturing the essence of Egyptian culinary heritage.\
        How might we achieve this? With Layla\'s poetic touch and Hani\'s knowledge of local ingredients, they aim to co-author this cookbook. They\'re also considering online cooking sessions, allowing Imani to connect with a broader audience.\
        What strengths and support networks do you have to help you? Imani\'s family is her backbone, each member playing a unique role in keeping her grounded. Her eatery\'s loyal customers and the local community provide an extended network of love and appreciation.'
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