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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Diego Serrano. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Diego Serrano Gender: Male Age: 59 Ethnicity: Hispanic Religion: Catholic Medical Condition: Alzheimer’s First language: Spanish Family: Married, two daughters Location: Bogotá, Colombia\
        Family Details: Wife - Isabella, 56, school teacher. Daughters - Sofia, 32, architect; and Maria, 28, journalist.\
        Diego was a renowned botanist, with an entire lifetime dedicated to the study of indigenous plants.\
        What\’s important to you? Diego\'s love for nature, particularly plants, has always been the core of his life. He\'s traveled extensively to study indigenous plant species, aiming to conserve and promote their importance.\
        What\’s happening for you at the moment? Recently, Diego has started mixing up plant names, often forgetting the properties of plants he once knew intimately. His treks into the forests have become less frequent due to his diminishing memory.\
        What is the impact on you? These forgetful moments have made Diego increasingly introspective and distant, fearful of losing his connection with nature and his life\'s work.\
        What would you like to happen in the future? Diego wishes to pass on his knowledge to the younger generation, inspiring them to continue his legacy and cherish the environment.\
        How might we achieve this? Sofia and Maria are compiling Diego\'s notes, photographs, and research to create a series of workshops and lectures. They aim to collaborate with local schools and colleges for a broader outreach.\
        What strengths and support networks do you have to help you? Despite his recent challenges, Diego\'s passion and vast knowledge remain largely intact. With the unwavering support of his family and the respect of the botanist community, he continues to inspire and educate.'
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