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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Tomo Nakajima. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Tomo Nakajima Gender: Male Age: 56 Ethnicity: Japanese Religion: Shinto Medical Condition: Alzheimer’s First language: Japanese Family: Wife and a daughter Location: Kyoto, Japan\
        Family Details: Wife - Yuki, 53, florist. Daughter - Mio, 21, art student in Tokyo.\
        Tomo was a master gardener, known for his Zen gardens. He loves tea ceremonies and traditional haikus.\
        What’s important to you? Maintaining harmony, engaging in tea ceremonies, and reading haikus.\
        What’s happening for you at the moment? Tomo occasionally mixes up plant names but remains at peace in his garden.\
        What is the impact on you? He is saddened when he can\'t remember the origins of certain plants.\
        What would you like to happen in the future? To witness the cherry blossoms with his family in Tokyo.\
        How might we achieve this? Yuki and Mio are planning a special trip during the sakura season.\
        What strengths and support networks do you have to help you? Tomo\'s local community cherishes his gardens, and his family is always there for him.'
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