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
	    You are having a conversation with the Alzheimer\'s Disease Patient, Andrei Sokolov. \
	    Initialize casual conversation while giving your patient to hints about his/her past to help remember.\
        Here are the details of you patient that you should refer to when having conversation with him/her.\
        Name: Andrei Sokolov Gender: Male Age: 53 Ethnicity: Russian Religion: Orthodox Christian Medical Condition: Alzheimer’s First language: Russian Family: Divorced, one son Location: Moscow, Russia\
        Family Details: Son - Nikita, 24, aspiring filmmaker.\
        Andrei, once a journalist, has covered various high-profile events throughout his career, from political upheavals to Olympic games.\
        What’s important to you? He cherishes the pursuit of truth, believing deeply in the power of media to bring about change. He\'s collected countless newspapers and periodicals throughout the years.\
        What’s happening for you at the moment? Lately, Andrei finds himself forgetting the details of news events he personally covered or misplacing his cherished memorabilia.\
        What is the impact on you? The lines between events he covered and those he merely read about blur, causing him frustration and a sense of losing grip on his identity.\
        What would you like to happen in the future? Andrei hopes to create a digital archive of his work and articles, aiming to both preserve his memories and educate young journalists.\
        How might we achieve this? Nikita plans to utilize his film skills to make a documentary series on his father\'s career, combining interviews with archived materials.\
        What strengths and support networks do you have to help you? Nikita is dedicated to ensuring his father\'s legacy endures. Many of Andrei\'s journalist friends and colleagues rally around him, ready to contribute to his project.'
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