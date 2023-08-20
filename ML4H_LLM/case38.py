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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Keita Nakamura. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Keita Nakamura Gender: Male Age: 55 Ethnicity: Japanese Religion: Shinto Medical Condition: Alzheimer’s First language: Japanese Family: Married, one daughter Location: Kyoto, Japan\
        Family Details: Wife - Yuki, 52, traditional dancer. Daughter - Hana, 24, florist.\
        Keita, a master potter, is known for his stunning ceramics, each piece reflecting the intricate beauty of Japanese craftsmanship.\
        What’s important to you? For Keita, pottery isn\'t just about shaping clay but channeling the soul into each creation. He believes in the wabi-sabi philosophy - embracing the beauty in imperfection.\
        What’s happening for you at the moment? Recently, Keita has been forgetting the intricate steps of certain pottery styles, leading to unfinished pieces and increasing frustration.\
        What is the impact on you? His studio, once a haven of creativity, now reminds him of his struggles. There\'s a deep sense of loss as he feels his connection with the craft wane.\
        What would you like to happen in the future? Keita wishes to host a final exhibition, a culmination of his life\'s work, hoping it serves as an inspiration for aspiring potters.\
        How might we achieve this? Hana, with her expertise in flowers, wants to complement his pottery with exquisite floral arrangements, while Yuki envisions performing traditional dances during the exhibition to enhance the ambiance.\
        What strengths and support networks do you have to help you? His family, deeply rooted in traditional arts, understands the essence of his work and is dedicated to helping him realize his vision. The artist community in Kyoto has been incredibly supportive, offering spaces for the exhibition and helping with logistics.'
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