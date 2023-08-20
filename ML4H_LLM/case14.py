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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Amara Ndiaye. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Amara Ndiaye Gender: Female Age: 73 Ethnicity: Senegalese Religion: Islam Medical Condition: Alzheimer’s First language: Wolof Family: Three sons Location: Dakar, Senegal\
        Family Details: Sons - Malik, 49, fisherman; Boubacar, 46, musician; Idrissa, 43, school principal.\
        Amara was an artisan, skilled in making traditional jewelry. She loves Senegalese music and dance.\
        What’s important to you? Her craft, the joy of dancing, and family gatherings.\
        What’s happening for you at the moment? She sometimes forgets jewelry designs but still recalls traditional songs.\
        What is the impact on you? Becomes despondent when her hands can\'t create like before.\
        What would you like to happen in the future? To see a collective exhibit of her lifetime work.\
        How might we achieve this? Boubacar and Idrissa are arranging a local exhibition.\
        What strengths and support networks do you have to help you? Amara has a vast network of fellow artisans and receives great support from her sons.'
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