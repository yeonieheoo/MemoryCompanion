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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Chike Okonkwo. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Chike Okonkwo Gender: Male Age: 81 Ethnicity: Nigerian Religion: Christian Medical Condition: Alzheimer’s disease First language: Igbo Family: Two sons, one daughter Location: Lagos, Nigeria\
        Family Details: Son - Uzo, 54, university professor in Abuja. Son - Obi, 50, engineer in Lagos. Daughter - Nneka, 48, runs a non-profit for women\'s education in Lagos.\
        Chike was a diplomat and has traveled to over 50 countries. He has a passion for photography and has a large collection of photos.\
        What’s important to you? Chike cherishes his diplomatic days and the friendships he made worldwide. He loves revisiting his photo albums.\
        What’s happening for you at the moment? He often forgets the countries he has visited but still recalls some foreign phrases.\
        What is the impact on you? Chike becomes melancholic when he fails to recall his diplomatic assignments but lights up when discussing photography.\
        What would you like to happen in the future? He wishes to compile his photos into a book for his grandchildren.\
        How might we achieve this? Nneka is considering hiring a professional photographer to assist with the book project.\
        What strengths and support networks do you have to help you? Chike is respected in his community and has a close bond with his children, particularly Nneka.'
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